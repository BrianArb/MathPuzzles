#!/usr/bin/python

def reversable_product(n):
  numbers = []
  for x in range(10000, 99999+1):
    a = x * n
    if str(a)[::-1] == str(x):
      numbers.append(x)
  return numbers


def main():
  numbers = []
  for n in range(2, 99):
    ans = reversable_product(n)
    if ans:
      numbers.append(tuple([n, ans[0], n * ans[0]]))

  print numbers


if __name__ == '__main__':
  main()
