from data_structures_and_algorithms_python.data_structures.linked_list.zip import *
import pytest



def test_lists_equal():
    l_list1 = create_list([6, 0, 4, 7,])
    l_list2 = create_list([2,11,3,5])
    ref_to_head = zip_list(l_list1, l_list2)
    assert ref_to_head.value == 7
    assert l_list1.__str__() == '7, 5, 4, 3, 0, 11, 6, 2'

def test_lists_empty():
    l_list1 = LinkedList()
    l_list2 = LinkedList()
    with pytest.raises(Exception):
        zip_list(l_list1, l_list2)

def test_list_1st_empty():
    l_list1 = LinkedList()
    l_list2 = create_list([6, 0, 4, 7,])
    ref_to_head = zip_list(l_list1, l_list2)
    assert ref_to_head.value == 7
    assert l_list1.__str__() ==  '7, 4, 0, 6'

def test_list2_empty():
    l_list2 = LinkedList()
    l_list1 = create_list([6, 0, 4, 7,])
    ref_to_head = zip_list(l_list1, l_list2)
    assert ref_to_head.value == 7
    assert l_list1.__str__() == '7, 4, 0, 6'


def test_list1_shorter():
    l_list1 = create_list([6, 0, 4, 7])
    l_list2 = create_list([2,11,3,5, 1])
    ref_to_head = zip_list(l_list1, l_list2)
    assert ref_to_head.value == 7
    assert l_list1.__str__() ==  '7, 1, 4, 5, 0, 3, 6, 11, 2'

def test_1slist_longer():
    l_list1 = create_list([6, 0, 4, 7, 1])
    l_list2 = create_list([2,11,3,5])
    ref_to_head = zip_list(l_list1, l_list2)
    assert ref_to_head.value == 1
    assert l_list1.__str__() == '1, 5, 7, 3, 4, 11, 0, 2, 6'