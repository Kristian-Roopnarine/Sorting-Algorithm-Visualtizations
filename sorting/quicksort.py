from random import randint
import time

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot=arr.pop(0)
        less = [i for i in arr if i <= pivot]
        greater = [i for i in arr if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)



