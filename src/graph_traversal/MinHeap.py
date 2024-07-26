class MinHeap:
    """ A min heap implementation with array (fixed size)
    Items must be comparable between themselves.

    Slightly modified for position mapping(see line 29, 66, 39)
    delete both lines to get original min heap.
    """
    MIN_CAPACITY = 1

    def __init__(self, max_capacity) -> None:
        self.array = [None] * (max(self.MIN_CAPACITY, max_capacity) + 1)
        self.length = 0

    def is_full(self):
        return self.length == (len(self.array) - 1)

    def is_empty(self):
        return self.length == 0

    def add(self, item):
        if self.is_full():
            raise IndexError("Min heap is full")
        self.length += 1
        self.array[self.length] = item
        self._rise(self.length)

        # unique to nodes
        item.position = self.length

    def _rise(self, idx):
        while (self.array[idx // 2] is not None) and (self.array[idx // 2] > self.array[idx]):
            self._swap(idx, idx // 2)
            idx = idx // 2

    def _swap(self, first_idx: int, second_idx: int):
        node_1, node_2 = self.array[first_idx], self.array[second_idx]

        # unique to nodes
        node_1.position = second_idx
        node_2.position = first_idx
        self.array[first_idx], self.array[second_idx] = node_2, node_1

    def get_min(self) -> object:
        if self.is_empty():
            raise IndexError("Min Heap is empty")
        min_item = self.array[1]
        self._swap(1, self.length)
        # must decrement before sink since sink sinks all the way until the last valid item(which is the updated length)
        self.length -= 1
        self._sink(1)
        return min_item

    def _sink(self, idx):
        # while there exists a child, try and swap
        while idx * 2 <= self.length:
            min_child_pos = self._get_smallest_child(idx)
            # break if the smallest child is already bigger than or equal
            if self.array[min_child_pos] >= self.array[idx]:
                break
            self._swap(idx, min_child_pos)
            idx = min_child_pos

    def _get_smallest_child(self, idx):
        assert idx * 2 <= self.length, f"there are no child for this item"
        # this line is unique to nodes
        child_1, child_2 = idx * 2, idx * 2 + 1

        # if this is the last item(meaning there are no child_2 item) or it is smaller than child 2
        if child_1 == self.length or self.array[child_1] <= self.array[child_2]:
            return child_1
        else:
            return child_2

    def update(self, idx):
        self._rise(idx)

    def __len__(self):
        return self.length


if __name__ == '__main__':
    from NodeEdgeDijkstra import Node

    nodes = [(0, float('inf')), (1, float('inf')), (2, float('inf')), (3, float('inf')), (4, float('inf'))]
    nodes_2 = []
    min_heap = MinHeap(len(nodes))
    for node in nodes:
        id, distance = node
        new_node = Node(id)
        nodes_2.append(new_node)
        new_node.distance = distance
        min_heap.add(new_node)

    nodes_2[0].distance = 0
    min_heap.update(nodes_2[0].position)
    min_node = min_heap.get_min()
    print(min_node.id, min_node.distance)

    nodes_2[1].distance = 10
    min_heap.update(nodes_2[1].position)
    nodes_2[2].distance = 5
    min_heap.update(nodes_2[2].position)
    min_node = min_heap.get_min()
    print(min_node.id, min_node.distance)
