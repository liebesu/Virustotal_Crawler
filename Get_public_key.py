__author__ = 'liebesu'

import urllib2, urllib
import re
import cookielib
import httplib
import sys


class Producer:
    def __init__(self):
        self.gen_token_and_cookie()
        self.headers = {
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
           'Origin': 'https://www.virustotal.com',
           'Referer': 'https://www.virustotal.com/en/#dlg-join',
           'Content-Type': 'application/x-www-form-urlencoded',
           'Cookie': self.str_cookie,
        }

    #generate request token and string format cookie
    def gen_token_and_cookie(self):
        try:
            cookie = cookielib.CookieJar()
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
            urllib2.install_opener(opener)
            html_doc = urllib2.urlopen('https://app.box.com/signup/personal/').read()
            self.request_token = re.search("request_token = '(.*?)'", html_doc).group(1)
            lst_cookie = ['%s=%s' % (c.name, c.value) for c in cookie]
            self.str_cookie = '; '.join(lst_cookie)
        except Exception,e:
            print 'fail to get request token or cookie:', e
            sys.exit(1)

    def post(self, params):
        print 'create user', params['email']
        conn = httplib.HTTPSConnection("www.virustotal.com")
        conn.request(method='POST', url='/signup/o/default_personal',
                     body=urllib.urlencode(params), headers=self.headers)
        response = conn.getresponse()
        if response.status == 302:
            location = response.getheader('location', '')
            if location == '/files':
                print 'user', i, 'successfully created'
        else:
            print '!!! error while create user', params['email'], '!!!'
        conn.close()


#create as many users as you like
if __name__=="__main__":
    for i in range(1, 10):
        p = Producer()
        params = {
            'first_name': 'your_first_name',
            'last_name': 'your_last_name',
            'username': 'autoruntest'+str(i),
            'email': 'email_pre_fix' + str(i) + '@hodreams.com',
            'password1': 'liebesuauto',
            'password2': 'liebebsuauto',
            'personal_plan': 'lite',
            'tier': 'lite',
            'plan_group': 'personal',
            'elqCustomerGUID': '',
            'elqCookieWrite': 0,
            'request_token': p.request_token,
            }
        p.post(params)
