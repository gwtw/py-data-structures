import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'datastructure'))
import binary_heap

class BinaryHeapSizeTest(unittest.TestCase):
  def test_return_size_of_heap(self):
    heap = binary_heap.BinaryHeap()
    self.assertEqual(heap.size(), 0)
    heap.insert(1)
    self.assertEqual(heap.size(), 1)
    heap.insert(2)
    self.assertEqual(heap.size(), 2)
    heap.insert(3)
    self.assertEqual(heap.size(), 3)
    heap.insert(4)
    self.assertEqual(heap.size(), 4)
    heap.insert(5)
    self.assertEqual(heap.size(), 5)
    heap.insert(6)
    self.assertEqual(heap.size(), 6)
    heap.insert(7)
    self.assertEqual(heap.size(), 7)
    heap.insert(8)
    self.assertEqual(heap.size(), 8)
    heap.insert(9)
    self.assertEqual(heap.size(), 9)
    heap.insert(10)
    self.assertEqual(heap.size(), 10)
