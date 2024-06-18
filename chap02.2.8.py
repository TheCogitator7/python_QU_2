#Date and time
import datetime

var=datetime.datetime.now()
print(var)#2024-06-18 14:42:45.076973

type(var)

print(var.year)#2024

print(var.month, var.day)#6 18

print(var.weekday())#1
#0 is Monday, 1 is Tuesday

print(var.date(), var.time())#2024-06-18 14:44:53.305855

print(var.strftime('%Y-%m-%d'))#2024-06-18

print(var.strftime('%H시 %M분 %S초'))#14시 46분 58초

print(datetime.datetime.strptime("2024-12-31 11:59:59", "%Y-%m-%d %H:%M:%S"))
#2024-12-31 11:59:59


#Calculate date and time

dt1=datetime.datetime(2022, 12, 31)
dt2=datetime.datetime(2021, 12, 31)
dt3=dt1-dt2

print(dt3)#365 days, 0:00:00

dt4=datetime.datetime(2022, 12, 31)
dt5=dt4+datetime.timedelta(days=1)
print(dt5)#2023-01-01 00:00:00



from dateutil.relativedelta import relativedelta
dt6=dt4+relativedelta(months=1)
print(dt6)#2023-01-31 00:00:00


#Pause the code
import datetime
import time

for i in range(3):
    print(i)#0 1 2
    print(datetime.datetime.now())
    print('----------')
    time.sleep(2)
    
#0
#2024-06-18 15:19:26.174366
#----------
#1
#2024-06-18 15:19:28.182577
#----------
#2
#2024-06-18 15:19:30.197712
#----------




