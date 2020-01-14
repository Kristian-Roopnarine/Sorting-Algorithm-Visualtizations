from sorting.bubble_sort import bubbleSort
import time
import unittest

class BubbleSortTestCase(unittest.TestCase):

    def test_normal_array(self):
        array = [-3,1,5,2,-10,35,2,0,2]
        sorted_array = bubbleSort(array)
        expected_array = [-10,-3,0,1,2,2,2,5,35]
        self.assertEqual(sorted_array,expected_array)
    
    def test_seeing_bubble_sort(self):
        """ Using print statements to see bubble sort."""
        
        array = [0,1,0,3,0,6,0,2,0,10]
        sorted_array = bubbleSort(array)
        expected_array = [0,0,0,0,0,1,2,3,6,10]
        self.assertEqual(sorted_array,expected_array)
