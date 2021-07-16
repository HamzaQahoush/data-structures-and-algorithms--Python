from data_structures_and_algorithms_python.data_structures.hashtable.hashtable import *


# 1 Adding a key/value to your hashtable results in the value
# being in the data structure

def test_add_value():
    hashtable = Hashtable()
    hashtable.add('Hamza', 'Qahoush')
    actual = ''
    for i in hashtable.array:
        if i:
            actual += i.__str__()
    expected = "[['Hamza', 'Qahoush']]"
    assert actual == expected

# 2 Retrieving based on a key returns the value stored


def test_get_value():
    hashtable = Hashtable()
    hashtable.add('Hamza', 'Qahoush')

    actual = hashtable.get('Hamza')
    expected = 'Qahoush'
    assert actual == expected


# 3 Successfully returns null for a key that does not exist in the hashtable

def test_null_for_not_exist_key():
    hashtable = Hashtable()
    hashtable.add('Hamza', 'Qahoush')

    actual = hashtable.get('Hadi')
    expected = None
    assert actual == expected


# 4 Successfully handle a collision within the hashtable
def test_collosion():
    hashtable = Hashtable()
    hashtable.add(
        'ease', ' it\'s verb ,  mean make something unpleasant, painful, or intense less serious or severe.')
    hashtable.add('seas', ' it\'s Noun plural of sea')
    actual = []
    for i in hashtable.array:
        if i:
            actual.append(i.__str__())
    expected = ['[[\'seas\', " it\'s Noun plural of sea"]]',
                '[[\'ease\', " it\'s verb ,  mean make something unpleasant, painful, or intense less serious or severe."]]']
    assert actual == expected


# 5  Successfully retrieve a value from a bucket within the hashtable that has a collision

def test_retrieve_value_from_collision():
    hashtable = Hashtable()
    hashtable.add(
        'GRAINED', 'Having a grain or markings due to a particular arrangement, as in wood')
    hashtable.add(
        'READING', 'The act of looking at printed words and comprehending them')

    actual = hashtable.get('READING')
    expected = 'The act of looking at printed words and comprehending them'
    assert actual == expected


# 6 Successfully hash a key to an in-range value

def test_hash_key():
    hashtable = Hashtable()
    actual = f"{hashtable.hash('Name')}"
    expected = '401'
    assert actual == expected
