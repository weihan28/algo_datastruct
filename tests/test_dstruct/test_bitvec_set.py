""" Test Set ADT implemented with bit vector.
"""
import pytest

from src.dstruct.ADT_implementations.Set.bitvec_set import BSet

@pytest.fixture
def set_adt():
    return BSet()


@pytest.fixture
def setA():
    """
    setA = {1, 2, 3, 4, 5}
    """
    seta = BSet()
    for i in range(1,6):
        seta.add(i)
    return seta


@pytest.fixture
def setB():
    """
    setB = {2, 3, 4, 5, 6}
    """
    setb = BSet()
    for i in range(2,7):
        setb.add(i)
    return setb


@pytest.fixture
def setC():
    """
    setC = {10, 11, 12, 13, 14}
    """
    setc = BSet()
    for i in range(10, 15):
        setc.add(i)
    return setc


def test_init(set_adt):
    assert len(set_adt) == 0


def test_add(set_adt):
    set_adt.add(1)
    set_adt.add(2)
    assert len(set_adt) == 2
    assert set_adt.elems == 0b11


def test_add_duplicate(set_adt):
    set_adt.add(1)
    set_adt.add(1)
    assert len(set_adt) == 1
    assert str(set_adt) == '{1}'


def test_remove(set_adt):
    set_adt.add(1)
    set_adt.add(2)
    set_adt.remove(1)
    assert len(set_adt) == 1
    assert set_adt.elems == 0b10


def test_remove_nonexistent(set_adt):
    set_adt.add(1)
    with pytest.raises(ValueError):
        set_adt.remove(2)


def test_clear(set_adt):
    set_adt.add(1)
    set_adt.add(2)
    set_adt.clear()
    assert len(set_adt) == 0
    assert set_adt.elems == 0b0


def test_contains(set_adt):
    set_adt.add(1)
    set_adt.add(2)
    assert 1 in set_adt
    assert 2 in set_adt
    assert 3 not in set_adt


def test_union(setA, setB):
    set_union = setA | setA
    assert len(set_union) == 5
    assert str(set_union) == "{1, 2, 3, 4, 5}"

    set_union = setA | setB
    assert len(set_union) == 6
    assert str(set_union) == "{1, 2, 3, 4, 5, 6}"

    set_union = setB | setA
    assert len(set_union) == 6
    assert str(set_union) == "{1, 2, 3, 4, 5, 6}"


def test_intersection(setA, setB):
    set_intersection = setA & setA
    assert len(set_intersection) == 5
    assert str(set_intersection) == "{1, 2, 3, 4, 5}"

    set_intersection = setA & setB
    assert len(set_intersection) == 4
    assert str(set_intersection) == "{2, 3, 4, 5}"

    set_intersection = setB & setA
    assert len(set_intersection) == 4
    assert str(set_intersection) == "{2, 3, 4, 5}"


def test_difference(setA, setB):
    set_difference = setA - setA
    assert len(set_difference) == 0
    assert str(set_difference) == "{}"

    set_difference = setA - setB
    assert len(set_difference) == 1
    assert str(set_difference) == "{1}"

    set_difference = setB - setA
    assert len(set_difference) == 1
    assert str(set_difference) == "{6}"