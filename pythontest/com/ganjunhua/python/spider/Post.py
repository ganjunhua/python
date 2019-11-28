import urllib.request
import urllib.parse

url = "http://www.iqianyue.com/mypost"
postData = urllib.parse.urlencode({"name": "holiday", "pass": "asfsd"}).encode("utf-8")
req = urllib.request.Request(url, postData)
data = urllib.request.urlopen(req).read()
fileName = open("D:\\python\\test.html", "wb")
fileName.write(data)
fileName.close()
