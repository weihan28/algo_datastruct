from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class List(ABC, Generic[T]):
    """ Abstract Base List Class.

    Note:
        Setters are not included in the abstract base class because
        some implementations(like sorted lists) may not support them.
    """

    def __init__(self) -> None:
        self.length = 0

    def __len__(self) -> int:
        """ Returns the number of elements in the list."""
        return self.length

    def is_empty(self) -> bool:
        """ Returns True if the list is empty."""
        return self.length == 0

    @abstractmethod
    def __contains__(self, value: T) -> bool:
        """ Returns True if the list contains the given value."""
        pass

    @abstractmethod
    def __getitem__(self, index: int) -> T:
        """ Returns the element at the given index.

        :IndexError: if index < 0 or index >= self.length
        """
        pass

    @abstractmethod
    def pop(self, index: int) -> T:
        """ Removes and returns the element at the given index.

        :IndexError: if index < 0 or index >= self.length
        """
        pass

    @abstractmethod
    def clear(self) -> None:
        """ Removes all elements from the list.
        """
        pass

    @abstractmethod
    def remove(self, value: T) -> None:
        """ Removes the first occurrence of the given value from the list.

        :ValueError: if the list does not contain the given value.
        """
        pass

    @abstractmethod
    def index(self, value: T) -> int:
        """ Returns the index of the first occurrence of the given value.

        :ValueError: if the list does not contain the given value.
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """ Returns a string representation of the list."""
        pass


class GenericList(List[T], ABC):
    @abstractmethod
    def __setitem__(self, index: int, value: T) -> None:
        """ Sets the element at the given index to the given value.

        :IndexError: if index < 0 or index >= self.length
        """
        pass

    @abstractmethod
    def append(self, value: T) -> None:
        """ Adds the given value to the end of the list."""
        pass

    @abstractmethod
    def insert(self, index: int, value: T) -> None:
        """ Inserts the given value at the given index.

        :IndexError: if index < 0 or index >= self.length
        """
        pass


class SortedList(List[T], ABC):
    @abstractmethod
    def add(self, value: T) -> None:
        """ Adds the given value to the list in sorted order."""
        pass
