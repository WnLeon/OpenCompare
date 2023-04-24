DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'opencompare'
PASSWORD = 'www.51idc.COM'
HOST = '43.254.55.108'
PORT = '9606'
DATABASE = 'opencompare'
DB_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
JSON_AS_ASCII = False #禁止中文转义