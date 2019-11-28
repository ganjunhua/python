import urllib.request
import re


class helloBiClass():
    # 定义入口网站
    mainUrl = 'https://edu.hellobi.com/course/'

    # 发送请求获取接口或网站的数据
    def getData(self,url):
        return urllib.request.urlopen(url).read().decode("utf-8", "ignore")

    # 使用正则获取对应的数据
    def getPat(self,pat, data):
        data = re.compile(pat, re.S).findall(data)
        if (len(data) > 0):
            data = data[0]
        else:
            data = "暂无"
        return data

    def getTargetData(self, data):
        # 使用正则获取已经得到的数据
        titlePat = '<li class="active">(.*?)</li>'
        teacherPat = 'class="lec-name">(.*?) <'
        pricePat = '<span class="price-expense"><sub>￥</sub>(.*?)<b></b></span>'

        title = self.getPat(titlePat, data)
        teacher = self.getPat(teacherPat, data)
        price = self.getPat(pricePat, data)

        return 'title=' + title + "\n" + 'teacher=' + teacher + "\n" + 'price=' + price

    def hellobi(self):
        for i in range(0, 1000):
            print("正在执行第----" + str(i) + "------页数据")
            thisUrl = self.mainUrl + str(i + 1)
            pageData = self.getData(thisUrl)
            data = self.getTargetData(pageData)
            print(data)

helloBiClass().hellobi()
