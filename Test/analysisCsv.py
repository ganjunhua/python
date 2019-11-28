import csv,os

fileName = "test.csv"

f=file(fileName,'r')

with open(fileName, encoding='gbk') as f:
    render1 = csv.reader(f)
    xaray = []
    for row in render1:
        try:
            id = row[0]
        except(Exception):
            id = 'holiday'
        try:
            id1 = row[1]
        except(Exception):
            id1 = 'holiday'
        try:
            id2 = row[2]
        except(Exception):
            id2 = 'holiday'
        xaray.append(id1)
        xaray.append(id2)
        xaray.append(id)
        if 'holiday' in xaray:
            xaray.remove('holiday')
            #print(len(xaray))
            #print(xaray)

