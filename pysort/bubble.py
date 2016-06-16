
def bubble_sort(list):
    list_size = len(list)

    for i in xrange(list_size):
        for j in xrange(list_size - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
