import pandas as pd


def get_df():
    lagou = pd.read_csv('dataset/lagou_copy1_copy1.csv')
    n_lagou = lagou.drop_duplicates(subset='url', keep="first")
    n_lagou[['lower_salary', 'avg_salary', 'upper_salary']] = n_lagou.apply(lambda x: get_salary(x['salary']),
                                                                            axis=1,
                                                                            result_type="expand")

    return n_lagou


def get_salary(salary):
    salary = salary.lower().replace('k', '').replace('以上', '')
    salary_range = salary.split('-')

    if len(salary_range) == 1:
        return int(salary_range[0]), int(salary_range[0]), int(salary_range[0])

    avg_salary = (int(salary_range[0]) + int(salary_range[1])) / 2.0
    return int(salary_range[0]), avg_salary, int(salary_range[1])
