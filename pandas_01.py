import pandas as pd

# creating a data frame from list , this will have just one column
list_a1 = ['hi', 'how', 'are', 'you']
df1 = pd.DataFrame(list_a1)
print(df1)
# to get more than one column and give column name
list_a2 = {'Numbers': [1, 2, 3, 4, 5], 'words': ['one', 'two', 'three', 'four', 'five']}
df2 = pd.DataFrame(list_a2)
print(df2)

# creating data frame from a dict
dict_01 = {'Name': ['Jai', 'Anuj', 'Jai', 'Princi', 'Gaurav', 'Anuj', 'Princi', 'Abhi'],
           'Age': [27, 24, 22, 32, 33, 36, 27, 32],
           'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj', 'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'],
           'Qualification': ['Msc', 'MA', 'MCA', 'Phd', 'B.Tech', 'B.com', 'Msc', 'MA']}

df3 = pd.DataFrame(dict_01)
print(df3)

df = pd.read_csv('nba.csv')
# df = pd.read_csv('nba.csv', index_col='Name')  # making name column as index
print(df.head())
print(df.columns)
print(df['Age'])
                       # displaying rows from 3 to 9 and columns from 2 to 3
print(df.loc[(df.Name == 'John Holland')])      # using label name
print(df.isnull())                             # get true value where the cell is empty
print(df.dropna())                             # to delete rows with at least one Nan value(s)
print(df.fillna(0))                            # put zero in the empty cells

"""for i, j in df.iterrows():
    print(i, j)"""

l1 = df.columns
print(l1)
for i in l1:
    print(df[i][2])

# series in pandas
df = pd.read_csv('nba.csv')
series_01 = pd.Series(df['Name'])
sr01 = series_01.head()
print(sr01)        # to get  names from 'Name' column in a series
print(sr01[0:3])

