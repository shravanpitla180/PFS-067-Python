#Pandas library
'''
--> pandas is a python library used for working with strcctured data...
-->pandas works on data that looks like a table.
-->ex: csv files, excelfiles, databases, data analysis projects.

series--one column
dataframe--multiple columns +rows

'''
#eg:
#pandas series --1D labeled data strcuture

import pandas as pd
marks=pd.Series([10,20,30,40,50])
print(marks)
print(marks.iloc[1])

#2
marks =pd.Series(
    [80,90,30,50],
    index=["A","B","C","D"]
)
print(marks.loc["B"])

#3 series operations
marks=pd.Series([80,90,70])
print(marks+5)
print(marks*2)
print(marks-10)

# Dataframe--2D labled data structure
import pandas as pd
data={
    "Name":["A","B","C","D"],
    "Age": [21,22,23,24],
    "Marks":[85,90,95,74]
} 
dataframe=pd.DataFrame(data)
print(dataframe)
print(dataframe[["Name", "Marks"]]) #accessing by coloumn ,use--[[]]
print(dataframe.iloc[0])
# Accessing specific data
print(dataframe.loc[1, "Marks"])
print(dataframe.shape)

# Reading CSV files
# Name, Age, Marks
# A, 21, 85
# B, 22, 83
# C, 25, 80

import pandas as pd
df = pd.read_csv("Annual.csv")
# print(df.head(10))
# print(df.tail())
# print(df.info())
print(df.describe())


# # Data Cleaning Basics
# # Finding Missing Values
import pandas as pd 
dd = pd.read_csv("Annual.csv")
print(dd.isnull())
print(dd.isnull().sum())

# Removing Missing Rows
dd = dd.dropna()

# Filling Missing Values
dd["year"] = dd["year"].fillna(2026)


# Duplicates Data
print(dd.duplicated())

# Remove Duplicates
dd = dd.drop_duplicates()

# Changing Column Names
dd = dd.rename(columns={"industry_co_ANZSIC":"ANZ"})
print(dd.head())

# Filter

result = dd[dd["year"]>2011]
print(result)