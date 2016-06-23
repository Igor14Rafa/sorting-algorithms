"""
Run analyzes tests for sorting algorithms.
"""

import random
import itertools
import os
import time
import csv
import logging

from pysort import SortingList

TEST_CODITIONS = (
    'CRESCENT',
    'DECRESCENT',
    'RANDOM'
)

# Test sizes range.
TEST_SIZES = (
    100,
    500,
    1000,
    5000,
    30000,
    80000,
    100000,
    150000,
    200000
)

SORT_ALGS = (
    'bubble_sort',
    'heap_sort',
    'insertion_sort',
    'merge_sort',
    'quick_sort',
    'selection_sort',
    'hybrid_sort'
)

def timeit(function):
    """
    A time measurement function.

    `timeit` from `timeit` module is too complex for this use.

    @param function: a callable with no args.

    @return: a float in seconds between starts and ends the function.
    """

    start = time.time()
    function()

    return time.time() - start

def build_list(size, condition, range=(0, 2e20)):
    """
    Builds a list of `size` size and `condition` arrangement.

    @param size: a integer.
    @param condition: a `TEST_CODITIONS` item.
    @param range: a tuple with start and end range of the numbers
        generated.

    @return: a `SortingList` object.
    """

    logging.debug('building a list with %d elements and %s' % (
        size,
        condition.lower()
    ))

    list = [random.randint(range[0], range[1])
                for _ in __builtins__.range(size)]

    if condition == 'CRESCENT' or condition == 'DECRESCENT':
        list.sort()
    elif condition == 'DECRESCENT':
        list = list[::-1]
    elif condition == 'RANDOM':
        random.shuffle(list)

    return SortingList(list)

def run_test(size, condition, sortalg):
    """
    Run 3 tests for the `sortalg` and returns the time average.

    @param size: a integer, the list size to test.
    @param condition: a `TEST_CODITIONS` item.
    @param sortalg: a string, a `SORT_ALGS` item.

    @return: a average between tree tests time.
    """

    times = []

    logging.debug('running tests for %d elements and %s' % (
        size,
        condition.lower()
    ))

    for i in xrange(3):
        list = build_list(size, condition)
        logging.debug('running sort algorithm')
        times.append(timeit(getattr(list, sortalg)))

    result = sum(times)/3.
    logging.debug('result: %.2f s' % result)
    return result

def run_all_tests():
    """
    Run all tests possibilities and saves it to CSV files.
    """

    logging.debug('starting testing')

    for alg in SORT_ALGS:
        logging.debug('running for %s' % alg)

        fp = open(os.path.join('results', '%s.csv' % alg), 'w')
        fd = csv.writer(fp)
        fd.writerow(('Size', 'Result', 'Condition'))

        for test_case in itertools.product(TEST_SIZES, TEST_CODITIONS):
            size = test_case[0]
            condition = test_case[1]

            result = run_test(size, condition, alg)
            fd.writerow((size, result, condition))

        fp.close()

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    run_all_tests()
