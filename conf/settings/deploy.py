from conf.settings.base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ["*"]


DATABASES = {
    'default': {
        'ENGINE':   get_secret_key("DB_DP_ENGINE"),
        'NAME':     get_secret_key("DB_DP_NAME"),
        "USER":     get_secret_key("DB_DP_USER"),
        "PASSWORD": get_secret_key("DB_DP_PASSWORD"),
        "HOST":     get_secret_key("DB_DP_HOST"),
        "PORT":     get_secret_key("DB_DP_PORT"),
    }
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES["default"].update(db_from_env)