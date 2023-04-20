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
#print(type(data['date'])) # --> <class 'pandas.core.indexes.datetimes.DatetimeIndex'>

# Create the dataframe and set the column 'date' as the index
df = pd.DataFrame(data=data).set_index('date')
#print(df)

# Output:
#                                firm action
# date
# 2012-02-16 07:42:00       JP Morgan   main
# 2020-09-23 08:58:55   Deutsche Bank   main
# 2020-09-23 09:01:26   Deutsche Bank   main
# 2020-09-23 09:11:01      Wunderlich   down
# 2020-09-23 11:15:12   Deutsche Bank     up
# 2020-11-18 11:07:44  Morgan Stanley     up
# 2020-12-09 15:34:34       JP Morgan   main

# ----------------------------------------------------------------------------
#   Creating groupby objects
# ----------------------------------------------------------------------------
groups = df.groupby(by='firm')
print(groups)

# Output:
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x7f8463863640>


print(groups.groups)

for firm, idx in groups.groups.items():
    print(f"Data for Firm == {firm}:")
    print("----------------------------------------")
    print(df.loc[idx])
    print("----------------------------------------")
    print("")

for firm, idx in groups.groups.items():
    nobs = len(df.loc[idx])
    print(f"Number of obs for Firm == {firm} is {nobs}")

print(df.iloc[-1])

def get_last(df):
    """ Sorts the dataframe on its index and returns
        last row of the sorted dataframe
    """
    df.sort_index(inplace=True)
    return df.iloc[-1]

for firm, idx in groups.groups.items():
    print(f"get_last applied to df[df.firm=='{firm}']:")
    print("----------------------------------------")
    print(get_last(df.loc[idx]))
    print("----------------------------------------")
    print("")

res = groups.apply(get_last)
print(res)

print(groups.groups.values())
list=[]

column_names=df.columns[:-1]
print(column_names)
print (df)