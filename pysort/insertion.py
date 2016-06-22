
from .counter import counter

def insertion_sort(list):
    """
    A insertion sort algorithm implemetation.

    @param list: a list object.
    """

    for i in xrange(1, len(list)):
        key = list[i]
        j = i - 1
        counter.next()
        while j >= 0 and list[j] > key:
            list[j + 1] = list[j]
            j -= 1
            counter.next()
        list[j + 1] = key
