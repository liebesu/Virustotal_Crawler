import cookielib
import httplib
from multiprocessing import Pool
#import MySQLdb.cursors
import re
#import MySQLdb
import urllib2, urllib
import sys
from lib.readconf import read_conf
datebaseip,datebaseuser,datebasepsw,datebasename,datebasetable,reg_username,reg_premail,reg_password,numkey=read_conf()
cookies = list()
class Producer:
    def __init__(self):
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
            print html_doc
            self.request_token = re.search("csrfmiddlewaretoken'(.*?)'", html_doc).group(1)
            lst_cookie = ['%s=%s' % (c.name, c.value) for c in cookie]
            self.str_cookie = '; '.join(lst_cookie)
            #print self.str_cookie
        except Exception,e:
            print 'fail to get request token or cookie:', e

    def post(self, params):
        cookie = cookielib.CookieJar()
        cookie_handler = urllib2.HTTPCookieProcessor(cookie)
        conn = httplib.HTTPSConnection("www.virustotal.com")
        req=conn.request(method='POST', url='/en/account/signin/',
                     body=urllib.urlencode(params), headers=self.headers)
        opener = urllib2.build_opener(cookie_handler)
        urllib2.install_opener(opener)
        response = opener.open(req)
        response = conn.getresponse()
        '''if response.code==302:
            print "logingingging"'''
        HTML=response.read()
        #<ul class="errorlist"><li>
        error=re.search('<ul\s+?class="errorlist"><li>(?P<errorlist>.+?)</li></ul>',HTML)
        if error:
            error1=error.group("errorlist")
            print error1
        else:
            print "login Scucess"
        #print HTML
        url='/en/user/'+params['username']+'/apikey/'
        conn = httplib.HTTPSConnection("www.virustotal.com")
        conn.request(method='GET', url=url,
                      headers=self.headers)
        response = conn.getresponse()
        print response.read()

        rep=urllib2.urlopen("https://www.virustotal.com/en/user/"+params['username']+"/apikey/")
        resp=rep.read()
        print resp
        a=open("resp","w")
        a.write(resp)
        a.close()
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
    #data=db_sql(i)
    p = Producer()
    #print data['Username']
    #print data['Password']
    '''param = {
    'username': data['Username'],
    'password': data['Password'],
    }'''
    param = {
     'next':'/en/',
    'response_format': 'json',
    'username': 'polydata123',
    'password': 'polydata',
    }
    p.post(param)
if __name__=="__main__":
   ''' pool=Pool(processes=1)
    pool.map(post,range(1,2))
    pool.close()
    pool.join()'''
   post(1)

