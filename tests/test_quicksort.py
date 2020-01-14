import unittest
from sorting.quicksort import quicksort
import time

class QuicksortTestCase(unittest.TestCase):

    def test_normal_array_(self):
        """ Returns the correct sorted array."""

        array = [0,8,9,11,3,4,59]
        sorted_array = quicksort(array)
        expected_output = [0,3,4,8,9,11,59]
        self.assertEqual(sorted_array,expected_output)
    
    def test_array_with_duplicates(self):
        """ Testing quicksort with duplicates."""

        array = [1,0,1,2,9,3,1,5,2]
        sorted_array = quicksort(array)
        expected_output = [0,1,1,1,2,2,3,5,9]
        self.assertEqual(sorted_array,expected_output)

    def test_with_negative_numbers(self):
        """ Testing quicksort with negative numbers."""

        array = [0,-5,-9,3,99,5,-3,2]
        sorted_array = quicksort(array)
        expected_output = [-9,-5,-3,0,2,3,5,99]
        self.assertEqual(sorted_array,expected_output)