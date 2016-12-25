# py-data-structures <http://github.com/gwtw/py-data-structures>
# Copyright 2016 Daniel Imms <http://www.growingwiththeweb.com>
# Released under the MIT license <http://github.com/gwtw/py-data-structures/blob/master/LICENSE>

def default_compare(a, b):
  if a < b:
    return -1
  elif a > b:
    return 1
  return 0
