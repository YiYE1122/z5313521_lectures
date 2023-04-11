import pandas as pd

data = {
      'col_a': [1, 2, 3],
      'col_b': [10.0, None, 13.0],
      }
print(data)
# First a data frame without a user-defined index
df0 = pd.DataFrame(data)
print('\nprint(df0) -->')
print(df0)
print('\ndf0.info() --> ')
df0.info()


# A data frame with a strings as index labels
idx = ['2020-01-01', '2020-01-02', '2020-01-03']
df1 = pd.DataFrame(data, index=idx)
print('\nprint(df1) -->')
print(df1)
print('\ndf1.info() --> ')
df1.info()

# A data frame with a datetime objs as index labels
idx_dt = pd.to_datetime(idx)
df2 = pd.DataFrame(data, index=idx_dt)
print('\nprint(df2) -->')
print(df2)
print('\ndf2.info() --> ')
df2.info()