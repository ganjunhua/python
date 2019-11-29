import urllib.request

# 伪装浏览器
url = "http://www.baidu.com"
headers = ('User-Agent',
               'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36')

# 方法1---------------
opener = urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
# ----------------

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    "Content-Type": "text/html;charset=utf-8"
}
# 方法2------------
opener = urllib.request.build_opener()
headll = []
for key, value in headers.items():
    item = (key, value)
    headll.append(item)
opener.addheaders = headll
urllib.request.install_opener(opener)
# ------------------

headers = ('User-Agent',
           'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36')

# 方法3----------------
req1 = urllib.request.Request(url)
req1.add_header=(headers)
# -----------------
req1data = urllib.request.urlopen(req1).read().decode("utf-8", "ignore")
