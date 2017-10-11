import os

class config(object):
    SECRET_KEY = os.getenv('SECRET_KEY','samplekey')

class dev_config(config):

    SECRET_KEY = os.getenv('SECRET_KEY','awskey')
    ENGINE = 'mysql+pymysql'
    USERNAME = 'root'
    PASSWORD = 'QaWsEd179'
    HOST = 'localhost'
    DBNAME = 'react_flask'
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}/{}'.format(ENGINE,USERNAME,PASSWORD,HOST,DBNAME)
