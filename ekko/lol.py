import pandas as pd
from os import path

def where_is(name):
    base_dir = path.abspath(path.dirname(__file__))
    df = pd.read_csv(path.join(base_dir, './data.csv'))
    result = df[df['name'].str.contains(name)]
    if result.empty:
        return None
    floor = result['number'].values[0]
    return str(floor)

# Test
# print(where_is('臭豆腐'))
# print(where_is('雞蛋糕'))
