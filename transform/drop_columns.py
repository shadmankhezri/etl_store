

import pandas as pd


def drop_unnecessary_columns(data , columns):

    for col in columns:
        data.drop(col , axis = 1 , inplace = True)
        
    return data