import pytest
from data_structures_and_algorithms_python.challenges.graph_business_trip.graph_business_trip import *


def test_happy_path():
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

    actual = graph.business_trip([metroville, pandora])
    expected = (True, '$82')
    assert actual == expected


def test_edge_case():
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

    actual = graph.business_trip([arendelle, manstropolis, naboo, narina])
    expected = (True, '$365')
    assert actual == expected


def test_expected_failure():
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

    actual = graph.business_trip([manstropolis, narina, naboo])
    expected = (True, '$26')
    assert actual != expected
