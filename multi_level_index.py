import pandas as pd
data = {
    'Category1': ['A', 'A', 'B', 'B', 'A', 'B'],
    'Category2': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
    'Value': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)
df_multi = df.set_index(['Category1', 'Category2'])
print("Датафрейм с MultiIndex:")
print(df_multi)
print("\nСтруктура индекса:")
print(df_multi.index)
grouped = df_multi.groupby(level='Category1').sum()
print("\nРезультат группировки по Category1:")
print(grouped)
grouped_level2 = df_multi.groupby(level='Category2').mean()
print("\nРезультат группировки по Category2:")
print(grouped_level2)
