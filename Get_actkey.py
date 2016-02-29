from multiprocessing import Pool
import re
import MySQLdb
import requests
import sys
from lib.readconf import read_conf
datebaseip,datebaseuser,datebasepsw,datebasename,datebasetable,reg_username,reg_premail,reg_password,numkey=read_conf()
cookies = list()

def vtpost(param):
    s=requests.session()
    url='https://www.virustotal.com/en/account/signin/'
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "application/json, text/javascript, */*; q=0.01", "Referer": url}
    try:
        r=s.post(url,data=param,headers=headers,allow_redirects=False)
    except Exception as e:
        print "post failed "
        print e
        sys.exit()
    if r.status_code ==302:
        apiurl='https://www.virustotal.com/en/user/'+param['username']+'/apikey/'
        r=s.get(apiurl,allow_redirects=False)
        if r.status_code == 200:
            page=r.text.encode('ascii', 'ignore')
            print page
            key=re.search(r'<center>(.+?)</center>',page)
            print key
            key=key.group().replace('<center>','').replace('</center>','')

            db = MySQLdb.connect(host=datebaseip,user=datebaseuser,passwd=datebasepsw,db=datebasename,port=3306)
            cursor = db.cursor(cursorclass = MySQLdb.cursors.DictCursor)
            updatesql="update  "+datebasetable+" set VTKey = '"+key+"' where Username='"+param['username']+"'"
            print updatesql
            cursor.execute(updatesql)
            db.commit()
            cursor.close()
            db.close()

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
        print data1

def post(i):
    data=db_sql(i)
    param = {
    'next': '/en/',
    'username': data['Username'],
    'password': data['Password']
    }
    vtpost(param)
if __name__=="__main__":
    pool=Pool(processes=10)
    pool.map(post,range(1,9816))
    pool.close()
    pool.join()

