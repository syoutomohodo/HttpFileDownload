#coding:utf-8

#根据url解析得到的path, host构造Http请求包

from analysisUrl import path, host

packet = 'GET ' + path + ' HTTP/1.1\r\nHost: ' + host + '\r\n\r\n'

