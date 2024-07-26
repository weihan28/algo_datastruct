from src.dstruct.ADT.List import SortedList, T
from src.dstruct.ADT_implementations.referential_array import ArrayR


class ASortedList(SortedList[T]):
    """ Array-based Sorted List Implementation.
    Dynamic resizing is used.
    """
    MIN_CAPACITY = 1

    def __init__(self, capacity: int = 10) -> None:
        """ Initializes the array with the given length.
        Args:
            capacity (int): initial capacity of the list.
        """
        super().__init__()
        self.length = 0
        self.array = ArrayR(max(capacity, self.MIN_CAPACITY))

    def add(self, value: T) -> None:
        """ Adds the given value to the list."""
        if self.is_full():
            self.resize()

        for i in range(self.length):
            if self.array[i] > value:
                self.length += 1
                self._shift_right(i)
                self.array[i] = value
                return
        # item is greater than all items in the list(or is equal to the max item)
        self.array[self.length] = value
        self.length += 1

    def __contains__(self, value: T) -> bool:
        """ Returns True if the list contains the given value."""
        for i in range(self.length):
            if self.array[i] == value:
                return True
            elif self.array[i] > value:
                break
        return False

    def __getitem__(self, index: int) -> T:
        """ Returns the element at the given index.

        :IndexError: if index < 0 or index >= self.length
        """
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        return self.array[index]

    def pop(self, index: int) -> T:
        """ Removes and returns the element at the given index.

        :IndexError: if index < 0 or index >= self.length
        """
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        res = self.array[index]
        self._shift_left(index)
        self.length -= 1
        return res

    def clear(self) -> None:
        """ Removes all elements from the list.
        """
        self.length = 0

    def remove(self, value: T) -> None:
        """ Removes the first occurrence of the given value from the list.

        :ValueError: if the list does not contain the given value.
        """
        self.pop(self.index(value))

    def index(self, value: T) -> int:
        """ Returns the index of the first occurrence of the given value.

        :ValueError: if the list does not contain the given value.
        """
        for i in range(self.length):
            if self.array[i] == value:
                return i
        raise ValueError("Value not found")

    def is_full(self) -> bool:
        """ Returns True if the list is full."""
        return self.length == len(self.array)

    def resize(self) -> None:
        """ Resizes the array to twice its current length."""
        new_array = ArrayR(len(self.array) * 2)
        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array

    def _shift_left(self, index: int) -> None:
        """ Shifts all elements from the given index to the left.
        The element at the given index is overwritten.
        """
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i + 1]

    def _shift_right(self, index: int) -> None:
        """ Shifts all elements from the given index to the right.
        The element at the given index is overwritten.
        """
        for i in range(self.length - 1, index, -1):
            self.array[i] = self.array[i - 1]

    def __str__(self) -> str:
        """ Returns a string representation of the list."""
        res = "["
        for i in range(self.length):
            if i < self.length - 1:
                res += str(self.array[i]) + ", "
            else:
                res += str(self.array[i])
        res += "]"
        return res


"""
stable(duplicate items added last are at the back.)

Advantages over generic list:
    - faster add() method
    - faster remove() method
    - faster index() method
    - faster __contains__() method
    - list is sorted
"""
