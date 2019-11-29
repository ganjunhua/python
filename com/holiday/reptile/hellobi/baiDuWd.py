# -*- conding: utf-8 -*-
import urllib.request
import re


class BaiDuWd():
    mainUrl = 'https://www.baidu.com/s?wd='
    key = "象棋"
    # 对着急词进行编码，因为url中需要对中文等进行处理
    key_code = urllib.request.quote(key)
    # 带检索关键词的url
    urlKey = mainUrl + key_code + "&ie=utf-8"

    def getPageData(self, thisUrl):
        data = urllib.request.urlopen(thisUrl).read().decode("utf-8", "ignore")
        return data

    def getData(self):
        for i in range(0, 10):
            print("开始第+" + str(i) + "页")
            thisUrl = self.urlKey + "&pn=" + str(i * 10)
            data = self.getPageData(thisUrl)
            titlePat = '"title":"(.*?)"'
            title = re.compile(titlePat, re.S).findall(data)
            print("title"+str(title))
            break
            for j in range(0, len(title)):
                print("开始第+" + str(i) + "页的是标题是：" + title[j])
BaiDuWd().getData()