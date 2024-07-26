class Node:
    def __init__(self, id) -> None:
        self.edges = []
        self.discovered = False

        self.id = id

    def add_edge(self, edge):
        self.edges.append(edge)


class Edge:
    def __init__(self, u, v) -> None:
        self.u = u
        self.v = v


def BFS(source: Node):
    result = []

    queue = [source]

    while len(queue) > 0:
        curr_node = queue.pop(0)

        result.append(curr_node.id)

        for edge in curr_node.edges:
            v = edge.v
            if not v.discovered:
                queue.append(v)
                v.discovered = True
    return result


def DFS(source: Node):
    return DFS_aux(source, [source.id])


def DFS_aux(source: Node, path):
    if len(source.edges) == 0:
        return path

    for edge in source.edges:
        v = edge.v
        if not v.discovered:
            v.discovered = True
            path.append(v.id)
            DFS_aux(v, path)
    return path


def create_graph():
    nodes = []
    for i in range(6):
        nodes.append(Node(i))

    edges_num = [(0, 1), (1, 2), (1, 3), (2, 3), (2, 4), (3, 5)]
    for edge in edges_num:
        u_num, v_num = edge
        node_u, node_v = nodes[u_num], nodes[v_num]
        node_u.add_edge(Edge(node_u, node_v))
    return nodes


def reset_graph(nodes):
    for node in nodes:
        node.discovered = False


if __name__ == '__main__':
    nodes = create_graph()
    res = BFS(nodes[0])
    print(f"BFS using iteration:{res}")
    reset_graph(nodes)

    res = DFS(nodes[0])
    print(f"DFS using recursion:{res}")
    reset_graph(nodes)
