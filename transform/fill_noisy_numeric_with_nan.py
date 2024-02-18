

import pandas as pd

# داده های عددی که مقدار ولیو غیر عددی دارند را میاییم و اون ولیوهای غیر عددی را با نن پر میکنیم

def fill_noisy_numeric_with_nan(data):

    data["Quantity"] = pd.to_numeric(data["Quantity"] , errors="coerce")
    data["PurchaseAmount"] = pd.to_numeric(data["PurchaseAmount"] , errors="coerce")
    data["Weight"] = pd.to_numeric(data["Weight"] , errors="coerce")

    return data