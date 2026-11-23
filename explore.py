# Excersise 1

import pandas as pd

df = pd.read_csv('data/retail_sales.csv')

print(df.shape)

# Exercise 2

south = df[df['region'] == 'South']
print(len(south))
print(south.head())

# Exercise 3
highest_revenue = df.sort_values('revenue', ascending=False).head(5)
print(highest_revenue)

# Exercise 4
big_south = df[(df['region']=='South') & (df['revenue']>10000)]
print(len(big_south))
print(big_south.head(5))