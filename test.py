
import unittest
import random

from pysort import SortingList

def build_list(size):
    list = range(size)
    random.shuffle(list)

    return list

def is_sorted(list):
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


if __name__ == '__main__':
    unittest.main()
