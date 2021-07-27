# from linked_list import *
from data_structures_and_algorithms_python.data_structures.hashtable.linked_list import *


class Hashtable():
    def __init__(self, size=1024):
        self.size = size
        self.array = [None]*size

    def display(self):
        hashtable = Hashtable()
        arr = []
        for i, items in enumerate(hashtable.array):
            if i and items:
                arr.append(i)
        return arr

    def hash(self, key):
        sumAsci = 0
        for char in key:
            sumAsci += ord(char)
        hashed_key = (sumAsci*17) % self.size
        return hashed_key

    def add(self, key, value):
        index = self.hash(key)
        if not self.array[index]:
            self.array[index] = Linked_List()
        self.array[index].ll_append([key, value])

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


if __name__ == "__main__":
    hashtable = Hashtable()

    hashtable.add('ahmad', 25)
    hashtable.add('silent', True)
    hashtable.add('hamad', '26')
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
