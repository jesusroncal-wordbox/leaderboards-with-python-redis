import json
from typing import Dict
from typing import Final
from typing import List

from .common_constants import COUNTRY_CODE_ALIAS
from .common_constants import FIRST_PLACE_OF_LEADERBOARD_BY_COUNTRY
from .common_constants import LEADERBOARD_KEY
from .common_constants import LEVEL_ALIAS
from .common_constants import MEXICO_COUNTRY_CODE
from .common_constants import NAME_ALIAS
from .common_constants import PHOTO_URL_ALIAS
from .common_constants import TENTH_PLACE_OF_LEADERBOARD_BY_COUNTRY
from .common_constants import TOTAL_EXPERIENCE_ALIAS
from .common_constants import USER_ID_ALIAS
from .providers import get_redis_module


PARAMS: Final[Dict] = {
    USER_ID_ALIAS: "MX-userid1000001",
    COUNTRY_CODE_ALIAS: MEXICO_COUNTRY_CODE,
    TOTAL_EXPERIENCE_ALIAS: 1000001,
    NAME_ALIAS: NAME_ALIAS + str(1000001),
    LEVEL_ALIAS: 1000001,
    PHOTO_URL_ALIAS: PHOTO_URL_ALIAS + str(1000001),
}


redis_client = get_redis_module()
# Updates user to leaderboard
user_to_update = PARAMS.copy()
leaderboard_key = LEADERBOARD_KEY.format(
    country_code=user_to_update.pop(COUNTRY_CODE_ALIAS)
)
redis_client.zadd(
    leaderboard_key,
    user_to_update.pop(TOTAL_EXPERIENCE_ALIAS),
    user_to_update[USER_ID_ALIAS],
)
redis_client.hset(
    user_to_update.pop(USER_ID_ALIAS),
    mapping=user_to_update,
)
# Gets users with scores
leaderboard_with_scores = redis_client.zrange(
    leaderboard_key,
    FIRST_PLACE_OF_LEADERBOARD_BY_COUNTRY,
    TENTH_PLACE_OF_LEADERBOARD_BY_COUNTRY,
    withscores=True,
    desc=True,
)
# Builds response
users_list: List[Dict] = []
for user_id, total_experience in leaderboard_with_scores:
    user_extra_data = redis_client.hgetall(user_id)
    user_dict = {
        USER_ID_ALIAS: str(user_id),
        TOTAL_EXPERIENCE_ALIAS: total_experience,
        **user_extra_data,
    }
    users_list.append(user_dict)
print(json.dumps(users_list))
