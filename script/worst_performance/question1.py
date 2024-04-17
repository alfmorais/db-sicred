import time

from memory_profiler import profile
from src.worst_question1 import Contract, Contracts


@profile
def main(range_limit: int) -> None:
    open_contracts = [Contract(index, index) for index in range(1, range_limit, 1)]
    renegotiated_contracts = [3]
    top_n = 3

    contracts = Contracts()
    contracts.get_top_N_open_contracts(
        open_contracts,
        renegotiated_contracts,
        top_n,
    )


if __name__ == "__main__":
    for range_limit in [1_000, 5_000, 10_000, 50_000, 100_000]:
        start_time = time.time()
        main(range_limit)
        end_time = time.time()

        delta_time = end_time - start_time
        print("Time: {} for {} Contracts".format(delta_time, range_limit))
