from com.ganjunhua.python.spider.wechat.SpiderAgent import *
from com.ganjunhua.python.spider.wechat.WeChat import WeChat

import urllib.request
import re
import time

myurl = "https://www.baidu.com/"
agent = SpiderAgent()
wechat = WeChat()
# ippools, data = wechat.ua_ip(0, myurl, agent.IP_Agent, agent.User_Agent)

key = "机器学习"
key = urllib.request.quote(key)
name = "微信爬虫_" + str(key)
for i in range(0, 100):
    thispageurl = "https://weixin.sogou.com/weixin?oq=&query=" + key + "&type=2&page=" + str(i + 1)
    if (i % 3 == 0 and i == 0):
        ippools, thispagedata = wechat.ua_ip(0, thispageurl, agent.IP_Agent, agent.User_Agent)
    elif (i % 3 == 0):
        print("正在延时中。。。。")
        time.sleep(3)
        print("延时完成，正在调用ip")
        ippools, thispagedata = wechat.ua_ip(0, thispageurl, agent.IP_Agent, agent.User_Agent)
    else:
        ippools, thispagedata = wechat.ua_ip(ippools, thispageurl, agent.IP_Agent, agent.User_Agent)
    pat = '<div class="txt-box">.*?href="(.*?)"'
    pages = re.compile(pat, re.S).findall(thispagedata)
    #print("主网页" + str(len(thispagedata)))
    #print("子网页" + str(pages))
    if (len(pages) > 0):
        for j in range(0, len(pages)):
            thisurl = pages[j]
            pat_2 = 'amp;'
            thisurl = thisurl.replace(pat_2, "")
            print("开始爬虫" + str(thisurl))
            ippools, thisdata = wechat.ua_ip(ippools, thisurl, agent.IP_Agent, agent.User_Agent)
            print("子网内容" + str(len(thisdata)))
            fh = open("D:/spider/wechat/" + str(i) + str(j) + ".html", "w", encoding="utf-8")
            fh.write(thisdata)
            fh.close()
