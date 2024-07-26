""" Test Cases for QueueArray
"""
import pytest
from src.dstruct.ADT_implementations.Queue.linked_queue import LinkedQueue


@pytest.fixture
def queue():
    return LinkedQueue()

def test_init(queue):
    assert queue.is_empty() == True
    assert len(queue) == 0

def test_append(queue):
    queue.append(1)
    queue.append(2)
    assert len(queue) == 2

def test_serve(queue):
    with pytest.raises(ValueError):
        queue.serve()
    
    for i in range(10):
        queue.append(i)

    for i in range(10):
        assert queue.serve() == i
        assert len(queue) == 9 - i
    assert queue.is_empty() == True