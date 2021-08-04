#date
import datetime

from datetime import date

today = date.today()
print("Today's date:", today)

#
import time
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))

#
from datetime import date 
   
todays_date = date.today()  
print("Current date: ", todays_date) 
print("Current year:", todays_date.year) 
print("Current month:", todays_date.month) 
print("Current day:", todays_date.day)

#
import datetime
now=datetime.datetime.now().year
print("year :",now)

#
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))
x = datetime.datetime(2020, 5, 19)
print(x.strftime("%B"))

today = datetime.today()
print("Current date =", today)

a = datetime(11, 34, 56)
print("hour =", a.hour)
print("minute =", a.minute)
print("second =", a.second)
print("microsecond =", a.microsecond)
