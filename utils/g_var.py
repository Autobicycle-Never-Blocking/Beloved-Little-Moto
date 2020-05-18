from functools import wraps

from flask import g

from models.knn import main


def df_login_data(view_func):
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        neigh, vectorizer, lagou_df = main()
        g.neigh = neigh
        g.vectorizer = vectorizer
        g.lagou_df = lagou_df

        return view_func(*args, **kwargs)

    return wrapper
