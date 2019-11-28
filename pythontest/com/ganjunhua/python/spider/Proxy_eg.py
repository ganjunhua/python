import urllib.request
import  random
url ='http://www.whatismyip.com.tw'
iplst = ['115.223.193.6:9000','115.159.221.219:8118','175.155.136.36:1133']
# 随机选择一个ip
proxy_ip = {'http':random.choice(iplst)}
#注册代理ip
proxy_support =  urllib.request.ProxyHandler(proxy_ip)
#创建代理ip opener
opener = urllib.request.build_opener(proxy_support)
# 虚拟 agent，虚拟浏览器
opener.addheaders=[( 'User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')]
# 安装openner
urllib.request.install_opener(opener)
#请求网页
response = urllib.request.urlopen(url)
#读取网页
html = response.read().decode('utf-8')
print(html)