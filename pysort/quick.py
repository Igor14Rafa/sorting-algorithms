import random

def partition(aList, first, last):
    """
    Creates two partitions in aList, with the elements at left end being lesses than the pivot, and the rigth end being bigger than the pivot.
    @param aList = list being partitioned
    @param first = an integer, first index of aList
    @param last = an integer, last index of aList
    returns the final value of first (elements lesser than pivot)
    """

    pivot = first + random.randrange(last - first + 1)
    
    swap(aList, pivot, last)
    
    for i in range(first, last):
      
        if aList[i] <= aList[last]:
        
            swap(aList, i, first)
        
            first += 1
 
    

    swap(aList, first, last)
    
    return first



def swap(A, x, y):
    """
    Swaps two elements in A
    @param A = list object
    @param x,y = two indexes of A
    """
  
    A[x],A[y]=A[y],A[x]
 


def quick_sort(aList):

    
    _quicksort(aList, 0, len(aList) - 1)
 


def _quicksort(aList, first, last):
    
    """
    Perfoms the quicksort method
    @param aList = list being sorted
    @param first = an integer, first index of aList
    @param last = an integer, last index of aList
    """

    
    if first < last:
      
        pivot = partition(aList, first, last)
      
        _quicksort(aList, first, pivot - 1)
      
        _quicksort(aList, pivot + 1, last)
 
 
 
 
