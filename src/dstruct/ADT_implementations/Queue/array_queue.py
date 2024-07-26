from src.dstruct.ADT.Queue import Queue, T
from src.dstruct.ADT_implementations.referential_array import ArrayR


class AQueue(Queue[T]):
    """  Array-based Queue Implementation.
    Note: This is a circular queue.
    """
    MIN_CAPACITY = 1

    def __init__(self, capacity: int = 10) -> None:
        """Create a Queue with the given starting capacity.

        Args:
            capacity (int): initial capacity of the queue.

        Attributes:
            length (int): The number of elements in the queue.
            array (ArrayR): The array that holds the queue elements.
            front (int): The index of the first valid element(inclusive).
            rear (int): The end of the valid elements(exclusive).
        """
        super().__init__()
        self.array = ArrayR(max(capacity, AQueue.MIN_CAPACITY))
        self.front = 0
        self.rear = 0

    def append(self, item: T) -> None:
        """ Add item to the end of the queue.

        Args:
            item (T): The item to be added.
        """
        if self.is_full():
            self._resize(2 * len(self.array))
        self.array[self.rear] = item
        self.rear = (self.rear + 1) % len(self.array)
        self.length += 1

    def serve(self) -> T:
        """ Remove and return the first element of the queue.
        
        :ValueError: if the queue is empty.
        """
        if self.is_empty():
            raise ValueError("Queue is empty.")
        item = self.array[self.front]
        self.front = (self.front + 1) % len(self.array)
        self.length -= 1
        return item

    def clear(self) -> None:
        self.front = 0
        self.rear = 0

    def is_full(self) -> bool:
        return len(self) == len(self.array)

    def _resize(self, new_capacity: int) -> None:
        """Resize the internal array to capacity new_capacity.
        
        Args:
            new_capacity (int): The new capacity of the internal array.
            new_capacity must be greater than or equal to the current length of the queue.
        """
        assert new_capacity >= len(self)
        old_array = self.array
        self.array = ArrayR(new_capacity)
        curr_i = self.front
        for i in range(len(self)):
            self.array[i] = old_array[curr_i]
            curr_i = (curr_i + 1) % len(old_array)
        self.front = 0
        self.rear = len(self)

    def __str__(self) -> str:
        """Return a string representation of the queue.
        """
        res = "start of queue <- "
        curr_i = self.front
        for i in range(len(self)):
            res += str(self.array[curr_i]) + " <- "
            curr_i = (curr_i + 1) % len(self.array)
        res += "end of queue"
        return res


"""
array[front..rear-1] are the valid elements.
rear loops back to the front when it reaches the end of the array.
"""
