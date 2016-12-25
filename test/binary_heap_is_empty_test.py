import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'datastructure'))
import binary_heap

class BinaryHeapIsEmptyTest(unittest.TestCase):
  def test_return_whether_heap_is_empty(self):
    heap = binary_heap.BinaryHeap()
    self.assertTrue(heap.isEmpty())
    heap.insert(1)
    self.assertFalse(heap.isEmpty())
    heap.extractMinimum()
    self.assertTrue(heap.isEmpty())
