import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'datastructure'))
import binary_heap

class BinaryHeapClearTest(unittest.TestCase):
  def test_return_minimum_item_from_heap(self):
    heap = binary_heap.BinaryHeap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(1)
    heap.insert(4)
    heap.insert(2)
    self.assertEqual(heap.findMinimum().key, 1)
