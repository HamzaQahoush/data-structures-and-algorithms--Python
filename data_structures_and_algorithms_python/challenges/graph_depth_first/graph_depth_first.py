from data_structures_and_algorithms_python.data_structures.graphs.graph import *
from collections import deque


class Queue():
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value)

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)


class Graph():
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        if value in self._adjacency_list:
            print('The value is already exist')
        else:
            new_v = str(Vertex(value))
            self._adjacency_list[new_v] = []
            return new_v

    def get_neighbors(self, vertex):
        return self._adjacency_list[vertex]

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self._adjacency_list:
            raise KeyError('Start vertex is not found in the graph')
        elif end_vertex not in self._adjacency_list:
            raise KeyError('end vertex is not found in the graph')
        else:
            self._adjacency_list[start_vertex].append(
                (str(end_vertex), weight))

    def depth_first(self, start_vertex):
        try:
            visited = []

            def helper(vertex):
                visited.append(vertex)
                neighbors = self.get_neighbors(vertex)
                for neighbor in neighbors:
                    if neighbor[0] not in visited:
                        helper(neighbor[0])

            helper(start_vertex)
            return visited
        except TypeError:
            return 'Start vertex is not found in the graph'


if __name__ == "__main__":
    graph = Graph()
    a = graph.add_node('A')
    b = graph.add_node('B')
    c = graph.add_node('C')
    d = graph.add_node('D')
    e = graph.add_node('E')
    f = graph.add_node('F')
    g = graph.add_node('G')
    h = graph.add_node('H')
    graph.add_edge(a, b, 1)
    graph.add_edge(b, c, 1)
    graph.add_edge(c, g, 1)
    graph.add_edge(a, d, 4)
    graph.add_edge(d, e, 2)
    graph.add_edge(d, b, 2)
    graph.add_edge(d, f, 8)
    graph.add_edge(d, h, 3)
    graph.add_edge(d, e, 5)

    print(graph.depth_first(a))
