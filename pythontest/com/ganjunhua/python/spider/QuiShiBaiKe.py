import urllib.request
import re

for i in range(0, 40):
    try:
        thisurl = "https://www.qiushibaike.com/8hr/page/" + str(i + 1) + "/"
        req = urllib.request.Request(thisurl)
        req.add_header("User-Agent",
                       "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")
        data = urllib.request.urlopen(req).read().decode("utf-8", "ignore")
        title_pat = '<div class="content">.*?<span>(.*?)</span>'
        title=re.compile(title_pat,re.S).findall(data)
        for i in range(0,len(title)):
            print(title[i])
    except:
        pass