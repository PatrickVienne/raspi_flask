import logging

class Config(object):
    SECRET_KEY = '{SECRET_KEY}'
    SITE_NAME = 'Flask Site'
    SITE_ROOT_URL = 'http://it-q.space'
    LOG_LEVEL = logging.DEBUG

    MEMCACHED_SERVERS = ['localhost:80']
    SYS_ADMINS = ['codingbuddytest@gmail.com']

    # SQL support
    DB_HOST = "192.168.0.88"
    DB_PORT = 3306
    DB_USER = "root"
    DB_PW = "my-secret-pw"
    DB_NAME = "test_db"
    SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}:{}/{}'.format(DB_USER,DB_PW,DB_HOST,DB_PORT,DB_NAME)#
    SQLALCHEMY_TRACK_MODIFICATIONS = True


    # Mongo support
    MONGO_HOST = "192.168.0.88"
    MONGO_PORT = 27017
    MONGO_NAME = "mongo_test_db"
    SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}/{}'.format(DB_HOST,DB_PORT,DB_NAME)#
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # Configured for Gmail
    DEFAULT_MAIL_SENDER = 'Admin < codingbuddytest@gmail.com >'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'codingbuddytest@gmail.com'
    MAIL_PASSWORD = 'test010203'

    # Flask-Security setup
    SECURITY_EMAIL_SENDER = 'Security < security@example.com >'
    SECURITY_LOGIN_WITHOUT_CONFIRMATION = True
    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_URL_PREFIX = '/auth'
    SECUIRTY_POST_LOGIN = '/'
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    # import uuid; salt = uuid.uuid4().hex
    SECURITY_PASSWORD_SALT = '2b8b74efc58e489e879810905b6b6d4dc6'

    # CACHE
    CACHE_TYPE = 'simple'