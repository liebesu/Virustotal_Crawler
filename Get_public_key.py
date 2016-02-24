#coding=gbk
'''
    my[at]lijiejie.com    http://www.lijiejie.com
    auto create a large number of box.net accounets
'''
import HTMLParser
import imaplib
from multiprocessing import Pool
import re
import MySQLdb
import urllib2, urllib
import httplib
import BeautifulSoup
import time
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
        try:
            conn = httplib.HTTPSConnection("www.virustotal.com")
            conn.request(method='POST', url='/en/account/signup/',
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
        except:
            time.sleep(5)
            conn = httplib.HTTPSConnection("www.virustotal.com")
            conn.request(method='POST', url='/en/account/signup/',
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
            db = MySQLdb.connect(datebaseip,datebaseuser,datebasepsw,datebasename)
            cursor = db.cursor()
            insertsql='insert into '+datebasetable+ ' (Username,Email,Password) values ('+"'"+params['username']+"','"\
                      +str(params['email'])+"','"+params['password1']+"'"+')'
            cursor.execute(insertsql)
            db.commit()
            cursor.close()
            db.close()
        except Exception as e:
            print e

class GetactURL:
    def __init__(self):
        self.IMAP_SERVER='imap.gmail.com'
        self.IMAP_PORT=993
        self.M = None
        self.respons
        self.mailboxes = []
    def login(self, username, password):
        self.M = imaplib.IMAP4_SSL(self.IMAP_SERVER, self.IMAP_PORT)
        rc, self.response = self.M.login(username, password)
        self.M.select('Inbox')
#create as many users as you like
def mian(i):

    p = Producer()

    param = {
    'first_name': 'your_first_name',
    'last_name': 'your_last_name',
    'username': reg_username+str(i),
    'email': reg_premail + str(i) + '@hodreams.com',
    'password1': reg_password,
    'password2': reg_password,
    }
    p.post(param)
if __name__=="__main__":
    pool=Pool(processes=1000)
    pool.map(mian,range(int(numkey)))
    pool.close()
    pool.join()


