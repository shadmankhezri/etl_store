

from sklearn.preprocessing import MinMaxScaler
import pandas as pd


def normalization_data(data , columns):

    nm = MinMaxScaler()
    data = nm.fit_transform(data)

    data = pd.DataFrame(data)

    data.columns = columns

    return data 
