import time

import pytest
from src.worst_question1 import Contract, Contracts


@pytest.mark.parametrize(
    "open_contracts,renegotiated_contracts,top_n,response",
    [
        (
            [
                Contract(1, 1),
                Contract(2, 2),
                Contract(3, 3),
                Contract(4, 4),
                Contract(5, 5),
            ],
            [3],
            3,
            [5, 4, 2],
        ),
        (
            [
                Contract(15, 100),
                Contract(28, 289),
                Contract(39, 378),
                Contract(44, 468),
                Contract(59, 598),
            ],
            [15, 39],
            2,
            [59, 44],
        ),
        (
            [
                Contract(17, 987),
                Contract(28, 478),
                Contract(39, 352),
                Contract(40, 452),
                Contract(51, 547),
            ],
            [],
            1,
            [17],
        ),
    ],
)
def test_contract_success(
    open_contracts,
    renegotiated_contracts,
    top_n,
    response,
):
    contract = Contracts()

    start_time = time.time()
    response_open_contracts = contract.get_top_N_open_contracts(
        open_contracts,
        renegotiated_contracts,
        top_n,
    )
    end_time = time.time()

    excecution_time = end_time - start_time

    assert response_open_contracts == response
    assert excecution_time < 0.1
