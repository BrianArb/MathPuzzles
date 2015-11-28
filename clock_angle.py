#!/usr/bin/env python

import collections
import sys

HOURS = 12
MINUTES = 60
# Calculate the degrees each hand moves by each minute.
HOUR_HAND = float(360) / HOURS / MINUTES
MINUTE_HAND = float(360) / MINUTES


HourMinute = collections.namedtuple('HourMinute', 'hour minute')


class Error(Exception):
  """Custom Exception for module."""

def calculate_angle(hour, minute):
  """Calculate the angle between hour hand and minute hand.

  Args:
    hour: int
    minute: int
  Return:
    int, the minimum angle between the hour and minute hand.
  """
  if hour not in range(HOURS + 1) or minute not in range(MINUTES + 1):
    raise Error("Wrong input", hour, minute)

  hour = 0 if hour == HOURS else hour
  minute = 0 if minute == MINUTES else minute

  hour_angle = int(HOUR_HAND * (hour * MINUTES + minute))
  minute_angle = int(MINUTE_HAND * minute)

  angle = abs(hour_angle - minute_angle)

  return min(abs(360 - angle), angle)


def split_hour_minute(arg):
  time_value = [int(n) for n in arg.split(':') if n.isdigit()]
  if len(time_value) == 2:
    return HourMinute(hour=time_value[0], minute=time_value[1])
  else:
    return False


def tests():
  """Some simple tests."""
  assert HOUR_HAND == 0.5
  assert MINUTE_HAND == 6
  assert calculate_angle(9, 60) == 90
  assert calculate_angle(3, 30) == 75

  try:
    calculate_angle(24, 0)
  except Error:
    assert True
  else:
    assert False

  assert split_hour_minute('3:30').hour == 3
  assert split_hour_minute('3:30').minute == 30


def main(arg):
  time_value = split_hour_minute(arg)
  angle = calculate_angle(time_value.hour, time_value.minute)
  print (
      'The angle between the hour and minute '
      'hand for {0} is {1} degrees.'.format(arg, angle))


if __name__ == '__main__':
  tests()
  if len(sys.argv[1:]) >= 1:
    main(' '.join(sys.argv[1:]))
