# encoding:utf-8
import httplib
import urllib, urllib2, cookielib, re
 
# 账号相关参数
username = 'polydata123'
password = 'polydata'
 
# cookie设置
cj = cookielib.CookieJar()
cookie_hanler = urllib2.HTTPCookieProcessor(cj)
 
# 获取once的值
lgurl = 'https://www.virustotal.com/'
req = urllib2.Request(url = lgurl)
opener = urllib2.build_opener(cookie_hanler)
urllib2.install_opener(opener)
contents = opener.open(req)
contents = contents.read()
 
# 根据正则表达式匹配once值
reg = r'value="(.*)" name="csrfmiddlewaretoken"'
pattern = re.compile(reg)
result = pattern.findall(contents)
print result
# 登录参数设置
lgurl = 'https://www.virustotal.com'
once = result
data = {'u':username, 'p':password, 'next':'/en/','response_format':'json'}
data = urllib.urlencode(data)
hdr = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36', 'Referer':'https://www.virustotal.com/'}
conn = httplib.HTTPSConnection("www.virustotal.com")
req = conn.request(method='POST', url='/en/account/signin/', body=urllib.urlencode(data), headers = hdr)
opener = urllib2.build_opener(cookie_hanler)
 
# 进行登录操作
response = opener.open(req)
page = response.read()
print(page)
 
# 可以随便访问其他的链接
contents = urllib2.urlopen('https://www.virustotal.com/en/user/polydata123/apikey/')
contents = contents.read()
print(contents)