import pytest

from data_structures_and_algorithms_python.data_structures.linked_list import Node , Linked_List



def test_instance():
    ll = Linked_List()
    assert isinstance(ll, Linked_List) 

def test_LinkedList_include():
    test_LinkedList = Linked_List()
    test_LinkedList.insert(0)
    test_LinkedList.insert(1)
    assert test_LinkedList.include(1) == True
    assert test_LinkedList.include(88) == False   

def test_append_1():
    ll = Linked_List()
    ll.append(1)
    ll.append(2)
    assert ll.head.value == 1
    assert ll.head.next.value==2


def test__str__():
    test_LinkedList = Linked_List()
    test_LinkedList.insert('H')
    test_LinkedList.insert('A')
    test_LinkedList.insert('Z')
    test_LinkedList.insert('M')
    test_LinkedList.insert('A')
    test_LinkedList.insert('H')
    assert test_LinkedList.__str__() == "H -> A -> M -> Z -> A -> H -> Null"




@pytest.fixture
def linked_list_ob():
    linked_list_o=Linkedlist()
    linked_list_o.insert(1)
    linked_list_o.insert(2)
    linked_list_o.insert(3)
    linked_list_o.insert(0)
    return linked_list_o

@pytest.fixture
def linked_list_ob2():
    linked_list_o2=Linkedlist()
    linked_list_o2.insert(0)
    linked_list_o2.insert(3)
    linked_list_o2.insert(2)
    linked_list_o2.insert(1)
    return linked_list_o2

