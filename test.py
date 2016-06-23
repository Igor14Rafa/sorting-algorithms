
import unittest
import random

from pysort import SortingList

def build_list(size):
    """
    Build a list with values from 0 to `size` and shuffle it.

    @param size: a integer with the list size.

    @return: a list object.
    """

    list = range(size)
    random.shuffle(list)

    return list

def is_sorted(list):
    """
    Return true if the list is sorted.

    @param list: any iterable with `__len__` and `__getitem__` methods.

    @return: a boolean.
    """

    for i in xrange(len(list) - 1):
        if list[i] > list[i+1]:
            return False
    return True

class SortAlgs(unittest.TestCase):

    def test_bubble(self):
        list = SortingList(build_list(30))
        list.bubble_sort()
        self.assertTrue(is_sorted(list))

    def test_heap(self):
        list = SortingList(build_list(30))
        list.heap_sort()
        self.assertTrue(is_sorted(list))

    def test_insertion(self):
        list = SortingList(build_list(30))
        list.insertion_sort()
        self.assertTrue(is_sorted(list))

    def test_merge(self):
        list = SortingList(build_list(30))
        list = list.merge_sort()
        self.assertTrue(is_sorted(list))

    def test_quick(self):
        list = SortingList(build_list(30))
        list.quick_sort()
        self.assertTrue(is_sorted(list))

    def test_selection(self):
        list = SortingList(build_list(30))
        list.selection_sort()
        self.assertTrue(is_sorted(list))
        
    def test_hybrid(self):
        list = SortingList(build_list(30))
        list.hybrid_sort()
        self.assertTrue(is_sorted(list))


if __name__ == '__main__':
    unittest.main()
