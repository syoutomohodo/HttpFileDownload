#coding:utf-8
#解析URL中的host,port,path,filename

import urllib

#解析host和path
def analyHostAndPath(totalUrl):
    protocol,s1 = urllib.splittype(totalUrl)
    host, path = urllib.splithost(s1)
    if path == '':
        path = '/'
    return host, path

#解析port
def analysisPort(host):
    host, port = urllib.splitport(host)
    if port is None:
        return 80
    return port

#解析filename
def analysisFilename(path):
    filename = path.split('/')[-1]
    if '.' not in filename:
        return None
    return filename

print "Please input url:"
url = raw_input()
host = analyHostAndPath(url)[0]
path = analyHostAndPath(url)[1]
port = analysisPort(host)
filename = analysisFilename(path)
#判断用户意愿
print "Do you want to change a filename?('y' or other words)"
answer = raw_input()
if answer == "y" or filename is None:
    print "Please input your new filename:"
    filename = raw_input()
