### PANDAS100 ###

# 1. Import pandas as pd
import pandas as pd

# 2. Print pandas version
print(pd.__version__)

# 3. Print complete pandas version information
pd.show_versions()

## 4. Create the DataFrame

import pandas as pd
import numpy as np

data = {
    'animal': ['cat', 'cat', 'snake', 'dog', 'dog',
               'cat', 'snake', 'cat', 'dog', 'dog'],
    'age': [2.5, 3, 0.5, np.nan, 5,
            2, 4.5, np.nan, 7, 3],
    'visits': [1,3,2,3,2,3,1,1,2,1],
    'priority': ['yes','yes','no','yes','no',
                 'no','no','yes','no','no']
}

labels = ['a','b','c','d','e','f','g','h','i','j']

df = pd.DataFrame(data, index=labels)


## 5. Display basic information

df.info()

## 6. Return first 3 rows

df.head(3)

## 7. Select animal and age columns

df[['animal', 'age']]

## 8. Select rows [3,4,8] and columns ['animal','age']

df.iloc[[3,4,8]][['animal','age']]

## 9. Rows where visits > 3

df[df['visits'] > 3]

## 10. Rows where age is NaN

df[df['age'].isna()]

## 11. Cats with age < 3

df[(df['animal'] == 'cat') & (df['age'] < 3)]

## 12. Age between 2 and 4 inclusive

df[df['age'].between(2,4)]

## 13. Change age in row 'f' to 1.5

df.loc['f', 'age'] = 1.5

## 14. Total visits

df['visits'].sum()

## 15. Mean age for each animal

df.groupby('animal')['age'].mean()

## 16. Add row 'k' then delete it

df.loc['k'] = ['dog', 4.5, 2, 'yes']

# Delete it
df = df.drop('k')

## 17. Count each animal

df['animal'].value_counts()

## 18. Sort by age (descending) then visits (ascending)

df.sort_values(by=['age','visits'],
               ascending=[False, True])

## 19. Replace yes/no with True/False

df['priority'] = df['priority'].map({
    'yes': True,
    'no': False
})

## 20. Replace snake with python

df['animal'] = df['animal'].replace('snake', 'python')

## 21. Pivot table

df.pivot_table(values='age',
               index='animal',
               columns='visits',
               aggfunc='mean')

## 22. Remove consecutive duplicate values

df = pd.DataFrame({'A':[1,2,2,3,4,5,5,5,6,7,7]})

df.loc[df['A'].shift() != df['A']]

## 23. Subtract row mean

df = pd.DataFrame(np.random.random((5,3)))

df.sub(df.mean(axis=1), axis=0)

## 24. Column with smallest sum

df = pd.DataFrame(
    np.random.random((5,10)),
    columns=list('abcdefghij')
)

df.sum().idxmin()

## 25. Count unique rows

df = pd.DataFrame(np.random.randint(0,2,(10,3)))

len(df.drop_duplicates())

## 26. Find third NaN column

nan = np.nan

data = [
[0.04,nan,nan,0.25,nan,0.43,0.71,0.51,nan,nan],
[nan,nan,nan,0.04,0.76,nan,nan,0.67,0.76,0.16],
[nan,nan,0.5,nan,0.31,0.4,nan,nan,0.24,0.01],
[0.49,nan,nan,0.62,0.73,0.26,0.85,nan,nan,nan],
[nan,nan,0.41,nan,0.05,nan,0.61,nan,0.48,0.68]
]

columns = list('abcdefghij')

df = pd.DataFrame(data, columns=columns)

df.isna().apply(lambda x: x.index[x].tolist()[2], axis=1)

## 27. Sum of largest three values per group

df = pd.DataFrame({
    'grps': list('aaabbcaabcccbbc'),
    'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]
})

df.groupby('grps')['vals'].apply(lambda x: x.nlargest(3).sum())

## 28. Sum B for groups of 10 in A

df = pd.DataFrame(
    np.random.RandomState(8765).randint(1,101,(100,2)),
    columns=['A','B']
)

df.groupby(pd.cut(df['A'], np.arange(0,101,10)))['B'].sum()

## 29. Count distance from previous zero

df = pd.DataFrame({
    'X':[7,2,0,3,4,2,5,0,3,4]
})

df['Y'] = df.groupby(df['X'].eq(0).cumsum()).cumcount()

print(df)

## 30. Locations of the three largest values

df = pd.DataFrame(
    np.random.RandomState(30).randint(1,101,(8,8))
)

result = list(
    df.unstack()
      .sort_values(ascending=False)
      .index[:3]
)

print(result)

