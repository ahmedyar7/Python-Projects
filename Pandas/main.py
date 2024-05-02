import pandas as pd
import numpy as np

# Creating the dataframe
dict_1 = {
    "name": ["harry", "rohaan", "skillf", "shub"],
    "marks": [12, 23, 43, 54],
    "city": ["quetta", "kolkata", "Karachi", "america"],
}
# where key are columns and the values are the rows for the each columns
# df = pd.DataFrame(dict_1)  # transfor the dictionary into the excel sheet format
# print(df)

# exporting to the csv.file
# df.to_csv("friend.csv", index=False)

# For seeing specific number of rows from start:
# print(df.head(3))

# for seeting the specific number of rows from the end then:
# print(df.tail(1))

# for describet the details of the table
# print(df.describe())

# Reading from the CSV:
friend_df = pd.read_csv("friend.csv")
# print(friend_df)

# Retreving the specific inforomation from the dataframe:
# print(friend_df["marks"])
# print(friend_df["TrainNum"])
# print(friend_df["city"])

# Retreving the specific index information
# print(friend_df["marks"][0])
# print(friend_df["TrainNum"][2])
# print(friend_df["city"][1])


# Creting the series:
# ser = pd.Series(np.random.rand(2))
# print(type(ser))
# print(ser)

newdf = pd.DataFrame(np.random.rand(334, 5), index=np.arange(334))
# print(type(newdf))
# print(newdf.describe())
# print(newdf.dtypes())

# print(newdf.index)
# print(newdf.columns)

# converting to numpy array:
# print(newdf.to_numpy())

## Transpose:
# print(newdf.T)
