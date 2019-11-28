import pymysql
import urllib.request
import re

conn = pymysql.connect(
    host="localhost",
    user="root",
    passwd="admin123",
    db="holiday"
)
for i in range(0, 10):
    thisurl = "https://edu.hellobi.com/course/" + str(i + 1)
    data = urllib.request.urlopen(thisurl).read().decode("utf-8", "ignore")
    title_pat = '<li class="active">(.*?)</li>'
    teacher_pat = 'class="lec-name">(.*?)<'
    price_pat = '￥</sub>(.*?)<b>'
    title = re.compile(title_pat, re.S).findall(data)
    if (len(title) > 0):
        title = title[0]
    else:
        continue
    teacher = re.compile(teacher_pat, re.S).findall(data)
    if (len(teacher) > 0):
        teacher = teacher[0]
    else:
        teacher = "缺失"
    price = re.compile(price_pat, re.S).findall(data)
    if (len(price) > 0):
        price = price[0]
    else:
        price = "免费"
    sql = "insert into lesson(title,teacher,price)  VALUES  ('" + str(title) + "','" + str(teacher) + "','" + str(
        price) + "')"

    conn.query(sql)
    conn.commit()
conn.close()
