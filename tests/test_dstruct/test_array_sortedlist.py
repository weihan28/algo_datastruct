""" Testing the array implementation of a Dynamic Sorted List.
"""

import pytest

from src.dstruct.ADT_implementations.List.array_sortedlist import ASortedList

SIZE = 10
DS = ASortedList


@pytest.fixture
def lst():
    return DS(SIZE)


def test_init(lst):
    # number of elements is 0
    assert len(lst) == 0
    assert lst.is_empty() == True


def test_init_invalid_length():
    # when length is negative, it should be set to 1
    lst = DS(-1)
    assert len(lst.array) == 1


def test_str_empty(lst):
    assert str(lst) == "[]"


def test_add(lst):
    lst.add(100)
    assert str(lst) == "[100]"
    assert len(lst) == 1

    lst.add(50)
    assert str(lst) == "[50, 100]"
    assert len(lst) == 2

    lst.add(101)
    assert str(lst) == "[50, 100, 101]"
    assert len(lst) == 3


def test_get(lst):
    for i in reversed(range(1,4)):
        lst.add(i)

    assert lst[0] == 1
    assert lst[1] == 2
    assert lst[2] == 3
    assert len(lst) == 3

    with pytest.raises(IndexError):
        lst[3]
    
    with pytest.raises(IndexError):
        lst[-1]


def test_pop(lst):
    for i in reversed(range(1,4)):
        lst.add(i)

    with pytest.raises(IndexError):
        lst.pop(3)
    with pytest.raises(IndexError):
        lst.pop(-1)

    assert lst.pop(0) == 1
    assert str(lst) == "[2, 3]"
    assert len(lst) == 2
    assert lst.pop(1) == 3
    assert str(lst) == "[2]"
    assert lst.pop(0) == 2
    assert str(lst) == "[]"
    assert len(lst) == 0

    with pytest.raises(IndexError):
        lst.pop(0)


def test_clear(lst):
    for i in range(1,4):
        lst.add(i)

    lst.clear()
    assert str(lst) == "[]"
    assert len(lst) == 0


def test_dynamic_size_add(lst):
    # used in fixed size lst implementation where it doubles the capacity
    for i in range(SIZE):
        lst.add(i)

    assert len(lst) == SIZE
    assert lst.is_full() == True

    lst.add(1)
    assert len(lst.array) == SIZE*2
    assert len(lst) == SIZE+1


def test_remove(lst):
    for i in range(1,4):
        lst.add(i)
        lst.add(i)

    lst.remove(1)
    assert str(lst) == "[1, 2, 2, 3, 3]"
    assert len(lst) == 5

    lst.remove(2)
    assert str(lst) == "[1, 2, 3, 3]"
    assert len(lst) == 4

    lst.remove(3)
    assert str(lst) == "[1, 2, 3]"
    assert len(lst) == 3
    lst.remove(3)
    assert str(lst) == "[1, 2]"
    assert len(lst) == 2
    with pytest.raises(ValueError):
        lst.remove(3)


def test_index(lst):
    for i in range(1,4):
        lst.add(i)
        lst.add(i)

    assert str(lst) == "[1, 1, 2, 2, 3, 3]"
    assert lst.index(1) == 0
    assert lst.index(2) == 2
    assert lst.index(3) == 4
    with pytest.raises(ValueError):
        lst.index(4)


def test_contains(lst):
    for i in range(1,4):
        lst.add(i)

    assert 1 in lst
    assert 2 in lst
    assert 3 in lst
    assert 4 not in lst