
from .bubble import bubble_sort
from .heap import heap_sort
from .insertion import insertion_sort
from .merge import merge_sort
from .quick import quick_sort

class SortingList(list):

    def bubble_sort(self):
        return bubble_sort(self)

    def heap_sort(self):
        return heap_sort(self)

    def insertion_sort(self):
        return insertion_sort(self)

    def merge_sort(self):
        return merge_sort(self)

    def quick_sort(self):
        return quick_sort(self)
