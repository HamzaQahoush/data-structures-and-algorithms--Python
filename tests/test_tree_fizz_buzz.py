from data_structures_and_algorithms_python.challenges.tree_fizz_buzz.tree_fizz_buzz import *
import pytest 


def test_fizz(fizz_buzz_game): 
    fizz_Buzz_Tree(fizz_buzz_game)
    expected = 'Fizz'
    actual =fizz_buzz_game.root.child[1].value
    assert actual == expected

def test_Buzz(fizz_buzz_game): 
    fizz_Buzz_Tree(fizz_buzz_game)
    expected = 'Buzz'
    actual =fizz_buzz_game.root.child[2].value
    assert actual == expected

def test_Fizz_and_Buzz(fizz_buzz_game): 
    fizz_Buzz_Tree(fizz_buzz_game)
    expected = "Fizz Buzz"
    actual =fizz_buzz_game.root.child[0].value
    assert actual == expected


def test_Not_Fizz_Not_Buzz(fizz_buzz_game): 
    fizz_Buzz_Tree(fizz_buzz_game)
    expected = '1'
    actual =fizz_buzz_game.root.value
    assert actual == expected








@pytest.fixture
def fizz_buzz_game(): 
    kAryTree = KAryTree()
    kAryTree.root=Node(1) #root
    kAryTree.root.child+=[Node(15)] #child 0
    kAryTree.root.child+=[Node(3)] #child 1
    kAryTree.root.child+=[Node(5)] #child 2
    kAryTree.root.child[0].child+=[Node(5)] #child[0,0]
    return kAryTree
