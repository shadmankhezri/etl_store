


from sklearn.preprocessing import StandardScaler
import pandas as pd


def standardization_data(data , columns):
    st = StandardScaler()

    data = st.fit_transform(data)

    data = pd.DataFrame(data)

    data.columns = columns

    return data