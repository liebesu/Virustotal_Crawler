from multiprocessing import Pool

__author__ = 'liebesu'
#coding=gbk
import HTMLParser
import imaplib
import MySQLdb.cursors
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

        conn = httplib.HTTPSConnection("www.virustotal.com")
        conn.request(method='POST', url='/en/account/signin/',
                     body=urllib.urlencode(params), headers=self.headers)
        response = conn.getresponse()
        HTML=response.read()
        print HTML
        #<ul class="errorlist"><li>
        error=re.search('<ul\s+?class="errorlist"><li>(?P<errorlist>.+?)</li></ul>',HTML)
        if error:
            error1=error.group("errorlist")
            print error1
        else:
            print "login Scucess"

        url='/en/user/'+params['username']+'/apikey'
        print url
        conn.request(method='GET', url=url,
                      headers=self.headers)
        response = conn.getresponse()
        print response.read()
        conn.close()

def db_sql(id):
    '''try:'''

    db = MySQLdb.connect(host=datebaseip,user=datebaseuser,passwd=datebasepsw,db=datebasename,port=3306)
    cursor = db.cursor(cursorclass = MySQLdb.cursors.DictCursor)
    sql='select Username,Email,Password from '+datebasetable +' where Id='+str(id)
    cursor.execute(sql)
    data = cursor.fetchall()
    db.commit()
    cursor.close()
    db.close()
    for data1 in data:
        return data1

    '''except:
        print Exception
        cursor.close()
        db.close()'''



def post(i):
    data=db_sql(i)
    p = Producer()
    print data['Username']
    print data['Password']
    '''param = {
    'username': data['Username'],
    'password': data['Password'],
    }'''
    param = {
    'username': 'polydata123',
    'password': 'polydata',
    }
    p.post(param)
if __name__=="__main__":
    pool=Pool(processes=1)
    pool.map(post,range(1,2))
    pool.close()
    pool.join()

