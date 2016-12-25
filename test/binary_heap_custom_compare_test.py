import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'datastructure'))
import binary_heap

class BinaryHeapCustomCompareTest(unittest.TestCase):
  def test_gives_min_heap_given_non_reverse_compare(self):
    def compare(a, b):
      return a - b
    heap = binary_heap.BinaryHeap(compare)
    node3 = heap.insert(13)
    node4 = heap.insert(26)
    node2 = heap.insert(3)
    node1 = heap.insert(-6)
    node5 = heap.insert(27)
    self.assertEqual(heap.size(), 5)
    self.assertEqual(heap.extractMinimum().key, node1.key)
    self.assertEqual(heap.extractMinimum().key, node2.key)
    self.assertEqual(heap.extractMinimum().key, node3.key)
    self.assertEqual(heap.extractMinimum().key, node4.key)
    self.assertEqual(heap.extractMinimum().key, node5.key)
    self.assertTrue(heap.isEmpty())

  def test_gives_max_heap_given_reverse_compare(self):
    def compare(a, b):
      return b - a
    heap = binary_heap.BinaryHeap(compare)
    node3 = heap.insert(13)
    node4 = heap.insert(26)
    node2 = heap.insert(3)
    node1 = heap.insert(-6)
    node5 = heap.insert(27)
    self.assertEqual(heap.size(), 5)
    self.assertEqual(heap.extractMinimum().key, node5.key)
    self.assertEqual(heap.extractMinimum().key, node4.key)
    self.assertEqual(heap.extractMinimum().key, node3.key)
    self.assertEqual(heap.extractMinimum().key, node2.key)
    self.assertEqual(heap.extractMinimum().key, node1.key)
    self.assertTrue(heap.isEmpty())
