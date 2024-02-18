

import pandas as pd


def one_hot_encoder_isavailable(data , columns):
    return pd.get_dummies(data , columns=columns)