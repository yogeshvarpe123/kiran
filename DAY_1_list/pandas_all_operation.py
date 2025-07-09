import pandas as pd
import numpy as np
import io # For simulating file operations
import matplotlib.pyplot as plt # For plotting

print("--- Pandas Operations and Use Cases ---")

# --- 1. Series: Creation and Basic Operations ---
# A Series is a one-dimensional labeled array capable of holding any data type.

print("\n--- 1. Series: Creation and Basic Operations ---")

# Example 1.1: Creating a Series
s1 = pd.Series([1, 2, 3, 4, 5])
print(f"Series from list:\n{s1}")

s2 = pd.Series([10, 20, 30], index=['a', 'b', 'c'], name='MyData')
print(f"\nSeries with custom index and name:\n{s2}")

# Example 1.2: Accessing elements
print(f"\nElement at index 0: {s1[0]}")
print(f"Element with label 'b': {s2['b']}")

# Corner Case: Accessing non-existent label (KeyError)
try:
    print(s2['d'])
except KeyError as e:
    print(f"Error accessing non-existent label: {e}")

# Example 1.3: Series operations (broadcasting)
print(f"\nSeries + 5:\n{s1 + 5}")
print(f"Series * 2:\n{s2 * 2}")

# Example 1.4: Boolean indexing
print(f"\nElements > 3:\n{s1[s1 > 3]}")

# Example 1.5: Handling missing values in Series
s_missing = pd.Series([1, 2, np.nan, 4, 5])
print(f"\nSeries with NaN:\n{s_missing}")
print(f"Is null:\n{s_missing.isnull()}")
print(f"Drop null:\n{s_missing.dropna()}")
print(f"Fill null with 0:\n{s_missing.fillna(0)}")


# --- 2. DataFrame: Creation ---
# A DataFrame is a two-dimensional labeled data structure with columns of potentially different types.

print("\n--- 2. DataFrame: Creation ---")

# Example 2.1: From a dictionary of lists (common)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'London', 'Paris', 'New York']
}
df1 = pd.DataFrame(data)
print(f"\nDataFrame from dict of lists:\n{df1}")

# Example 2.2: From a list of dictionaries
records = [
    {'Name': 'Eve', 'Age': 22, 'City': 'Tokyo'},
    {'Name': 'Frank', 'Age': 28, 'City': 'London'}
]
df2 = pd.DataFrame(records)
print(f"\nDataFrame from list of dicts:\n{df2}")

# Example 2.3: From a NumPy array
np_array = np.array([[1, 2, 3], [4, 5, 6]])
df_np = pd.DataFrame(np_array, columns=['ColA', 'ColB', 'ColC'], index=['Row1', 'Row2'])
print(f"\nDataFrame from NumPy array:\n{df_np}")

# Corner Case: Mismatched list lengths in dict (raises ValueError)
try:
    pd.DataFrame({'A': [1, 2], 'B': [3]})
except ValueError as e:
    print(f"Error creating DataFrame with mismatched lengths: {e}")


# --- 3. DataFrame: Inspection ---
# Problem: Get a quick overview of the DataFrame's structure and data.
# Functions/Methods: head(), tail(), info(), describe(), shape, dtypes, columns, index

print("\n--- 3. DataFrame: Inspection ---")

print(f"\nFirst 3 rows:\n{df1.head(3)}")
print(f"\nLast 2 rows:\n{df1.tail(2)}")
print(f"\nDataFrame info (non-nulls, dtypes):\n")
df1.info() # This prints directly to console, no return value
print(f"\nDescriptive statistics:\n{df1.describe()}")
print(f"\nShape (rows, columns): {df1.shape}")
print(f"Column data types:\n{df1.dtypes}")
print(f"Column names: {df1.columns.tolist()}")
print(f"Index: {df1.index.tolist()}")


# --- 4. DataFrame: Selection ---
# Problem: Select specific columns, rows, or cells.
# Functions/Methods: [], .loc[], .iloc[], boolean indexing

print("\n--- 4. DataFrame: Selection ---")

# Example 4.1: Selecting a single column (returns Series)
names = df1['Name']
print(f"\n'Name' column (Series):\n{names}")

# Example 4.2: Selecting multiple columns (returns DataFrame)
name_age = df1[['Name', 'Age']]
print(f"\n'Name' and 'Age' columns (DataFrame):\n{name_age}")

# Example 4.3: .loc[] - Label-based indexing (rows by label, columns by label)
# Select row by index label (default 0, 1, 2...)
row_0 = df1.loc[0]
print(f"\nRow with label 0:\n{row_0}")

# Select specific rows and columns by label
subset_loc = df1.loc[1:3, ['Name', 'City']] # Rows with labels 1 to 3 (inclusive), specific columns
print(f"\nSubset with .loc[1:3, ['Name', 'City']]:\n{subset_loc}")

# Example 4.4: .iloc[] - Integer-location based indexing (rows by integer position, columns by integer position)
row_by_pos = df1.iloc[1] # Second row (index 1)
print(f"\nRow at integer position 1:\n{row_by_pos}")

# Select specific rows and columns by integer position
subset_iloc = df1.iloc[0:2, [0, 2]] # First two rows, first and third column
print(f"\nSubset with .iloc[0:2, [0, 2]]:\n{subset_iloc}")

# Example 4.5: Boolean indexing (filtering rows)
adults = df1[df1['Age'] >= 30]
print(f"\nAdults (Age >= 30):\n{adults}")

# Combine multiple conditions
london_adults = df1[(df1['Age'] >= 30) & (df1['City'] == 'London')]
print(f"\nAdults in London:\n{london_adults}")

# Corner Case: SettingWithCopyWarning
# When you chain indexing operations, Pandas might warn you about modifying a copy.
# Use .loc[] for explicit assignment to avoid this.
df_copy = df1.copy()
# df_copy[df_copy['Age'] == 25]['City'] = 'Paris' # This might raise a warning
df_copy.loc[df_copy['Age'] == 25, 'City'] = 'Paris' # Correct way
print(f"\nDataFrame after modifying City for age 25:\n{df_copy}")


# --- 5. DataFrame: Data Cleaning ---
# Problem: Handle missing values and duplicate rows.
# Functions/Methods: isna(), dropna(), fillna(), duplicated(), drop_duplicates()

print("\n--- 5. DataFrame: Data Cleaning ---")

df_clean = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, 5],
    'C': [1, 2, 3, 4, np.nan],
    'D': [1, 2, 2, 4, 5] # Duplicate in D
})
print(f"\nOriginal DataFrame for cleaning:\n{df_clean}")

# Example 5.1: Check for missing values
print(f"\nIs NA:\n{df_clean.isna()}")
print(f"\nSum of NA per column:\n{df_clean.isna().sum()}")

# Example 5.2: Drop rows with any NaN
df_dropped_rows = df_clean.dropna()
print(f"\nDataFrame after dropping rows with any NaN:\n{df_dropped_rows}")

# Example 5.3: Drop columns with any NaN
df_dropped_cols = df_clean.dropna(axis=1)
print(f"\nDataFrame after dropping columns with any NaN:\n{df_dropped_cols}")

# Example 5.4: Fill missing values
df_filled = df_clean.fillna(0)
print(f"\nDataFrame after filling NaN with 0:\n{df_filled}")
df_filled_mean = df_clean.fillna(df_clean['A'].mean()) # Fill with column mean
print(f"\nDataFrame after filling NaN in A with mean of A:\n{df_filled_mean}")

# Example 5.5: Identify and drop duplicates
df_duplicates = pd.DataFrame({'col1': [1, 2, 2, 3], 'col2': ['A', 'B', 'B', 'C']})
print(f"\nDataFrame with duplicates:\n{df_duplicates}")
print(f"Are rows duplicated?\n{df_duplicates.duplicated()}")
df_no_duplicates = df_duplicates.drop_duplicates()
print(f"DataFrame after dropping duplicates:\n{df_no_duplicates}")

# Corner Case: drop_duplicates with 'subset' and 'keep'
df_more_duplicates = pd.DataFrame({
    'id': [1, 2, 1, 3],
    'value': ['A', 'B', 'A', 'C'],
    'timestamp': [1, 2, 3, 4]
})
print(f"\nMore duplicates:\n{df_more_duplicates}")
# Keep only unique 'id', keeping the first occurrence
df_unique_id_first = df_more_duplicates.drop_duplicates(subset=['id'], keep='first')
print(f"Unique 'id' (keep first):\n{df_unique_id_first}")
# Keep only unique 'id', keeping the last occurrence
df_unique_id_last = df_more_duplicates.drop_duplicates(subset=['id'], keep='last')
print(f"Unique 'id' (keep last):\n{df_unique_id_last}")


# --- 6. DataFrame: Data Manipulation and Transformation ---
# Problem: Apply functions, create new columns, transform existing ones.
# Functions/Methods: apply(), map(), applymap(), assign(), astype()

print("\n--- 6. DataFrame: Data Manipulation and Transformation ---")

df_manipulate = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [10, 20, 30],
    'C': ['apple', 'banana', 'cherry']
})
print(f"\nOriginal DataFrame for manipulation:\n{df_manipulate}")

# Example 6.1: apply() - Apply a function along an axis (row or column)
# Apply to a Series (column)
df_manipulate['A_squared'] = df_manipulate['A'].apply(lambda x: x**2)
print(f"\nAfter squaring column 'A':\n{df_manipulate}")

# Apply to each row (axis=1)
df_manipulate['Sum_AB'] = df_manipulate.apply(lambda row: row['A'] + row['B'], axis=1)
print(f"\nAfter summing 'A' and 'B' per row:\n{df_manipulate}")

# Example 6.2: map() - For Series, maps values from one set to another
# Only works on Series
mapping = {'apple': 'fruit', 'banana': 'fruit', 'cherry': 'fruit'}
df_manipulate['C_category'] = df_manipulate['C'].map(mapping)
print(f"\nAfter mapping 'C' to categories:\n{df_manipulate}")

# Example 6.3: applymap() - Apply a function element-wise to a DataFrame
# (Note: applymap is deprecated in favor of df.map() or df.apply(axis=1) in newer pandas)
# df_manipulate_str = df_manipulate[['A', 'B']].applymap(str) # Apply str conversion to all elements in A and B
# print(f"\nAfter applymap (str conversion):\n{df_manipulate_str}")

# Example 6.4: assign() - Create new columns (returns new DataFrame)
df_assigned = df_manipulate.assign(
    D=lambda x: x['A'] * 10,
    E=lambda x: x['C'].str.upper()
)
print(f"\nAfter assign() new columns:\n{df_assigned}")

# Example 6.5: astype() - Change data type of a column
df_types = pd.DataFrame({'A': ['1', '2', '3'], 'B': [1.1, 2.2, 3.3]})
df_types['A'] = df_types['A'].astype(int)
df_types['B'] = df_types['B'].astype(str)
print(f"\nAfter astype() changes:\n{df_types.dtypes}")
print(f"{df_types}")

# Corner Case: apply() vs map() vs applymap()
# - .map() is for Series (element-wise transformation using a dict or function)
# - .apply() is for Series or DataFrame (column-wise, row-wise, or element-wise depending on axis/function)
# - .applymap() (deprecated) was for element-wise on DataFrame (similar to df.map() in newer pandas)


# --- 7. DataFrame: Grouping and Aggregation ---
# Problem: Group data by one or more columns and perform aggregations (sum, mean, count, etc.).
# Functions/Methods: groupby(), agg(), size(), count()

print("\n--- 7. DataFrame: Grouping and Aggregation ---")

df_sales = pd.DataFrame({
    'Region': ['East', 'West', 'East', 'West', 'East'],
    'Product': ['A', 'B', 'A', 'C', 'B'],
    'Sales': [100, 150, 120, 200, 80],
    'Units': [10, 15, 12, 20, 8]
})
print(f"\nOriginal Sales Data:\n{df_sales}")

# Example 7.1: Group by single column and sum
sales_by_region = df_sales.groupby('Region')['Sales'].sum()
print(f"\nSales by Region:\n{sales_by_region}")

# Example 7.2: Group by multiple columns and get mean
avg_sales_by_region_product = df_sales.groupby(['Region', 'Product'])['Sales'].mean()
print(f"\nAverage Sales by Region and Product:\n{avg_sales_by_region_product}")

# Example 7.3: Multiple aggregations using .agg()
multi_agg = df_sales.groupby('Region').agg(
    Total_Sales=('Sales', 'sum'),
    Average_Units=('Units', 'mean'),
    Num_Transactions=('Product', 'count')
)
print(f"\nMultiple Aggregations by Region:\n{multi_agg}")

# Example 7.4: Group by and get size (number of rows in each group)
group_sizes = df_sales.groupby('Region').size()
print(f"\nNumber of transactions by Region:\n{group_sizes}")

# Corner Case: Resetting index after groupby
# By default, groupby columns become the new index. Use .reset_index() to convert them back to columns.
sales_by_region_df = df_sales.groupby('Region')['Sales'].sum().reset_index()
print(f"\nSales by Region (as DataFrame):\n{sales_by_region_df}")


# --- 8. DataFrame: Merging and Joining ---
# Problem: Combine DataFrames based on common columns (like SQL joins).
# Functions/Methods: merge(), concat()

print("\n--- 8. DataFrame: Merging and Joining ---")

df_customers = pd.DataFrame({
    'customer_id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David']
})

df_orders = pd.DataFrame({
    'order_id': [101, 102, 103, 104],
    'customer_id': [1, 3, 1, 5], # Customer 5 does not exist in df_customers
    'amount': [100, 150, 200, 50]
})

print(f"\nCustomers:\n{df_customers}")
print(f"\nOrders:\n{df_orders}")

# Example 8.1: Inner Join (default) - Only common customer_ids
merged_inner = pd.merge(df_customers, df_orders, on='customer_id', how='inner')
print(f"\nInner Merge (common customer_ids):\n{merged_inner}")

# Example 8.2: Left Join - Keep all rows from left (df_customers)
merged_left = pd.merge(df_customers, df_orders, on='customer_id', how='left')
print(f"\nLeft Merge (all customers, NaN for no orders):\n{merged_left}")

# Example 8.3: Right Join - Keep all rows from right (df_orders)
merged_right = pd.merge(df_customers, df_orders, on='customer_id', how='right')
print(f"\nRight Merge (all orders, NaN for no customer):\n{merged_right}")

# Example 8.4: Outer Join - Keep all rows from both
merged_outer = pd.merge(df_customers, df_orders, on='customer_id', how='outer')
print(f"\nOuter Merge (all customers and all orders):\n{merged_outer}")

# Example 8.5: concat() - Stacking DataFrames (rows or columns)
df_concat1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df_concat2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
df_concat_rows = pd.concat([df_concat1, df_concat2]) # Default axis=0 (rows)
print(f"\nConcatenated rows:\n{df_concat_rows}")

df_concat_cols = pd.concat([df_concat1, df_concat2], axis=1) # Concatenate columns
print(f"\nConcatenated columns:\n{df_concat_cols}")

# Corner Case: merge() with multiple join keys
df_multi_key1 = pd.DataFrame({'key1': ['A', 'B'], 'key2': ['X', 'Y'], 'val1': [1, 2]})
df_multi_key2 = pd.DataFrame({'key1': ['A', 'B'], 'key2': ['X', 'Z'], 'val2': [10, 20]})
merged_multi_key = pd.merge(df_multi_key1, df_multi_key2, on=['key1', 'key2'], how='inner')
print(f"\nMerge on multiple keys:\n{merged_multi_key}")


# --- 9. DataFrame: Reshaping and Pivoting ---
# Problem: Change the layout of a DataFrame (e.g., wide to long, long to wide).
# Functions/Methods: pivot(), pivot_table(), melt(), stack(), unstack()

print("\n--- 9. DataFrame: Reshaping and Pivoting ---")

df_sales_long = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
    'Product': ['A', 'B', 'A', 'B'],
    'Sales': [100, 150, 120, 180]
})
print(f"\nSales (Long Format):\n{df_sales_long}")

# Example 9.1: pivot() - Reshape data based on column values
# Requires unique index-columns pairs
df_sales_wide = df_sales_long.pivot(index='Date', columns='Product', values='Sales')
print(f"\nSales (Wide Format - pivot):\n{df_sales_wide}")

# Example 9.2: pivot_table() - More powerful, handles duplicates by aggregating
df_sales_agg = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-01', '2023-01-01'],
    'Product': ['A', 'A', 'B'], # Duplicate 'A' for same date
    'Sales': [100, 50, 150]
})
print(f"\nSales with duplicates:\n{df_sales_agg}")
pivot_table_sum = df_sales_agg.pivot_table(index='Date', columns='Product', values='Sales', aggfunc='sum')
print(f"\nPivot Table (sum aggfunc):\n{pivot_table_sum}")

# Example 9.3: melt() - Unpivot DataFrame from wide to long format
df_melt_wide = pd.DataFrame({
    'City': ['NY', 'LA'],
    'Jan': [100, 150],
    'Feb': [120, 180]
})
print(f"\nWide format for melt:\n{df_melt_wide}")
df_melted = df_melt_wide.melt(id_vars=['City'], var_name='Month', value_name='Sales')
print(f"\nLong format after melt:\n{df_melted}")

# Example 9.4: stack() and unstack() - Reshape based on MultiIndex
df_multi_index = df_sales_long.set_index(['Date', 'Product'])
print(f"\nMulti-index DataFrame:\n{df_multi_index}")
stacked_df = df_multi_index.stack()
print(f"\nStacked DataFrame:\n{stacked_df}")
unstacked_df = stacked_df.unstack()
print(f"\nUnstacked DataFrame:\n{unstacked_df}")


# --- 10. DataFrame: Time Series Operations ---
# Problem: Work with time-indexed data (resampling, rolling windows).
# Functions/Methods: to_datetime(), resample(), rolling()

print("\n--- 10. DataFrame: Time Series Operations ---")

dates = pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'])
ts_data = pd.Series([10, 12, 15, 11, 13], index=dates)
print(f"\nOriginal Time Series:\n{ts_data}")

# Example 10.1: Resampling (e.g., daily to weekly sum)
# Create a longer time series for better resampling demo
long_dates = pd.to_datetime(pd.date_range(start='2023-01-01', periods=10, freq='D'))
long_ts_data = pd.Series(range(10), index=long_dates)
print(f"\nLonger Time Series:\n{long_ts_data}")

weekly_sum = long_ts_data.resample('W').sum() # Sum per week
print(f"\nWeekly sum (resample):\n{weekly_sum}")

# Example 10.2: Rolling windows (e.g., 3-day moving average)
rolling_mean = ts_data.rolling(window=3).mean()
print(f"\n3-day rolling mean:\n{rolling_mean}")

# Corner Case: Handling time zones
# Always specify tz if working with time zones to avoid ambiguity.
# ts_data_tz = pd.Series([1,2], index=pd.to_datetime(['2023-01-01', '2023-01-02'], tz='UTC'))


# --- 11. Input/Output (I/O) ---
# Problem: Read data from and write data to various file formats.
# Functions/Methods: read_csv(), to_csv(), read_excel(), to_excel(), read_sql(), to_sql() etc.

print("\n--- 11. Input/Output (I/O) ---")

# Example 11.1: Reading from a CSV (simulated)
csv_data = """col1,col2,col3
1,A,True
2,B,False
3,C,True
"""
df_from_csv = pd.read_csv(io.StringIO(csv_data))
print(f"\nDataFrame from simulated CSV:\n{df_from_csv}")

# Example 11.2: Writing to a CSV (simulated)
csv_output = io.StringIO()
df_from_csv.to_csv(csv_output, index=False) # index=False to avoid writing DataFrame index
print(f"\nDataFrame written to simulated CSV:\n{csv_output.getvalue()}")

# Example 11.3: Reading from Excel (conceptual, requires openpyxl or xlrd)
# df_from_excel = pd.read_excel('your_file.xlsx', sheet_name='Sheet1')

# Example 11.4: Writing to Excel (conceptual)
# df_from_csv.to_excel('output.xlsx', index=False, sheet_name='Data')

# Corner Case: Handling parsing errors in CSV/Excel (e.g., bad lines)
# pd.read_csv('bad_data.csv', error_bad_lines=False) # Old way
# pd.read_csv('bad_data.csv', on_bad_lines='skip') # New way (Pandas 1.3+)


# --- 12. Miscellaneous Useful Operations ---
# Functions/Methods: value_counts(), unique(), isin(), clip(), rename(), replace()

print("\n--- 12. Miscellaneous Useful Operations ---")

misc_df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'C', 'B', 'A'],
    'Value': [10, 20, 10, 30, 20, 10],
    'Status': ['Good', 'Bad', 'Good', 'Bad', 'Good', 'Bad']
})
print(f"\nMiscellaneous DataFrame:\n{misc_df}")

# Example 12.1: value_counts() - Count unique values in a Series
category_counts = misc_df['Category'].value_counts()
print(f"\nCategory counts:\n{category_counts}")

# Example 12.2: unique() - Get unique values from a Series
unique_statuses = misc_df['Status'].unique()
print(f"\nUnique statuses: {unique_statuses}")

# Example 12.3: isin() - Check if elements are contained in a list/Series/set
filtered_categories = misc_df[misc_df['Category'].isin(['A', 'C'])]
print(f"\nRows where Category is 'A' or 'C':\n{filtered_categories}")

# Example 12.4: clip() - Clip values at a lower and upper bound
misc_df['Value_Clipped'] = misc_df['Value'].clip(lower=15, upper=25)
print(f"\nValues clipped between 15 and 25:\n{misc_df}")

# Example 12.5: rename() - Rename columns or index labels
df_renamed = misc_df.rename(columns={'Category': 'ProductType', 'Value': 'Amount'})
print(f"\nDataFrame after renaming columns:\n{df_renamed}")

# Example 12.6: replace() - Replace values in Series or DataFrame
df_replaced = misc_df.replace({'Good': 'OK', 'Bad': 'Not OK'})
print(f"\nDataFrame after replacing status values:\n{df_replaced}")

# Corner Case: inplace=True (modifies DataFrame directly, returns None)
# Generally, avoid inplace=True for clarity and chaining operations.
# df_replaced.replace({'Good': 'OK'}, inplace=True)


# --- 13. MultiIndex / Hierarchical Indexing ---
# Problem: Work with DataFrames having multiple levels of row or column labels.
# Functions/Methods: set_index(), reset_index(), .loc[] with tuples, .xs()

print("\n--- 13. MultiIndex / Hierarchical Indexing ---")

df_multi = pd.DataFrame({
    'Region': ['North', 'North', 'South', 'South'],
    'City': ['NY', 'Boston', 'Miami', 'Houston'],
    'Year': [2022, 2023, 2022, 2023],
    'Sales': [100, 120, 150, 130]
})
print(f"\nOriginal DataFrame for MultiIndex:\n{df_multi}")

# Example 13.1: set_index() - Create a MultiIndex
df_multi_indexed = df_multi.set_index(['Region', 'City'])
print(f"\nDataFrame with MultiIndex (Region, City):\n{df_multi_indexed}")

# Example 13.2: Accessing data with MultiIndex (.loc with tuples)
print(f"\nSales for North, NY:\n{df_multi_indexed.loc[('North', 'NY')]}")

# Example 13.3: .xs() - Cross-section from MultiIndex
# Select all data for '2022' from the 'Year' level (if 'Year' was an index level)
# Let's re-index to make 'Year' a level
df_multi_indexed_full = df_multi.set_index(['Region', 'City', 'Year'])
print(f"\nFull MultiIndex DataFrame:\n{df_multi_indexed_full}")

# Select data for a specific year across all regions/cities
sales_2022 = df_multi_indexed_full.xs(2022, level='Year')
print(f"\nSales for Year 2022 (using .xs()):\n{sales_2022}")

# Example 13.4: reset_index() - Convert MultiIndex back to columns
df_reset = df_multi_indexed.reset_index()
print(f"\nDataFrame after reset_index():\n{df_reset}")


# --- 14. Categorical Data ---
# Problem: Efficiently store and analyze data with a limited number of unique values (categories).
# Functions/Methods: astype('category'), .cat accessor (codes, categories)

print("\n--- 14. Categorical Data ---")

df_cat = pd.DataFrame({
    'Product': ['A', 'B', 'A', 'C', 'B'],
    'Size': ['M', 'L', 'S', 'M', 'L']
})
print(f"\nOriginal DataFrame for Categorical:\n{df_cat}")

# Example 14.1: Convert to categorical type
df_cat['Product'] = df_cat['Product'].astype('category')
df_cat['Size'] = df_cat['Size'].astype('category')
print(f"\nDataFrame with Categorical dtypes:\n{df_cat.dtypes}")

# Example 14.2: Accessing categorical properties
print(f"\nProduct categories: {df_cat['Product'].cat.categories}")
print(f"Product codes (numerical representation): {df_cat['Product'].cat.codes}")

# Benefits: Memory efficiency, faster comparisons/grouping for certain operations.
# Corner Case: Operations on categories (e.g., adding a new category not present)
# df_cat['Product'] = df_cat['Product'].cat.add_categories('D') # Add a new category
# df_cat.loc[5, 'Product'] = 'D' # Assign a new category


# --- 15. Advanced Window Functions (Expanding, Exponential Moving Average) ---
# Problem: Calculate statistics over expanding windows or with exponential weighting.
# Functions/Methods: .expanding(), .ewm()

print("\n--- 15. Advanced Window Functions ---")

data_series = pd.Series([10, 12, 15, 11, 13, 16, 14])
print(f"\nOriginal Series for Window Functions:\n{data_series}")

# Example 15.1: Expanding mean (mean of all data up to current point)
expanding_mean = data_series.expanding().mean()
print(f"\nExpanding Mean:\n{expanding_mean}")

# Example 15.2: Exponentially Weighted Moving Average (EWMA)
# `span` is a common parameter, roughly equivalent to a simple moving average window.
ewma = data_series.ewm(span=3, adjust=False).mean()
print(f"\nExponentially Weighted Moving Average (span=3):\n{ewma}")


# --- 16. String Operations (.str accessor) ---
# Problem: Perform string manipulations on Series of strings.
# Functions/Methods: .str.contains(), .str.startswith(), .str.split(), .str.replace(), .str.upper(), .str.lower(), .str.len()

print("\n--- 16. String Operations (.str accessor) ---")

df_str = pd.DataFrame({
    'Text': ['apple pie', 'banana split', 'cherry tart', 'Apple Juice'],
    'ID': ['id_1', 'id_2', 'id_3', 'id_4']
})
print(f"\nOriginal DataFrame for String Ops:\n{df_str}")

# Example 16.1: Check if string contains a substring (case-insensitive)
contains_apple = df_str['Text'].str.contains('apple', case=False)
print(f"\nText containing 'apple' (case-insensitive):\n{contains_apple}")

# Example 16.2: Check if string starts with a prefix
starts_with_b = df_str['Text'].str.startswith('b')
print(f"\nText starting with 'b':\n{starts_with_b}")

# Example 16.3: Split strings into lists
df_str['Words'] = df_str['Text'].str.split(' ')
print(f"\nText split into words:\n{df_str}")

# Example 16.4: Replace substrings
df_str['Text_Replaced'] = df_str['Text'].str.replace(' ', '-')
print(f"\nText with spaces replaced by hyphens:\n{df_str}")

# Example 16.5: Convert to uppercase
df_str['ID_Upper'] = df_str['ID'].str.upper()
print(f"\nID column in uppercase:\n{df_str}")

# Corner Case: NaN values in string columns
s_str_nan = pd.Series(['hello', np.nan, 'world'])
print(f"\nString Series with NaN:\n{s_str_nan.str.upper()}") # .str methods handle NaN gracefully, return NaN


# --- 17. Date/Time Accessors (.dt accessor) ---
# Problem: Extract specific components (year, month, day, day of week) from datetime Series.
# Functions/Methods: .dt.year, .dt.month, .dt.day, .dt.dayofweek, .dt.day_name(), .dt.hour, etc.

print("\n--- 17. Date/Time Accessors (.dt accessor) ---")

dates_series = pd.Series(pd.to_datetime(['2023-01-15 10:30:00', '2023-02-20 14:00:00', '2023-03-25 08:15:00']))
print(f"\nOriginal Date Series:\n{dates_series}")

# Example 17.1: Extract year, month, day
print(f"\nYears: {dates_series.dt.year}")
print(f"Months: {dates_series.dt.month}")
print(f"Days: {dates_series.dt.day}")

# Example 17.2: Day of week and day name
print(f"Day of week (0=Monday): {dates_series.dt.dayofweek}")
print(f"Day names: {dates_series.dt.day_name()}")

# Example 17.3: Extract time components
print(f"Hours: {dates_series.dt.hour}")
print(f"Minutes: {dates_series.dt.minute}")

# Corner Case: Non-datetime series (raises AttributeError)
non_date_series = pd.Series(['abc', 'def'])
try:
    print(non_date_series.dt.year)
except AttributeError as e:
    print(f"Error accessing .dt on non-datetime series: {e}")


# --- 18. Basic Plotting (.plot() method) ---
# Problem: Quickly visualize data directly from Series or DataFrames.
# Functions/Methods: .plot(), .plot.bar(), .plot.hist(), .plot.scatter() etc.
# Note: Requires matplotlib to be installed (`pip install matplotlib`)

print("\n--- 18. Basic Plotting (.plot() method) ---")

# Example 18.1: Line plot from Series
plot_series = pd.Series([10, 12, 8, 15, 11], index=pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']))
print(f"\nSeries for plotting:\n{plot_series}")
# plot_series.plot(title="Daily Data Trend")
# plt.show() # Uncomment to display the plot

# Example 18.2: Bar plot from DataFrame
plot_df = pd.DataFrame({'Category': ['A', 'B', 'C'], 'Value': [100, 150, 80]})
# plot_df.plot.bar(x='Category', y='Value', title="Category Values")
# plt.show() # Uncomment to display the plot

# Example 18.3: Histogram
hist_series = pd.Series(np.random.randn(1000)) # 1000 random numbers
# hist_series.plot.hist(bins=30, title="Histogram of Random Data")
# plt.show() # Uncomment to display the plot

print("\n(Plotting examples are commented out. Uncomment `plt.show()` to display plots.)")

