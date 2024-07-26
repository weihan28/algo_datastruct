from src.dstruct.ADT.Stack import Stack, T
from src.dstruct.ADT_implementations.referential_array import ArrayR


class AStack(Stack[T]):
    """Array-based Stack ADT.
    Dynamic resizing is used.
    """
    MIN_CAPACITY = 1

    def __init__(self, capacity: int = 10) -> None:
        """ Initializes the array with the given length.

        Args:
            capacity (int): initial capacity of the stack.

        Attributes:
            length (int): The number of elements in the stack.
            array (ArrayR): The array that holds the stack elements.
        """
        super().__init__()
        self.length = 0
        self.array = ArrayR(max(capacity, self.MIN_CAPACITY))

    def push(self, item: T) -> None:
        """ Pushes the given item onto the stack."""
        if self.is_full():
            self._resize(2 * len(self.array))
        self.array[len(self)] = item
        self.length += 1

    def pop(self) -> T:
        """ Removes and returns the top item of the stack.

        :ValueError: if the stack is empty.
        """
        if self.is_empty():
            raise ValueError("Stack is empty")
        item = self.array[len(self) - 1]
        self.length -= 1
        return item

    def peek(self) -> T:
        """ Returns the top item of the stack without removing it.

        :ValueError: if the stack is empty.
        """
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.array[len(self) - 1]

    def clear(self) -> None:
        self.length = 0

    def is_full(self) -> bool:
        return len(self.array) == len(self)

    def _resize(self, new_capacity: int) -> None:
        """Resize the internal array to capacity new_capacity.
        
        Args:
            new_capacity (int): The new capacity of the internal array.
            new_capacity must be greater than or equal to the current length of the stack.
        """
        assert new_capacity >= len(self)
        new_array = ArrayR(new_capacity)
        for i in range(len(self)):
            new_array[i] = self.array[i]
        self.array = new_array
