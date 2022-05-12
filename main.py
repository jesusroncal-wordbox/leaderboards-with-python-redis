import time
from typing import Dict
from typing import Final

from src.common_constants import COLOMBIA_COUNTRY_CODE
from src.common_constants import COUNTRY_CODE_ALIAS
from src.common_constants import MEXICO_COUNTRY_CODE
from src.common_constants import PERU_COUNTRY_CODE
from src.common_constants import USER_ID_ALIAS
from src.get_leaderboard import get_leaderboard_by_country

# from src.load_data import load_dummy_data_to_redis_by_country_code
# from src.providers import get_redis_module


CASE_1_WITH_10K_RECORDS: Final[Dict] = {
    USER_ID_ALIAS: "PE-userid10000",
    COUNTRY_CODE_ALIAS: PERU_COUNTRY_CODE,
}
CASE_1_WITH_100K_RECORDS: Final[Dict] = {
    USER_ID_ALIAS: "CO-userid99999",
    COUNTRY_CODE_ALIAS: COLOMBIA_COUNTRY_CODE,
}
CASE_1_WITH_1M_RECORDS: Final[Dict] = {
    USER_ID_ALIAS: "MX-userid999998",
    COUNTRY_CODE_ALIAS: MEXICO_COUNTRY_CODE,
}

CASE_2_WITH_10K_RECORDS: Final[Dict] = {
    USER_ID_ALIAS: "PE-userid9971",
    COUNTRY_CODE_ALIAS: PERU_COUNTRY_CODE,
}
CASE_2_WITH_100K_RECORDS: Final[Dict] = {
    USER_ID_ALIAS: "CO-userid99941",
    COUNTRY_CODE_ALIAS: COLOMBIA_COUNTRY_CODE,
}
CASE_2_WITH_1M_RECORDS: Final[Dict] = {
    USER_ID_ALIAS: "MX-userid999911",
    COUNTRY_CODE_ALIAS: MEXICO_COUNTRY_CODE,
}

CASE_3_WITH_10K_RECORDS: Final[Dict] = {
    USER_ID_ALIAS: "PE-userid5001",
    COUNTRY_CODE_ALIAS: PERU_COUNTRY_CODE,
}
CASE_3_WITH_100K_RECORDS: Final[Dict] = {
    USER_ID_ALIAS: "CO-userid50001",
    COUNTRY_CODE_ALIAS: COLOMBIA_COUNTRY_CODE,
}
CASE_3_WITH_1M_RECORDS: Final[Dict] = {
    USER_ID_ALIAS: "MX-userid500001",
    COUNTRY_CODE_ALIAS: MEXICO_COUNTRY_CODE,
}
ELAPSED_TIME_MSG: Final = "Elapsed time: {elapsed_time:0.4f} seconds\n"


if __name__ == "__main__":
    # Initial context
    # redis_client = get_redis_module()
    # redis_client.flushdb()
    # load_dummy_data_to_redis_by_country_code(10000, PERU_COUNTRY_CODE)
    # load_dummy_data_to_redis_by_country_code(100000, COLOMBIA_COUNTRY_CODE)
    # load_dummy_data_to_redis_by_country_code(1000000, MEXICO_COUNTRY_CODE)

    with open("report.txt", "w") as file:
        file.write(
            "RESPONSE TIME REPORT TO GET THE LEADERBOARD BY COUNTRY WITH DIFFERENT NUMBER OF RECORDS AND USER PLACE\n\n"
        )

        # Case 1: Get leaderboard per country when the user is within the first 10 places
        file.write(
            "Case 1: Get leaderboard per country when the user is within the first 10 places with 10K records\n"
        )
        tic = time.perf_counter()
        leaderboard_of_case_1_with_10k = get_leaderboard_by_country(
            CASE_1_WITH_10K_RECORDS
        )
        toc = time.perf_counter()
        file.write(ELAPSED_TIME_MSG.format(elapsed_time=toc - tic))
        file.write(f"input: {CASE_1_WITH_10K_RECORDS}\n")
        file.write(f"output: {leaderboard_of_case_1_with_10k}\n\n")

        file.write(
            "Case 1: Get leaderboard per country when the user is within the first 10 places with 100K records\n"
        )
        tic = time.perf_counter()
        leaderboard_of_case_1_with_100k = get_leaderboard_by_country(
            CASE_1_WITH_100K_RECORDS
        )
        toc = time.perf_counter()
        file.write(ELAPSED_TIME_MSG.format(elapsed_time=toc - tic))
        file.write(f"input: {CASE_1_WITH_100K_RECORDS}\n")
        file.write(f"output: {leaderboard_of_case_1_with_100k}\n\n")

        file.write(
            "Case 1: Get leaderboard per country when the user is within the first 10 places with 1M records\n"
        )
        tic = time.perf_counter()
        leaderboard_of_case_1_with_1m = get_leaderboard_by_country(
            CASE_1_WITH_1M_RECORDS
        )
        toc = time.perf_counter()
        file.write(ELAPSED_TIME_MSG.format(elapsed_time=toc - tic))
        file.write(f"input: {CASE_1_WITH_1M_RECORDS}\n")
        file.write(f"output: {leaderboard_of_case_1_with_1m}\n\n\n")

        # Case 2: Get leaderboard by country when the user is between 11th place and 99th place
        file.write(
            "Case 2: Get leaderboard by country when the user is between 11th place and 99th place with 10K records\n"
        )
        tic = time.perf_counter()
        leaderboard_of_case_2_with_10k = get_leaderboard_by_country(
            CASE_2_WITH_10K_RECORDS
        )
        toc = time.perf_counter()
        file.write(ELAPSED_TIME_MSG.format(elapsed_time=toc - tic))
        file.write(f"input: {CASE_2_WITH_10K_RECORDS}\n")
        file.write(f"output: {leaderboard_of_case_2_with_10k}\n\n")

        file.write(
            "Case 2: Get leaderboard by country when the user is between 11th place and 99th place with 100K records\n"
        )
        tic = time.perf_counter()
        leaderboard_of_case_2_with_100k = get_leaderboard_by_country(
            CASE_2_WITH_100K_RECORDS
        )
        toc = time.perf_counter()
        file.write(ELAPSED_TIME_MSG.format(elapsed_time=toc - tic))
        file.write(f"input: {CASE_2_WITH_100K_RECORDS}\n")
        file.write(f"output: {leaderboard_of_case_2_with_100k}\n\n")

        file.write(
            "Case 2: Get leaderboard by country when the user is between 11th place and 99th place with 1M records\n"
        )
        tic = time.perf_counter()
        leaderboard_of_case_2_with_1m = get_leaderboard_by_country(
            CASE_2_WITH_1M_RECORDS
        )
        toc = time.perf_counter()
        file.write(ELAPSED_TIME_MSG.format(elapsed_time=toc - tic))
        file.write(f"input: {CASE_2_WITH_1M_RECORDS}\n")
        file.write(f"output: {leaderboard_of_case_2_with_1m}\n\n\n")

        # Case 3: Get leaderboard by country when the user is above 99th place
        file.write(
            "Case 3: Get leaderboard by country when the user is above 99th place with 10K records\n"
        )
        tic = time.perf_counter()
        leaderboard_of_case_3_with_10k = get_leaderboard_by_country(
            CASE_3_WITH_10K_RECORDS
        )
        toc = time.perf_counter()
        file.write(ELAPSED_TIME_MSG.format(elapsed_time=toc - tic))
        file.write(f"input: {CASE_3_WITH_10K_RECORDS}\n")
        file.write(f"output: {leaderboard_of_case_3_with_10k}\n\n")

        file.write(
            "Case 3: Get leaderboard by country when the user is above 99th place with 100K records\n"
        )
        tic = time.perf_counter()
        leaderboard_of_case_3_with_100k = get_leaderboard_by_country(
            CASE_3_WITH_100K_RECORDS
        )
        toc = time.perf_counter()
        file.write(ELAPSED_TIME_MSG.format(elapsed_time=toc - tic))
        file.write(f"input: {CASE_3_WITH_100K_RECORDS}\n")
        file.write(f"output: {leaderboard_of_case_3_with_100k}\n\n")

        file.write(
            "Case 3: Get leaderboard by country when the user is above 99th place with 1M records\n"
        )
        tic = time.perf_counter()
        leaderboard_of_case_3_with_1m = get_leaderboard_by_country(
            CASE_3_WITH_1M_RECORDS
        )
        toc = time.perf_counter()
        file.write(ELAPSED_TIME_MSG.format(elapsed_time=toc - tic))
        file.write(f"input: {CASE_3_WITH_1M_RECORDS}\n")
        file.write(f"output: {leaderboard_of_case_3_with_1m}\n")

        file.close()
