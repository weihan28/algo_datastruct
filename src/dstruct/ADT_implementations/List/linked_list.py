from __future__ import annotations
from src.dstruct.ADT.List import GenericList, T
from src.dstruct.ADT_implementations.utils.node import Node
from typing import Generic


class LinkedList(GenericList[T]):
    """ Linked List Implementation.
    """

    def __init__(self) -> None:
        """ Initializes the list.

        Attributes:
            length (int): number of elements in the list.
            head (Node): first node in the list.
        """
        super().__init__()
        self.head = None

    def __setitem__(self, index: int, value: T) -> None:
        """ Sets the element at the given index to the given value.

        :IndexError: if index < 0 or index >= self.length
        """
        # _get_node raises IndexError if index out of bounds
        curr_node = self._get_node(index)
        curr_node.value = value

    def __getitem__(self, index: int) -> T:
        """ Returns the element at the given index.

        :IndexError: if index < 0 or index >= self.length
        """
        node = self._get_node(index)
        return node.value

    def append(self, value: T) -> None:
        """ Adds the given value to the end of the list."""
        new_node = Node(value)
        if not self.is_empty():
            end_node = self._get_node(self.length - 1)
            end_node.next = new_node
        else:
            self.head = new_node
        self.length += 1

    def _get_node(self, index: int) -> Node:
        """ Returns the node at the given index.

        :IndexError: if index < 0 or index >= self.length
        """
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")

        curr_node = self.head
        for _ in range(index):
            curr_node = curr_node.next
        return curr_node

    def insert(self, index: int, value: T) -> None:
        """ Inserts the given value at the given index.

        :IndexError: if index < 0 or index >= self.length
        """
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        new_node = Node(value)
        if index >= 1:
            prev_node = self._get_node(index - 1)
            new_node.next = prev_node.next
            prev_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def __contains__(self, value: T) -> bool:
        """ Returns True if the list contains the given value."""
        curr_node = self.head
        for _ in range(self.length):
            if curr_node.value == value:
                return True
            curr_node = curr_node.next
        return False

    def pop(self, index: int) -> T:
        """ Removes and returns the element at the given index.

        :IndexError: if index < 0 or index >= self.length
        """
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")

        idx_value = None
        if index >= 1:
            prev_node = self._get_node(index - 1)
            idx_node = prev_node.next
            idx_value = idx_node.value
            prev_node.next = idx_node.next
        else:
            idx_value = self.head.value
            self.head = self.head.next
        self.length -= 1
        return idx_value

    def clear(self) -> None:
        """ Removes all elements from the list.
        """
        self.head = None
        self.length = 0

    def remove(self, value: T) -> None:
        """ Removes the first occurrence of the given value from the list.

        :ValueError: if the list does not contain the given value.
        """
        if self.is_empty():
            raise ValueError("Value not in list")
        # item at head
        if self.head.value == value:
            self.head = self.head.next
            self.length -= 1
            return
        # scan through item after head
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                prev.next = curr.next
                self.length -= 1
                return
            else:
                prev = curr
                curr = curr.next
        raise ValueError("Value not in list")

    def index(self, value: T) -> int:
        """ Returns the index of the first occurrence of the given value.

        :ValueError: if the list does not contain the given value.
        """
        index = 0
        curr_node = self.head
        for _ in range(self.length):
            if curr_node.value == value:
                return index
            curr_node = curr_node.next
            index += 1
        raise ValueError("Value not in list")

    def __iter__(self) -> LinkedListIterator[T]:
        """ Returns an iterator for the list."""
        return LinkedListIterator(self.head, self)

    def __str__(self) -> str:
        """ Returns a string representation of the list."""
        res = "["
        curr_node = self.head
        for i in range(self.length):
            if i < self.length - 1:
                res += str(curr_node.value) + ", "
            else:
                res += str(curr_node.value)
            curr_node = curr_node.next
        res += "]"
        return res


class LinkedListIterator(Generic[T]):
    """ Modifying(deletion) Iterator for LinkedLists.

    Warning: Do not modify the list while having an iterator in progress.
    """

    def __init__(self, head: Node[T], lst: LinkedList) -> None:
        self.lst = lst
        self._curr = head
        self._prev = None

    # iter and next are the base methods for iterators
    def __iter__(self) -> LinkedListIterator[T]:
        return self

    def __next__(self) -> T:
        if self._curr is None:
            raise StopIteration("No more elements in the list")
        else:
            value = self._curr.value
            self._prev = self._curr
            self._curr = self._curr.next
            return value

    def has_next(self) -> bool:
        return self._curr is not None

    def peek(self) -> T:
        try:
            return self._curr.value
        except AttributeError:
            raise StopIteration

    def delete(self) -> T:
        """ Deletes the current node and returns its value.
        Also sets the current node to the next node.
        """
        if not self.has_next():
            raise StopIteration("No more elements in the list")
        else:
            item = self._curr.value
            self._curr = self._curr.next
            if self._prev is None:  # head
                self.lst.head = self._curr
            else:
                self._prev.next = self._curr
            self.lst.length -= 1
            return item


"""
Singly linked list.

Time Complexity(worst):
    - append: O(n)
    - __setitem__: O(n)
    - insert: O(n)
    - __contains__: O(n)
    - __getitem__: O(n)
    - pop: O(n)
    - clear: O(1)
    - remove: O(n)
    - index: O(n)
    - __str__: O(n)

Advantages over array implementation:
    - The deleting, swapping, inserting is O(1) instead of O(n) to shift.
    However, the swap operation is still O(n) because we need to find the node


    When half or less of an array implementation is used,
    linked implementation is more space efficient.

    example:
        capacity of array=10
        used=5, overhead/wasted/empty=5
        linkedlist: used=10, 5 for value, 5 for pointer.

        capacity of array=10
        used=2, overhead/wasted/empty=8
        linkedlist: used=4, 2 for value, 2 for pointer.

        capacity of array=10
        used=10, overhead/wasted/empty=0
        linkedlist: used=20, 10 for value, 10 for pointer.
"""
