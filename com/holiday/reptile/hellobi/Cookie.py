# -*- coding:utf-8 -*-
import urllib.request
import http.cookiejar

# 建立cookie处理
cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
# 将opener安装全局，所有的地方都进行了cookie处理
urllib.request.install_opener(opener)

# cookie读取
print(str(cjar))
