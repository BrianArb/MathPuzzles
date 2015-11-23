#!/usr/bin/python
"""
Number Theory: Reverse digits by multiplying by 4

Find two five-digit numbers such that
one is 4 times the other, and the digits
of the first are the reverse of the digits of the second.
In other words, ABCDE * 4 = EDCBA?
"""

def reversable_product(n):
  """Find two five-digit numbers.

  Args:
    n: int, the factor to multiply by.
  Returns:
    list the factor when reversed matches the product.
  """
  numbers = []
  for x in range(10000, 99999+1):
    a = x * n
    if str(a)[::-1] == str(x):
      numbers.append(x)
  return numbers


def main():
  """
  Find two five-digit numbers with factors from 2 to 99.
  """

  numbers = []
  for n in range(2, 100):
    ans = reversable_product(n)
    if ans:
      numbers.append(tuple([n, ans[0], n * ans[0]]))

  print numbers


if __name__ == '__main__':
  main()
