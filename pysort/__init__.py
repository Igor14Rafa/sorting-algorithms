
from .bubble import bubble_sort
from .heap import heap_sort
from .insertion import insertion_sort
from .merge import merge_sort
from .quick import quick_sort
from .selection import selection_sort

class SortingList(list):
    """
    A list with many sorting methods.
    """

    def bubble_sort(self):
        """
        Sort with bubble sort algorithm.
        """

        return bubble_sort(self)

    def heap_sort(self):
        """
        Sort with heap sort algorithm.
        """

        return heap_sort(self)

    def insertion_sort(self):
        """
        Sort with insertion sort algorithm.
        """

        return insertion_sort(self)

    def merge_sort(self):
        """
        Sort with merge sort algorithm.
        """

        return merge_sort(self)

    def quick_sort(self):
        """
        Sort with quick sort algorithm.
        """

        return quick_sort(self)

    def selection_sort(self):
        """
        Sort with selection sort algorithm.
        """

        return selection_sort(self)
