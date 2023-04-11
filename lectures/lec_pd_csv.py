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