from data_structures_and_algorithms_python.data_structures.hashtable.hashtable import *


def left_join(hash1, hash2):

    result = []
    for item in hash1.array:
        if item:
            current = item.head
            while current:
                result += [[current.value[0], current.value[1]], ]
                current = current.next
    # print(result)
    for item in result:

        if hash2.contains(item[0]):
            print(item[0])
            val = hash2.get(item[0])
            item.append(val)
        else:
            item.append(None)

    return result


if __name__ == "__main__":
    hash1 = Hashtable()
    hash1.add_('fond', 'enamored')
    hash1.add_('wrath', 'anger')
    hash1.add_('diligent', 'employed')
    hash1.add_('outfit', 'grap')
    hash1.add_('guide', 'usher')

    hash2 = Hashtable()
    hash2.add_('fond', 'averse')
    hash2.add_('wrath', 'delight')
    hash2.add_('diligent', 'idle')
    hash2.add_('guide', 'follow')
    hash2.add_('flow', 'jam')
    print(left_join(hash1, hash2))
