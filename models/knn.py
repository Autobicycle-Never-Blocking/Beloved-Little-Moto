import re
import numpy as np
import jieba
from sklearn.neighbors import KNeighborsRegressor
from sklearn.feature_extraction.text import TfidfVectorizer

from dataset.data import get_df


def split_data(df):
    X_content = df.drop(['salary'], axis=1)
    target = df['salary'].tolist()

    X_content['merged'] = X_content.apply(lambda x: ''.join(str(x)), axis=1)
    X_string = X_content['merged'].tolist()

    return X_string, target


def get_one_row_job_string(x_string_row):
    job_string = ''

    for i, element in enumerate(x_string_row.split('\n')):
        if len(element.split()) == 2:
            _, value = element.split()
            if i == 0:
                continue
            # print(value)

            job_string += value

    return job_string


def get_train_X(cutted_X):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(cutted_X)
    return X, vectorizer


def get_train_Y(target):
    target_numical = [np.mean(list(map(float, re.findall('\d+', s)))) for s in target]
    return target_numical


def knn_model(X, Y):
    neigh = KNeighborsRegressor(n_neighbors=4)
    neigh.fit(X, Y)
    return neigh


def predicate_by_label(test_string, model, vectorizer):
    test_words = list(jieba.cut(test_string))

    test_vec = vectorizer.transform(test_words)

    predicated_value = model.predict(test_vec)

    return predicated_value[0]


def token(string):
    return re.findall('\w+', string)


def main():
    lagou_df = get_df()
    X_string, target = split_data(lagou_df)
    string_training_corpus = []
    cutted_X = []
    for i, row in enumerate(X_string):
        job_string = get_one_row_job_string(row)

        cutted_X.append(' '.join(list(jieba.cut(''.join(token(job_string))))))
    X, vectorizer = get_train_X(cutted_X)
    Y = get_train_Y(target)
    neigh = knn_model(X, Y)

    return neigh, vectorizer, lagou_df


if __name__ == '__main__':
    neigh, vectorizer, lagou_df = main()
    test = '算法 北京 4年 本科'
    print(predicate_by_label(test, neigh, vectorizer))
