from data_structures_and_algorithms_python.challenges.multi_bracket_validation.multi_bracket_validation import *
import pytest 


def test_2_curly_2_parentheses (): 
    x= multi_bracket_validation('{}(){}')
    expected= 'True' 
    actual = f'{x}'
    assert actual == expected

def test_1_curly (): 
    x= multi_bracket_validation('{}')
    expected= 'True' 
    actual = f'{x}'
    assert actual == expected

def test_2parentheses_2squres (): 
    x= multi_bracket_validation('()[[Extra Characters]]')
    expected= 'True' 
    actual = f'{x}'
    assert actual == expected

def test_2parentheses_1curly_3square (): 
    x= multi_bracket_validation('(){}[[]]')
    expected= 'True' 
    actual = f'{x}'
    assert actual == expected

def test_single_parentheses_False (): 
    x=multi_bracket_validation('{}{Code}[Fellows](()')
    expected= 'False' 
    actual = f'{x}'
    assert actual == expected


def test_single_parentheses_False_with_2_squres (): 
    x=multi_bracket_validation('[({}]')
    expected= 'False' 
    actual = f'{x}'
    assert actual == expected


def test_reveres_parentheses_one_squres (): 
    x=multi_bracket_validation('(](')
    expected= 'False' 
    actual = f'{x}'
    assert actual == expected


def test_parentheses_with_curly (): 
    x=multi_bracket_validation('{(})')
    expected= 'False' 
    actual = f'{x}'
    assert actual == expected














