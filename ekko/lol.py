import pandas as pd
from os import path

def where_is(name):
    base_dir = path.abspath(path.dirname(__file__))
    df = pd.read_csv(path.join(base_dir, './data.csv'))
    result = df[df['name'].str.contains(name)]
    if result.empty:
        return None
    # print(result)
    floor = result['floor'].values[0]
    # print(floor)
    return str(floor)

# print(where_is('蘋果公司'))
# print(where_is('哈哈'))
