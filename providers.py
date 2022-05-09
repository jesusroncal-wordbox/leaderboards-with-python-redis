import os
import redis
from dotenv import load_dotenv
from typing import Final


load_dotenv()


EMPTY_STRING: Final[str] = ""
INTEGER_DEFAULT: Final[int] = 0
REDIS_HOST_KEY: Final[str] = "REDIS_HOST"
REDIS_PORT_KEY: Final[str] = "REDIS_PORT"
REDIS_DATABASE_KEY: Final[str] = "REDIS_DATABASE"
REDIS_PASSWORD_KEY: Final[str] = "REDIS_PASSWORD"


def get_redis_module() -> redis.Redis:
    redis_host = os.getenv(REDIS_HOST_KEY, EMPTY_STRING)
    redis_port = int(os.getenv(REDIS_PORT_KEY, INTEGER_DEFAULT))
    redis_database = int(os.getenv(REDIS_DATABASE_KEY, INTEGER_DEFAULT))
    redis_password = os.getenv(REDIS_PASSWORD_KEY, None)
    redis_client = redis.StrictRedis(
        host=redis_host, port=redis_port, db=redis_database, password=redis_password, decode_responses=True
    )
    return redis_client
