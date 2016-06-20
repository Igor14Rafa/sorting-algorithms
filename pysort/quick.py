
def quick_sort(list):
    """
    A quick sort algorithm implemetation.

    @param list: a list object.
    """

    if len(list) > 1:
        pivot_index = len(list) // 2
        smaller_list = []
        larger_list = []

        for i, val in enumerate(list):
            if i != pivot_index:
                if val < list[pivot_index]:
                    smaller_list.append(val)
                else:
                    larger_list.append(val)

        quick_sort(smaller_list)
        quick_sort(larger_list)
        list[:] = smaller_list + [list[pivot_index]] + larger_list
