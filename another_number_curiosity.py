#!/usr/bin/env python
"""What comes next and when does the pattern stop.

1 x 1 + 8 = 9
12 x 2 + 8 = 98
123 x 3 + 8 = 987
1234 x 4 + 8 = 9876
12345 x 5 + 8 = ?????
"""

def when_does_the_pattern_stop(start=1, stop=100, step=1, factor=8):
  """What comes next and when does the pattern stop."""
  pattern_stops = False
  for i in range(start, stop, step):
    number_a = int(''.join(str(n) for n in range(1, i+1)))
    number_b = i

    number_c = number_a * factor + number_b
    as_string = str(number_c)
    for i in range(len(as_string)-1):
      if int(as_string[i])-1 != int(as_string[i+1]):
        pattern_stops = True
        break
    if pattern_stops:
      break
    yield number_a, number_b, factor, number_c


def main():
  """Hooray for main!"""
  for num1, num2, factor, num3 in when_does_the_pattern_stop():
    print '{} x {} + {} = {}'.format(num1, num2, factor, num3 )


if __name__ == '__main__':
  main()
