""" Test Set ADT implemented with Array.
"""
import pytest

from src.dstruct.ADT_implementations.Set.array_set import ASet


CAPACITY = 10


@pytest.fixture
def set_adt():
    return ASet(CAPACITY)


@pytest.fixture
def setA():
    """
    setA = {1, 2, 3, 4, 5}
    """
    set_a = ASet(CAPACITY)
    for i in range(1, 6):
        set_a.add(i)
    return set_a


@pytest.fixture
def setB():
    """
    setB = {2, 3, 4, 5, 6}
    """
    set_b = ASet(CAPACITY)
    for i in range(2, 7):
        set_b.add(i)
    return set_b


@pytest.fixture
def setC():
    """
    setC = {10, 11, 12, 13, 14}
    """
    set_c = ASet(CAPACITY)
    for i in range(10, 15):
        set_c.add(i)
    return set_c


def test_init(set_adt):
    assert len(set_adt) == 0
    assert len(set_adt.array) == CAPACITY


def test_add(set_adt):
    set_adt.add(1)
    set_adt.add(2)
    assert len(set_adt) == 2
    assert set_adt.array[0] == 1
    assert set_adt.array[1] == 2


def test_add_duplicate(set_adt):
    set_adt.add(1)
    set_adt.add(1)
    assert len(set_adt) == 1
    assert set_adt.array[0] == 1
    assert set_adt.array[1] == None


def test_add_resize(set_adt):
    for i in range(CAPACITY):
        set_adt.add(i)
    assert set_adt.is_full() == True
    assert len(set_adt) == CAPACITY

    set_adt.add(100)
    assert set_adt.is_full() == False
    assert len(set_adt) == CAPACITY + 1


def test_str(set_adt):
    set_adt.add(1)
    set_adt.add(2)
    assert str(set_adt) == "{1, 2}"


def test_contains(set_adt):
    set_adt.add(1)
    set_adt.add(2)
    assert 1 in set_adt
    assert 2 in set_adt
    assert 3 not in set_adt


def test_remove(set_adt):
    set_adt.add(1)
    set_adt.add(1)
    set_adt.add(2)
    assert len(set_adt) == 2
    set_adt.remove(1)
    assert len(set_adt) == 1
    set_adt.remove(2)
    assert len(set_adt) == 0


def test_remove_not_found(set_adt):
    with pytest.raises(ValueError):
        set_adt.remove(1)


def test_clear(set_adt):
    set_adt.add(1)
    set_adt.add(2)
    assert len(set_adt) == 2
    set_adt.clear()
    assert len(set_adt) == 0


def test_union(setA, setB, setC):
    set_union = setA | setA
    assert len(set_union) == 5
    assert str(set_union) == "{1, 2, 3, 4, 5}"

    set_union = setA | setB
    assert len(set_union) == 6
    assert str(set_union) == "{1, 2, 3, 4, 5, 6}"

    set_union = setA | setC
    assert len(set_union) == 10
    assert str(set_union) == "{1, 2, 3, 4, 5, 10, 11, 12, 13, 14}"

    set_union = setB | setA
    assert len(set_union) == 6
    assert str(set_union) == "{2, 3, 4, 5, 6, 1}"


def test_intersection(setA, setB, setC):
    set_intersection = setA & setA
    assert len(set_intersection) == 5
    assert str(set_intersection) == "{1, 2, 3, 4, 5}"

    set_intersection = setA & setB
    assert len(set_intersection) == 4
    assert str(set_intersection) == "{2, 3, 4, 5}"

    set_intersection = setA & setC
    assert len(set_intersection) == 0
    assert str(set_intersection) == "{}"

    set_intersection = setB & setA
    assert len(set_intersection) == 4
    assert str(set_intersection) == "{2, 3, 4, 5}"


def test_difference(setA, setB, setC):
    set_difference = setA - setA
    assert len(set_difference) == 0
    assert str(set_difference) == "{}"

    set_difference = setA - setB
    assert len(set_difference) == 1
    assert str(set_difference) == "{1}"

    set_difference = setA - setC
    assert len(set_difference) == 5
    assert str(set_difference) == "{1, 2, 3, 4, 5}"

    set_difference = setB - setA
    assert len(set_difference) == 1
    assert str(set_difference) == "{6}"


def test_symmetric_difference(setA, setB, setC):
    set_symmetric_difference = setA ^ setA
    assert len(set_symmetric_difference) == 0
    assert str(set_symmetric_difference) == "{}"

    set_symmetric_difference = setA ^ setB
    assert len(set_symmetric_difference) == 2
    assert str(set_symmetric_difference) == "{1, 6}"

    set_symmetric_difference = setA ^ setC
    assert len(set_symmetric_difference) == 10
    assert str(set_symmetric_difference) == "{1, 2, 3, 4, 5, 10, 11, 12, 13, 14}"

    set_symmetric_difference = setB ^ setA
    assert len(set_symmetric_difference) == 2
    assert str(set_symmetric_difference) == "{6, 1}"
