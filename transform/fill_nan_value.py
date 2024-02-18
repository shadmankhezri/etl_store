

import pandas as pd

def fill_nan_value(data):
    data.fillna(value = {
            "CustomerName" : data.CustomerName.mode()[0],
            "PurchaseDate" : data.PurchaseDate.mode()[0],
            "Product" : data.Product.mode()[0],
            "Quantity" : data.Quantity.mean(),
            "PurchaseAmount" : data.PurchaseAmount.mean(),
            "Color" : data.Color.mode()[0],
            "IsAvailable" : data.IsAvailable.mode()[0],
            "Weight" : data.Weight.mean()

                        } , inplace = True)
    
    return data