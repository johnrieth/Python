import pandas as pd

hour = pd.read_csv("/home/code/Python/hour.csv")
# print(hour.head())

# calculating summary statistics
print(hour["count"].mean())
print(hour["count"].median())
print(hour["count"].std())
print(hour["registered"].min())
print(hour["registered"].max())

# prints summary statistics
print(hour.describe())
