import urllib.request
import re

vid = '3281055320'
cid = '6463242326085829412'
for i in range(0, 10):
    print("--------------第" + str(i) + "页数据-----------------")
    url = 'https://video.coral.qq.com/varticle/' + str(vid) + '/comment/v2?callback=_varticle' + str(vid) + 'commentv2&orinum=10&oriorder=o&pageflag=1&cursor=' + str(cid) + '&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=9'
    data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
    patContent = '"content":"(.*?)"'
    allcomment = re.compile(patContent, re.S).findall(data)
    patLast = '"last":"(.*?)"'
    cid = re.compile(patLast, re.S).findall(data)[0]
    print("--------------" + str(cid) + "-----------------")
    for j in allcomment:
        try:
            print(eval("u'" + str(j) + "'"))
        except:
            pass
