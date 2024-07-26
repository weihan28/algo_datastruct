""" Testcase for basic operations of an array.
"""
import pytest
from src.dstruct.ADT_implementations.referential_array import ArrayR


SIZE = 10
DS = ArrayR

@pytest.fixture
def array():
    return DS(SIZE)


def test_init(array):
    assert len(array) == SIZE


def test_init_invalid_length():
    with pytest.raises(ValueError):
        DS(-1)


def test_setitem(array):
    array[0] = 1
    assert str(array) == "[1, None, None, None, None, None, None, None, None, None]"

    array[0] = 2
    assert str(array) == "[2, None, None, None, None, None, None, None, None, None]"

    array[SIZE-1] = 1
    assert str(array) == "[2, None, None, None, None, None, None, None, None, 1]"


def test_setitem_invalid_index(array):
    with pytest.raises(IndexError):
        array[SIZE] = 1

    with pytest.raises(IndexError):
        array[-1] = 1


def test_getitem(array):
    array[0] = 1
    assert array[0] == 1

    array[0] = 100
    assert array[0] == 100

    array[SIZE-1] = 1
    assert array[SIZE-1] == 1


def test_getitem_invalid_index(array):
    with pytest.raises(IndexError):
        array[SIZE]

    with pytest.raises(IndexError):
        array[-1]


def test_str(array):
    assert str(array) == "[None, None, None, None, None, None, None, None, None, None]"
    array[0] = 1
    assert str(array) == "[1, None, None, None, None, None, None, None, None, None]"
    array[1] = 2
    assert str(array) == "[1, 2, None, None, None, None, None, None, None, None]"
    array[2] = 3
    assert str(array) == "[1, 2, 3, None, None, None, None, None, None, None]"
    array[3] = 4
    assert str(array) == "[1, 2, 3, 4, None, None, None, None, None, None]"
    array[4] = 5
    assert str(array) == "[1, 2, 3, 4, 5, None, None, None, None, None]"
    array[5] = 6
    assert str(array) == "[1, 2, 3, 4, 5, 6, None, None, None, None]"
    array[6] = 7
    assert str(array) == "[1, 2, 3, 4, 5, 6, 7, None, None, None]"
    array[7] = 8
    assert str(array) == "[1, 2, 3, 4, 5, 6, 7, 8, None, None]"
    array[8] = 9
    assert str(array) == "[1, 2, 3, 4, 5, 6, 7, 8, 9, None]"
    array[9] = 10
    assert str(array) == "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"


def test_str_empty(array):
    assert str(array) == "[None, None, None, None, None, None, None, None, None, None]"