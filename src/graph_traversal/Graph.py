from NodeEdgeDijkstra import *


class Graph:
    """
    u and v is from 0~V
    w is non-negative (for dijkstra)

    nodes: [Node_0, Node_1, .. Node_V]
    """

    def __init__(self, paths: list[(int, int, int)]):
        self.total_nodes = self.get_max_node(paths) + 1
        self.nodes = self.create_nodes(self.total_nodes)
        self.append_edges(paths)

    def get_max_node(self, paths: list[(int, int, int)]):
        max_u = float("-inf")
        for path in paths:
            if path[0] > max_u:
                max_u = path[0]
        return max_u

    def create_nodes(self, total_nodes) -> list[Node]:
        nodes = []
        for i in range(total_nodes):
            nodes.append(Node(i))
        return nodes

    def append_edges(self, paths: list[(int, int, int)]):
        for path in paths:
            u, v, w = path
            self.add_edge(u, v, w)

    def add_edge(self, u: int, v: int, w: int):
        edge = Edge(self.nodes[u], self.nodes[v], w)
        self.nodes[u].add_edge(edge)

    def get_node(self, id: int):
        return self.nodes[id]

    def get_nodes(self):
        return self.nodes

    def __str__(self):
        res = ""
        for node in self.nodes:
            res += f"{node} has:\n"
            for edge in node.edges:
                res += f"\t{edge}\n"
        return res
