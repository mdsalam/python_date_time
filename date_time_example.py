# python date time

import time
import calendar

localtime = time.localtime(time.time())
print "Local current time :", localtime

# getting formatted time
ft = time.asctime( time.localtime(time.time()) )
print "Local current time :", localtime

# calendar for a month
cal = calendar.month(2008,1)
print "Here is the calendar: "
print cal
