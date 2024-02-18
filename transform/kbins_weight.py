

from sklearn.preprocessing import KBinsDiscretizer



def k_bins_discretizer(data , columns):

    dis = KBinsDiscretizer(n_bins=5 , encode='ordinal' , strategy='uniform')

    for col in columns:
        data[col] = dis.fit_transform(data[[col]])
        data = data.astype({col : 'int'})
        
    return data 