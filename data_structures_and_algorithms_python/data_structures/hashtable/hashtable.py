# from linked_list import *
from data_structures_and_algorithms_python.data_structures.hashtable.linked_list import *


class Hashtable():
    def __init__(self, size=1024):
        self.size = size
        self.array = [None]*size

    def hash(self, key):
        sumAsci = 0
        for char in key:
            sumAsci += ord(char)
        hashed_key = (sumAsci*17) % self.size
        return hashed_key

    def add_(self, key, value):
        index = self.hash(key)
        if not self.array[index]:
            self.array[index] = Linked_List()
        self.array[index].ll_append([key, value])
        return self.__str__()

    def get(self, key):
        try:
            index = self.hash(key)
            bucket = self.array[index]

            current = bucket.head
            while current:
                if current.value[0] == key:
                    return current.value[1]

                current = current.next
        except:
            return None

    def contains(self, key):

        index = self.hash(key)
        bucket = self.array[index]
        if bucket:
            current = bucket.head
            while current:
                if current.value[0] == key:
                    return True
                current = current.next
        return False

    def __str__(self):
        result = ""
        for i in self.array:
            if i is not None:
                temp = i.head
                while temp:
                    result += "{%s}" % (temp.value,)
                    temp = temp.next

        return result


if __name__ == "__main__":
    hashtable = Hashtable()

    hashtable.add_('ahmad', 25)
    hashtable.add_('silent', True)
    hashtable.add_('hamad', '26')
    print(hashtable.get('hamad'))
    print(hashtable.contains('hamad'))

    for i, items in enumerate(hashtable.array):
        if i and items:
            print(i, items)
        # try:
        #     index = self.hash(key)
        #     bucket = self.array[index]
        #     current = bucket.head
        #     while current:
        #         if current.value[0] == key:
        #             return True
        #         current = current.next
        # except:
        #     return False
