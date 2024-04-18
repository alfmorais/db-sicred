from typing import Generator, List


class Orders:
    def bubble_sort(self, arr: List[int]) -> List[int]:
        array_size = len(arr)

        for index in range(array_size):
            for _index in range(0, array_size - index - 1):
                if arr[_index] < arr[_index + 1]:
                    arr[_index], arr[_index + 1] = arr[_index + 1], arr[_index]
        
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
                )

                if second_condition:
                    yield
                    sorted_requests.pop(0)
                    sorted_requests.pop()
                else:
                    yield
                    sorted_requests.pop(0)
