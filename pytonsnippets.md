#  Pandas

## EDA

```
# Get info on dataset
df.info()

# List all df columns
df.columns

# Show first few rows of dataset
df.head()

# Show last few rows of dataset
df.tail()

# Number of rows in df
len(df)

# counts null values
df.isnull()

# counts NA values
df.isna()

# counts values that aren't NA
df.notna()

# assert that there are no missing values in the dataframe
assert pd.notnull(df).all().all()

# assert all values are greater than 0

assert (df >=0).all().all()
```


## Filters and queries 

```
# Show specific rows and columns
df.iloc[2:10, 5:10]

# Show specific row numbers and column names
df.loc[[3, 10, 14, 23], ["nationality", "weight_kg", "height_cm"]]

# Filter rows in df
df.query("shooting > passing")

# Show all dtypes of df columns
df.dtypes

# select the variables or columns of a certain data type
df.select_dtypes(include="int64")

# query a dataset based on a boolean condition
df["random_col"].where(df["random_col"] > 50)

# used to find out the unique values of a categorical column
df.skill_moves.unique()

# remove duplicates from a list
unique_list = list(set(numbers))

# find most common element
from collections import Counter
most_common = Counter(numbers).most_common(1)

# make a subset of the dataset that will contain only a few nationalities of players using .isin() function
nationality = ["Argentina", "Portugal", "Sweden", "England"]
df[df.nationality.isin(nationality)]

# provides some basic statistical measures
df["wage_eur"].describe()

# number of data in the DataFrame in the specified direction.
# When the direction is 0, it provides the number of data in the columns.
# When the direction is 1, it provides the number of data in the rows
df.count(level="Pclass")
```


## Totals and grouping

```
# provides you with the cumulative sum of all the values of the previous rows
df[["value_eur", "wage_eur"]].cumsum()

# lets you know how many unique values do you have in a column
df.nationality.nunique()

# group the data as per a certain variable
df.groupby("death")[
    "creatinine_phosphokinase",
    "ejection_fraction",
    "platelets",
    "serum_creatinine",
    "serum_sodium",
    "time",
].agg([np.mean, np.median])
.sum()

# value counts of each category
df["Pclass"].value_counts(sort=True, ascending=True, normalize=True)

# Melted the data
melted_df_single_var = pd.melt(df, id_vars=['Date', 'City'], var_name='Variable', value_name='Value')

# Melt the data with multiple value_vars
melted_df = pd.melt(df, id_vars=['Date', 'City'], value_vars=['Temperature', 'Humidity'], var_name='Variable', value_name='Value')

# Stack - pivot the innermost column index to become the innermost row index
stacked_df = df.set_index(['Date', 'City']).stack()

# Unstack - pivot the innermost row index to become the innermost column index
unstacked_df = stacked_df.unstack()

# Pivot Table
pivot_table_df = df.pivot_table(index='Date', columns='City', values=['Temperature', 'Humidity'], aggfunc='mean')

# Wide to Long
long_df = pd.wide_to_long(df, stubnames=['Temperature', 'Humidity'], i=['Date', 'City'], j='Variable', sep='_').reset_index()

pd.crosstab(
    df["league_rank"], df["international_reputation"]
)  # gives you a frequency table that is a cross-tabulation of two variables

# bins the data or segments the data based on the distribution of the data
pd.qcut(df["value_eur"], q=5)

# provide number of bins and split up dataset
pd.cut(df["value_eur"], bins=5).value_counts()

# percentage change between the current and a prior element in a Series or DataFrame
data = {
    "date": pd.date_range(start="2022-01-01", end="2022-01-05"),
    "price": [100, 105, 98, 110, 120],
}

df = pd.DataFrame(data).set_index("date")

df["price"].pct_change()

# Calculate rolling mean with a 7-day window
rolling_mean = data['value'].rolling(window=7).mean()

# Compute exponential moving average (EMA)
ema = data['value'].ewm(span=10).mean()

# find intersection of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection = set1 & set2
```

## Update dataset

```
# When we reset the index, the old index is added as a column, and a new sequential index is used:
df.reset_index(names=['classes', 'names'])

# slice list
subset = numbers[2:5]

# list comprehension
squared_dict = {x: x**2 for x in range(5)}

# zip lists
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
person_info = dict(zip(names, ages))

# Append dataframes using result
result = df1.append([df2, df3])

# Append dataframes using pd.concat
frames = [df1, df2, df3]
result = pd.concat(frames)

# Drop columns from df
df = df.drop(columns=["Unnamed: 0", "weak_foot", "real_face"])

# replaces the values of a column
df.replace(1.0, 1.1)

# rename columns
df.rename(columns={"weight_kg": "Weight (kg)", "height_cm": "Height (cm)"})

# Update segment of data
df.loc[(df['COUNCIL'] == 'LEEDS') & (df['POSTCODE'] == 'LS8'), ['CCG']] = 'LEEDS NORTH CCG'

# replaces the null values with some other value of your choice
df["pace"].fillna(0, inplace=True)

# drop null values
df.dropna()

# Drop duplicates
people = people.drop_duplicates(subset="Name")

# Drop columns from dataframe
to_drop = ['Edition Statement', 'Corporate Author', 'Corporate Contributors', 'Former owner', 'Engraver', 'Contributors',
            'Issuance type',
            'Shelfmarks']
df.drop(to_drop, inplace=True, axis=1)

# Convert to DateTime format
pd.to_datetime(people["Graduation"])

# Change all strings to lower case in a column
people["Standing"] = people["Standing"].str.lower()

# Handling invalid values
df["height(cm)"] = pd.to_numeric(df["height(cm)"], errors='coerce')

# Split columns
df[['age','sex']] = df.age_sex.str.split("_", expand = True)

# Reorder column labels
df = df[['fname','lname','age','sex','section','height(cm)','weight(kg)','spend_A','spend_B','spend_C']]

#  unpivots a DataFrame from wide format to long format
#  massage a DataFrame into a format where one or more columns are identifier variables, while all other columns, considered measured variables, are unpivoted to the row axis, leaving just two non-identifier columns, variable and value.
pd.melt(df, id_vars=['A'], value_vars=['B'])

# Explode function to to reformat it in a way that there is a separate row for each item in that list
df_new = df.explode(column="data").reset_index(drop=True)

# Assign: reate a new DataFrame with additional columns, assigning values based on existing columns or operations
df.assign(value_cat=np.where(df["Value"] > 20, "high", "low"))
df.assign(value_cat=np.where(df["Value"] > 20, "high", "low")).groupby(
    "value_cat"
).mean()

#combine_first: choosing values from the first Series and filling in any missing values with the corresponding values from the second Series
s1 = pd.Series([1, 2, np.nan, 4, np.nan, 6])
s2 = pd.Series([10, np.nan, 30, 40, np.nan, 60])

s1.combine_first(s2)

s3 = pd.Series([1, 2, 3, 4, 5, 6])
s1.combine_first(s2).combine_first(s3)

# Sort List based on another List
list1 =  ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
list2 = [ 0, 1, 1, 1, 2, 2, 0, 1, 1, 3, 4]
C = [x for _, x in sorted(zip(list2, list1), key=lambda pair: pair[0])]
print(C) # ['a', 'g', 'b', 'c', 'd', 'h', 'i', 'e', 'f', 'j', 'k']

# Reading lines from a file until an empty line is encountered using walrus
# allows for assignment and return of a value within an expression
with open('myfile.txt') as file:
    while (line := file.readline().rstrip()):
        print(line)
```

# Numpy

```
# Find out number of dimensions in array
df.ndim

# generate equally spaced values within a given interval
np.arange(5, 11, 2)

# Create linearly spaced array
linear_spaced = np.linspace(0, 1, 5)  # 5 values from 0 to 1

# Accessing Array Elements
element = a[2]  # Retrieve the third element of array 'a'
row = reshaped[1, :]  # Retrieve the second row of 'reshaped'

# Boolean indexing
filtered = a[a > 2]  # Elements of 'a' greater than 2

# transpose a NumPy array
a = np.arange(12).reshape((6, 2))
a.transpose()

# sort the array in-place
np.sort(a) ## sort based on rows
np.sort(a, axis=None) ## sort the flattened array
np.sort(a, axis=0) ## sort based on columns

```

# Regular expressions

```
# Replace text
replaced_text = re.sub(r"string", "sentence", text)
print(replaced_text)
```

## Misc

```
# Chain custom functions
result = (
    df.pipe(subtract_federal_tax)
      .pipe(subtract_state_tax, rate=0.12)
      .pipe(
          (subtract_national_insurance, 'df'),
          rate=0.05,
          rate_increase=0.02
      )
)
print(result)

# # Normalize numeric columns
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df[['numeric_column']] = scaler.fit_transform(df[['numeric_column']]

# Create permutations
from itertools import permutations
paths = permutations([1, 2, 3])  # Generate all permutations of the list [1, 2, 3]
for path in paths:
    print(path)

# Create a DataFrame from a JSON file
import json

with open("data.json") as f:
    data = json.load(f)

data
# output
{'data': [{'id': 101,
   'category': {'level_1': 'code design', 'level_2': 'method design'},
   'priority': 9},
  {'id': 102,
   'category': {'level_1': 'error handling', 'level_2': 'exception logging'},
   'priority': 8}]}

df = pd.json_normalize(data, "data")

# pretty printing
import pprint
data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
pprint.pprint(data)
```