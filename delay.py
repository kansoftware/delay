#!/usr/bin/python3
import datetime
import time
import sys

param_value = None
if len(sys.argv) > 1:
    param_value = sys.argv[1]
else:
    exit(1)

now = datetime.datetime.now()

curr_time = "{:2}:{:2}".format(now.hour, now.minute)
print("curr_time: {}".format(curr_time))

base = datetime.date.today()

if not param_value is None :
    if param_value <= curr_time:
        base = datetime.date.today() + datetime.timedelta(days=1)

dt = param_value.split(":")

twu = datetime.datetime(base.year, base.month, base.day, int(dt[0]), int(dt[1]) )
print("wakeup_time: {}".format(twu))

dlt = twu - now
print("sleep to: {}".format(dlt))

time.sleep( dlt.seconds )

exit(0)

