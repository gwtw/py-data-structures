import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'datastructure'))
import binary_heap

class BinaryHeapInsertTest(unittest.TestCase):
  def test_insert_items_into_heap(self):
    heap = binary_heap.BinaryHeap()
    heap.insert(1)
    heap.insert(2)
    heap.insert(3)
    heap.insert(4)
    heap.insert(5)
    self.assertEqual(heap.size(), 5)

  def test_return_inserted_node(self):
    heap = binary_heap.BinaryHeap()
    ret = heap.insert(1, 'foo')
    self.assertEqual(ret.key, 1)
    self.assertEqual(ret.value, 'foo')

  def test_insert_multiple_items_with_same_key(self):
    heap = binary_heap.BinaryHeap()
    heap.insert(1)
    heap.insert(1)
    self.assertEqual(1, heap.extractMinimum().key)
    self.assertEqual(1, heap.extractMinimum().key)
