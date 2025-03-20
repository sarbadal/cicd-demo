import pytest
from func.utils import get_firstname, get_lastname

FULL_NAME = "Tanya Howard"


def test_get_firstname() -> None:
    first_name = "Tanya"
    result = get_firstname(full_name=FULL_NAME)
    assert result == first_name
    


def test_get_lastname() -> None:
    last_name = "Howard"
    result = get_lastname(full_name=FULL_NAME)
    assert result == last_name