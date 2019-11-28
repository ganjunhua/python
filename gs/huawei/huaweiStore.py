import urllib.request
import requests
import re
import pymysql


class huaweiStore:
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            user="root",
            passwd="admin123",
            db="holiday"
        )

    def addData(self, appName, downloadCount, issueDate, content):
        sql = "insert into huaweistore VALUES  ('" + str(appName) + "','" + str(downloadCount) + "','" + str(
            issueDate) + "','" + str(content) + "')"
        self.conn.query(sql)
        self.conn.commit()

    def getData(self, count):
        headers = {"User-Agent":
                       "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
                   "Referer": "http://appstore.huawei.com/search/%E9%87%91%E8%9E%8D/9",
                   "Cookie": "__hau=SUPPORTE.1536724243.410734256; support_last_vist=carrier; cs6k_langid=zh_cn"}
        url = "http://appstore.huawei.com/search/%E9%87%91%E8%9E%8D/" + str(count)
        # data = urllib.request.urlopen(url, headers=headers).read().deocde("utf-8", "ignore")
        response = requests.get(url, headers=headers)
        data = response.content.decode("utf-8")
        titlepat = '<div class="game-info  whole">.*?<.*? class="title">.*?<a title="(.*?)".*?href="/app/.*?">'
        issuedatepat = '<p class="date"><span>发布时间： (.*?)</span></p>'
        downloadpat = '<span>下载</span>.*?</a>.*?<span>下载:(.*?)</span>'
        contentpat = '<div class="game-info-dtail part">.*?<p class="content">(.*?)</p>'
        contentList = re.compile(contentpat, re.S).findall(data)
        titleList = re.compile(titlepat, re.S).findall(data)
        downloadList = re.compile(downloadpat, re.S).findall(data)
        issuedateList = re.compile(issuedatepat, re.S).findall(data)
        for i in range(0, len(titleList)):
            try:
                self.download = downloadList[i]
            except:
                self.download = ""

            try:
                self.title = titleList[i]
            except:
                self.title = ""

            try:
                self.issuedate = issuedateList[i]
            except:
                self.issuedate = ""

            try:
                self.content = contentList[i]
            except:
                self.content = ""

            self.addData(self.title, self.download, self.issuedate, self.content)

        self.conn.close()


if __name__ == '__main__':
    for i in range(5, 10):
        a = huaweiStore()
        a.getData(i)
