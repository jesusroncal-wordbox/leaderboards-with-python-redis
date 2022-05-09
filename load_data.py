from concurrent.futures import ThreadPoolExecutor
from typing import Union
from typing import Dict
from typing import Final
from typing import Tuple

from common_constants import LEADERBOARD_KEY
from common_constants import NAME_ALIAS
from common_constants import URL_PHOTO_ALIAS
from common_constants import USER_ID_ALIAS
from providers import get_redis_module


BATCH: Final[int] = 50000
HYPHEN: Final[str] = "-"


redis_client = get_redis_module()


def create_dummy_data(country_code: str, index: str) -> Tuple[str, Dict[str, str], Dict[str, Union[str, int]]]:
    return (
        country_code + HYPHEN + USER_ID_ALIAS + index,
        {
            USER_ID_ALIAS + HYPHEN + index: int(index),
        },
        {
            NAME_ALIAS: NAME_ALIAS + index,
            URL_PHOTO_ALIAS: URL_PHOTO_ALIAS + index,
        },
    )


def load_dummy_data_to_redis_by_country_code(number_of_records: int, country_code: str) -> None:
    executor = ThreadPoolExecutor()
    for i in range(0, number_of_records, BATCH):
        start = i + 1
        end = i + BATCH
        executor.submit(_load_dummy_data_to_redis_by_country_code, start, end, country_code)
    executor.shutdown()


def _load_dummy_data_to_redis_by_country_code(start: int, end: int, country_code: str) ->  None:
    leaderboard_key = LEADERBOARD_KEY.format(country_code=country_code)
    for i in range(start, end+1):
        user_id, user_data_to_zadd, user_data_to_hset = create_dummy_data(country_code, str(i))
        redis_client.zadd(leaderboard_key, mapping=user_data_to_zadd)
        redis_client.hset(user_id, mapping=user_data_to_hset)
