from typing import Generator, List


class Orders:
    def combine_orders(self, requests: List[int], n_max: int) -> int:
        sorted_requests = sorted(requests, reverse=True)
        how_many = sum(1 for _ in Orders().generate(sorted_requests, n_max))
        return how_many

    def generate(self, sorted_requests: List[int], n_max: int) -> Generator:
        while sorted_requests:
            first_condition = len(sorted_requests) == 1

            if first_condition:
                yield
                sorted_requests.pop()

            else:
                second_condition = (
                    sorted_requests[0] + sorted_requests[-1] <= n_max
                )  # noqa E501

                if second_condition:
                    yield
                    sorted_requests.pop(0)
                    sorted_requests.pop()
                else:
                    yield
                    sorted_requests.pop(0)
