#!/usr/bin/env python
"""
You are given a set of rectangular buildings in a city, and you should return
the skyline view of the city. Input is a sequence of tuples
(xleft,height,xright), each describing a building. The output is a sequence of
pairs (x,height) meaning that the height of skyline changed to height at the
given x coordinate.

For example, for the input:

[(1,11,5),(2,6,7),(3,13,9),(12,7,16),(14,3,25),(19,18,22),(23,13,29),(24,4,28)]
The output should be:

[(1,11),(3,13),(9,0),(12,7),(16,3),(19,18),(22,3),(23,13),(29,0)]
"""

def find_max_by_key(as_list, key=-1):
  """return the max value from a list of tuples.

  Args:
    as_list: list, A list of tuples.
    key: the index of the tuple to use as the key for the max value.
  Returns:
    the tuple with the max value.
  """
  return max(as_list, key=lambda x: x[key])


def add_to_skyline(as_list, xleft, height, xright):
  """Add height to our skyline.

  Args:
    as_list: list, our skyline.
    xleft: int, left position of building.
    height: int, heigth of building.
    xright: int, right of building.
  Returns:
    as_list
  """
  for index in range(xleft-1, xright-1):
    if as_list[index] < height:
      as_list[index] = height
  return as_list


def make_skyline(my_input):
  """Flatten the list of tuples into one list.
  Args:
    my_input: list, a list of tuples example: [(1,11,5), ...]
  Returns: list, our skyline.
  """
  as_list = [0] * find_max_by_key(my_input)[-1]
  for xleft, height, xright in my_input:
    as_list = add_to_skyline(as_list, xleft, height, xright)
  return as_list

def compress_list(as_list):
  """Compress the skyline list into the desired output.

  Args:
    as_list: our skyline as a list.
  Returns:
    list of tuples to draw the silhouette of our skyline.
  """
  compressed = []
  for index, value in enumerate(as_list, 1):
    if index == 1:
      compressed.append(tuple([index, value]))
    elif compressed[-1][-1] != value:
      compressed.append(tuple([index, value]))
  return compressed


def tests():
  my_input = [(1,11,5),(2,6,7),(3,13,9),(12,7,16),(14,3,25),(19,18,22),
              (23,13,29),(24,4,28)]
  assert find_max_by_key(my_input) == (23,13,29)

  expected_output = [(1,11),(3,13),(9,0),(12,7),(16,3),(19,18),(22,3),
                     (23,13),(29,0)]
  as_list = make_skyline(my_input)
  assert expected_output == compress_list(as_list)


if __name__ == '__main__':
  tests()
