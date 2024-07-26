from NodeEdgeDijkstra import Node
from MinHeap import MinHeap
from Graph import Graph


def Dijkstra(source: Node, target: Node, nodes: list[Node]):
    """ Dijkstra's implementation with fixed size minheap node initialisation
    Pro: discovered is not needed, and O(logV) time for rise/sink.
        - since it is only there to append to queue/heap/stack, we already initialised min_heap with nodes.
    Cons: min_heap must be modified for 'index mapping (node.position swapping)'

    Note: can add check for if curr is not target at the end for edge case when the target is unreachable.
    """
    min_heap = initialise_min_heap(nodes)

    # initialise source to 0 (so that it is the first to be visited)
    update_distance(source, 0, min_heap)

    while not min_heap.is_empty():
        curr_node = min_heap.get_min()

        # finalise distance
        curr_node.visited = True
        # break if we are at the destination(this is the place where we check for exits, target.is_exit==true)
        if curr_node.id == target.id:  # this is normal dijkstra
            break
        # same as bfs
        for edge in curr_node.edges:
            v = edge.v
            # edge relaxation for non-finalised nodes
            new_distance = curr_node.distance + edge.w
            if not v.visited and new_distance < v.distance:
                update_distance(v, new_distance, min_heap)
                v.previous = curr_node

            # no discovered needed
            """ Note: we only check for discovered in BFS
            We add it to queue no matter what if it is dijkstra(except its visited ofcourse), 
            so appending would be in the else statement of the visited check, or just pass when visited.
            """

    return backtrack(target), target.distance


def Dijkstra_modified(source: Node, nodes: list[Node]):
    """ Modified Dijkstra
    Changed termination condition from checking for one target to checking exits.
    Functions the same if only one Node is an exit, but this uses more space.
    """
    min_heap = initialise_min_heap(nodes)

    # initialise source to 0 (so that it is the first to be visited)
    update_distance(source, 0, min_heap)

    while not min_heap.is_empty():
        curr_node = min_heap.get_min()
        curr_node.visited = True
        if curr_node.is_exit:
            break
        for edge in curr_node.edges:
            v = edge.v
            new_distance = curr_node.distance + edge.w
            if not v.visited and new_distance < v.distance:
                update_distance(v, new_distance, min_heap)
                v.previous = curr_node
    # curr_node is the target node
    return backtrack_modified(curr_node), curr_node.distance


def backtrack_modified(node: Node):
    curr = node
    backward_path = []
    prev_curr_id = None
    while curr is not None:
        if prev_curr_id != curr.id:
            backward_path.append(curr.id)
        prev_curr_id = curr.id
        curr = curr.previous

    backward_path.reverse()
    return backward_path


def update_distance(node, new_distance, min_heap):
    node.distance = new_distance
    min_heap.update(node.position)


def initialise_min_heap(nodes):
    min_heap = MinHeap(len(nodes))
    for node in nodes:
        min_heap.add(node)
    return min_heap


def backtrack(node: Node):
    curr = node
    backward_path = []
    while curr is not None:
        backward_path.append(curr.id)
        curr = curr.previous
    backward_path.reverse()
    return backward_path


if __name__ == '__main__':
    uvw = [
        (0, 1, 10), (0, 2, 5), (1, 2, 2), (1, 3, 1), (2, 1, 3),
        (2, 3, 9), (2, 4, 2), (3, 4, 4), (4, 3, 6)
    ]
    graph = Graph(uvw)

    nodes = graph.get_nodes()

    # initialise exit
    nodes[-2].is_exit = True
    path = Dijkstra_modified(nodes[0], nodes)

    print(path)
