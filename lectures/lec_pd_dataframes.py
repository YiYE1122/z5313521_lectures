""" lec_pd_dataframes.py

Companion codes for the lecture on Dataframes
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

# Business (trading) day counter
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
#   Create two series
# ----------------------------------------------------------------------------

# Series with prices
prc_ser = pd.Series(data=prices, index=dates)

# Series with trading day
bday_ser = pd.Series(data=bday, index=dates)
print(prc_ser,bday_ser)

# ----------------------------------------------------------------------------
#   Create a dataframe
# ----------------------------------------------------------------------------
# Using the series we created above...

# Data Frame with close and Bday columns
df = pd.DataFrame({'Close': prc_ser, 'Bday': bday_ser})

print(df)
# Output:
#             Close  Bday
# 2020-01-02   7.16     1
# 2020-01-03   7.19     2
# 2020-01-06   7.00     3
# 2020-01-07   7.10     4
# 2020-01-08   6.86     5
# 2020-01-09   6.95     6
# 2020-01-10   7.00     7
# 2020-01-13   7.02     8
# 2020-01-14   7.11     9
# 2020-01-15   7.04    10

other_dates = [
  '2020-01-06',
  '2020-01-07',
  '2020-01-08',
  '2020-01-09',
  '2020-01-10',
  '2020-01-13',
  '2020-01-14',
  '2020-01-15',
  '2020-01-16',
  '2020-01-17',
  ]
other_bday = [
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        ]
new_bday_ser = pd.Series(data=other_bday, index=other_dates)
new_df = pd.DataFrame({'Close': prc_ser, 'Bday': new_bday_ser})
print(new_df)
# Returns:
#             Close  Bday
# 2020-01-02   7.16   NaN
# 2020-01-03   7.19   NaN
# 2020-01-06   7.00   3.0
# 2020-01-07   7.10   4.0
# 2020-01-08   6.86   5.0
# 2020-01-09   6.95   6.0
# 2020-01-10   7.00   7.0
# 2020-01-13   7.02   8.0
# 2020-01-14   7.11   9.0
# 2020-01-15   7.04  10.0
# 2020-01-16    NaN  11.0
# 2020-01-17    NaN  12.0
# ----------------------------------------------------------------------------
#   Accessing the indexes in a dataframe
# ----------------------------------------------------------------------------
# The attribute `columns` returns the column index
print(df.columns)

# Output:
# Index(['Close', 'Bday'], dtype='object')

print(type(df.columns))

# Output: <class 'pandas.core.indexes.base.Index'>

col0 = df['Close']
print(col0)
new_ser = pd.Series(data=[1,3,2], index=['a', 'c', 'b'])

# This will return 'False'

ss=new_df.iloc[1]-new_df.iloc[0]
