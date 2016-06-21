def partition(A, p, r):
    i = p - 1
    x = A[p]
    j = r 
    while True:
        while A[j] > x: j -= 1
        while A[i] < x: i += 1
        if i < j: A[i], A[j] = A[j], A[i]
        else: return j

def quick_sort(A, p, r):
    if p < r:
        pivot = partition(A,p, r)
        quick_sort(A, p, pivot - 1)
        quick_sort(A, pivot + 1, r)
