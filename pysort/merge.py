
def merge(left, right):
    """
    Merge two lists into a ordered one.

    @param left: a list object.
    @param right: a list object.

    @return: a list object.
    """

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(list):
    """
    A merge sort algorithm implemetation.

    @param list: a list object.

    @return: a new ordered list.
    """

    if len(list) < 2:
        return list
    m = len(list) / 2

    return merge(merge_sort(list[:m]), merge_sort(list[m:]))
