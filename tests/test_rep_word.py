from data_structures_and_algorithms_python.challenges.hashmap_repeated_word.hashmap_repeated_word import *


def test_text_No1():
    actual = f'{first_rep("Once upon a time, there was a brave princess who..."	)}'
    expected = 'a'
    assert actual == expected


def test_text_No2():
    actual = f'{first_rep("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."		)}'
    expected = 'summer'
    assert actual == expected


def test_empty_string():
    actual = f'{first_rep(" ")}'
    expected = 'None'
    assert actual == expected
