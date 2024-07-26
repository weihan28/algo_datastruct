from src.dstruct.ADT.Stack import Stack, T
from src.dstruct.ADT_implementations.utils.node import Node


class LinkedStack(Stack[T]):
    """Linked Stack implementation."""

    def __init__(self) -> None:
        """ Initializes the stack.

        Attributes:
            length (int): number of elements in the stack.
            head (Node): first node in the stack.
        """
        super().__init__()
        self.length = 0
        self.head = None

    def push(self, item: T) -> None:
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def pop(self) -> T:
        if self.is_empty():
            raise ValueError("Stack is empty")
        item = self.head.value
        self.head = self.head.next
        self.length -= 1
        return item

    def peek(self) -> T:
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.head.value

    def clear(self) -> None:
        self.head = None
        self.length = 0
