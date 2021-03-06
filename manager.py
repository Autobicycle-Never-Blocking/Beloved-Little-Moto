import random

from flask import Flask, request, jsonify
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


@app.route("/top5")
def top5():
    firstTypeDF = lagou_df['firstType'].value_counts()
    top5_p_list = []
    top5_nums_list = []
    for k, v in firstTypeDF[:5].items():
        top5_p_list.append(k)
        top5_nums_list.append(v)
    data = {
        'top5_p_list': top5_p_list,
        'top5_nums_list': top5_nums_list,
    }
    return jsonify(data)


@app.route("/p_top5")
def p_top5():
    firstTypeDF = lagou_df['secondType'].value_counts()
    top5_p_list = []
    top5_nums_list = []
    for k, v in firstTypeDF[:5].items():
        top5_p_list.append(k)
        top5_nums_list.append(v)
    data = {
        'top5_p_list': top5_p_list,
        'top5_nums_list': top5_nums_list,
    }
    return jsonify(data)


@app.route("/get_data", methods=['POST'])
def get_data():
    data = request.json
    city = data.get('city')
    print(type(city))
    company_size = data.get('company_size')
    degree = data.get('degree')
    work_year = data.get('work_year')
    position = data.get('position')

    if all([company_size, degree, work_year, position]):
        res_df = lagou_df.loc[(lagou_df['thirdType'] == position) & (lagou_df['companySize'] == company_size) & (
                lagou_df['education'] == degree) & (lagou_df['workYear'] == work_year)]
    elif company_size and degree and work_year and not position:
        res_df = lagou_df.loc[(lagou_df['companySize'] == company_size) & (
                lagou_df['education'] == degree) & (lagou_df['workYear'] == work_year)]
    elif company_size and degree and not work_year and position:
        res_df = lagou_df.loc[(lagou_df['thirdType'] == position) & (lagou_df['companySize'] == company_size) & (
                lagou_df['education'] == degree)]
    elif company_size and not degree and work_year and position:
        res_df = lagou_df.loc[(lagou_df['thirdType'] == position) & (lagou_df['companySize'] == company_size) & (
                lagou_df['workYear'] == work_year)]
    elif not company_size and degree and work_year and position:
        res_df = lagou_df.loc[(lagou_df['thirdType'] == position) & (
                lagou_df['education'] == degree) & (lagou_df['workYear'] == work_year)]
    elif company_size and degree and not work_year and not position:
        res_df = lagou_df.loc[(lagou_df['companySize'] == company_size) & (
                lagou_df['education'] == degree)]
    elif company_size and not degree and work_year and not position:
        res_df = lagou_df.loc[(lagou_df['companySize'] == company_size) & (lagou_df['workYear'] == work_year)]
    elif not company_size and degree and work_year and not position:
        res_df = lagou_df.loc[(lagou_df['education'] == degree) & (lagou_df['workYear'] == work_year)]
    elif company_size and not degree and not work_year and position:
        res_df = lagou_df.loc[(lagou_df['companySize'] == company_size) & (lagou_df['thirdType'] == position)]
    elif not company_size and degree and not work_year and position:
        res_df = lagou_df.loc[(lagou_df['thirdType'] == position) & (lagou_df['education'] == degree)]
    elif not company_size and not degree and work_year and position:
        res_df = lagou_df.loc[(lagou_df['workYear'] == work_year) & (lagou_df['thirdType'] == position)]
    elif company_size and not degree and not work_year and not position:
        res_df = lagou_df.loc[(lagou_df['companySize'] == company_size)]
    elif not company_size and degree and not work_year and not position:
        res_df = lagou_df.loc[(lagou_df['education'] == degree)]
    elif not company_size and not degree and work_year and not position:
        res_df = lagou_df.loc[(lagou_df['workYear'] == work_year)]
    elif not company_size and not degree and not work_year and position:
        res_df = lagou_df.loc[(lagou_df['thirdType'] == position)]
    else:
        res_df = None

    if city and res_df is not None:
        city_salary = [round(res_df.loc[res_df['city'] == i].mean()['avg_salary'], 2) for i in city]

        data = {
            'city_salary': city_salary,
            'city': city,
        }
        print(data)
        return jsonify(data)

    elif city and res_df is None:
        city_salary = [round(lagou_df.loc[lagou_df['city'] == i].mean()['avg_salary'], 2) for i in city]

        data = {
            'city_salary': city_salary,
            'city': city,
        }
        print(data)
        return jsonify(data)

    else:
        return jsonify({'code': 404, 'msg': '未输入任何搜索条件，无法返回'})
    # data_dict = {
    #     "上海": 19.678295,
    #     "东莞": 12.750000,
    #     "北京": 24.003906,
    #     "南京": 15.125000,
    #     "天津": 13.800000,
    #     "宁波": 9.250000,
    #     "广州": 18.018519,
    #     "成都": 13.584906,
    #     "无锡": 8.000000,
    #     "昆明": 6.000000,
    #     "杭州": 17.668919,
    #     "武汉": 13.051724,
    #     "深圳": 19.259259,
    #     "苏州": 15.343750,
    #     "西安": 13.308824,
    #     "郑州": 8.500000,
    #     "重庆": 11.500000,
    #     "长沙": 10.750000,
    #     "青岛": 13.187500,
    # }
    #
    # data = {
    #     'city_salary': [data_dict.get(city1), data_dict.get(city2), data_dict.get(city3), data_dict.get(city4)],
    #     'city': [city1, city2, city3, city4],
    # }
    #
    # return jsonify(data)


@app.route("/predict_salary", methods=['POST'])
def predict_salary():
    data = request.json
    # print(data)
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
    app.config['JSON_AS_ASCII'] = False
    app.run(host="0.0.0.0", port=15015, debug=True)
