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

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self._adjacency_list:
            raise KeyError('Start vertex is not found in the graph')
        elif end_vertex not in self._adjacency_list:
            raise KeyError('end vertex is not found in the graph')
        else:
            self._adjacency_list[start_vertex].append(
                (str(end_vertex), weight))

    def breath_first_search(self, start_vertex):
        list = []
        queue = Queue()
        visited = set()

        queue .enqueue(start_vertex)
        visited.add(start_vertex)

        while queue:
            current_vertex = queue.dequeue()
            list.append(current_vertex)
            for child in self._adjacency_list[current_vertex]:
                if child[0] not in visited:
                    child = child[0]
                    visited.add(child)
                    queue.enqueue(child)
        return list


if __name__ == "__main__":
    graph = Graph()
    a = graph.add_node('A')
    b = graph.add_node('B')
    c = graph.add_node('C')
    d = graph.add_node('D')
    e = graph.add_node('E')
    f = graph.add_node('F')
    graph.add_edge(a, b, 1)
    graph.add_edge(a, c, 2)
    graph.add_edge(b, d, 4)
    graph.add_edge(c, d, 8)
    graph.add_edge(c, e, 3)
    graph.add_edge(d, f, 5)

    print(graph.breath_first_search(a))
