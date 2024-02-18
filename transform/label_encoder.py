

from sklearn.preprocessing import LabelEncoder


def label_encoder_color_product(data , columns):
    le = LabelEncoder()

    for col in columns:
        data[col] = le.fit_transform(data[col])
        
    return data