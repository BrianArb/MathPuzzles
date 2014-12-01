#!/usr/bin/env python
"""Given a number n, is n divisible by each of its digits?

For example...
128 will pass this test, it is divisible by 1,2, and 8. Any numbers
with a zero automatically disqualify the number.
"""

def divides_self(num):
  """Is the number divisible by each of its digits.

  Args:
    num: int, the number to test.
  Returns:
    boolean True is the number is divisable by all of it's digits
    and False if not.
  """
  as_str = str(num)

  if '0' in as_str:
    return False

  return all([num % int(x) == 0 for x in as_str])


def tests():
  """assertion tests"""
  assert divides_self(128)
  assert not(divides_self(108))
  assert not(divides_self(53))
  print 'All tests pass'


if __name__ == '__main__':
  tests()
