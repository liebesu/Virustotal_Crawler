import urllib2

__author__ = 'liebesu'
import requests
login_data={'next':'/en/',
    'response_format': 'json',
    'username': 'polydata123',
    'password': 'polydata',
            }
s=requests.session()
a=s.post('https://www.virustotal.com/en/account/signin/',login_data)
r=urllib2.urlopen('https://www.virustotal.com/en/user/polydata123/apikey/')
print a.text
print r
