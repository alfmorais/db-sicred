from typing import List


class Contract:
    def __init__(self, id: int, debt: int) -> None:
        self.id = id
        self.debt = debt

    def __str__(self) -> str:
        return "id={}, debt={}".format(self.id, self.debt)


class Contracts:
    def bubble_sort_contracts(self, contracts: List[Contract]) -> List[Contract]:
        n = len(contracts)
        for i in range(n):
            for j in range(0, n - i - 1):
                if contracts[j].debt < contracts[j + 1].debt:
                    contracts[j], contracts[j + 1] = contracts[j + 1], contracts[j]
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
