#coding:utf-8

#根据解析Url获取的host解析出IP地址，根据url+port连接url所指向的服务器。

import socket
from analysisUrl import port,host

ip = socket.gethostbyname(host)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip, port))

print "success connected webServer！！"

