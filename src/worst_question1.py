from typing import List


class Contract:
    def __init__(self, id: int, debt: int) -> None:
        self.id = id
        self.debt = debt

    def __str__(self) -> str:
        return "id={}, debt={}".format(self.id, self.debt)


class Contracts:
    def bubble_sort_contracts(self, contracts: List[Contract]) -> List[Contract]:
        array_size = len(contracts)

        for index in range(array_size):
            for _index in range(0, array_size - index - 1):
                if contracts[_index].debt < contracts[_index + 1].debt:
                    contracts[_index], contracts[_index + 1] = (
                        contracts[_index + 1],
                        contracts[_index],
                    )

        return contracts

    def get_top_N_open_contracts(
        self,
        open_contracts: List[Contract],
        renegotiated_contracts: List[int],
        top_n: int,
    ):
        sorted_contracts = self.bubble_sort_contracts(open_contracts)
        filter_contracts = [
            contract
            for contract in sorted_contracts
            if contract.id not in renegotiated_contracts
        ]
        return [contract.id for contract in filter_contracts[:top_n]]
