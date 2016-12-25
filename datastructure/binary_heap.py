# py-sorting <http://github.com/gwtw/py-sorting>
# Copyright 2016 Daniel Imms <http://www.growingwiththeweb.com>
# Released under the MIT license <http://github.com/gwtw/py-data-structures/blob/master/LICENSE>

import math
from common.helpers import default_compare

class BinaryHeap:
  def __init__(self, compare=default_compare):
    self.list = []
    self.compare = compare

  def buildHeap(self, keys, values=None):
    if values is not None and len(values) != len(keys):
      raise ValueError('Key array must be the same length as value array')

    nodeArray = []

    for i in range(0, len(keys)):
      nodeArray.append(Node(keys[i], None if values is None else values[i]))

    self.buildHeapFromNodeArray(nodeArray)

  def clear(self):
    self.list = []

  def extractMinimum(self):
    if len(self.list) == 0:
      return None

    if len(self.list) == 1:
      return self.list.pop()

    min = self.list[0]
    self.list[0] = self.list.pop()
    self.heapify(0)
    return min

  def findMinimum(self):
    return None if self.isEmpty() else self.list[0]

  def insert(self, key, value=None):
    i = len(self.list)
    node = Node(key, value)
    self.list.append(node)
    parent = self.getParent(i)
    while parent is not None and self.compare(self.list[i].key, self.list[parent].key) < 0:
      self.swap(self.list, i, parent)
      i = parent
      parent = self.getParent(i)
    return node

  def isEmpty(self):
    return len(self.list) == 0

  def size(self):
    return len(self.list)

  def union(self, otherHeap):
    array = self.list + otherHeap.list
    self.buildHeapFromNodeArray(array)

  def heapify(self, i):
    l = self.getLeft(i)
    r = self.getRight(i)
    smallest = i
    if l < len(self.list) and \
        self.compare(self.list[l].key, self.list[i].key) < 0:
      smallest = l
    if r < len(self.list) and \
        self.compare(self.list[r].key, self.list[smallest].key) < 0:
      smallest = r
    if smallest != i:
      self.swap(self.list, i, smallest)
      self.heapify(smallest)

  def buildHeapFromNodeArray(self, nodeArray):
    self.list = nodeArray
    for i in range(math.floor(len(self.list) / 2), -1, -1):
      self.heapify(i)

  def swap(self, array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp

  def getParent(self, i):
    if i == 0:
      return None
    return math.floor((i - 1) / 2)

  def getLeft(self, i):
    return 2 * i + 1

  def getRight(self, i):
    return 2 * i + 2

class Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value
