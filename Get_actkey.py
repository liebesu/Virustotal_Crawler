from multiprocessing import Pool

__author__ = 'liebesu'
#coding=gbk
'''
    my[at]lijiejie.com    http://www.lijiejie.com
    auto create a large number of box.net accounets
'''
import HTMLParser
import imaplib
import re
import MySQLdb
import urllib2, urllib
import httplib
import BeautifulSoup
from lib.readconf import read_conf
datebaseip,datebaseuser,datebasepsw,datebasename,datebasetable,reg_username,reg_premail,reg_password,numkey=read_conf()
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

    def post(self, params):
        print 'create user', params['email']
        conn = httplib.HTTPSConnection("www.virustotal.com")
        conn.request(method='POST', url='/en/account/signin/',
                     body=urllib.urlencode(params), headers=self.headers)
        response = conn.getresponse()
        HTML=response.read()
        #<ul class="errorlist"><li>
        error=re.search('<ul\s+?class="errorlist"><li>(?P<errorlist>.+?)</li></ul>',HTML)
        if error:
            error1=error.group("errorlist")
            print error1
        else:
            print "creat Scucess:",params['email']
            self.db_sql(params)
        '''if "Welcome to the VirusTotal community" in str(response.read):
            print 'user', params['email'], 'successfully created'
        else:
            print '!!! error while create user', params['email'], '!!!'''''
        conn.close()

    def db_sql(self,params):
        try:
            db = MySQLdb.connect(datebaseip,datebaseuser,datebasepsw,datebasename,cursorclass = MySQLdb.cursors.DictCursor)
            cursor = db.cursor()
            sql='select * from '+datebasetable
            cursor.execute(sql)
            data = cursor.fetchall()
            db.commit()
            cursor.close()
            db.close()
        except Exception as e:
            print e



def mian(i):
    p = Producer()

    param = {
    'username': reg_username+str(i),
    'email': reg_premail + str(i) + '@hodreams.com',
    'password': reg_password,
    }
    p.post(param)
if __name__=="__main__":
    pool=Pool()
    pool

