

class Vertex():
    def __init__(self, key):
        self.key = key

    def __str__(self):
        return str(self.key)


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
            # self._adjacency_list[end_vertex].append(
            #     (str(start_vertex), weight))

    def get_nodes(self):
        return self._adjacency_list.keys()

    def neighbors(self, vertex):
        return self._adjacency_list[vertex]

    def size(self):
        return len(self._adjacency_list)

    def print_graph(self):
        print(self._adjacency_list)


if __name__ == '__main__':
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    graph.add_edge(a, c)
    graph.add_edge(a, d)
    graph.add_edge(b, c)
    graph.add_edge(b, f)
    graph.add_edge(c, a)
    graph.add_edge(c, b)
    graph.add_edge(c, e)
    graph.add_edge(d, a)
    graph.add_edge(d, e)
    graph.add_edge(e, c)
    graph.add_edge(e, d)
    graph.add_edge(e, f)
    graph.add_edge(f, b)
    graph.add_edge(f, e)
    assert graph.size() == 6
    print(graph.get_nodes())
    graph.print_graph()
    print(graph.neighbors(a))
