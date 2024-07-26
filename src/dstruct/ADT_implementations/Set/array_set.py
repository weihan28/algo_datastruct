from src.dstruct.ADT.Set import Set, T
from src.dstruct.ADT_implementations.referential_array import ArrayR


class ASet(Set[T]):
    """ Array-based Set Implementation.
    Dynamic resizing is used.
    """
    MIN_CAPACITY = 1

    def __init__(self, capacity: int = 10) -> None:
        """ Initializes the array with the given length.
        Args:
            capacity (int): initial capacity of the set.

        Attributes:
            length (int): The number of elements in the set.
            array (ArrayR): The array that holds the set elements.
        """
        super().__init__()
        self.length = 0
        self.array = ArrayR(max(capacity, self.MIN_CAPACITY))

    def __len__(self) -> int:
        return self.length

    def is_empty(self) -> bool:
        return self.length == 0

    def __contains__(self, item: T) -> bool:
        """Returns True if item is in the set, False otherwise."""
        for i in range(self.length):
            if self.array[i] == item:
                return True
        return False

    def add(self, item: T) -> None:
        """Adds item to the set if it is not already in the set."""
        if self.is_full():
            self._resize(2 * len(self.array))
        if item not in self:
            self.array[self.length] = item
            self.length += 1

    def index(self, value: T) -> int:
        """ Returns the index of the first occurrence of the given value.

        :ValueError: if the list does not contain the given value.
        """
        for i in range(self.length):
            if self.array[i] == value:
                return i
        raise ValueError("Item not in set")

    def remove(self, item: T) -> None:
        """ Removes item from the set if it is in the set.

        :ValueError: if item is not in the set.
        """
        idx = self.index(item)
        self._shift_left(idx)
        self.length -= 1

    def clear(self) -> None:
        self.length = 0

    def _shift_left(self, index: int) -> None:
        """ Shifts all elements from the given index to the left.
        The element at the given index is overwritten.
        """
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i + 1]

    def __or__(self, __other: Set) -> Set:
        """Returns the union of this set and other set.
        Union: in A or B.

        called by: A | B
        """
        new_set = ASet(len(self) + len(__other))
        for i in range(len(self)):
            new_set.add(self.array[i])
        for i in range(len(__other)):
            new_set.add(__other.array[i])
        return new_set

    def __and__(self, __other: Set) -> Set:
        """Returns the intersection of this set and other set.
        Intersection: in both A and B.

        called by: A & B
        """
        new_set = ASet(len(self))
        for i in range(len(self)):
            if self.array[i] in __other:
                new_set.add(self.array[i])
        return new_set

    def __sub__(self, __other: Set) -> Set:
        """Returns the difference of this set and other set.
        Difference: in A but not in B.

        called by: A - B
        """
        new_set = ASet(len(self))
        for i in range(len(self)):
            if self.array[i] not in __other:
                new_set.add(self.array[i])
        return new_set

    def __xor__(self, __other: Set) -> Set:
        """Returns the symmetric difference of this set and other set.
        Symmetric difference: in A or B but not both.

        called by: A ^ B
        """
        return (self - __other) | (__other - self)

    def is_full(self) -> bool:
        """Returns True if the array is full, False otherwise."""
        return self.length == len(self.array)

    def _resize(self, new_capacity: int) -> None:
        """Resize the internal array to capacity new_capacity.
        
        Args:
            new_capacity (int): The new capacity of the internal array.
            new_capacity must be greater than or equal to the current length of the queue.
        """
        assert new_capacity >= len(self)
        new_array = ArrayR(new_capacity)
        for i in range(len(self)):
            new_array[i] = self.array[i]
        self.array = new_array

    def __str__(self) -> str:
        """Returns a string representation of the set."""
        res = "{"
        for i in range(self.length):
            res += str(self.array[i])
            if i < self.length - 1:
                res += ", "
        res += "}"
        return res
