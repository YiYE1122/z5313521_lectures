""" lec_pd_csv.py

Companion codes for the lecture on reading and writing CSV files with Pandas
"""

import os

import pandas as pd

import toolkit_config as cfg

QAN_PRC_CSV = os.path.join(cfg.DATADIR, 'qan_prc_2020.csv')
QAN_NOHEAD_CSV = os.path.join(cfg.DATADIR, 'qan_prc_no_header.csv')
QAN_CLOSE_CSV = os.path.join(cfg.DATADIR, 'qan_close_ser.csv')

# Load the data contained in qan_prc_2020.csv to a DF
qan_naive_read = pd.read_csv(QAN_PRC_CSV)
print(qan_naive_read)

qan_naive_read.info()

qan_naive_read.set_index('Date', inplace=True)
print(qan_naive_read)

qan_naive_read.info()


qan_better_read = pd.read_csv(QAN_PRC_CSV, index_col='Date')
print(qan_better_read)


qan_better_read.info()


# ----------------------------------------------------------------------------
#   Storing data to a CSV file
# ----------------------------------------------------------------------------
# First, we read the data into a dataframe
qan_better_read = pd.read_csv(QAN_PRC_CSV, index_col='Date')

# We then save the data into the file located at QAN_NOHEAD_CSV above.
# The column headers will not be saved
qan_better_read.to_csv(QAN_NOHEAD_CSV, header=False)

qan_better_read = pd.read_csv(QAN_PRC_CSV, index_col='Date')
ser = qan_better_read.loc[:, 'Close']
print(ser)

# Output:
#  Date
#  2020-01-02    7.16
#  2020-01-03    7.19
#  2020-01-06    7.00
#  2020-01-07    7.10
#  2020-01-08    6.86
#                ...
#  2020-12-22    4.80
#  2020-12-23    4.91
#  2020-12-24    4.89
#  2020-12-29    4.96
#  2020-12-30    4.96
#  Name: Close, Length: 254, dtype: float64


# Save the series to a CSV file
ser.to_csv(QAN_CLOSE_CSV)

# Create a series without a name
dates = list(qan_better_read.index) # --> list with the index labels
data = list(qan_better_read.Close)  # --> list with closing prices
ser_no_name = pd.Series(data, index=dates)
print(ser_no_name)

ser_no_name.to_csv(QAN_CLOSE_CSV)

