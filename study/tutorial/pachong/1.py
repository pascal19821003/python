#https://www.runoob.com/w3cnote/python-spider-intro.html
#Python 爬虫介绍

#https://blog.csdn.net/doudou19930614/article/details/83022308
#python3.6的cookielib

import urllib.parse
import urllib.request
from http import cookiejar

#import cookielib

#import urllib2

url = "http://www.baidu.com"
response1 = urllib.request.urlopen(url)
print("第一种方法")
#获取状态码，200表示成功
print(response1.getcode())
#获取网页内容的长度
print(str(response1.read()))
print(len(response1.read()))

print("第二种方法")
request = urllib.request.Request(url)
#模拟Mozilla浏览器进行爬虫
request.add_header("user-agent","Mozilla/5.0")
response2 = urllib.request.urlopen(request)
print(response2.getcode())
print(len(response2.read()))

print("第三种方法")
cookie = cookiejar.CookieJar()
#加入urllib2处理cookie的能力#
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)
print(response3.getcode())
print(len(response3.read()))
print(cookie)