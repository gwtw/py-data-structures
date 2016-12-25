import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'datastructure'))
import binary_heap

class BinaryHeapClearTest(unittest.TestCase):
  def test_sets_heaps_size_to_zero(self):
    heap = binary_heap.BinaryHeap()
    heap.insert(1)
    heap.insert(2)
    heap.insert(3)
    heap.clear()
    self.assertEqual(heap.size(), 0)

  def test_set_heaps_minimum_node_to_none(self):
    heap = binary_heap.BinaryHeap()
    heap.insert(1)
    heap.insert(2)
    heap.insert(3)
    heap.clear()
    self.assertEqual(heap.findMinimum(), None)
