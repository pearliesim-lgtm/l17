import random 
import time

def getRandomDate(s,e):
    print("Printing random date between",s,"and",e)
    randomGenerator =random.random()
    dateFormat='%m/%d/%Y'
    Sdate=time.mktime(time.strptime(s, dateFormat))
    Edate=time.mktime(time.strptime(e, dateFormat))
    ramdomTime=Sdate+randomGenerator*(Edate-Sdate)
    randomDate=time.strftime(dateFormat,time.localtime(ramdomTime))
    return randomDate

print("Random Date=",getRandomDate("01/01/2026","12/01/2026"))
