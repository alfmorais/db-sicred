import time

from memory_profiler import profile
from src.worst_question2 import Orders


@profile
def main(range_limit: int) -> None:
    requests = [number for number in range(1, range_limit, 1)]
    n_max = 3

    orders = Orders()
    orders.combine_orders(requests, n_max)


if __name__ == "__main__":
    for range_limit in [1_000, 5_000, 10_000, 50_000, 100_000]:
        start_time = time.time()
        main(range_limit)
        end_time = time.time()

        delta_time = end_time - start_time
        print("Time: {} for {} Contracts".format(delta_time, range_limit))
