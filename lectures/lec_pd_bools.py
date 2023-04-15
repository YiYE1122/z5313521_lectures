import pprint as pp

import pandas as pd


# ----------------------------------------------------------------------------
# Create an example dataset
# ----------------------------------------------------------------------------
data = {
    'date': [
        '2012-02-16 07:42:00',
        '2020-09-23 08:58:55',
        '2020-09-23 09:01:26',
        '2020-09-23 09:11:01',
        '2020-09-23 11:15:12',
        '2020-11-18 11:07:44',
        '2020-12-09 15:34:34',
        ],
    'firm': [
        'JP Morgan',
        'Deutsche Bank',
        'Deutsche Bank',
        'Wunderlich',
        'Deutsche Bank',
        'Morgan Stanley',
        'JP Morgan',
        ],
    'action': [
        'main',
        'main',
        'main',
        'down',
        'up',
        'up',
        'main',
        ],
}

# Convert the values in 'date' from a list to a `DatetimeIndex`
# Note: `pd.to_datetime` will return a `DatetimeIndex` instance if we pass it
# a list
data['date'] = pd.to_datetime(data['date'])
print(type(data['date'])) # --> <class 'pandas.core.indexes.datetimes.DatetimeIndex'>

# Create the dataframe and set the column 'date' as the index
df = pd.DataFrame(data=data).set_index('date')
print(df)

df.info()
cond = df.loc[:, 'action'] == 'up' # --> series with dtype: bool
print(cond)

res = df.loc[cond]
print(res)

crit = df.loc[:, 'action'].str.contains('up|down')
print(df.loc[crit])
