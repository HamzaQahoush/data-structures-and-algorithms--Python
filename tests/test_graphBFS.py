from data_structures_and_algorithms_python.challenges.graph_breadth_first.graph_breadth_first import *
import pytest


def test_breadth_first():
    graph = Graph()
    a = graph.add_node('A')
    b = graph.add_node('B')
    c = graph.add_node('C')
    d = graph.add_node('D')
    e = graph.add_node('E')
    f = graph.add_node('F')
    graph.add_edge(a, b)
    graph.add_edge(a, c)
    graph.add_edge(b, d)
    graph.add_edge(c, d)
    graph.add_edge(c, e)
    graph.add_edge(d, f)
    actual = f'{graph.breath_first_search(a)}'
    expected = "['A', 'B', 'C', 'D', 'E', 'F']"
    assert actual == expected
