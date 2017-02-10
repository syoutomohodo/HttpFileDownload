# HttpFileDownload
## 环境
windows/Linux + python2.7.x
## 项目介绍
本项目的目的是使用Python编写一个http下载器，并生成.exe可执行文件。
## 过程
### 实现单线程下载
1. 解析URL中的host, port, filename
2. 根据从URL中解析到的host和port，连接web服务器；
3. 构造http请求，也就是http包
4. 根据构造的http请求包，连接服务器，向服务器发送请求报文，并下载文件。
#### 解析URL
解析URL以获得host, port, filename。根据host和port连接web服务器。
#### 连接Web服务器
根据从URL中解析到的host和port,连接web服务器。
#### 构造http包
packet = 'GET ' + path + ' HTTP/1.1\r\nHost: ' + host + '\r\n\r\n'
#### 下载文件
根据构造的http请求包，连接服务器，想服务器发送请求报文，并下载文件。
### 多线程下载
抓取响应报文头部的"Content-Length"字段，结合线程个数加锁分段下载。
### 生成可执行文件
使用py2exe结合所编写的.py文件生成.exe可执行文件。





