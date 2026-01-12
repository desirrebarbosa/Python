# Working with Data in Python Cheat Sheet

## Reading and Writing Files

### File Opening Modes
Different modes to open files for specific operations.

**Syntax:**
- `r` - reading
- `w` - writing
- `a` - appending
- `+` - updating (read/write)
- `b` - binary (otherwise text)

**Examples:**
```python
# Read mode
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# Write mode
with open("output.txt", "w") as file:
    file.write("Hello, world!")

# Append mode
with open("log.txt", "a") as file:
    file.write("Log entry: Something happened.")

# Read/write mode
with open("data.txt", "r+") as file:
    content = file.read()
    file.write("Updated content: " + content)
```

### File Reading Methods
Different methods to read file content in various ways.

**Syntax:**
```python
file.readlines()  # reads all lines as a list
file.readline()   # reads the next line as a string
file.read()       # reads the entire file content as a string
```

**Example:**
```python
with open("data.txt", "r") as file:
    lines = file.readlines()
    next_line = file.readline()
    content = file.read()
```

### File Writing Methods
Different write methods to write content to a file.

**Syntax:**
```python
file.write(content)      # writes a string to the file
file.writelines(lines)   # writes a list of strings to the file
```

**Example:**
```python
lines = ["Hello\n", "World\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)
```

### Iterating Over Lines
Iterates through each line in the file using a loop.

**Syntax:**
```python
for line in file:
    # Code to process each line
```

**Example:**
```python
with open("data.txt", "r") as file:
    for line in file:
        print(line)
```

### open() and close()
Opens a file, performs operations, and explicitly closes the file using the `close()` method.

**Syntax:**
```python
file = open(filename, mode)
# Code that uses the file
file.close()
```

**Example:**
```python
file = open("data.txt", "r")
content = file.read()
file.close()
```

### with open()
Opens a file using a with block, ensuring automatic file closure after usage.

**Syntax:**
```python
with open(filename, mode) as file:
    # Code that uses the file
```

**Example:**
```python
with open("data.txt", "r") as file:
    content = file.read()
```

## Pandas

### Import pandas
Imports the Pandas library with the alias pd.

**Syntax:**
```python
import pandas as pd
```

### .read_csv()
Reads data from a CSV file and creates a DataFrame.

**Syntax:**
```python
dataframe_name = pd.read_csv("filename.csv")
```

**Example:**
```python
df = pd.read_csv("data.csv")
```

### .read_excel()
Reads data from an Excel file and creates a DataFrame.

**Syntax:**
```python
dataframe_name = pd.read_excel("filename.xlsx")
```

**Example:**
```python
df = pd.read_excel("data.xlsx")
```

### .to_csv()
Writes DataFrame to a CSV file.

**Syntax:**
```python
dataframe_name.to_csv("output.csv", index=False)
```

**Example:**
```python
df.to_csv("output.csv", index=False)
```

### Access Columns
Accesses a specific column using [] in the DataFrame.

**Syntax:**
```python
dataframe_name["column_name"]              # Accesses single column
dataframe_name[["column1", "column2"]]     # Accesses multiple columns
```

**Example:**
```python
df["age"]
df[["name", "age"]]
```

### describe()
Generates statistics summary of numeric columns in the DataFrame.

**Syntax:**
```python
dataframe_name.describe()
```

**Example:**
```python
df.describe()
```

### drop()
Removes specified rows or columns from the DataFrame. `axis=1` indicates columns. `axis=0` indicates rows.

**Syntax:**
```python
dataframe_name.drop(["column1", "column2"], axis=1, inplace=True)
dataframe_name.drop(index=[row1, row2], axis=0, inplace=True)
```

**Example:**
```python
df.drop(["age", "salary"], axis=1, inplace=True)  # Will drop columns
df.drop(index=[5, 10], axis=0, inplace=True)      # Will drop rows
```

### dropna()
Removes rows with missing NaN values from the DataFrame. `axis=0` indicates rows.

**Syntax:**
```python
dataframe_name.dropna(axis=0, inplace=True)
```

**Example:**
```python
df.dropna(axis=0, inplace=True)
```

### duplicated()
Duplicate or repetitive values or records within a data set.

**Syntax:**
```python
dataframe_name.duplicated()
```

**Example:**
```python
duplicate_rows = df[df.duplicated()]
```

### Filter Rows
Creates a new DataFrame with rows that meet specified conditions.

**Syntax:**
```python
filtered_df = dataframe_name[(Conditional_statements)]
```

**Example:**
```python
filtered_df = df[(df["age"] > 30) & (df["salary"] < 50000)]
```

### groupby()
Splits a DataFrame into groups based on specified criteria, enabling subsequent aggregation, transformation, or analysis within each group.

**Syntax:**
```python
grouped = dataframe_name.groupby(by, axis=0, level=None, as_index=True,
                                 sort=True, group_keys=True, squeeze=False, 
                                 observed=False, dropna=True)
```

**Example:**
```python
grouped = df.groupby(["category", "region"]).agg({"sales": "sum"})
```

### head()
Displays the first n rows of the DataFrame.

**Syntax:**
```python
dataframe_name.head(n)
```

**Example:**
```python
df.head(5)
```

### info()
Provides information about the DataFrame, including data types and memory usage.

**Syntax:**
```python
dataframe_name.info()
```

**Example:**
```python
df.info()
```

### merge()
Merges two DataFrames based on multiple common columns.

**Syntax:**
```python
merged_df = pd.merge(df1, df2, on=["column1", "column2"])
```

**Example:**
```python
merged_df = pd.merge(sales, products, on=["product_id", "category_id"])
```

### print DataFrame
Displays the content of the DataFrame.

**Syntax:**
```python
print(df)  # or just type df
```

**Example:**
```python
print(df)
df
```

### replace()
Replaces specific values in a column with new values.

**Syntax:**
```python
dataframe_name["column_name"].replace(old_value, new_value, inplace=True)
```

**Example:**
```python
df["status"].replace("In Progress", "Active", inplace=True)
```

### tail()
Displays the last n rows of the DataFrame.

**Syntax:**
```python
dataframe_name.tail(n)
```

**Example:**
```python
df.tail(5)
```

## NumPy

### Importing NumPy
Imports the NumPy library.

**Syntax:**
```python
import numpy as np
```

**Example:**
```python
import numpy as np
```

### np.array()
Creates a one or multi-dimensional array.

**Syntax:**
```python
array_1d = np.array([list1_values])                      # 1D Array
array_2d = np.array([[list1_values], [list2_values]])   # 2D Array
```

**Example:**
```python
array_1d = np.array([1, 2, 3])           # 1D Array
array_2d = np.array([[1, 2], [3, 4]])    # 2D Array
```

### NumPy Array Attributes
Common operations on NumPy arrays:
- Calculates the mean of array elements
- Calculates the sum of array elements
- Finds the minimum value in the array
- Finds the maximum value in the array
- Computes dot product of two arrays

**Example:**
```python
np.mean(array)
np.sum(array)
np.min(array)
np.max(array)
np.dot(array_1, array_2)
```

---

*© IBM Corporation. All rights reserved.*