#!/usr/bin/env python
"""
1 1 2 3 5 8 13
"""
from decimal import Decimal

import math


def term_in_fibonacci(n):
  a = 0
  b = 1
  for _ in range(1, n):
    a, b = b, a + b
  return b


def binet(n):
  sqrt_five = Decimal(5 ** 0.5)
  a = ((1 + sqrt_five) / 2) ** n
  b = ((1 - sqrt_five) / 2) ** n

  fibonacci_number = (1 / sqrt_five) * (a - b)

  return Decimal.to_integral_value(fibonacci_number)


def tests():
  fibonacci_numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34]

  for n in range(len(fibonacci_numbers)):
    assert term_in_fibonacci(n+1) == fibonacci_numbers[n]

  for n in range(len(fibonacci_numbers)):
    assert binet(n+1) == fibonacci_numbers[n]


if __name__ == '__main__':
  tests()
