from conf.settings.base import *
import dj_database_url

DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE':   get_secret_key("DB_DV_ENGINE"),
        'NAME':     get_secret_key("DB_DV_NAME"),
        "USER":     get_secret_key("DB_DV_USER"),
        "PASSWORD": get_secret_key("DB_DV_PASSWORD"),
        "HOST":     get_secret_key("DB_DV_HOST"),
        "PORT":     get_secret_key("DB_DV_PORT"),
    }
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES["default"].update(db_from_env)