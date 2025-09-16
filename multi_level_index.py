import pandas as pd

def create_dataframe(data: dict) -> pd.DataFrame:
    if not isinstance(data, dict):
        raise TypeError("Аргумент data должен быть словарем.")
    if not data:
        raise ValueError("Словарь data не может быть пустым.")
    try:
        df = pd.DataFrame(data)
    except Exception as e:
        raise ValueError(f"Не удалось создать DataFrame: {e}")
    return df


def set_multiindex(df: pd.DataFrame, index_cols: list) -> pd.DataFrame:
    if not isinstance(index_cols, list):
        raise TypeError("index_cols должен быть списком.")
    for col in index_cols:
        if col not in df.columns:
            raise KeyError(f"Колонка {col} отсутствует в DataFrame.")
    return df.set_index(index_cols)


def group_by_level(df: pd.DataFrame, level: str, agg_func: str = "sum") -> pd.DataFrame:
    if level not in df.index.names:
        raise KeyError(f"Уровень {level} отсутствует в индексе.")
    if agg_func not in ["sum", "mean", "max", "min"]:
        raise ValueError(f"Аггрегация {agg_func} не поддерживается.")
    return getattr(df.groupby(level=level), agg_func)()


def main(data: dict, index_cols: list):
    try:
        df = create_dataframe(data)
        df_multi = set_multiindex(df, index_cols)
        print("Датафрейм с MultiIndex:")
        print(df_multi)

        print("\nСтруктура индекса:")
        print(df_multi.index)

        grouped = group_by_level(df_multi, level="Category1", agg_func="sum")
        print("\nРезультат группировки по Category1 (sum):")
        print(grouped)

        grouped_level2 = group_by_level(df_multi, level="Category2", agg_func="mean")
        print("\nРезультат группировки по Category2 (mean):")
        print(grouped_level2)

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    data = {
        'Category1': ['A', 'A', 'B', 'B', 'A', 'B'],
        'Category2': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
        'Value': [10, 20, 30, 40, 50, 60]
    }
    main(data, ['Category1', 'Category2'])
