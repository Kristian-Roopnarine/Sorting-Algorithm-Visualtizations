import unittest
from sorting.selection_sort import selectionSort,findSmallet

class SelectionSortTestCase(unittest.TestCase):

    def test_sorting_works(self):
        """ Testing that a normal array works."""

        array = [0,1,2,4,5,91,234,2342,3,2,402,5]
        sorted_array=selectionSort(array)
        expected_array = [0,1,2,2,3,4,5,5,91,234,402,2342]
        self.assertEqual(sorted_array,expected_array)
    
    def test_with_negative_numbers(self):
        """ Testing with an array containing negative numbers."""

        array = [-9,-100,0,4,2,-1,5,32]
        sorted_array = selectionSort(array)
        expected_array = [-100,-9,-1,0,2,4,5,32]
        self.assertEqual(sorted_array,expected_array)