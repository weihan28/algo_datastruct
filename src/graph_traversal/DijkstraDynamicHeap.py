"""
The dijkstra algorithm with imported heap

MinHeap is not fixed in size, duplicates would be added when performing edge relaxation
O(log(V**2) time comp for rise. O(log(V**2) heap space complexity for dense graph.
"""
import heapq
from NodeEdgeDijkstra import Node


def dijkstra(source: Node, nodes: list[Node]):
    min_heap = [source]
    source.discovered = True
    source.distance = 0
    heapq.heapify(min_heap)

    while len(min_heap) > 0:
        curr = heapq.heappop(min_heap)
        curr.visited = True
        # break early if it is an exit
        if curr.is_exit:
            break

        for edge in curr.edges:
            u, v, w = edge.u, edge.v, edge.w

            if not v.visited:
                # perform edge relaxation here
                new_distance = curr.distance + w
                if v.distance > new_distance:
                    v.distance = new_distance
                    v.previous = curr
            # only add into heap after edge update(because adding it too early will use the old distance)
            if not v.discovered:
                heapq.heappush(min_heap, v)
                v.discovered = True
    return backtrack(curr), curr.distance


def backtrack(node: Node):
    curr = node
    backward_path = []
    while curr is not None:
        backward_path.append(curr.id)
        curr = curr.previous
    backward_path.reverse()
    return backward_path


if __name__ == '__main__':
    from Graph import Graph

    uvw = [
        (0, 1, 10), (0, 2, 5), (1, 2, 2), (1, 3, 1), (2, 1, 3),
        (2, 3, 9), (2, 4, 2), (3, 4, 4), (4, 3, 6)
    ]
    graph = Graph(uvw)

    nodes = graph.get_nodes()

    # initialise exit
    nodes[-2].is_exit = True
    path = dijkstra(nodes[0], nodes)

    print(path)
