""" Testing the array implementation of a Linked List.
"""
import pytest

from src.dstruct.ADT_implementations.List.linked_list import LinkedList, LinkedListIterator
DS = LinkedList

@pytest.fixture
def lst():
    return DS()


def test_init(lst):
    # number of elements is 0
    assert len(lst) == 0
    assert lst.is_empty() == True
    

def test_str_empty(lst):
    assert str(lst) == "[]"


def test_append(lst):
    lst.append(1)
    assert str(lst) == "[1]"
    assert len(lst) == 1

    lst.append(2)
    assert str(lst) == "[1, 2]"
    assert len(lst) == 2

    lst.append(3)
    assert str(lst) == "[1, 2, 3]"
    assert len(lst) == 3


def test_insert(lst):
    for i in range(1,4):
        lst.append(i)

    lst.insert(0, 0)
    assert str(lst) == "[0, 1, 2, 3]"
    assert len(lst) == 4

    with pytest.raises(IndexError):
        # note python inbuilt actually allows this and appends to the end
        lst.insert(4, 3)

    with pytest.raises(IndexError):
        lst.insert(-1, 3)

def test_set(lst):
    for i in range(1,4):
        lst.append(i)

    lst[0] = 100
    assert str(lst) == "[100, 2, 3]"
    assert len(lst) == 3
    lst[1] = 200
    assert str(lst) == "[100, 200, 3]"

    with pytest.raises(IndexError):
        lst[3] = 3
    
    with pytest.raises(IndexError):
        lst[-1] = 3


def test_get(lst):
    for i in range(1,4):
        lst.append(i)

    assert lst[0] == 1
    assert lst[1] == 2
    assert lst[2] == 3
    assert len(lst) == 3

    with pytest.raises(IndexError):
        lst[3]
    
    with pytest.raises(IndexError):
        lst[-1]


def test_pop(lst):
    for i in range(1,4):
        lst.append(i)

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
        lst.append(i)

    lst.clear()
    assert str(lst) == "[]"
    assert len(lst) == 0


def test_remove(lst):
    for i in range(1,4):
        lst.append(i)
        lst.append(i)

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
        lst.append(i)
        lst.append(i)

    assert str(lst) == "[1, 1, 2, 2, 3, 3]"
    assert lst.index(1) == 0
    assert lst.index(2) == 2
    assert lst.index(3) == 4
    with pytest.raises(ValueError):
        lst.index(4)


def test_contains(lst):
    for i in range(1,4):
        lst.append(i)

    assert 1 in lst
    assert 2 in lst
    assert 3 in lst
    assert 4 not in lst


def test_iter_next(lst):
    for i in range(1,4):
        lst.append(i)

    iter_lst = iter(lst)
    assert isinstance(iter_lst, LinkedListIterator)
    for i in range(1,4):
        assert i == next(iter_lst)
    with pytest.raises(StopIteration):
        next(iter_lst)

def test_iter_modify(lst):
    for i in range(1,4):
        lst.append(i)

    iter_lst = iter(lst)
    iter_lst2 = iter(lst)

    assert next(iter_lst) == 1
    assert iter_lst.delete() == 2
    assert iter_lst.peek() == 3
    assert iter_lst.delete() == 3
    with pytest.raises(StopIteration):
        next(iter_lst)

    # warning, do not modify list while having another iterator in progress.
    assert str(lst) == "[1]"
    assert next(iter_lst2) == 1
    with pytest.raises(StopIteration):
        next(iter_lst2)
    


