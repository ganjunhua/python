import urllib.request
import urllib.parse
import  json
import  time

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://fanyi.youdao.com/"
data = {}
# head = {} # 模拟人工访问 方法1
# head ['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
data['from'] = 'AUTO'
data['i'] = 'i love holiday'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['typoResult'] = 'true'
data = urllib.parse.urlencode(data).encode('utf-8')

req = urllib.request.Request(url,data)
req.add_header(  'User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
) #方式 2
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')

jsondata = json.loads(html) # 返回是字典
print(jsondata['errorCode']) #返回值
time.sleep(5)