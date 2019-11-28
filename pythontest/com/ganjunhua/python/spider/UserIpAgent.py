# 同时使用用户代理与IP代理池
import time
import urllib.request
import random


def ua_ip(ippools, myurl, thsapi):
    uapools = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
        ,
        "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
        ,
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    ]
    #通过接口获取IP
    def api(thisapi):
        print("这一次调用了接口")
        urllib.request.urlcleanup()
        thisall=urllib.request.urlopen(thisapi).read().decode("utf-8","ignore")
        print("接口调用完成")
        #返回IP
        return thisall
    def ip(ippools,uapools):
        #获取用户代理
        thisua=random.choice(uapools)
        print(thisua)
        #获取用户代理
        headers=["User-Agent",thisua]
        thisip=ippools
        #代理设置
        proxy=urllib.request.ProxyHandler({"http":thisip})
        opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
        #用户代理设置
        opener.addheaders=[headers]
        urllib.request.install_opener(opener)
    if (ippools==0):
        while True:
            #获取IP
            ippools=api(thsapi)
            #代理
            ip(ippools,uapools)
            #验证IP有效性
            data1=urllib.request.urlopen("http://www.baidu.com").read().decode("utf-8")
            if(len(data1)>5000):
                print("有效")
                break
            else:
                print("无效")
                time.sleep(60)
        url=myurl
        data1=urllib.request.urlopen(url).read()
        data=data1.decode("gbk","ignore")
        return ippools,data