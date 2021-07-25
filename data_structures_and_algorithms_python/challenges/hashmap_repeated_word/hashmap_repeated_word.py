from data_structures_and_algorithms_python.data_structures.hashtable.hashtable import *
from data_structures_and_algorithms_python.data_structures.hashtable.linked_list import *
import re


def first_rep(string):
    hashtable = Hashtable()
    if string is None:
        return
    string = re.sub('\W+', ' ', string).lower().split()
    print(string)
    for char in string:
        if hashtable.contains(char):
            return char
        else:
            hashtable.add(char, "")


print(first_rep("Once upon a time, there was a brave princess who..."	))
print(first_rep("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."))
