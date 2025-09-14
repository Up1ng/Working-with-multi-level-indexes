# Working with MultiIndex in Pandas

This project demonstrates the use of multi-level indexes (MultiIndex) in the Pandas library for data analysis.

## About the Pandas Library

Pandas is a powerful Python library for data analysis, providing data structures and tools for efficient work with tabular data. Main data structures:
- **Series** - one-dimensional array with labels
- **DataFrame** - two-dimensional table with row and column labels

## About MultiIndex

MultiIndex (or hierarchical index) allows having multiple levels of indexes in one dimension (rows or columns). This is particularly useful for:
- Working with high-dimensional data in a two-dimensional structure
- Efficient data grouping and aggregation
- Simplifying complex data queries
- Creating pivot tables

## Program Description

The program demonstrates the creation and use of MultiIndex in Pandas:

### 1. Creating Source Data
A DataFrame is created with synthetic data containing:
- Two categorical variables (Category1, Category2)
- Two numerical variables (Value, Count)

### 2. Setting MultiIndex
Categorical columns are converted to a multi-level index using the `set_index()` method

### 3. Data Grouping
Various types of grouping are performed:
- By the first index level with sum aggregation
- By the second index level with mean value aggregation
- By both index levels simultaneously

### 4. Additional Operations
Additional MultiIndex capabilities are demonstrated:
- Data selection by index levels
- Using the `unstack()` method for data structure transformation
- Accessing data by specific index combinations

## Requirements

- Python 3.6+
- Pandas library

Install dependencies:
```
pip install pandas
```

## Running the Program

Save the code to a file named `multiindex_demo.py` and run:
```
python multiindex_demo.py
```

## Sample Output

The program will output to the console:
1. Original DataFrame
2. DataFrame with set MultiIndex
3. Results of various grouping operations
4. Examples of data selection using MultiIndex

## Real-World Applications

MultiIndex is particularly useful when working with:
- Time series with multiple dimensions
- Data with hierarchical structure (regions -> cities -> districts)
- A/B testing results with multiple variables
- Sales analysis by product categories and subcategories

This example serves as a foundation for more complex data analysis operations using multi-level indexes in Pandas.
