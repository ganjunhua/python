import requests
import re

# get 请求方法
# 请求网页，返回给response
response = requests.get("https://edu.hellobi.com/")
cookie = requests.utils.dict_from_cookiejar(response.cookies)
# 获取title
title = re.compile("<title>(.*?)</title>", re.S).findall(response.text)
# 代理
px = {"http": "http://127.0.0.1:8888", "https": "http://127.0.0.1:8888"}
# 请求当参数伪装浏览器
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
# 伪装浏览器、添加cookies、代理
response = requests.get("https://edu.hellobi.com/", headers=head, cookies=cookie)

# 带参数请求，where条件
key = {"wd": "天眼查"}
rsp = requests.get("https://www.baidu.com/s", headers=head, cookies=cookie, params=key)
title = re.compile("<title>(.*?)</title>", re.S).findall(rsp.text)

# post请求
# 带参数请求，where条件
postdata = {"wd": "天津"}
rsp = requests.post("https://www.baidu.com/s", data=postdata)
x = re.compile("<title>(.*?)</title>", re.S).findall(rsp.text)
print(x)