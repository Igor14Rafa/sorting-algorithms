from math import *
from insertion import *
from quick import *

def hybridsort(list):
    l = len(list)
    maxdepth = int(log(l,2)) * int(log(l,2))		
    _hybridsort(list, 0, l - 1, maxdepth)

def _hybridsort(list, first, last, maxdepth):
    n = len(list)
    if maxdepth == 0:
        insertion_sort(list)
	return
    if first < last:
        p = partition(list, first, last)
        _hybridsort(list, first, p - 1, maxdepth - 1)
        _hybridsort(list, p + 1, last, maxdepth - 1)
