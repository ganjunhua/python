# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse

url = 'https://www.iqianyue.com/mypost'
# 将数据使用urlencode编码处理后，使用encode()设置utf-8编码
postdata = urllib.parse.urlencode({
    "name": "xxx"
    , "pass": "xxx"
}).encode('utf-8')
# 发送请求，并添加参数
req = urllib.request.Request(url, postdata)
req.add_header('User-Agent',
               'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36')
data = urllib.request.urlopen(req).read()
file = open('baidu.txt', 'wb')
file.write(data)
file.close()
