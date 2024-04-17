import pytest
from src.question2 import Orders


@pytest.mark.parametrize(
    "requests,n_max,expected_requests",
    [
        (
            [70, 30, 10],
            100,
            2,
        ),
        (
            [450, 320, 150],
            470,
            2,
        ),
        (
            [1500, 3500, 7500],
            5000,
            2,
        ),
    ],
)
def test_contract_success(requests, n_max, expected_requests):
    orders = Orders()
    how_many = orders.combine_orders(requests, n_max)

    assert how_many == expected_requests
