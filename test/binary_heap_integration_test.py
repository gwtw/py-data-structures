import unittest
import os
import sys
import math
import random

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'datastructure'))
import binary_heap

class BinaryHeapIntegrationTest(unittest.TestCase):
  def test_works_with_string_keys(self):
    heap = binary_heap.BinaryHeap()
    node3 = heap.insert('f')
    node4 = heap.insert('o')
    node2 = heap.insert('c')
    node1 = heap.insert('a')
    node5 = heap.insert('q')
    self.assertEqual(heap.size(), 5)
    self.assertEqual(heap.extractMinimum().key, node1.key)
    self.assertEqual(heap.extractMinimum().key, node2.key)
    self.assertEqual(heap.extractMinimum().key, node3.key)
    self.assertEqual(heap.extractMinimum().key, node4.key)
    self.assertEqual(heap.extractMinimum().key, node5.key)
    self.assertTrue(heap.isEmpty())

  def test_gives_empty_heap_after_inserting_and_extracting_1000_in_order_elements(self):
    heap = binary_heap.BinaryHeap()
    for i in range(0, 1000):
      heap.insert(i, i)
    for i in range(0, 1000):
      heap.extractMinimum()
    self.assertTrue(heap.isEmpty())

  def test_gives_empty_heap_after_inserting_and_extracting_1000_reversed_elements(self):
    heap = binary_heap.BinaryHeap()
    for i in range(999, -1, -1):
      heap.insert(i, i)
    for i in range(0, 1000):
      heap.extractMinimum()
    self.assertTrue(heap.isEmpty())

  def test_gives_empty_heap_after_inserting_and_extracting_1000_pseudo_randomized_elements(self):
    heap = binary_heap.BinaryHeap()
    for i in range(0, 1000):
      if i % 2 == 0:
        heap.insert(i, i)
      else:
        heap.insert(999 - i, 999 - i)
    for i in range(0, 1000):
      heap.extractMinimum()
    self.assertTrue(heap.isEmpty())

  def test_handles_1000_shuffled_elements(self):
    heap = binary_heap.BinaryHeap()
    input = []
    for i in range(0, 1000):
      input.append(i)
    # shuffle
    for i in range(0, 1000):
      swapWith = math.floor(random.random() * 1000)
      temp = input[i]
      input[i] = input[swapWith]
      input[swapWith] = temp
    # insert
    for i in range(0, 1000):
      heap.insert(input[i])
    # extract
    output = []
    errorReported = False
    counter = 0
    while not heap.isEmpty():
      output.append(heap.extractMinimum().key)
      if (not errorReported and counter != output[len(output) - 1]):
        self.fail('the heap property was not maintained (elements in order 0, 1, 2, ..., 997, 998, 999)')
      counter += 1
    self.assertEqual(len(output), 1000)
