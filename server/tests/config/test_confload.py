from xmlrpc.client import Fault

import pytest

from server.nfl.config.confload import to_bool


@pytest.mark.parametrize(
    "input_val, expected",
    [
        (True, True),
        (False, False),
        ("True", True),
        ("False", False),
        ("true", True),
        ("false", False),
        ("TrUe", True),
        ("faLse", False)
    ]
)
def test_to_bool(input_val, expected):
    assert to_bool(input_val) is expected


def test_to_bool_invalid():
    with pytest.raises(ValueError) as e:
        to_bool("talse")
