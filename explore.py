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

# Exercise 5
df['per_unit'] = df['revenue'] / df['quantity']
print(df.head())
print(df['per_unit'].mean())

# Exercise 6
print(df['region'].unique())
print(df['region'].value_counts())

# Exercise 7
select_df = df[['region', 'product', 'revenue']]
print(select_df.head())

# Exercise 8
df.to_csv('data.explored.csv', index=False)