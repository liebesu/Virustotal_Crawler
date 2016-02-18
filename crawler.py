import json
import urllib
import urllib2
import time

__author__ = 'liebesu'

class Virustotal():
    def  __init__(self):
        self.base='https://www.virustotal.com/vtapi/v2/'
    def getreport(self,sha256,apikey):
        param= { 'resource':sha256,'apikey':apikey}
        url = self.base+"file/report"
        data=urllib.urlencode(param)
        print url,data
        try:
            result=urllib2.urlopen(url,data)
            jdata =json.loads(result.read())
            return jdata
        except:
            time.sleep(5)
            result = urllib2.urlopen(url,data)
            jdata =  json.loads(result.read())
            return jdata









if __name__ == "__main__":
    sha256='63b6416457366b2dac84bfc65c4d4c0ddb136f87a56fc6549850272c1b80517c'
    apikey='1f6d0b2aa12cdc6ea3ef9fc4e95483e0432d3eaaffb1be468d48fa8d4425805c'
    vt=Virustotal()
    jdata=vt.getreport(sha256,apikey)
    #print jdata