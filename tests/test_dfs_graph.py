from data_structures_and_algorithms_python.challenges.graph_depth_first.graph_depth_first import *
import pytest


def test_depth_first():
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
    actual = f'{graph.depth_first(a)}'
    expected = "['A', 'B', 'C', 'G', 'D', 'E', 'F', 'H']"
    assert actual == expected
