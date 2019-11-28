from selenium import webdriver
import time
import re

# 输入参数
fromCity = input("请输入出发城市")
toCity = input("请输入到达城市")
beginDate = input("请输入出发日期")
# 创建浏览器
brower = webdriver.PhantomJS(executable_path=r'D:/Holiday/App/Python3/phantomjs-2.1.1/bin/phantomjs.exe')
# 打开网页
brower.get("https://www.ly.com/?refId=4140683")
# 加载网页
time.sleep(30)
# 出发地址
brower.find_element_by_xpath('//*[@id="txtAirplaneCity1"]').clear()
brower.find_element_by_xpath('//*[@id="txtAirplaneCity1"]').send_keys(fromCity)
# 到达地址
brower.find_element_by_xpath('//*[@id="txtAirplaneCity2"]').clear()
brower.find_element_by_xpath('//*[@id="txtAirplaneCity2"]').send_keys(toCity)
# 出发日期
brower.find_element_by_xpath('//*[@id="txtAirplaneTime1"]').clear()
brower.find_element_by_xpath('//*[@id="txtAirplaneTime1"]').send_keys(beginDate)
# 搜索功能
brower.find_element_by_xpath('//*[@id="airplaneSubmit"]').click()
# 加载网页
time.sleep(30)
# 查看当前网页
brower.get_screenshot_as_file("D:/scrapy/selenium/ly.jpg")
# 获取网页内容
data = brower.page_source
# 退出无头浏览器
brower.quit()
# 处理数据
# 提取航空正则
patHk = '<div class="hk"><span.*?></span>(.*?)</div>'
# 登机时间正则
patStartDate = '<div class="f_size24">(.*?)</div>'
# 登机机场正则
patCheckIn = '<div class="f_size12 morehidden110">(.*?)</div>'
# 落地时间正则
# patEndDate='<div class="f_size24">21:40</div>'
# 落地机场
patlognOut = '<div class="f_size12 morehidden108">(.*?)</div>'
# 价格
patPrice = '<em class="f_size26 emprice_margin">(.*?)</em>'
hk = re.compile(patHk, re.S).findall(data)
StartDate = re.compile(patStartDate, re.S).findall(data)
CheckIn = re.compile(patCheckIn, re.S).findall(data)
lognOut = re.compile(patlognOut, re.S).findall(data)
price = re.compile(patPrice, re.S).findall(data)
print("公司\t出发地\t到达地\t出发时间\t到达时间\t价格")
for i in range(0, len(hk)):
    print(hk[i] + "\t" + CheckIn[i] + "\t" + lognOut[i] + "\t" + StartDate[i * 2] + "\t" + StartDate[i * 2 + 1] + "\t" +
          price[i])