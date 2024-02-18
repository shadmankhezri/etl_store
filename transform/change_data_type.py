



def change_data_type(data):

    data["Weight"] = round(data["Weight"] , 0)
    data = data.astype({"Quantity" : "int"})

    return data