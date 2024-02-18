


def remove_weight_outlier(data , min_w , max_w):
    return data[(data['Weight'] >= min_w) & (data['Weight'] <= max_w)]