from data_structures_and_algorithms_python.challenges.fifo_animal_shelter.fifo_animal_shelter import *
import pytest




def test_queue_cat_multiple_enqueue(shelter_input):
    expected = 'dog1 <- dog2 <- dog3'
    actual = f"{shelter_input}"
    assert actual == expected


def test_dequeue_enqueue(shelter_input): 
    expected = 'dog1'
    actual = f"{shelter_input.dequeue()}"
    assert actual == expected


def test_dequeue_neither_dog_or_cat(): 
    shelter= AnimalShelter()
    expected = "Null"
    actual= f"{shelter.dequeue('mouse')}"
    assert actual == expected



@pytest.fixture
def shelter_input() : 
    shelter= AnimalShelter()
    dog1 = Dog("dog1")
    dog2 = Dog("dog2")
    dog3 =Dog("dog3")
    shelter.enqueue(dog1)
    shelter.enqueue(dog2)
    shelter.enqueue(dog3)
    return shelter.dog