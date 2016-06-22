
from .counter import counter

def bubble_sort(list):
    """
    A bubble sort algorithm implemetation

    @param list: a list object.
    """

    list_size = len(list)

    for i in xrange(list_size):
        for j in xrange(list_size - 1 - i):
            counter.next()
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
