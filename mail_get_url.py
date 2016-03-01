from multiprocessing import Pool
import urllib
import gmail
import re
from lib.readconf import read_conf
datebaseip,datebaseuser,datebasepsw,datebasename,datebasetable,reg_username,reg_premail,reg_password,numkey,\
           mail_user,mail_pass=read_conf()
def gmail_login(mail_user,mail_pass):
    g=gmail.login(mail_user,mail_pass)
    emails=g.inbox().mail(sender="noreply@vt-community.com")
    pool=Pool(processes=250)
    pool.map(anmail,range(len(emails)))
    pool.close()
    pool.join()
def anmail(n):
    #for email in emails:
    emails[n].fetch()
    url=re.search(r'https://www.virustotal.com/en/account/activate/.*',emails[n].body).group()
    url=url.replace('\r','')
    openurl2(url)
def openurl2(url):
    urllib.urlopen(url)

if __name__=="__main__":
    gmail_login()
    print "finished"



