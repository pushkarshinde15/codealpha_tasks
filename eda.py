import pandas as pd

# Load dataset
df = pd.read_csv("quotes_dataset.csv")

# View first 5 rows
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nBasic Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())


print("\nNumber of unique authors:")
print(df['Author'].nunique())

print("\nTop 5 authors by number of quotes:")
print(df['Author'].value_counts().head())


import matplotlib.pyplot as plt

# Top 5 authors visualization
df['Author'].value_counts().head().plot(kind='bar')
plt.title("Top 5 Authors by Number of Quotes")
plt.xlabel("Author")
plt.ylabel("Number of Quotes")
plt.show()
