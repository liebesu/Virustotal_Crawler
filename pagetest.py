# encoding:utf-8
import urllib, urllib2, re, cookielib
import BeautifulSoup
# 账号相关参数
username = 'polydata123'
password = 'polydata'
cookie = cookielib.CookieJar()
handler=urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
# 打开目标链接，获取Html
url = 'https://www.virustotal.com/#dlg-signin'
#opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'), ('Accept', 'application/json, text/javascript'), ('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6')]
urlopen = opener.open(url)
print type(cookie)
for item in cookie:
    print item.name
    print item.value
rsp = urlopen.read()
a=open("virustotal","a")
a.write(rsp)
a.close()
# print(contents)
# 获取xsrf值
# 保存cookie
lgurl = 'https://www.virustotal.com/en/'
cookie = cookielib.CookieJar()
cookie_handler = urllib2.HTTPCookieProcessor(cookie)
hdr = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36'}
post_data = { 'email':username, 'password':password,}
dt = urllib.urlencode(post_data)
req = urllib2.Request(lgurl, dt, hdr)
opener = urllib2.build_opener(cookie_handler)
urllib2.install_opener(opener)
response = opener.open(req)
page = response.read()
# print(page)
testurl = 'https://www.virustotal.com/en/user/polydata123/apikey/'
req = urllib2.urlopen(testurl)
print(req.read())