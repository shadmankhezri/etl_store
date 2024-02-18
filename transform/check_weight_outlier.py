

import plotly.express as px


def check_weight_outlier(data , columns):
    fig = px.box(data , y=columns)
    fig.show()

