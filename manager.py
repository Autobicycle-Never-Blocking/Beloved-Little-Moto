import random

from flask import Flask, request, g, jsonify
from flask_cors import CORS

from models.knn import main, predicate_by_label
from utils.g_var import df_login_data
from utils.predict_position_utils import get_position_list

app = Flask(__name__)
CORS(app, supports_credentials=True)
neigh, vectorizer, lagou_df = main()


@app.route("/")
def index():
    return "hello flask"


@app.route("/get_data", methods=['POST'])
def get_data():
    data = request.json
    city1 = data.get('city1')
    city2 = data.get('city2')
    city3 = data.get('city3')
    city4 = data.get('city4')

    data_dict = {
        "上海":    19.678295,
        "东莞":    12.750000,
        "北京":    24.003906,
        "南京":    15.125000,
        "天津":    13.800000,
        "宁波":     9.250000,
        "广州":    18.018519,
        "成都":    13.584906,
        "无锡":     8.000000,
        "昆明":     6.000000,
        "杭州":    17.668919,
        "武汉":    13.051724,
        "深圳":    19.259259,
        "苏州":    15.343750,
        "西安":    13.308824,
        "郑州":     8.500000,
        "重庆":    11.500000,
        "长沙":    10.750000,
        "青岛":    13.187500,
    }

    data = {
        'data': [data_dict.get(city1),data_dict.get(city2),data_dict.get(city3),data_dict.get(city4)]
    }

    return jsonify(data)


@app.route("/predict_salary", methods=['POST'])
def predict_salary():
    data = request.json
    print(data)
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
