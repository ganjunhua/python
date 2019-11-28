import urllib.request

url = 'http://placekitten.com/500/900'
respone = urllib.request.urlopen(url)
cat_img = respone.read()
cat_path = 'D://cat_img'
with open(cat_path, 'wb') as f:
    f.write(cat_img)
print(respone.geturl()) # 获得访问的地址
print(respone.info()) #获取服务器信息
print(respone.getcode()) #获取网页状态。 200 正常