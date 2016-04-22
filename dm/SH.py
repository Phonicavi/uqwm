import pandas as pd
import time
import datetime

AM = ''
PM = ''
one_minute = datetime.timedelta(minutes=1)


# AM9:30-11:30
x = datetime.datetime.strptime('09:30', "%H:%M")
for i in range(121):
    now = datetime.datetime.strftime(x, '%H:%M').decode('utf-8')
    AM += DataAPI.BarRTIntraDayOneMinuteGet(time=now, unit=u"", field="", pandas="0")
    x += one_minute

write('AM.csv', AM)

print AM

# PM13:01-15:00
x = datetime.datetime.strptime('13:01', "%H:%M")
for i in range(121):
    now = datetime.datetime.strftime(x, '%H:%M').decode('utf-8')
    PM += DataAPI.BarRTIntraDayOneMinuteGet(time=now, unit=u"", field="", pandas="0")
    x += one_minute

write('PM.csv', PM)

print PM