from src.dstruct.ADT.List import GenericList, T
from src.dstruct.ADT_implementations.referential_array import ArrayR


class AList(GenericList[T]):
    """ Array-based List Implementation.
    Dynamic resizing is used.
    """
    MIN_CAPACITY = 1

    def __init__(self, capacity: int) -> None:
        """ Initializes the array with the given length.

        Args:
            capacity (int): initial capacity of the array.

        :ValueError: if length <= 0
        """
        super().__init__()
        self.length = 0
        self.array = ArrayR(max(capacity, self.MIN_CAPACITY))

    def __setitem__(self, index: int, value: T) -> None:
        """ Sets the element at the given index to the given value.

        :IndexError: if index < 0 or index >= self.length
        """
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        self.array[index] = value

    def append(self, value: T) -> None:
        """ Adds the given value to the end of the list."""
        if self.is_full():
            self.resize()
        self.array[self.length] = value
        self.length += 1

    def insert(self, index: int, value: T) -> None:
        """ Inserts the given value at the given index.

        :IndexError: if index < 0 or index >= self.length
        """
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        if self.is_full():
            self.resize()
        self.length += 1
        self._shift_right(index)
        self.array[index] = value

    def __contains__(self, value: T) -> bool:
        """ Returns True if the list contains the given value."""
        for i in range(self.length):
            if self.array[i] == value:
                return True
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
            elif self.array[i] > value:
                break
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
Time Complexity(worst):
    Note: this doesnt account for dynamic resizing
    - append: O(1)
    - insert: O(n)
    - remove: O(n)
    - index: O(n)
    - resize: O(n)
    - _shift_left: O(n)
    - _shift_right: O(n)
    - __str__: O(n)
    - __contains__: O(n)
    - __getitem__: O(1)
    - pop: O(n)
    - clear: O(1)
    - is_full: O(1)
    - __setitem__: O(1)


Advantages over linked list:
    - random access
    - faster traversal
    - cache friendly
    - less memory overhead
    - faster indexing
    - faster searching

Disadvantages over linked list:
    - shifting is costly making deletion and insertion costly
"""
