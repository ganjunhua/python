# -*- coding: utf-8 -*-

import urllib.request


class urlLibModel():
    mainUrl = 'http://www.baidu.com'
    fileName = 'baidu'

    def getUrllibRequestPageData(self):
        # 将网页数据爬取到内存中方法1:urllib.request，即发送请求接口
        data = urllib.request.urlopen(self.mainUrl).read().decode("utf-8", "ignore")
        pass

    def getUrllibRequestRequestPageData(self):
        # 将网页数据爬取到内存中方法2:urllib.request，可以加参数，即发送请求接口
        req = urllib.request.Request(self.mainUrl)
        data = urllib.request.urlopen(req).read().decode("utf-8", "ignore")
        print(data)
        pass

    def getUrlRequestUrlretrieve(self):
        # 将网页数据爬取到硬盘中方法3：urllib.request.urlretrieve 爬取图片等
        urllib.request.urlretrieve(self.mainUrl, filename=self.fileName)
        print("getUrlRequestUrlretrieve")
        pass

    def getPageStatuCode(self):
        file = urllib.request.urlopen(self.mainUrl)
        # 得到网页状态码
        pageCode = file.getcode()
        print(pageCode)


urlLibModel().getPageStatuCode()
