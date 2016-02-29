__author__ = 'liebesu'
import requests
s=requests.session()
username = 'polydata123'
password = 'polydata'
url='https://www.virustotal.com/en/account/signin/'
csrfmiddlewaretoken = s.get(url)
headers ={
    'Referer':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Authorization':'access_token myToken',
    'content-type': 'application/json'
          }
data={'next': '/en/' ,'username': username, 'password': password}
r = s.post(url,data=data,headers=headers,allow_redirects=False)
#csrfmiddlewaretoken=r.cookies['csrfmiddlewaretoken']
print r.cookies
print r.status_code
apiurl='https://www.virustotal.com/en/user/polydata123/apikey/'
r = s.get(apiurl,allow_redirects=False)
print r.status_code
print r.text.encode('ascii', 'ignore')