from data_structures_and_algorithms_python.challenges.quick_sort.quick_sort import *


def test_insert_sample():
    sample_array = [8, 4, 23, 42, 16, 15]
    actual = f'{quick_sort(sample_array , 0 , len(sample_array)-1)}'
    expected = '[4, 8, 15, 16, 23, 42]'
    assert actual == expected


def test_insert_reverse_sorted():
    reverse_sorted = [20, 18, 12, 8, 5, -2]
    actual = f'{quick_sort(reverse_sorted, 0 , len(reverse_sorted)-1)}'
    expected = '[-2, 5, 8, 12, 18, 20]'
    assert actual == expected


def test_insert_few_uniques():
    few_uniques = [5, 12, 7, 5, 5, 7]
    actual = f'{quick_sort(few_uniques,0 , len(few_uniques)-1)}'
    expected = '[5, 5, 5, 7, 7, 12]'
    assert actual == expected


def test_insert_nearly_sorted():
    nearly_sorted = [2, 3, 5, 7, 13, 11]
    actual = f'{quick_sort(nearly_sorted,0 , len(nearly_sorted)-1)}'
    expected = '[2, 3, 5, 7, 11, 13]'
    assert actual == expected
