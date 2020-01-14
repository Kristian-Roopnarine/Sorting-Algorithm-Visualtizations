import unittest
from sorting.insertion_sort import insertionSort

class InsertionSortTestCase(unittest.TestCase):

    def test_normal_array(self):
        """Testing insertion sort."""
        
        array = [134,342,95,3,2,9,0]
        sorted_array = insertionSort(array)
        expected_array = [0,2,3,9,95,134,342]
        self.assertEqual(sorted_array,expected_array)