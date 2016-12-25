import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'datastructure'))
import binary_heap

class BinaryHeapExtractMinTest(unittest.TestCase):
  def test_returns_none_on_empty_heap(self):
    heap = binary_heap.BinaryHeap()
    self.assertEqual(heap.extractMinimum(), None)

  def test_extract_minimum_item_from_heap(self):
    heap = binary_heap.BinaryHeap()
    node5 = heap.insert(5)
    node3 = heap.insert(3)
    node4 = heap.insert(4)
    node1 = heap.insert(1)
    node2 = heap.insert(2)
    self.assertEqual(heap.extractMinimum().key, node1.key)
    self.assertEqual(heap.extractMinimum().key, node2.key)
    self.assertEqual(heap.extractMinimum().key, node3.key)
    self.assertEqual(heap.extractMinimum().key, node4.key)
    self.assertEqual(heap.extractMinimum().key, node5.key)

  def test_extract_the_minimum_item_from_jumbled_heap(self):
    heap = binary_heap.BinaryHeap()
    node1 = heap.insert(1)
    node4 = heap.insert(4)
    node3 = heap.insert(3)
    node5 = heap.insert(5)
    node2 = heap.insert(2)
    self.assertEqual(heap.extractMinimum().key, node1.key)
    self.assertEqual(heap.extractMinimum().key, node2.key)
    self.assertEqual(heap.extractMinimum().key, node3.key)
    self.assertEqual(heap.extractMinimum().key, node4.key)
    self.assertEqual(heap.extractMinimum().key, node5.key)

  def test_extract_minimum_item_from_heap_with_negatives(self):
    heap = binary_heap.BinaryHeap()
    node1 = heap.insert(-9)
    node4 = heap.insert(6)
    node3 = heap.insert(3)
    node5 = heap.insert(10)
    node2 = heap.insert(-4)
    self.assertEqual(heap.extractMinimum().key, node1.key)
    self.assertEqual(heap.extractMinimum().key, node2.key)
    self.assertEqual(heap.extractMinimum().key, node3.key)
    self.assertEqual(heap.extractMinimum().key, node4.key)
    self.assertEqual(heap.extractMinimum().key, node5.key)
