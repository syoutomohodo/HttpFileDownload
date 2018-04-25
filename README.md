# HttpFileDownload

## 项目介绍
本项目使用Python编写http下载器。

## Version 01
### 环境
windows/Linux + python2.7.x
### 实现单线程下载
1. 解析URL；
2. 连接web服务器；
3. 构造http请求包；
4. 下载文件。

#### 解析URL(analysisUrl.py)
解析URL以获得host, port, path，filename。

#### 连接Web服务器(conWebserver.py)
根据从URL中解析到的host和port,连接web服务器。

#### 构造http包(httpPacket.py)
packet = 'GET ' + path + ' HTTP/1.1\r\nHost: ' + host + '\r\n\r\n'

#### 下载文件(singleThread.py)
根据构造的http请求包，连接服务器，想服务器发送请求报文，并下载文件。

### 多线程下载
抓取响应报文头部的"Content-Length"字段，结合线程个数加锁分段下载。

### 生成可执行文件
py2exe将python脚本转换成windows上的可独立执行的可执行程序
(*.exe）的工具，这样，你就可以不用装Python而在windows系统上运行
这个可执行程序。

#### 安装
下载地址：https://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/
根据你安装的Python版本，结合windows属性下载对应文件，下载完成打开，
安装。

#### 使用（以该项目为准，需要生成的是multiThreadDownload.exe）
在multiThreadDownload.py的同目录下建立mysetup.py文件，编写代码。
执行命令：**Python mysetup.py py2exe**.
生成dist文件夹，multiThreadDownload.exe于该文件夹中，点击运行即可执行。

## Version 02







