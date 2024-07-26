class Node:
    def __init__(self, id) -> None:
        self.id = id
        self.edges = []

        # used in dijkstra
        self.distance = float('inf')
        self.previous = None
        self.visited = False
        self.is_exit = False
        # used for index mapping in heap
        self.position = None
        # used in the normal dijkstra with imported heap.
        self.discovered = False

    def add_edge(self, edge):
        self.edges.append(edge)

    def __ge__(self, other):
        return self.distance >= other.distance

    def __gt__(self, other):
        return self.distance > other.distance

    def __str__(self) -> str:
        return f"Vertex:{self.id}"

    def __repr__(self):
        return f"(id {self.id}: dist {self.distance})"


class Edge:
    def __init__(self, u, v, w) -> None:
        self.u = u
        self.v = v
        self.w = w

    def __str__(self) -> str:
        return f"Edge({self.u}->{self.v} with edge {self.w})"
