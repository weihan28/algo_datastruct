from __future__ import annotations
from abc import ABC, abstractclassmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class Set(ABC, Generic[T]):
    """Abstract Class of a Set ADT."""

    def __init__(self) -> None:
        self.clear()

    @abstractclassmethod
    def __len__(self) -> int:
        pass

    @abstractclassmethod
    def is_empty(self) -> bool:
        pass

    @abstractclassmethod
    def add(self, item: T) -> None:
        pass

    @abstractclassmethod
    def remove(self, item: T) -> None:
        """ Removes item from the set if it is in the set.

        :ValueError: if item is not in the set.
        """
        pass

    @abstractclassmethod
    def clear(self) -> None:
        pass

    @abstractclassmethod
    def __contains__(self, item: T) -> bool:
        """Returns True if item is in the set, False otherwise."""
        pass

    @abstractclassmethod
    def __or__(self, __other: Set) -> Set:
        """Returns the union of this set and other set.
        Union: in A or B.

        called by: A | B
        """
        pass

    @abstractclassmethod
    def __and__(self, __other: Set) -> Set:
        """Returns the intersection of this set and other set.
        Intersection: in both A and B.

        called by: A & B
        """
        pass

    @abstractclassmethod
    def __sub__(self, __other: Set) -> Set:
        """Returns the difference of this set and other set.
        Difference: in A but not in B.

        called by: A - B
        """
        pass

    @abstractclassmethod
    def __xor__(self, __other: Set) -> Set:
        """Returns the symmetric difference of this set and other set.
        Symmetric difference: in A or B but not both.

        called by: A ^ B
        """
        pass
