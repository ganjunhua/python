import requests
import re

# 请求方式：get、post、put
# 参数：params 用于设置get的请求方式的请求参数；data用于设置post的参数；通用headers设置请求对信息，proxies、cookies、
url = "http://baidu.com"
# 发送请求
response = requests.get("https://baidu.com")
# 发送请求后，使用utf-8解码
response.encoding = "utf-8"
# 得到请求后的内容，这个结果是解码后的
response.text
# 得到二进制的内容
response.content
# 得到当前访问的网址
response.url
# 得到当前网页的编码
response.encoding
# 得到当前的cookies
response.cookies
# 将cookie将为字典
requests.utils.dict_from_cookiejar(response.cookies)
# 得网页的状态码
response.status_code

print(response.encoding)
print(re.compile(r'<title>(.*?)</title>', re.S).findall(response.text))

# 请求带参数
headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
# 添加cookies
cookie = requests.utils.dict_from_cookiejar(response.cookies)
# 添加代理
px = {"http": "http://127.0.0.1:8888"}
# rsp = requests.get(url, headers=headers, cookies=cookie, proxies=px)

# 添加请求的实际参数
key = {"wd": "甘俊华"}
rsp = requests.get(url, headers=headers, params=key)
rsp.encoding = "utf-8"
print(re.compile("<title>(.*?)</title>").findall(rsp.text))

# post 请求
url = 'https://www.iqianyue.com/mypost'
data = {"name": "测试账号", "pass": "xxx"}
rsp =  requests.post(url, data=data)
print(rsp.text)

