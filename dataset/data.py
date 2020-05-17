import pandas as pd


def get_df():
    lagou = pd.read_csv('../dataset/lagou_copy1_copy1.csv')
    n_lagou = lagou.drop_duplicates(subset='url', keep="first")

    return n_lagou

