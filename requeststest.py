import re

__author__ = 'liebesu'
import requests
s=requests.session()
username = 'polydata1231'
password = 'polydata'
url='https://www.virustotal.com/en/account/signin/'
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "application/json, text/javascript, */*; q=0.01", "Referer": url}
data={'next': '/en/' ,'username': username, 'password': password}
r = s.post(url,data=data,headers=headers,allow_redirects=False)
print r.cookies
print r.status_code
apiurl='https://www.virustotal.com/en/user/polydata123/apikey/'
r = s.get(apiurl,allow_redirects=False)
print r.status_code
page = r.text.encode('ascii', 'ignore')
key=re.search(r'<center>(.+?)</center>',page)
key=key.group().replace('<center>','').replace('</center>','')
print key