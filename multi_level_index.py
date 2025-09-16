import pandas as pd


def create_dataframe(data: dict) -> pd.DataFrame:
    """
    Создает pandas DataFrame из словаря данных

    Parameters:
    -----------
    data : dict
        Словарь с данными для создания DataFrame
        Ключи - названия колонок,
        значения - списки данных соответствующих колонок

    Returns:
    --------
    pd.DataFrame
        Созданный DataFrame

    Raises:
    -------
    TypeError
        Если аргумент data не является словарем
    ValueError
        Если словарь data пустой или не удалось создать DataFrame
    """
    if not isinstance(data, dict):
        raise TypeError("Аргумент data должен быть словарем")
    if not data:
        raise ValueError("Словарь data не может быть пустым")
    try:
        df = pd.DataFrame(data)
    except Exception as e:
        raise ValueError(f"Не удалось создать DataFrame: {e}")
    return df


def set_multiindex(df: pd.DataFrame, index_cols: list) -> pd.DataFrame:
    """
    Устанавливает MultiIndex для DataFrame на основе указанных колонок

    Parameters:
    -----------
    df : pd.DataFrame
        Исходный DataFrame
    index_cols : list
        Список названий колонок, которые будут использоваться для создания MultiIndex

    Returns:
    --------
    pd.DataFrame
        DataFrame с установленным MultiIndex

    Raises:
    -------
    TypeError
        Если index_cols не является списком
    KeyError
        Если какая-либо из указанных колонок отсутствует в DataFrame
    """
    if not isinstance(index_cols, list):
        raise TypeError("index_cols должен быть списком")
    for col in index_cols:
        if col not in df.columns:
            raise KeyError(f"Колонка {col} отсутствует в DataFrame")
    return df.set_index(index_cols)


def group_by_level(df: pd.DataFrame, level: str, agg_func: str = "sum") -> pd.DataFrame:
    """
    Группирует DataFrame по указанному уровню MultiIndex с применением агрегирующей функции

    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame с MultiIndex
    level : str
        Название уровня MultiIndex для группировки
    agg_func : str, optional
        Агрегирующая функция. Доступные значения: "sum", "mean", "max", "min"
        По умолчанию "sum"

    Returns:
    --------
    pd.DataFrame
        Результат группировки с примененной агрегирующей функцией

    Raises:
    -------
    KeyError
        Если указанный уровень отсутствует в индексе DataFrame
    ValueError
        Если указана неподдерживаемая агрегирующая функция
    """
    if level not in df.index.names:
        raise KeyError(f"Уровень {level} отсутствует в индексе")
    if agg_func not in ["sum", "mean", "max", "min"]:
        raise ValueError(f"Аггрегация {agg_func} не поддерживается")
    return getattr(df.groupby(level=level), agg_func)()


def main(data: dict, index_cols: list) -> None:
    """
    Основная функция для демонстрации работы с DataFrame и MultiIndex

    Parameters:
    -----------
    data : dict
        Словарь с данными для создания DataFrame
    index_cols : list
        Список колонок для создания MultiIndex

    Returns:
    --------
    None
    """
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
