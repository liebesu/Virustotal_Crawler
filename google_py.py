import re
import requests

s=requests.session()
url='https://www.google.com.tw/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=inurl:analysis+site:www.virustotal.com&num=100'
headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
r=s.get(url,headers=headers)
a=open("google","w")
a.write(r.text.encode('utf-8').strip())
a.close()
urls=re.search('<a\s+?href="https://www.virustotal.com/en/file/(.+?)onmousedown=',r.text)
print urls.group()

