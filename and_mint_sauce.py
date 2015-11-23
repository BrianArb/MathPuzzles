#!/usr/bin/env python

import datetime
import sys


NUMBER_OF_WOLVES = 6

for minute in xrange(1, sys.maxint):
  time_stamp = (datetime.datetime(1972, 1, 1) +
    datetime.timedelta(minutes=minute*NUMBER_OF_WOLVES)).strftime('%H:%M:%S')
  print NUMBER_OF_WOLVES * minute, time_stamp
  if time_stamp == '01:00:00':
    break

