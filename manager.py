import random

from flask import Flask, request, g, jsonify

from models.knn import main, predicate_by_label
from utils.g_var import df_login_data
from utils.predict_position_utils import get_position_list

app = Flask(__name__)
neigh, vectorizer, lagou_df = main()


@app.route("/")
def index():
    return "hello flask"


@app.route("/predict_salary", methods=['POST'])
def predict_salary():
    data = request.json
    # "work": '',
    # "part": "",
    # "year": "",
    # "education": "",
    # print(data)
    # work = '算法'
    # part = '北京'
    # year = '5年'
    # education = '本科'
    work = data.get('work')
    part = data.get('part')
    year = data.get('year')
    education = data.get('education')
    test = ' '.join([work, part, year, education])
    salary = predicate_by_label(test, neigh, vectorizer)
    positionList = get_position_list(lagou_df, random.randint(6, 10))
    data = {
        'salary': salary,
        'positionList': positionList,
    }
    return jsonify(data)


@app.route("/search_ratio")
def search_ratio():
    pass


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=15015, debug=True)
