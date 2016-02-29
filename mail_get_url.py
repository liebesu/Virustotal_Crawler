import httplib
from multiprocessing import Pool
import urllib
import urllib2
import gmail
import re
def anmail(n):
    #for email in emails:
    emails[n].fetch()
    url1=re.search(r'https://www.virustotal.com/en/account/activate/.*',emails[n].body).group()
    r0=open("url",'a')
    r0.writelines(url1)
    r0.close()
def gmail_login():
    g=gmail.login('','')
    emails=g.inbox().mail(sender="noreply@vt-community.com")
    pool=Pool(processes=250)
    pool.map(anmail,range(len(emails)))
    pool.close()
    pool.join()

        #break
def openurl1():
    all=open('url.txt','r').readlines()
    all=[each.replace('\r','')for each in all]
    pool=Pool(processes=100)
    pool.map(openurl2,all)
    pool.close()
    pool.join()
def openurl2(url):
    urllib.urlopen(url)

if __name__=="__main__":

    #emails=gmail_login()


    openurl1()
    print "finished"



