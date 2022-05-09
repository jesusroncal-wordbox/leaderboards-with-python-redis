from typing import Dict
from typing import Final
from common_constants import COLOMBIA_COUNTRY_CODE
from common_constants import COUNTRY_CODE_ALIAS
from common_constants import MEXICO_COUNTRY_CODE
from common_constants import PERU_COUNTRY_CODE
from common_constants import USER_ID_ALIAS
from get_leaderboard import get_leaderboard_by_country
from load_data import load_dummy_data_to_redis_by_country_code
from providers import get_redis_module


CASE_1_WITH_10K_RECORDS: Final[Dict] = {
    USER_ID_ALIAS: "PE-userid1000000",
    COUNTRY_CODE_ALIAS: PERU_COUNTRY_CODE
}
CASE_1_WITH_100K_RECORDS: Final[Dict] = {
    USER_ID_ALIAS: "CO-userid99999",
    COUNTRY_CODE_ALIAS: COLOMBIA_COUNTRY_CODE
}
CASE_1_WITH_1M_RECORDS: Final[Dict] = {
    USER_ID_ALIAS: "MX-userid999998",
    COUNTRY_CODE_ALIAS: MEXICO_COUNTRY_CODE
}


if __name__ == "__main__":
    redis_client = get_redis_module()
    redis_client.flushdb()

    # Initial context
    load_dummy_data_to_redis_by_country_code(10000, PERU_COUNTRY_CODE)
    load_dummy_data_to_redis_by_country_code(100000, COLOMBIA_COUNTRY_CODE)
    load_dummy_data_to_redis_by_country_code(1000000, MEXICO_COUNTRY_CODE)

    # CASE 1: Get leaderboard per country when the user is within the first 10 places 
    get_leaderboard_by_country(CASE_1_WITH_10K_RECORDS)
    get_leaderboard_by_country(CASE_1_WITH_100K_RECORDS)
    get_leaderboard_by_country(CASE_1_WITH_1M_RECORDS)
