from math import ceil
from typing import Dict, List
from .providers import get_redis_module

from .common_constants import COUNTRY_CODE_ALIAS
from .common_constants import FIRST_PLACE_OF_LEADERBOARD_BY_COUNTRY
from .common_constants import LEADERBOARD_KEY
from .common_constants import NINETY_NINE_PLACE_LEADERBOARD_BY_COUNTRY
from .common_constants import PERCENT_SYMBOL
from .common_constants import PLACE_ALIAS
from .common_constants import PLUS_SYMBOL
from .common_constants import TENTH_PLACE_OF_LEADERBOARD_BY_COUNTRY
from .common_constants import TOP_ALIAS
from .common_constants import TOTAL_EXPERIENCE_ALIAS
from .common_constants import USER_ID_ALIAS


def get_leaderboard_by_country(user: Dict):
    redis_client = get_redis_module()
    leaderboard_key = LEADERBOARD_KEY.format(country_code=user[COUNTRY_CODE_ALIAS])
    leaderboard_with_scores = redis_client.zrange(
        leaderboard_key,
        FIRST_PLACE_OF_LEADERBOARD_BY_COUNTRY,
        TENTH_PLACE_OF_LEADERBOARD_BY_COUNTRY,
        withscores=True,
        desc=True
    )
    leaderboard: List[Dict] = []
    for place, (user_id, total_experience) in enumerate(leaderboard_with_scores):
        user_extra_data = redis_client.hgetall(user_id)
        user_dict = {
            PLACE_ALIAS: str(place+1),
            USER_ID_ALIAS: str(user_id),
            TOTAL_EXPERIENCE_ALIAS: total_experience,
            **user_extra_data,
        }
        leaderboard.append(user_dict)
    user_place = redis_client.zrevrank(leaderboard_key, user[USER_ID_ALIAS])
    user_score = redis_client.zscore(leaderboard_key, user[USER_ID_ALIAS])
    user_extra_data = redis_client.hgetall(user[USER_ID_ALIAS])
    number_of_users = redis_client.zcard(leaderboard_key)
    user_top = ceil(((user_place+1)*100)/number_of_users)
    if FIRST_PLACE_OF_LEADERBOARD_BY_COUNTRY <= user_place <= TENTH_PLACE_OF_LEADERBOARD_BY_COUNTRY:
        custom_user_place = str(user_place+1)
        index_in_leaderboard = user_place
    elif TENTH_PLACE_OF_LEADERBOARD_BY_COUNTRY < user_place <= NINETY_NINE_PLACE_LEADERBOARD_BY_COUNTRY:
        custom_user_place = str(user_place+1)
        index_in_leaderboard = TENTH_PLACE_OF_LEADERBOARD_BY_COUNTRY
    elif user_place > NINETY_NINE_PLACE_LEADERBOARD_BY_COUNTRY:
        custom_user_place = str(NINETY_NINE_PLACE_LEADERBOARD_BY_COUNTRY) + PLUS_SYMBOL
        index_in_leaderboard = TENTH_PLACE_OF_LEADERBOARD_BY_COUNTRY
    user_dict = {
        PLACE_ALIAS: custom_user_place,
        TOP_ALIAS: str(user_top+1) + PERCENT_SYMBOL,
        USER_ID_ALIAS: user[USER_ID_ALIAS],
        TOTAL_EXPERIENCE_ALIAS: user_score,
        **user_extra_data,
    }
    leaderboard.pop(index_in_leaderboard)
    leaderboard.insert(index_in_leaderboard, user_dict)
    return leaderboard
