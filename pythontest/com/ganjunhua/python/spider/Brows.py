import urllib.request

url = "https://www.qiushibaike.com/"
# 方法-1:opener
# 创建用户代理，使用元组
headers = (
    "User-Agent",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
)
# 创建opener对象
opener = urllib.request.build_opener()
# 将代理添加到opener对象中
opener.addheaders = [headers]
# 将opener安装至全局
urllib.request.install_opener(opener)
# 开始爬虫
data = urllib.request.urlopen(url).read()

# 方法-2：批量添加headers
headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    , "Referer": "https: // www.qiushibaike.com /"
}
opener = urllib.request.build_opener()
headall = []
for key, value in headers.items():
    item = (key, value)
    headall.append(item)
opener.addheaders = headall
urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read()

# 方法-3：Request
req = urllib.request.Request(url)
req.add_header("User-Agent",
               "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")
data = urllib.request.urlopen(req).read().decode("utf-8", "ignore")
