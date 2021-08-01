import pytest
from data_structures_and_algorithms_python.data_structures.graphs.graph import *

# 1 Node can be successfully added to the graph


def test_add_node_successfully():
    graph = Graph()
    graph.add_node('A')
    expected = 1
    actual = graph.size()
    assert actual == expected

# 2 An edge can be successfully added to the graph


def test_add_edge_successfully():
    graph = Graph()
    v1 = graph.add_node('A')
    v2 = graph.add_node('B')
    graph.add_edge(v1, v2)
    assert graph._adjacency_list[v1] == [(v2, 0)]


def test_get_all_nodes_and_check_the_size():
    graph = Graph()
    v1 = graph.add_node('A')
    v2 = graph.add_node('B')
    v3 = graph.add_node('C')
    v4 = graph.add_node('D')
    v5 = graph.add_node('E')
    assert graph.size() == 5


def test_get_neighbor_and_with_weights():
    graph = Graph()
    v1 = graph.add_node('A')
    v2 = graph.add_node('B')
    v3 = graph.add_node('C')
    graph.add_edge(v1, v2, 1)
    graph.add_edge(v1, v3, 2)
    assert graph.neighbors(v1) == [('B', 1), ('C', 2)]

# 7A graph with only one node and edge can be properly returned


def test_graph_with_one_node_and_edge():
    graph = Graph()
    v1 = graph.add_node('A')
    with pytest.raises(KeyError):
        graph.add_edge(v1, None)

# 8 An empty graph properly returns null


def test_empty_graph():
    graph = Graph()
    assert graph.print_graph() == None
    print('pass')
