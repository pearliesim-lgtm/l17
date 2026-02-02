from datetime import date,time,datetime

today=date.today()
print("Today's date is",today)
print("Date components:",today.day,"/",today.month,"/",today.year)
now=datetime.now()
print("current date and time is",now)