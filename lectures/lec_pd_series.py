""" lec_pd_series.py

Companion codes for the lecture on pandas Series
"""

import pandas as pd


# ----------------------------------------------------------------------------
#   The dates and prices lists
# ----------------------------------------------------------------------------
dates = [
  '2020-01-02',
  '2020-01-03',
  '2020-01-06',
  '2020-01-07',
  '2020-01-08',
  '2020-01-09',
  '2020-01-10',
  '2020-01-13',
  '2020-01-14',
  '2020-01-15',
  ]

prices = [
  7.1600,
  7.1900,
  7.0000,
  7.1000,
  6.8600,
  6.9500,
  7.0000,
  7.0200,
  7.1100,
  7.0400,
  ]



# Create a series object
ser = pd.Series(data=prices, index=dates)
print(ser)
# Select Qantas price on '2020-01-02' ($7.16) using ...

# ... the `prices` list
prc0 = prices[dates.index('2020-01-02')]
print(prc0)

# ... the `ser` series
prc1 = ser['2020-01-02']
print(prc1)

ary = ser.array
print(ary)

print(type(ser.array))

# Use the `index` attribute to get the index from a series
the_index = ser.index
print(the_index)

# ----------------------------------------------------------------------------
#   Create a dataframe
# ----------------------------------------------------------------------------
# Using the series we created above...

print(1+ser)