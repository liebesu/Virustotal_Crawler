#coding=gbk
'''
    my[at]lijiejie.com    http://www.lijiejie.com
    auto create a large number of box.net accounets
'''

import urllib2, urllib
import re
import cookielib
import httplib
import sys


class Producer:
    def __init__(self):        
        #self.gen_token_and_cookie()
        self.headers = {
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
           'Origin': 'https://www.virustotal.com',
           'Referer': 'https://www.virustotal.com/en/',
           'Content-Type': 'application/x-www-form-urlencoded',

        }

    #generate request token and string format cookie
    def gen_token_and_cookie(self):
        try:
            cookie = cookielib.CookieJar()
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
            urllib2.install_opener(opener)
            html_doc = urllib2.urlopen('https://www.virustotal.com/en/').read()
            self.request_token = re.search("request_token = '(.*?)'", html_doc).group(1)
            lst_cookie = ['%s=%s' % (c.name, c.value) for c in cookie]
            self.str_cookie = '; '.join(lst_cookie)    
        except Exception,e:
            print 'fail to get request token or cookie:', e    
            sys.exit(1)
    
    def post(self, params):
        print 'create user', params['email']
        conn = httplib.HTTPSConnection("www.virustotal.com")
        conn.request(method='POST', url='/en/account/signup/',
                     body=urllib.urlencode(params), headers=self.headers)
        response = conn.getresponse()
        if response.status == 302:
            location = response.getheader('location', '')
            if location == '/files':
                print 'user', i, 'successfully created'
        else:
            print '!!! error while create user', params['email'], '!!!'
        conn.close()

class Getkey:
    def mailactiv(self):
#create as many users as you like
for i in range(1, 10):
    p = Producer()

    param = {
    'first_name': 'your_first_name',
    'last_name': 'your_last_name',
    'username': 'autoruntest'+str(i),
    'email': 'test' + str(i) + '@hodreams.com',
    'password1': 'liebesuauto',
    'password2': 'liebesuauto',
    }
    p.post(param)
