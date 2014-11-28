#!/usr/bin/env python
"""Make a list of three numbers using the digits 1-9.

Using each of the nine digits 1-9 make a list of the integers where the
second item in the list is twice the first item and the third item is
three times the first.

Example:
192, 384, 576 is ok...
384 = 192 * 2
576 = 192 * 3

123, 456, 789 is not...
456 != 123 * 2
789 != 123 * 3
"""

import itertools


def make_sets():
  """Make a list of three numbers using the digits 1-9.

  Using each of the nine digits 1-9 make a list of the integers where the
  second item in the list is twice the first item and the third item is
  three times the first.

  Yields:
    list of three integers.
  """
  digits = set('123456789')

  for each in itertools.permutations(digits, 3):
    num = ''.join(each)
    nums = [int(num) * (i+1) for i in range(3)]
    check = {c
             for each in nums
             if len(str(each)) == 3
             for c in str(each)
            }
    if check == digits:
      yield nums


def main():
  """Print out the list of itegers."""
  for once, twice, thrice in make_sets():
    print '{0}, {1}, {2}'.format(once, twice, thrice)


if __name__ == '__main__':
  main()
