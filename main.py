import os
import requests

url = "https://api.oioweb.cn/api/common/today?type=text"
response = requests.get(url)
response.raise_for_status()  # 检查请求是否成功
# 解析响应内容为JSON
data = response.json()
# 从响应中提取"date"、"news"和"weiyu"
date = data.get('result', {}).get('date', '未知日期')  # 从"result"字典中提取"date"
news_list = data.get('result', {}).get('news', [])  # 从"result"字典中提取"news"列表
weiyu = data.get('result', {}).get('weiyu', '无微语')  # 从顶层字典中提取"weiyu"
imageURL = data.get('result', {}).get('image', '无image')  # 从顶层字典中提取"weiyu"
news_str = "\n".join(news_list)
# 将"date"、"news"和"weiyu"合并为一个列表
combined_data = f"{date}\n{news_str}\n{weiyu}"

pushplus_token = os.environ.get('pushplus_token')
topic = os.environ.get('topic')
image_url = imageURL
content = combined_data

pushplus_url = "http://www.pushplus.plus//send"

pushplus_data = {
    "token": "677889bab50d44a3ae7004b672a77112",
    "title": "每天60秒读懂世界",
    "content": "{}<br/><img src='{}' />".format(content,image_url),
    "topic": "daily60s",
    "template": "html"
}

requests.post(pushplus_url, json=pushplus_data)






