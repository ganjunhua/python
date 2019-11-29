import urllib.request
import re

url = "https://www.baidu.com/s?wd="
key = "除夕"
# 对关键词进行编码，因为url中需要对中文等进行处理
key_code = urllib.request.quote(key)
# 构造带检索关键的url
url_key = url + key_code + "&ie=utf-8"
# 通过for循环爬取各页信息
for i in range(0, 10):
    print("正在爬取" + str(i + 1) + "页数据")
    thisurl = url_key + "&pn=" + str(i * 10)
    # 爬取这一页的数据
    data = urllib.request.urlopen(thisurl).read().decode("utf-8")
    print(thisurl)
    print(data)
    # 成功得到数据，根据正则表达将爬到的网页的标题进行提取
    pat = '"title":"(.*?)"'
    # "title":"氨氮废水处理_百度百科"
    # 返回列表类型
    title = re.compile(pat, re.S).findall(data)
    # 循环提取列表

    for k in range(0, len(title)):
        print("第" + str(k) + "页，标题是：" + str(title[k]))