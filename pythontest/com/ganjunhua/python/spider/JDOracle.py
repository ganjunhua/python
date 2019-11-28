import urllib.request
import re
import  random
#构造IP代理池
ippools=[
    "95.79.28.168:53491",
    "117.191.11.78:8080",
    "117.191.11.74:8080"
    ]
#添加IP代理
def ua(ippools):
    thisua=random.choice(ippools)
    print(thisua)
    proxy=urllib.request.ProxyHandler({"http":thisua})
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    #安装为全局
    urllib.request.install_opener(opener)
keyname = "iphone"
key = urllib.request.quote(keyname)
for i in [k for k in range(10) if k % 2]:
    try:
        #使用IP代理
        ua(ippools)
        url = 'https://search.jd.com/Search?keyword=' + key + '&page=' + str(i)
        data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
        pat = 'source-data-lazy-img="//(.*?)" '
        imgList = re.compile(pat, re.S).findall(data)
        for j in range(0, len(imgList)):
            thisimg = imgList[j]
            thisImgUrl = "http://" + thisimg
            localFile = "D:/spider/" + str(i) + keyname + ".jpg"
            urllib.request.urlretrieve(thisImgUrl, filename=localFile)
    except:
        pass