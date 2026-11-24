
# Reflection questions

# 1. A boolean filter is a method of filtering data in a Dataframe so that each row meets a condition. 
# Then it returns only those rows that meet that condition.

# 2. Using one bracket such as df["revenue"] returns a series. This is a single column of data. 
# On the other hand, using two brackets such as df[["revenue"]] returns a whole Dataframe. 
# This distinction matters when you want to use pandas operations that require a Dataframe, while others work with a series

# 3. If a collegue asked me explain why I'd choose pandas for this tast over excel, I would tell them that 
# pandas can process large datasets and it makes it easier to repreat the same analysits without manually completing each step 
# in excel.









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
df.to_csv('data/explored.csv', index=False) 