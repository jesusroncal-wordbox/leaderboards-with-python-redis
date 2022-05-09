from concurrent.futures import ThreadPoolExecutor
from typing import Union
from typing import Dict
from typing import Final
from typing import Tuple

from .common_constants import LEADERBOARD_KEY
from .common_constants import NAME_ALIAS
from .common_constants import URL_PHOTO_ALIAS
from .common_constants import USER_ID_ALIAS
from .decorators import timer
from .providers import get_redis_module


BATCH: Final[int] = 1000
HYPHEN: Final[str] = "-"
LOAD_DUMMY_DATA_TO_REDIS_BY_COUNTRY_CODE_MSG: Final = "{number_of_records} records loaded into redis for {leaderboard} leaderboard "


redis_client = get_redis_module()


def create_dummy_data(country_code: str, index: str) -> Tuple[str, Dict[str, str], Dict[str, Union[str, int]]]:
    return (
        country_code + HYPHEN + USER_ID_ALIAS + index,
        {
            country_code + HYPHEN + USER_ID_ALIAS + index: int(index),
        },
        {
            NAME_ALIAS: NAME_ALIAS + index,
            URL_PHOTO_ALIAS: URL_PHOTO_ALIAS + index,
        },
    )

@timer
def load_dummy_data_to_redis_by_country_code(number_of_records: int, country_code: str) -> None:
    leaderboard_key = LEADERBOARD_KEY.format(country_code=country_code)
    executor = ThreadPoolExecutor()
    for i in range(0, number_of_records, BATCH):
        start = i + 1
        end = i + BATCH
        executor.submit(_load_dummy_data_to_redis_by_country_code, start, end, leaderboard_key, country_code)
    executor.shutdown()
    print(LOAD_DUMMY_DATA_TO_REDIS_BY_COUNTRY_CODE_MSG.format(number_of_records=number_of_records, leaderboard=leaderboard_key))


def _load_dummy_data_to_redis_by_country_code(start: int, end: int, leaderboard_key: str, country_code: str) ->  None:
    for i in range(start, end+1):
        user_id, user_data_to_zadd, user_data_to_hset = create_dummy_data(country_code, str(i))
        redis_client.zadd(leaderboard_key, mapping=user_data_to_zadd)
        redis_client.hset(user_id, mapping=user_data_to_hset)
