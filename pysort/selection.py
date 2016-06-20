
def selection_sort (list):
    """
    A selection sort algorithm implemetation.

    @param list: a list object.
    """

    list_size = len(list)

    for i in range(0, list_size):
        smallest = i
        for j in range(i, list_size):
            if list[j] < list[smallest]:
                smallest = j
        list[smallest] , list[i] = list[i] , list[smallest]
