from flask import Flask

# 创建一个应用
app = Flask(__name__)


@app.route("/")
def index():
    return "hello flask"


@app.route("/predict_salary")
def predict_salary():

    return "hello flask"




if __name__ == '__main__':
    app.run(host="127.0.0.1", port=15111, debug=True)
