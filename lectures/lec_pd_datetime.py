""" lec_pd_datetime.py

Companion codes for the lecture on working with time-series data in Pandas
"""
import os
import datetime as dt

import pandas as pd

import toolkit_config as cfg

CSVLOC = os.path.join(cfg.DATADIR, 'tsla_prc.csv')

# Instance of `dt.datetime` with the current date/time
dt_now = dt.datetime.now()

# This will produce a string representing the date/time in `dt_now`
print(dt_now)

# This will confirm that `dt_now` is an instance of the `datetime` class
print(type(dt_now)) # --> <class 'datetime.datetime'>

# Create a datatime object
date = dt.datetime(year=2020, month=12, day=31, hour=0)

# Create a string with the representation we want:
s = date.strftime('%d-%m-%Y')
print(s)


# Output:
#  '2020-12-31'
