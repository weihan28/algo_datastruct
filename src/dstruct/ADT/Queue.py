from typing import Generic, TypeVar
from abc import ABC, abstractclassmethod

T = TypeVar('T')


class Queue(ABC, Generic[T]):
    """Abstract Class of a Queue ADT."""

    def __init__(self) -> None:
        self.length = 0

    def __len__(self) -> int:
        return self.length

    def is_empty(self) -> bool:
        return self.length == 0

    @abstractclassmethod
    def append(self, item: T) -> None:
        pass

    @abstractclassmethod
    def serve(self) -> T:
        pass

    @abstractclassmethod
    def clear(self) -> None:
        pass
