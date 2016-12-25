import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'datastructure'))
import binary_heap

class BinaryHeapBuildHeapTest(unittest.TestCase):
  def test_throws_if_keys_and_values_lengths_differ(self):
    with self.assertRaises(ValueError):
      binary_heap.BinaryHeap().buildHeap([], [1])
    with self.assertRaises(ValueError):
      binary_heap.BinaryHeap().buildHeap([1], [])
    with self.assertRaises(ValueError):
      binary_heap.BinaryHeap().buildHeap([1], [1, 2])
    with self.assertRaises(ValueError):
      binary_heap.BinaryHeap().buildHeap([1, 2], [])
    with self.assertRaises(ValueError):
      binary_heap.BinaryHeap().buildHeap([1, 2], [1])
    with self.assertRaises(ValueError):
      binary_heap.BinaryHeap().buildHeap([1, 2], [1, 2, 3])

  def test_doesnt_throw_with_undefined_values(self):
    binary_heap.BinaryHeap().buildHeap([1])

  def test_doesnt_throw_with_keys_and_values_lengths_same(self):
    binary_heap.BinaryHeap().buildHeap([], [])
    binary_heap.BinaryHeap().buildHeap([1], [1])
    binary_heap.BinaryHeap().buildHeap([1, 2], [1, 2])

  def test_constructs_a_valid_heap_with_keys_only(self):
    keys = [5, 8, 9, 1, 2, 6, 3, 7, 4]
    heap = binary_heap.BinaryHeap()
    heap.buildHeap(keys)
    self.assertEqual(heap.size(), 9)
    self.assertEqual(heap.extractMinimum().key, 1)
    self.assertEqual(heap.extractMinimum().key, 2)
    self.assertEqual(heap.extractMinimum().key, 3)
    self.assertEqual(heap.extractMinimum().key, 4)
    self.assertEqual(heap.extractMinimum().key, 5)
    self.assertEqual(heap.extractMinimum().key, 6)
    self.assertEqual(heap.extractMinimum().key, 7)
    self.assertEqual(heap.extractMinimum().key, 8)
    self.assertEqual(heap.extractMinimum().key, 9)
    self.assertTrue(heap.isEmpty())

  def test_constructs_valid_heap_with_keys_and_values(self):
    keys = [5, 8, 9, 1, 2, 6, 3, 7, 4];
    values = ['e', 'h', 'i', 'a', 'b', 'f', 'c', 'g', 'd'];
    heap = binary_heap.BinaryHeap();
    heap.buildHeap(keys, values);
    self.assertEqual(heap.size(), 9);
    minNode = heap.extractMinimum();
    self.assertEqual(minNode.key, 1);
    self.assertEqual(minNode.value, 'a');
    minNode = heap.extractMinimum();
    self.assertEqual(minNode.key, 2);
    self.assertEqual(minNode.value, 'b');
    minNode = heap.extractMinimum();
    self.assertEqual(minNode.key, 3);
    self.assertEqual(minNode.value, 'c');
    minNode = heap.extractMinimum();
    self.assertEqual(minNode.key, 4);
    self.assertEqual(minNode.value, 'd');
    minNode = heap.extractMinimum();
    self.assertEqual(minNode.key, 5);
    self.assertEqual(minNode.value, 'e');
    minNode = heap.extractMinimum();
    self.assertEqual(minNode.key, 6);
    self.assertEqual(minNode.value, 'f');
    minNode = heap.extractMinimum();
    self.assertEqual(minNode.key, 7);
    self.assertEqual(minNode.value, 'g');
    minNode = heap.extractMinimum();
    self.assertEqual(minNode.key, 8);
    self.assertEqual(minNode.value, 'h');
    minNode = heap.extractMinimum();
    self.assertEqual(minNode.key, 9);
    self.assertEqual(minNode.value, 'i');
    self.assertTrue(heap.isEmpty());
