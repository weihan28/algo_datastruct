from ctypes import py_object
from typing import TypeVar, Generic

T = TypeVar('T')


class ArrayR(Generic[T]):
    """Simple Referential Array Implementation.
    
    Attributes:
        length (int): size of the array.
        array (py_object * length): array of py_object.
    """

    def __init__(self, length: int) -> None:
        """ Initializes the array with the given length.
        Args:
            length (int): length of the array.
        :ValueError: if length <= 0
        """
        if length <= 0:
            raise ValueError("ArrayR length should be > 0")

        self.length = length
        self.array = (py_object * length)()
        self.array[:] = [None for _ in range(length)]

    def __len__(self) -> int:
        return self.length

    def __getitem__(self, index: int) -> T:
        """ Returns the element at the given index.

        :IndexError: if index < 0 or index >= self.length
        """
        if index < 0 or index >= self.length:
            raise IndexError("ArrayR index out of range")
        return self.array[index]

    def __setitem__(self, index: int, value: T) -> None:
        """ Sets the element at the given index to the given value.

        :IndexError: if index < 0 or index >= self.length
        """
        if index < 0 or index >= self.length:
            raise IndexError("ArrayR index out of range")
        self.array[index] = value

    def __str__(self):
        elems = []
        for elem in self.array:
            elems.append(elem)
        return elems.__str__()
