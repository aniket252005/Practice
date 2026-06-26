import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, np.nan, 30, 28, np.nan],
    "Marks": [85, 90, np.nan, 88, 92],
    "City": ["Delhi", "Mumbai", None, "Pune", "Delhi"]
})

print(df)

### LOC(Label-based indexing) ###

### Select a row
print(df.loc[2])

### Select one value
print(df.loc[1, "Marks"])

### Multiple Rows
print(df.loc[[0, 3]])

### Multiple Columns
print(df.loc[:, ["Name", "Marks"]])

### Condition
print(df.loc[df["Marks"] > 88])

### Update values
df.loc[df["Age"] > 27, "City"] = "Updated"
print(df)

### ILOC(Integer-location indexing) ###

### first row
print(df.iloc[0])

### First 3 rows
print(df.iloc[:3])

### Rows and columns
print(df.iloc[1:4, 0:2])

### Last row
print(df.iloc[-1])

### Remove missing values.  ###


### Remove rows containing NaN
df.dropna()

### Remove columns containing NaN
df.dropna(axis=1)

### Remove rows if all values are NaN
df.dropna(how="all")

### Keep rows with at least 3 non-null values
df.dropna(thresh=3)

### Remove rows where Age is missing
df.dropna(subset=["Age"])

### Replace missing values. ###

### Replace with 0
df.fillna(0)
print(df)

### Replace Age with average
df["Age"] = df["Age"].fillna(df["Age"].mean())

### Replace City
df["City"] = df["City"].fillna("Unknown")

### Forward Fill
df.fillna(method="ffill")

### Backward Fill
df.fillna(method="bfill")

print(df)


