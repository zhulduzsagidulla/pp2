#1
import datetime
date = datetime.datetime.now() - datetime.timedelta(5)
print(date)

#2
import datetime 
date1 = datetime.datetime.now() - datetime.timedelta(1)
date2 = datetime.datetime.now() 
date3 = datetime.datetime.now() + datetime.timedelta(1)
print(date1, date2, date3)

#3
import datetime 
date = datetime.datetime.now().strftime('%Y %m %d %H %I %M %S %f')
print(date)

#4
import datetime

date1 = datetime.datetime.now()
date2 = datetime.datetime.now() - datetime.timedelta(2)
print((date1 - date2).total_seconds())

