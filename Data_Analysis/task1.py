import pandas as pd
import matplotlib.pyplot as plt

# 1: Return the columns names as a list from the dataframe
df = pd.read_csv('transactions.csv')
column_names = df.columns.tolist()
# print(column_names)

# 2: Return the first k rows from the dataframe
k = 5
k_rows = df.head(k)
# print(k_rows)

# 3:Return a random sample of k rows from the dataframe
random_sample = df.sample(k)
# print(random_sample)

# 4: Return a list of unique transactions type
unique_transaction_type = df['type'].unique().tolist()
# print(unique_transaction_type)

# 5: Return pandas series of the top 10 transaction destinations with frequencies
top_10_transactions = df['nameDest'].value_counts().head(10)
# print(top_10_transactions) 

# 6: Return all the rows from the dataframe for which fraud is detected
fraud_detected_rows = df[df['isFraud']==1]
# print(fraud_detected_rows)

# 7: Return a dataframe that contains the number of distinct destinations that each source has interacted with to
# sorted in descending order 
distinct_destinations_per_source = df.groupby('oldbalanceDest')['newbalanceDest'].agg(lambda x: len(x.unique())).reset_index()
distinct_destinations_per_source = distinct_destinations_per_source.rename(columns={'newbalanceDest': 'distinct_destinations'})
distinct_destinations_per_source_sorted = distinct_destinations_per_source.sort_values(by='distinct_destinations', ascending=False)
# print(distinct_destinations_per_source_sorted)


# Transaction types bar chart
plt.figure(figsize=(10, 6))
df['type'].value_counts().plot(kind='bar')
plt.title('Transaction Types Bar Chart')
plt.xlabel('Transaction Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Transaction types split by fraud bar chart
plt.figure(figsize=(10, 6))
fraud_split = df.groupby(['type', 'isFraud']).size().unstack(fill_value=0)
fraud_split.plot(kind='bar', stacked=True)
plt.title('Transaction Types Split by Fraud Bar Chart')
plt.xlabel('Transaction Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(title='Fraud Detected', loc='upper right')
plt.show()
