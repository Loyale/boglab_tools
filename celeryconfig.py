from datetime import timedelta

BROKER_BACKEND = "redis"
BROKER_HOST = "127.0.0.1"
BROKER_PORT = 6379
BROKER_VHOST = "0"
BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "redis"
CELERY_REDIS_HOST = "localhost"
CELERY_REDIS_PORT = 6379
CELERY_REDIS_DB = 0

CELERY_TRACK_STARTED = True
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"

CELERYCAM_EXPIRE_SUCCESS = timedelta(days=7)
CELERYCAM_EXPIRE_ERROR = timedelta(days=7)
CELERYCAM_EXPIRE_PENDING = timedelta(days=7)

BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 172800} # 2 days

#CELERY_ALWAYS_EAGER = True
#CELERY_EAGER_PROPAGATES_EXCEPTIONS = True

#CELERY_IMPORTS = ("talent.tasks", )
