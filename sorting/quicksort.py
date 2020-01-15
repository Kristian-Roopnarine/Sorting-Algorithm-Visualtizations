from random import randint
import time


def partition(A,low,hi):
    pivotIndex = get_pivot(A,low,hi)
    pivotValue = A[pivotIndex]
    A[pivotIndex],A[low] = A[low],A[pivotIndex]
    border = low

    for i in range(low,hi+1):
        if A[i] < pivotValue:
            border += 1
            A[i],A[border] = A[border],A[i]
    A[low], A[border] = A[border],A[low]
    time.sleep(1)

    return border

def get_pivot(A,low,hi):
    mid = (low+hi) // 2
    pivot = hi
    if A[low] < A[mid]:
        if A[mid] < A[hi]:
            pivot=mid
    elif A[low] < A[hi]:
        pivot = low
    return pivot

def quicksort2(A,low,hi):
    if low < hi:
        p = partition(A,low,hi)
        quicksort2(A,low,p-1)
        quicksort2(A,p+1,hi)

def quicksort(A):
    quicksort2(A,0,len(A)-1)

