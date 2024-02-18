

import pandas as pd


def read_file(PATH):
    df_orders = pd.read_csv(PATH)
    return df_orders