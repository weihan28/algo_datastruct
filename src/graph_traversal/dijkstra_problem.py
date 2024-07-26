from NodeEdgeDijkstra import Edge
from Graph import Graph
from Dijkstra import Dijkstra_modified

"""
This demonstrates how dijkstra can be used to solve complex problems.

Problem description: 

There are a list of paths connecting different locations,
keys on some of the locations that are each guarded by a different monster,
and exits that players can exit using a key.

Each path takes a certain amount of time to traverse,
If the player reaches a location with a key, they can choose defeat the monster to obtain the key.
Each monsters may require different but set amount of time to defeat.
To exit, a player must reach an exit with a key.

What is the minimum amount of time that a player must take starting from one location to exit.

Approach:

The problem can be generalised as this:
starting from S, we have to minimise the time taken for
S -> Key (defeat monster) -> Exit

We can split the problem into 2 parts:
S -> Key
Key -> Exit

we can do preprocessing on the input.

We can create two identical graphs instead of one,
- Keys only exist in the first, which is where we start
- Exits only exist in the second, which is where we end
- we connect the key locations to its corresponding node 
    from G1 to G2 using a weight of the time taken to defeat the monster

By doing so, we can simply solve this problem by running a dijkstra that simply stops when it reaches a exit node.


How this can be applied to other real world problems:

this can be solved for any problems that have the form S -> A -> B ... C -> Z
where we aim to visit every node and possibly spend additional time in the location.

For example: we can find the minimum time taken to go 
- from home to any McDonalds while also stopping by KfC in the middle.
- solve problems similar to google maps path planning, 
    where the user intends to stop by multiple locations before reaching their destination
    
The only downside of this approach is that each intermediate location will duplicate the graph by one.

the climb(dijkstra) algorithm takes O(ElogV) time and O(V+E) space, where 
V and E are the total number of nodes and edges of all the graphs.



paths are the edges [(u, v, w)], where u, v, w are integers
keys = [(node_id, time_defeat)] representing the location(node.id) of the keys and 
the time required to defeat the monster and get the key.

start = source_id (int)
exits = [int] location of exits


"""


class FloorGraph:
    def __init__(self, path, keys):
        self.graph_1 = Graph(paths)
        self.graph_2 = Graph(paths)
        self.nodes_1 = self.graph_1.get_nodes()
        self.nodes_2 = self.graph_2.get_nodes()
        self.initialise_total_nodes()
        self.initialise_keys(keys)

    def initialise_total_nodes(self):
        self.total_nodes = []
        for node in self.nodes_1:
            self.total_nodes.append(node)
        for node in self.nodes_2:
            self.total_nodes.append(node)

    def initialise_keys(self, keys):
        for key in keys:
            id, time_defeat = key
            start = self.graph_1.get_node(id)
            end = self.graph_2.get_node(id)
            start.add_edge(Edge(start, end, time_defeat))

    def initialise_exits(self, exits: list[int]):
        for id in exits:
            node = self.graph_2.get_node(id)
            node.is_exit = True

    def reset(self):  # to do
        """ Simply resets all the attributes for the nodes
        """
        pass

    def climb(self, start, exits):
        self.reset()
        source = self.graph_1.get_node(start)
        self.initialise_exits(exits)
        return Dijkstra_modified(source, self.total_nodes)


if __name__ == '__main__':
    paths = [(0, 1, 4), (1, 2, 2), (2, 3, 3), (3, 4, 1), (1, 5, 2),
             (5, 6, 5), (6, 3, 2), (6, 4, 3), (1, 7, 4), (7, 8, 2),
             (8, 7, 2), (7, 3, 2), (8, 0, 11), (4, 3, 1), (4, 8, 10)]

    keys = [(5, 10), (6, 1), (7, 5), (0, 3), (8, 4)]
    myfloor = FloorGraph(paths, keys)
    start = 3
    exits = [4]
    res = myfloor.climb(start, exits)
    print(res)
