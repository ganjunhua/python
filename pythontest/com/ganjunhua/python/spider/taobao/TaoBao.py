
import urllib.request
import re
import random
import http.cookiejar

from com.ganjunhua.python.spider.wechat.SpiderAgent import SpiderAgent

cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)
agent = SpiderAgent()
keyname = "女装"
kye = urllib.request.quote(keyname)


def ua(uapools):
    thisua = random.choice(uapools)
    print(thisua)
    headers = ("User-Agent", thisua)
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)


for i in range(1, 101):
    print("--------第" + str(i) + "页商品---------")
    url = "https://s.taobao.com/search?q=" + kye + "&s=" + str((i - 1) * 44)
    ua(agent.User_Agent)
    data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
    print("--------第" + str(url) + "页商品---------")
    pat = '"nid":"(.*?)"'
    idlist = re.compile(pat, re.S).findall(data)
    xx = open("D:/spider/taobao/" + "1.html", "w", encoding="utf-8")
    xx.write(data)
    xx.close()
    print("主页。。。。。" + str(len(data)))
    if (len(data) > 0):
        break
    for j in range(0, len(idlist)):
        print("找到店铺ID" + str(idlist[j]))
        thisid = idlist[j]
        thisurl = "https://item.taobao.com/item.htm?id=" + str(thisid)
        fh = urllib.request.urlopen(thisurl)
        if ("tmall.com") in str(fh.url):
            continue
        itemdata = fh.read().decode("gbk", "ignore")
        titlepat = '<h3 class="tb-main-title" data-title="(.*?)">'
        detailpat = '<meta name="description" content="(.*?)"'
        title = re.compile(titlepat, re.S).findall(itemdata)
        if (len(title) > 0):
            title = title[0]
        else:
            continue
        detail = re.compile(detailpat, re.S).findall(itemdata)
        if (len(detail) > 0):
            detail = detail[0]
        else:
            detail = 0

        headers = ("Referer", str(fh.url))
        opener = urllib.request.build_opener()
        opener.addheaders = [headers]
        urllib.request.install_opener(opener)

        priceUrl = 'https://detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=' + str(
            thisid) + '&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract&callback=onSibRequestSuccess'
        priceData = urllib.request.urlopen(priceUrl).read().decode("utf-8", "ignore")
        patPrice = 'price":"(.*?)"'
        price = re.compile(patPrice, re.S).findall(priceData)
        if (len(price) > 0):
            price = price[0]
        else:
            price = 0
        countUrl = 'https://rate.taobao.com/detailCount.do?_ksTS=1541420668561_157&callback=jsonp158&itemId=' + str(
            thisid)
        patCount = '"count":(.*?)}'
        countData = urllib.request.urlopen(countUrl).read().decode("utf-8", "ignore")
        count = re.compile(patCount, re.S).findall(countData)
        if (len(count) > 0):
            count = count[0]
        else:
            count = 0
        print("---------")
        print("商品名" + str(title))
        print("描述信息" + str(detail))
        print("价格" + str(price))
        print("评论" + str(count))
