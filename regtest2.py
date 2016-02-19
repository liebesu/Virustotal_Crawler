__author__ = 'liebesu'
# -*- coding:utf-8 -*-

import random,urllib,urllib2
import re,time
x=input("请输入需要注册的数量:")
# x=raw_input() #转换成字符串的

def h(i,y):

    user=str(random.randrange(10000000,99999999))

    QQ=str(random.randrange(10001,999999999999))

    pwd=str(random.randrange(100000,99999999))


    url="http://www.qb5.com/register.php?do=submit"


    data={"username":user,
    "password":pwd,
    "repassword":pwd,
    "email":QQ+"@qq.com",
    "qq":QQ,
    "sex":"0",
    "action":"newuser",
    "submit":""}

    data=urllib.urlencode(data)

    req=urllib2.Request(url,data=data)
    print data
    # html=urllib2.urlopen(req).read()
    # print(html)
    html=urllib2.urlopen(req).read().decode('gbk')

    # print(type(html))
    reg=u'您已成功注册成为本站用户'
    reg=re.compile(reg)
    r=re.findall(reg,html)
    if r!=[]:
        print("注册成功，账号为%s，密码为%s，目前注册到第%s,还剩%s个"%(user,pwd,i+1,y-i-1))
        f=open("c:\user.txt","a")
        f.write("%s----%s----%s@qq.com----%s\n" %(user,pwd,QQ,QQ))
        # f.write("qq----123456")
        f.close()

for i in range(x):
    h(i,x)
    # 延时
    time.sleep(2)