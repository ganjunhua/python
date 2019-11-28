import urllib.request
import http.cookiejar

# cookie自动处理 建立cookie处理
cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)
