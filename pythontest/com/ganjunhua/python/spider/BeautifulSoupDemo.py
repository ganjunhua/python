from bs4 import BeautifulSoup as bs
import urllib.request

data = urllib.request.urlopen("http://www.hellobi.com").read().decode("utf-8", "ignore")
# 将data返回对象转为bs
bs1 = bs(data)
#格式化输出网页
bs1.prettify()
#获取标签：bs对象 . 标签名
title=bs1.title
#获取标签里面的文字 bs对象.标签名.string
print(bs1.title.string)
#获取标签名：bs对象.标签名.name
bs1.title.name
#获取属性列表：bs对象.标签名.attrs,返回字典
bs1.a.attrs
#获取某个属性对应的值：bs对象.标签名[属性名]
#或者bs对象.标签名.get[属性名]
a=bs1.link["rel"]
a=bs1.link("rel")
#提取所有某个节点的内容，bs对象.find_all(‘标签名’)
#提取多个节点bs对象.find_all(['标签名',"标签名1"])
x=bs1.find_all('a')
x=bs1.find_all(['a','url'])

#提取所有子节点：bs对象.标签.contents 或bs对象.标签.children
k1=bs1.ul.contents
#返回list
k2=bs1.ul.children
#提取k2内容
allul=[i for i in k2]
print(allul)