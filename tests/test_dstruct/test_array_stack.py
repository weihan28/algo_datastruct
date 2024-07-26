""" Test Cases for Array based Stack.
"""
import pytest

from src.dstruct.ADT_implementations.Stack.array_stack import AStack

SIZE = 10

@pytest.fixture
def stack():
    return AStack(SIZE)


def test_init(stack):
    # number of elements is 0
    assert len(stack) == 0
    assert stack.is_empty() == True


def test_init_invalid_length():
    # when length is negative, it should be set to 1
    stack = AStack(-1)
    assert len(stack.array) == 1


def test_push(stack):
    stack.push(1)
    assert len(stack) == 1

    stack.push(2)
    assert len(stack) == 2

    stack.push(3)
    assert len(stack) == 3

def test_pop(stack):
    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1

    with pytest.raises(ValueError):
        stack.pop()

def test_peek(stack):
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.peek() == 3
    assert stack.peek() == 3

    stack.pop()
    assert stack.peek() == 2
    stack.pop()
    stack.pop()
    with pytest.raises(ValueError):
        stack.peek()


def test_clear(stack):
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.clear()
    assert len(stack) == 0
    assert stack.is_empty() == True


def test__dynamic_size(stack):
    for i in range(SIZE):
        stack.push(i)
    assert len(stack.array) == SIZE

    stack.push(1)
    assert len(stack.array) == 2*SIZE