#!/usr/bin/env python

import socket

# 创建服务器socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取主机名
host = socket.gethostname()
print("本地主机地址： %s" % host)
port = 10000

# 绑定端口
server_socket.bind((host, port))

# 设置最大连接数
server_socket.listen(5)

# 监听客户端连接
while True:
    client_socket, client_address = server_socket.accept()

    print("连接地址： %s" % str(client_address))

    msg = "这是一个Python网络测试服务！"

    # 向客户端发送信息并关闭连接
    client_socket.send(msg.encode("utf-8"))
    client_socket.close()
