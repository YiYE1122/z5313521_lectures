""" lec_pd_indexing.py

Companion codes for the lecture on indexing pandas objects
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
#   Create instances
# ----------------------------------------------------------------------------

# Create a series object
ser = pd.Series(data=prices, index=dates)
print(ser)

# Data Frame with close and Bday columns
df = pd.DataFrame(data={'Close': ser, 'Bday': bday}, index=dates)
print(df)

# ----------------------------------------------------------------------------
#   Outline:
#
#   1. Selection using loc (label based)
#     1.1 Series:
#       1.1.1 Selection using a single label
#       1.1.2 Selection using sequence of labels
#       1.1.3 Selection using slices
#     1.2 DataFrame:
#       1.2.1 Selection using a single label
#       1.2.2 Selection using sequence of labels
#       1.2.3 Selection using slices
#
#   2. Selection using iloc (position based)
#     2.1 Series:
#       2.1.1 Selection using a single label
#       2.1.2 Selection using sequence of labels
#       2.1.3 Selection using slices
#     2.2 DataFrame:
#       2.2.1 Selection using a single label
#       2.2.2 Selection using sequence of labels
#       2.2.3 Selection using slices
#
#   3. Selection using []
#     3.1 Series:
#       3.1.1 label, list of labels, label slices
#       3.1.2 position, list of positions, position slices
#
#     3.2 DataFrame:
#       3.2.1 column label, list of column labels
#       3.2.2 row label slices
#       3.2.3 row position slices
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
#  1. Selection using .loc
#   (only works with labels)
# ----------------------------------------------------------------------------

# 1.1 Series
# -------------