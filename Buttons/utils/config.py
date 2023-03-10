cache_config = {
    "CACHE_TYPE": "SimpleCache",
}

db_config = {
        'USER': 'flask_info',
        'PASSWORD': 'flask_info',
        'DB': 'info_db',
}
class Config():
    DEBUG =  True
    SECRET_KEY = 'kjbn#x^d8ut2$hkgds@fgj0'
    SQLALCHEMY_DATABASE_URI =  f'postgresql://{db_config["USER"]}:{db_config["PASSWORD"]}@localhost:5432/{db_config["DB"]}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    
 