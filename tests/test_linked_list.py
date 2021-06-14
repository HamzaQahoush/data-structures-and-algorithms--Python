import pytest

from data_structures_and_algorithms_python.data_structures.linked_list import Node , Linked_List




def test_instance():
    ll = Linked_List()
    assert isinstance(ll, Linked_List) 

def test_LinkedList_include():
    test_LinkedList = Linked_List()
    test_LinkedList.insert(0)
    test_LinkedList.insert(1)
    test_LinkedList.insert(4)
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


def test_insert_before(llFixture):
    llFixture.insertBefore(2,10)
    assert llFixture.__str__() == '7 -> 3 -> 10 -> 2 -> 5 -> Null'



def test_insert_after(llFixture):
    llFixture.insertAfter(3,12)     
    assert llFixture.__str__() == "7 -> 3 -> 12 -> 2 -> 5 -> Null"


def test_kthFromEnd(llFixture):
    actual_output1 =llFixture.kthFromEnd(3)
    actual_output2=llFixture.kthFromEnd(0)
    actual_output3 =llFixture.kthFromEnd(10)
    print (actual_output1,actual_output2,actual_output3 ,'hiiiiiii')
    expected_output1 = 7
    expected_output2 = 5
    expected_output3 = False
    assert actual_output1 == expected_output1
    assert actual_output2 == expected_output2
    assert actual_output3 == expected_output3

@pytest.fixture
def llFixture():
    linked_list_o=Linked_List()
    linked_list_o.insert(5) 
    linked_list_o.insert(2)
    linked_list_o.insert(3)
    linked_list_o.insert(7)
    return linked_list_o
