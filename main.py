
from extraction.extraction import read_file
from transform.display import display
from transform.drop_all_nan import drop_all_nan
from transform.fill_noisy_numeric_with_nan import fill_noisy_numeric_with_nan
from transform.fill_nan_value import fill_nan_value
from transform.change_data_type import change_data_type
from transform.check_weight_outlier import check_weight_outlier
from transform.remove_weight_outlier import remove_weight_outlier
from transform.kbins_weight import k_bins_discretizer
from transform.one_hot_isavailable import one_hot_encoder_isavailable
from transform.label_encoder import label_encoder_color_product
from transform.drop_columns import drop_unnecessary_columns
from transform.normalization import normalization_data
from transform.standardization import standardization_data
from load.load import save_final_data


PATH = "data/orders.csv"
FINAL_PATH = "data/final_orders.csv"


def main():
    

    df_orders = read_file(PATH)
    # display(f"\nFirst data file from orders.csv:\n\n{df_orders}")


    df_orders = drop_all_nan(df_orders)
    # display(f"\nDrop records that values are all null:\n\n{df_orders}")


    df_orders = fill_noisy_numeric_with_nan(df_orders)
    # display(f"\nFill noisy numeric recordes with nan:\n\n{df_orders}")


    df_orders = fill_nan_value(df_orders)
    # display(f"\nFill Nan Values with mode and mean:\n\n{df_orders}")


    # رند کردن اعداد این دوتا ستون
    df_orders = change_data_type(df_orders)
    # display(f"\nChange Quantity and Weight type :\n\n{df_orders}")


    # check_weight_outlier(df_orders , columns=['Weight'])

    df_orders = remove_weight_outlier(df_orders , min_w = 40 , max_w = 133)
    # display(f"\nRemove some of the weight :\n\n{df_orders}")


    df_orders = k_bins_discretizer(df_orders , columns=['Weight'])
    # display(f"\nMake 5 bins for weight columns :\n\n{df_orders}")

    # با ترو فالز نشون میده
    df_orders = one_hot_encoder_isavailable(df_orders , columns=['IsAvailable'])
    # display(f"\nUse one hot encoder for IsAvailable column :\n\n{df_orders}")


    df_orders = label_encoder_color_product(df_orders , columns=['Color' , 'Product'])
    # display(f"\nUse label encoder for color and product columns :\n\n{df_orders}")


    df_orders = drop_unnecessary_columns(df_orders , columns=['CustomerName' , 'PurchaseDate'])
    # display(f"\nDrop unnecessary columns like name and date :\n\n{df_orders}")


    # df_orders = normalization_data(df_orders , columns=['Product' , 'Quantity' , 'PurchaseAmount' , 'Color' , 'Weight' , 'IsAvailable_No' , 'IsAvailable_Yes'])
    # display(f"\nNormalization all data :\n\n{df_orders}")

    # میتونیم از نرمال سازی یا استاندارد سازی استفاده کنیم هرکدوم که دوست داشتیم و اینجا هر دو رو اوردم

    df_orders = standardization_data(df_orders , columns=['Product' , 'Quantity' , 'PurchaseAmount' , 'Color' , 'Weight' , 'IsAvailable_No' , 'IsAvailable_Yes'])
    # display(f"\nStandardization all data :\n\n{df_orders}")

    save_final_data(df_orders , FINAL_PATH)


if __name__ == "__main__":
    main()