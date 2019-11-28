# -*- conding:utf-8 -*-
import  re

#全局匹配函数 compile("正则表达式","模型匹配re.S")
re.compile("abc",re.S).findall("baiduabc")

string='aliyunedu'
pat='yu'
print(re.compile(pat,re.S).findall(string))
string="""aliyun
edu
"""
pat="yun\n"
print(re.compile(pat,re.S).findall(string))
string="aliyu89787nedu"
pat="\w\d\w\d\d\w"
print(re.compile(pat,re.S).findall(string))

string='aliyu89787nedu'
pat="\w\d[nedu]\w"
print(re.compile(pat,re.S).findall(string))

string='aliyunnnnji898989'
pat="ali..."
print(re.compile(pat,re.S).findall(string))

string='aliyunnnnji898989'
pat="^li..."
print(re.compile(pat,re.S).findall(string))

string='aliyunnnnji898989'
pat="yun{1,2}"
print(re.compile(pat,re.S).findall(string))

string='poyxxphony'
pat='p.*?y'
print(re.compile(pat,re.S).findall(string))