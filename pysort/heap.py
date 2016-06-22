
from .counter import counter

def siftdown(list, start, end):
    """
    Restore a heap.

    @param list: a list object.
    @param start: a integer, the start index of restoring.
    @param end: a integer, then end index of restoring.
    """

    root = start
    while True:
        child = root * 2 + 1

        counter.next()
        if child > end:
            break

        counter.next(); counter.next()
        if child + 1 <= end and list[child] < list[child + 1]:
            child += 1

        counter.next()
        if list[root] < list[child]:
            list[root], list[child] = list[child], list[root]
            root = child
        else:
            break

def heapify(list):
    """
    Transforms a list into a maximum heap.

    @param list: a list object.
    """

    for start in range((len(list) - 2) / 2, -1, -1):
        siftdown(list, start, len(list) - 1)

def heap_sort(list):
    """
    A heap sort algorithm implemetation

    @param list: a list object.
    """

    heapify(list)

    for end in range(len(list) - 1, 0, -1):
        list[end], list[0] = list[0], list[end]
        siftdown(list, 0, end - 1)
