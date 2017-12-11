#!/usr/bin/env python

import socket

# 创建客户端socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取主机名
host = socket.gethostname()
print("客户端主机： %s" % host)
port = 10000

# 连接服务器
client_socket.connect((host, port))

# 接收数据
msg = client_socket.recv(1024)

print(msg.decode("utf-8"))
