
def siftdown(list, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end: break
        if child + 1 <= end and list[child] < list[child + 1]:
            child += 1
        if list[root] < list[child]:
            list[root], list[child] = list[child], list[root]
            root = child
        else:
            break

def heapify(list):
    for start in range((len(list) - 2) / 2, -1, -1):
        siftdown(list, start, len(list) - 1)

def heap_sort(list):
    heapify(list)

    for end in range(len(list) - 1, 0, -1):
        list[end], list[0] = list[0], list[end]
        siftdown(list, 0, end - 1)
