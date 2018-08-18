import pandas as pd
from os import path

def where_is(name):
    base_dir = path.abspath(path.dirname(__file__))
    df = pd.read_csv(path.join(base_dir, './data.csv'))
    result = df[df['name'].str.contains(name)]
    if result.empty:
        return None
    number = result['number'].values[0]
    price = result['price'].values[0]
    return str(number), str(price)

