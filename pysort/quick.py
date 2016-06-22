import random

from .counter import counter

def partition(list, first, last):
    pivot = first + random.randrange(last - first + 1)
    swap(list, pivot, last)

    for i in range(first, last):
        counter.next()
        if list[i] <= list[last]:
            swap(list, i, first)
            first += 1

    swap(list, first, last)

    return first

def swap(A, x, y):
    A[x],A[y]=A[y],A[x]

def quick_sort(list):
    quicksort(list, 0, len(list) - 1)

def quicksort(list, first, last):
    counter.next()
    if first < last:
        pivot = partition(list, first, last)
        quicksort(list, first, pivot - 1)
        quicksort(list, pivot + 1, last)
