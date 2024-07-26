class Node():
    """ A simple node class for linked structures.
    """
    def __init__(self, value: any) -> None:
        """ Initializes the node with the given value.
        """
        self.value = value
        self.next = None