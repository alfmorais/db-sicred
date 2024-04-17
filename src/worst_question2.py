from typing import Generator, List


class Orders:
    def bubble_sort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def combine_orders(self, requests: List[int], n_max: int) -> int:
        sorted_requests = self.bubble_sort(requests)
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
