import urllib.request
import os
import random
def url_open(url):
    # 创建一个url对象
    req = urllib.request.Request(url)
    # 添加一个head,虚拟浏览器
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')

    # 使用代理 访问网址
    proxies = ['xx:90','xx:90']
    proxy = random.choice(proxies)
    proxy_support = urllib.request.ProxyHandler({'http':proxy})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    # 访问网址
    response = urllib.request.urlopen(url)
    # 读取网址
    html = response.read()
    return  html

def get_page(url):
    # 读取网址
    html = url_open(url).decode('utf-8')
    # 查找页码起始位置
    a = html.find('current-comment-page') + 23
    # 查找页码的结束位置。从a的位置开始找
    b = html.find(']',a)
    # 通过起始与结束索引 查出具体页码
    return html[a:b]

def find_imgs(url):
    # 读取图片的网页
    html = url_open(url).decode('utf-8')
    img_addrs = []
    #确定图片的具体来源地址
    a = html.find('img src="')
    #网页有很多图片。循环查找
    while a != -1:
        b = html.find('.jpg',a,a + 255)
        print(b)
        if b != -1:
            # 查找到具体的图片的url
            img_addrs.append(html[a+9:b+4])
        else:
            b = a + 9
        # 每次循环查找，a的位置就是上次查找出来b的位置
        a = html.find('src="',b)
    return img_addrs
def save_imgs(folder, img_addrs):
    for each in img_addrs:
        # 分隔网址，获取文件名
        filename =  each.split('/')[-1]
        with open(filename,'wb') as f:
            # 打开图片
            img = url_open(each)
            # 保存图片
            f.write(img)

# pages=10 默认查询十张图片
def downloan_mm(folder='ooxx', pages=10):
    # os.mkdir(folder)
    os.chdir(folder)

    url = 'http://jandan.net/ooxx/'

    # http://jandan.net/ooxx/page-45#comments
    # 获取起始页码
    page_num = int(get_page(url))
    print(" page_num = int(get_page(url))")
    for i in range(pages):
        # 每次循环 页码 减 1
        page_num -= i
        # 拼接图片地址
        page_url = url + 'page-' + str(page_num) + '#comments'
        # 将所有拼接的图片地址保存到一个列表中
        img_addrs = find_imgs(page_url)
        # 将图片保存至文件中
        save_imgs(folder, img_addrs)


if __name__ == '__main__':
    downloan_mm(folder='ooxx', pages=10)