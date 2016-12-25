import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'datastructure'))
import binary_heap

class BinaryHeapUnionTest(unittest.TestCase):
  def test_union_2_heaps_of_size_5_with_overlapping_elements_in_order(self):
    heap = binary_heap.BinaryHeap()
    heap.insert(0)
    heap.insert(2)
    heap.insert(4)
    heap.insert(6)
    heap.insert(8)
    other = binary_heap.BinaryHeap()
    other.insert(1)
    other.insert(3)
    other.insert(5)
    other.insert(7)
    other.insert(9)
    self.assertEqual(heap.size(), 5)
    self.assertEqual(other.size(), 5)

    heap.union(other)
    self.assertEqual(heap.size(), 10)
    for i in range(0, 10):
      self.assertEqual(heap.extractMinimum().key, i)
    self.assertTrue(heap.isEmpty())

  def test_union_2_heaps_of_size_5_with_overlapping_elements_in_reverse_order(self):
    heap = binary_heap.BinaryHeap()
    heap.insert(9)
    heap.insert(7)
    heap.insert(5)
    heap.insert(3)
    heap.insert(1)
    other = binary_heap.BinaryHeap()
    other.insert(8)
    other.insert(6)
    other.insert(4)
    other.insert(2)
    other.insert(0)
    self.assertEqual(heap.size(), 5)
    self.assertEqual(other.size(), 5)

    heap.union(other)
    self.assertEqual(heap.size(), 10)
    for i in range(0, 10):
      self.assertEqual(heap.extractMinimum().key, i)
    self.assertTrue(heap.isEmpty())

  def test_union_2_heaps(self):
    heaps = constructJumbledHeaps(self)
    heaps[0].union(heaps[1])
    self.assertEqual(heaps[0].size(), 10)
    for i in range(0, 10):
      self.assertEqual(heaps[0].extractMinimum().key, i)
    self.assertTrue(heaps[0].isEmpty())

  def test_union_2_heaps_after_extracting_minimum_from_each(self):
    heaps = constructJumbledHeaps(self)
    self.assertEqual(heaps[0].extractMinimum().key, 1)
    self.assertEqual(heaps[1].extractMinimum().key, 0)
    heaps[0].union(heaps[1])
    self.assertEqual(heaps[0].size(), 8)
    for i in range(2, 10):
      self.assertEqual(heaps[0].extractMinimum().key, i)
    self.assertTrue(heaps[0].isEmpty())

def constructJumbledHeaps(t):
  first = binary_heap.BinaryHeap()
  first.insert(9)
  first.insert(2)
  first.insert(6)
  first.insert(1)
  first.insert(3)
  t.assertEqual(first.size(), 5)
  second = binary_heap.BinaryHeap()
  second.insert(4)
  second.insert(8)
  second.insert(5)
  second.insert(7)
  second.insert(0)
  t.assertEqual(second.size(), 5)
  return [first, second]
