import socket

# 创建服务端
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 8125))
s.listen(8)
while 1:
    # 获取请求的连接与地址
    connection, address = s.accept()
    # 获取请求的数据
    buf = connection.recv(1024)
    #将请求的数据返回去
    connection.send(buf)
s.close()