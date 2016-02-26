# encoding:utf-8
import urllib, urllib2, cookielib, re
 
# 账号相关参数
username = 'polydata123'
password = 'polydata'
 
# cookie设置
cj = cookielib.CookieJar()
cookie_hanler = urllib2.HTTPCookieProcessor(cj)
 
# 获取once的值
lgurl = 'https://www.virustotal.com/en/'
req = urllib2.Request(url = lgurl)
opener = urllib2.build_opener(cookie_hanler)
urllib2.install_opener(opener)
contents = opener.open(req)
contents = contents.read()
for cje in cj:
    print cje.name+'='+cje.value
# 根据正则表达式匹配once值

 
# 登录参数设置
lgurl = 'https://www.virustotal.com/en/'
data = {'u':username, 'p':password}
data = urllib.urlencode(data)
hdr = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
req = urllib2.Request(url = lgurl, data = data, headers = hdr)
opener = urllib2.build_opener(cookie_hanler)
 
# 进行登录操作
response = opener.open(req)
page = response.read()
print(page)
print response.code
for cje in cj:
    print cje.name+'='+cje.value
# 可以随便访问其他的链接
contents = urllib2.urlopen('https://www.virustotal.com/en/'+username+'/apikey/')
contents = contents.read()
print(contents)