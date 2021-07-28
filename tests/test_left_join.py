from data_structures_and_algorithms_python.challenges.hashmap_left_join.hashmap_left_join import *
import pytest


def test_hash_tables(test_two_hash):
    expected = [['fond', 'enamored', 'averse'], ['outfit', 'grap', None], [
        'diligent', 'employed', 'idle'], ['wrath', 'anger', 'delight'], ['guide', 'usher', 'follow']]
    actual = test_two_hash
    assert actual == expected


@pytest.fixture
def test_two_hash():
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
    return left_join(hash1, hash2)
