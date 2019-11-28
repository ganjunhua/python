# IP代理池实现的第二种方式
# 接口调用法，这种方法更适合于代理IP不稳定的情况
import time
import urllib.request


def use_ip(ipools, myurl, thisapi):
    def api(thisapi):
        # 通过接口获取ip
        import urllib.request
        print("第一次调用了接口")
        import urllib.request
        urllib.request.urlcleanup()
        thisall = urllib.request.urlopen(thisapi).read().decode("utf-8", "ignore")
        print("接口调用完成")
        return thisall

    def ip(ippools):
        thisip = ippools
        print("当前用的IP是" + ippools)
        proxy = urllib.request.ProxyHandler({"http": thisip})
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)

    if (ipools == 0):
        ipools = api(thisapi)
    ip(ipools)
    url = myurl
    data1 = urllib.request.urlopen(url).read()
    data = data1.decode("gbk", "ignore")
    return ipools, data


x = 0
thisapi = "xx"
for i in range(0, 33):
    try:
        url = "http://www.baidu.com"
        if (i % 5 == 0 and i == 0):
            ipools, thisdata = use_ip(0, url, thisapi)
        elif (i % 5 == 0):
            time.sleep(120)
            ipools, thisdata = use_ip(0, url, thisapi)
        else:
            ipools, thisdata = use_ip(ipools, url, thisapi)
        print(len(thisdata))
    except:
        pass
