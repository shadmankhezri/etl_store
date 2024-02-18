

import pandas as pd


def drop_all_nan(data):
    return data.dropna(how='all' , axis = 0)