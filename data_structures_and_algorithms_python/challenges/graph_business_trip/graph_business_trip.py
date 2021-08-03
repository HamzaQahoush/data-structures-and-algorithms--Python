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

    def business_trip(self, cities: list):
        sumV = 0
        flag = False
        for i in range(len(cities)-1):
            neighbors = self._adjacency_list[cities[i]]

            for neighbor in neighbors:
                if cities[i+1] == neighbor[0]:
                    sumV += neighbor[1]
                    flag = True
                    break
                else:
                    sumV += 0
                    flag = False
        if flag is None:
            return False, '$0'

        return True, '$' + str(sumV)


if __name__ == '__main__':

    graph = Graph()

    pandora = graph.add_node('pandora')
    arendelle = graph.add_node('arendelle')
    metroville = graph.add_node('metroville')
    narina = graph.add_node('narina')
    naboo = graph.add_node('naboo')
    manstropolis = graph.add_node('manstropolis')

    graph.add_edge(pandora, arendelle, 150)
    graph.add_edge(pandora, metroville, 82)
    graph.add_edge(arendelle, pandora, 150)
    graph.add_edge(arendelle, metroville, 99)
    graph.add_edge(arendelle, manstropolis, 42)
    graph.add_edge(metroville, pandora, 82)
    graph.add_edge(metroville, arendelle, 99)
    graph.add_edge(metroville, manstropolis, 105)
    graph.add_edge(metroville, naboo, 26)
    graph.add_edge(metroville, narina, 37)
    graph.add_edge(narina, metroville, 37)
    graph.add_edge(narina, naboo, 250)
    graph.add_edge(naboo, narina, 250)
    graph.add_edge(naboo, metroville, 26)
    graph.add_edge(naboo, manstropolis, 73)
    graph.add_edge(manstropolis, naboo, 73)
    graph.add_edge(manstropolis, arendelle, 42)
    graph.add_edge(manstropolis, metroville, 105)

    print(graph.business_trip([pandora, arendelle]))
