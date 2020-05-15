from sqlalchemy import create_engine


def local_db():
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'root'
    PASSWORD = 'root'
    HOST = 'localhost'
    PORT = '3306'
    DATABASE = 'job'

    SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(
        DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE
    )

    local_db = create_engine(SQLALCHEMY_DATABASE_URI)
    return local_db
