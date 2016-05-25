#!/usr/bin/python

def bubbleSort(list):
    for i in range(len(list)):
        for j in range(len(list) - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

def insertionSort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and list[j] > key:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key

def selectionSort (list):
    for i in range(0,len(list)):
        smallest = i
        for j in range(i,len(list)):
            if list[j] < list[smallest]:
                smallest = j
        list[smallest] , list[i] = list[i] , list[smallest]
#   return list

def mergeSort(list):
    if len(list) < 2:
        return list
    m = len(list) / 2
    return merge(mergeSort(list[:m]), mergeSort(list[m:]))


def merge(left, right):
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

def quickSort(list):
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

        quickSort(smaller_list)
        quickSort(larger_list)
        list[:] = smaller_list + [list[pivot_index]] + larger_list

def heapSort(list):

    for start in range((len(list) - 2) / 2, -1, -1):
        siftdown(list, start, len(list) - 1)

    for end in range(len(list) - 1, 0, -1):
        list[end], list[0] = list[0], list[end]
        siftdown(list, 0, end - 1)
#   return list

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

if __name__ == "__main__":
    size = [100, 500, 1000, 5000, 30000, 80000, 100000, 150000, 200000]
    
