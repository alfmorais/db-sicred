from typing import List


class Contract:
    def __init__(self, id: int, debt: int) -> None:
        self.id = id
        self.debt = debt

    def __str__(self) -> str:
        return "id={}, debt={}".format(self.id, self.debt)


class Contracts:
    def get_top_N_open_contracts(
        self,
        open_contracts: List[Contract],
        renegotiated_contracts: List[int],
        top_n: int,
    ):
        filter_contracts = (
            contract
            for contract in open_contracts
            if contract.id not in renegotiated_contracts
        )
        sorted_contracts = sorted(
            filter_contracts,
            key=lambda contract: contract.debt,
            reverse=True,
        )
        return [contract.id for contract in sorted_contracts[:top_n]]
