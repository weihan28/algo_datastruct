""" Test Cases for QueueArray
"""
import pytest

from src.dstruct.ADT_implementations.Queue.array_queue import AQueue

SIZE = 10


@pytest.fixture
def queue():
    return AQueue(SIZE)


def test_init(queue):
    assert len(queue) == 0
    assert queue.front == 0
    assert queue.rear == 0


def test_invalid_capacity():
    # defaults to capacity of 1 when invalid capacity is given
    queue = AQueue(-1)
    assert len(queue) == 0
    assert len(queue.array) == 1


def test_is_empty(queue):
    assert queue.is_empty() == True


def test_is_full(queue):
    for i in range(SIZE):
        queue.append(i)
    assert queue.is_full() == True


def test_append(queue):
    queue.append(1)
    queue.append(2)
    assert len(queue) == 2
    assert queue.front == 0
    assert queue.rear == 2


def test_serve(queue):
    with pytest.raises(ValueError):
        queue.serve()

    for i in range(10):
        queue.append(i)

    for i in range(10):
        assert queue.serve() == i
        assert len(queue) == 9 - i
    assert queue.is_empty() == True


def test_circularity_append(queue):
    for i in range(SIZE):
        queue.append(i)
    assert queue.front == 0
    assert queue.rear == 0

    queue.serve()
    queue.append(100)
    assert queue.front == 1
    assert queue.rear == 1
    assert len(queue) == SIZE


def test_circularity_resize(queue):
    for i in range(SIZE + 1):
        queue.append(i)

    assert queue.front == 0
    assert queue.rear == SIZE + 1
    assert len(queue) == SIZE + 1
    assert len(queue.array) == 2 * SIZE
