from src.dstruct.ADT.Queue import Queue, T
from src.dstruct.ADT_implementations.utils.node import Node


class LinkedQueue(Queue[T]):
    """  Linked Queue Implementation.
    """

    def __init__(self) -> None:
        """Initialize an empty queue.

        Attributes:
            length (int): The number of elements in the queue.
            array (ArrayR): The array that holds the queue elements.
            head (Node): The first node in the queue.
        """
        super().__init__()
        self.head = None
        self.rear = None

    def append(self, item: T) -> None:
        """ Add item to the end of the queue.

        Args:
            item (T): The item to be added.
        """
        new_node = Node(item)
        if not self.is_empty():
            self.rear.next = new_node
        else:
            self.head = new_node
        self.rear = new_node
        self.length += 1

    def serve(self) -> T:
        """ Remove and return the first element of the queue.
        
        :ValueError: if the queue is empty.
        """
        if self.is_empty():
            raise ValueError("Queue is empty.")
        item = self.head.value
        self.head = self.head.next
        self.length -= 1
        # queue is empty if head is None
        if self.is_empty():
            self.rear = None
        return item

    def clear(self) -> None:
        self.head = None

    def __str__(self) -> str:
        """Return a string representation of the queue.
        """
        res = "start of queue <- "
        curr = self.head
        while curr is not None:
            res += str(curr.value) + " <- "
            curr = curr.next
        res += "end of queue"
        return res


"""
Time Complexity:
    append: O(1)
    serve: O(1)
    clear: O(1)
    __str__: O(n)
    is_empty: O(1)
    is_full: O(1)
    __len__: O(1)

cons:
    no random access
"""
