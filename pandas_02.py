import pandas as pd
df = pd.read_csv('nba.csv', index_col='Name')
print(df.head())
df.dropna(inplace=True)
print(df.describe())
print(df['Weight'].describe())

# using loc
print(df.loc[['Avery Bradley', 'Jeff Withey'], ['Team', 'College']])      # selecting some ows and some columns

print(df.loc[:, ['Team']])          # all rows some column

print(df.loc[['Avery Bradley', 'Jeff Withey'], :])       # some rows all columns

# using iloc

print(df.iloc[3])                               # using index number to access single row all columns
print(df.iloc[3:10])                            # selecting multiple rows and all columns
print(df.iloc[3:10, 2:4])                       # selecting rows  and columns in a range
print(df.iloc[[2, 3, 6]])                       # selecting rows with given index and all columns
print(df.iloc[[2, 3, 6], [2, 4]])               # selecting any row and any columns
print(df.iloc[:, [1, 2]])                       # all row some column
