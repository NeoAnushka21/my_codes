import pandas as pd
df = pd.read_csv('nba.csv')

gb01 = df.groupby('Team').groups
print(gb01)
gb02 = df.groupby('Team')

print(gb02.first())    # show value of first element of each group

gb03 = df.groupby('College')
print(gb03.first())
