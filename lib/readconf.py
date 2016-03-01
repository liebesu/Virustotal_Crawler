import ConfigParser
import os
from constants import CONFPATH
__author__ = 'liebesu'
def read_conf():
    config=ConfigParser.ConfigParser()
    config.read(os.path.join(CONFPATH,"crawler.conf"))
    datebaseip=config.get("Datebase","ip")
    datebaseuser=config.get("Datebase","user")
    datebasepsw=config.get("Datebase","password")
    datebasename=config.get("Datebase","databasename")
    datebasetable=config.get("Datebase","tablename")
    reg_username=config.get("reg_info","username")
    reg_premail=config.get("reg_info","premail")
    reg_password=config.get("reg_info","password")
    numkey=config.get("numkey","num")
    mail_user=config.get("mail_info","username")
    mail_pass=config.get("mail_info","password")

    return datebaseip,datebaseuser,datebasepsw,datebasename,datebasetable,reg_username,reg_premail,reg_password,numkey,\
           mail_user,mail_pass
