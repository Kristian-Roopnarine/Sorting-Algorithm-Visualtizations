from sorting.heap_sort import heapify,heapSort
import unittest
import time

class HeapSortTestCase(unittest.TestCase):

    def test_heap_sort(self):
        array = [3,5,2,45,32,0,32]
        sorted_array = heapSort(array)
        expected_array = [0,2,3,5,32,32,45]
        self.assertEqual(sorted_array,expected_array)