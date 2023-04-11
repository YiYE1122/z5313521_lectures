""" lec_pd_joins.py

Companion codes for the lecture on combining pandas objects
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

# Trading day counter
bday = [
  1,
  2,
  3,
  4,
  5,
  6,
  7,
  8,
  9,
  10]

# ----------------------------------------------------------------------------
#   Example series and data frame
# ----------------------------------------------------------------------------

# Series with prices
ser = pd.Series(data=prices, index=dates)
# Data Frame with close and bday columns
df = pd.DataFrame({'close': ser, 'bday': bday})


# ----------------------------------------------------------------------------
#   Review: The operator "+" behaves differently depending on the operands
# ----------------------------------------------------------------------------
# Simple sums with integers
print(1 + 1)              # --> 2

# String concatenation
print('1' + '1')          # --> '11'

# List concatenation
print([1] + [2, 3])       # --> [1, 2, 3]


# ----------------------------------------------------------------------------
#   Adding a scalar to a series
# ----------------------------------------------------------------------------
# ser is:
#  2020-01-02    7.16
#  2020-01-03    7.19
#  2020-01-06    7.00
#  2020-01-07    7.10
#  2020-01-08    6.86
#  2020-01-09    6.95
#  2020-01-10    7.00
#  2020-01-13    7.02
#  2020-01-14    7.11
#  2020-01-15    7.04
#  dtype: float64


# Adding an integer to a series of floats
new_ser = ser + 1
print(new_ser)

# Output:
#  2020-01-02    8.16
#  2020-01-03    8.19
#  2020-01-06    8.00
#  2020-01-07    8.10
#  2020-01-08    7.86
#  2020-01-09    7.95
#  2020-01-10    8.00
#  2020-01-13    8.02
#  2020-01-14    8.11
#  2020-01-15    8.04
#  dtype: float64


# If you try to add a string, an exception will be raised
# (Uncomment to test)
#new_ser = ser + '1'  # --> Exception

# We can add a string to a series containing strings
s0 = pd.Series(['1', '2', '3'])
s1 = s0 + '1'
print(s1)

print(ser + ser[:-1])

s2 = pd.Series([1,2], index=['2900-01-01', '2900-01-02'])

print(s2)
# Output:
#   2900-01-01    1
#   2900-01-02    2
#   dtype: int64

print(ser + s2)

left = pd.DataFrame(
        data=[('L1'), ('L2'), ('L3')],
        index=[1,2,3],
        columns=['L'],
        )
print(left)

right = pd.DataFrame(
        data=[('R3'), ('R4'), ('R5')],
        index=[3,4,5],
        columns=['R'],
        )
print(right)

print(left.join(right, how='left'))

print(left.join(right, how='inner'))

print(left.join(right, how='outer'))
