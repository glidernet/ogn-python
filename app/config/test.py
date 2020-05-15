SQLALCHEMY_DATABASE_URI = "postgresql://postgres@localhost:5432/ogn_test"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

# Flask-Cache stuff
CACHE_TYPE = "simple"
CACHE_DEFAULT_TIMEOUT = 300

# Celery stuff
CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "redis://localhost:6379/0"
