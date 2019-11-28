import random
import urllib.request


class WeChat:
    def ua_ip(self, ips, myurl, thisapi, uapools):
        print("ips" + str(ips))
        def api(thisapi):
            print("这一次随机选择IP")
            thisall = random.choice(thisapi)
            return thisall

        def ip(ippools, uapools):
            thisua = random.choice(uapools)
            print(thisua)
            headers = ("User-Agent", thisua)
            thisip = ippools
            proxy = urllib.request.ProxyHandler({"http": thisip})
            # 进行IP代理
            opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
            # 进行用户代理
            opener.addheaders = [headers]

        if (ips == 0):
            while True:
                ips = api(thisapi)
                print("提取IP" + ips)
                ip(ips, uapools)
                print("进行IP与用户代理注册")
                break
        else:
            ip(ips, uapools)
        url = myurl
        data1 = urllib.request.urlopen(url).read()
        data = data1.decode("utf-8", "ingore")
        return ips, data
