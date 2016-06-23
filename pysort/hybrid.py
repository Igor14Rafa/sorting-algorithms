from math import log

from .insertion import insertion_sort
from .quick import quick_sort

def hybrid_sort(list):
    """
    Calculates the maximum depth of recursion based on the number of elements in list.
    @param list = a list object.
    """
    l = len(list)
    maxdepth = int(log(l,2)) * int(log(l,2))
    _hybridsort(list, 0, l - 1, maxdepth)

def _hybridsort(list, first, last, maxdepth):
    """
    Performs Hybridsort, beginning with quicksort and switching to insertion sort when maximum depth is reached.
    @param list = a list object.
    @param first = an integer, initial index of list.
    @param last = an integer, final index of list.
    @param maxdepth = an integer, initially indicates the maximum level of recursion, and it's decreased at each level.
    """
    if maxdepth == 0:
        insertion_sort(list)
	return
    if first < last:
        p = partition(list, first, last)
        _hybridsort(list, first, p - 1, maxdepth - 1)
        _hybridsort(list, p + 1, last, maxdepth - 1)
