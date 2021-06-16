
class Node:
    """ Class for the Node instances"""

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """ Class for the LInkedLists instances"""

    def __init__(self):
        """method to iniate a LinkedList"""

        self.head = None

    def insert(self, value):
        """method to insert new node to the beginnig of the list"""

        node = Node(value)
        node.next = self.head
        self.head = node

    def __str__(self):
        """method that returns a string that represents all list elements"""

        list_str = ''
        current = self.head
        while current:
            # print(current, "current")
            list_str += str(current.value ) + ', '
            current = current.next
        return list_str[:-2]



def zip_list(list1, list2):
    """
    This code done with help from Ahmad Swedani , Faisal Abuzaid , Obada Al Hawajreh

    Merge_lists function which takes two linked lists as arguments. Zips them together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list.
    """

    current_List1 = list1.head
    current_List2 = list2.head

    if current_List1 == None and current_List2 == None:
        raise Exception("lists are empty")

    if not current_List1:
        list1.head = list2.head
        return list1.head

    if not current_List2:
        return list1.head

    temp = current_List2.next

    while current_List1.next and current_List2.next:
        current_List1.next, current_List2.next = current_List2, current_List1.next
        current_List1 = current_List2.next
        current_List2, temp = temp, temp.next

    if not current_List1.next:
        current_List1.next = current_List2
        return list1.head

    if not current_List2.next:
        current_List1.next, current_List2.next = current_List2, current_List1.next
        return list1.head



def create_list(vals):
    """helper function to create list with given values, used in test module"""
    my_list = LinkedList()
    for i in vals:
        my_list.insert(i)
    return my_list


if __name__ == "__main__":

    l_list1 = create_list([4, 3, 2, 1])
    print(l_list1.__str__())
    l_list2 = create_list([9, 8, 7, 6, 5])
    print(l_list2.__str__())
    ref_to_head = zip_list(l_list1, l_list2)

    print(l_list1.__str__())
    print(l_list2.__str__())
