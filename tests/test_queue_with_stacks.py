import pytest
from data_structures_and_algorithms_python.challenges.queue_with_stacks.queue_with_stacks import *



def test_queue_enqueue(): 
    expected = "4"
    queue = PseudoQueue()
    queue.enqueue(4)
    actual = f"{queue}"
    assert actual == expected



def test_queue_multible_enqueue(queue_values): 
    expected ='6 -> 4 -> 7 -> 8'
    actual = f'{queue_values}'
    assert actual == expected


def test_dequeue_enqueue(queue_values): 
    expected =8
    actual= queue_values.dequeue()
    assert actual == expected


def test_empty_queue(): 
    queue=PseudoQueue()
    expected = "can't dequeue from empty stack "
    actual =queue.dequeue()
    assert actual == expected


@pytest.fixture
def queue_values() : 
    queue=PseudoQueue()
    queue.enqueue(8)
    queue.enqueue(7)
    queue.enqueue(4)
    queue.enqueue(6)
    return queue
