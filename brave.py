#!/usr/bin/env python
"""
This square has eleven letters missing, which you have to replace:

      +---+---+---+---+---+
      | B | R | A | V | E |
      +---+---+---+---+---+
      |   | E | B | R |   |
      +---+---+---+---+---+
      |   |   | V |   | B |
      +---+---+---+---+---+
      |   | B | R |   |   |
      +---+---+---+---+---+
      |   |   | E | B |   |
      +---+---+---+---+---+

Every row, column AND the main diagonals contain all the letters
in the word "BRAVE".

referance: http://www.mathsisfun.com/puzzles/a-brave-puzzle.html
"""

import itertools
import sys
import time

WORD = 'BRAVE'
LENGHT = len(WORD)
DIGITS = set(range(1, LENGHT+1))
DIGIT_TO_CHAR = dict(zip(DIGITS, WORD))
CHAR_TO_DIGIT = dict(zip(WORD, DIGITS))
TEMPLATE = (
    '+---+---+---+---+---+\n'
    '| {0} | {1} | {2} | {3} | {4} |\n'
    '+---+---+---+---+---+\n'
    '| {5} | {6} | {7} | {8} | {9} |\n'
    '+---+---+---+---+---+\n'
    '| {10} | {11} | {12} | {13} | {14} |\n'
    '+---+---+---+---+---+\n'
    '| {15} | {16} | {17} | {18} | {19} |\n'
    '+---+---+---+---+---+\n'
    '| {20} | {21} | {22} | {23} | {24} |\n'
    '+---+---+---+---+---+\n')


def group_by_rows(puzzle):
  """Break the puzzle list into rows.

  Args:
    puzzle: puzzle as list.
  Returns:
    puzzle broken into a list of list to represent the rows.
  """
  return [puzzle[i*LENGHT:i*LENGHT+LENGHT] for i in range(LENGHT)]

def group_by_columns(puzzle):
  """Break the puzzle list into columns.

  Args:
    puzzle: puzzle as list.
  Returns:
    puzzle broken into a list of list to represent the columns.
  """
  order_by_columns = [puzzle[c+i]
                      for i in range(LENGHT)
                      for c in range(0, LENGHT * LENGHT, LENGHT)]
  return group_by_rows(order_by_columns)


def group_by_main_diagonals(puzzle):
  """Break the puzzle list into rows.

  Args:
    puzzle: puzzle as list.
  Returns:
    puzzle broken into a list of list to represent the main diagonals.
  """
  indexes = range(LENGHT)
  rows = group_by_rows(puzzle)
  main_diagonal_a = [rows[x][y] for x, y in zip(indexes, indexes)]
  main_diagonal_b = [rows[x][y] for x, y in zip(indexes, indexes[::-1])]
  return main_diagonal_a, main_diagonal_b


def check_puzzle(grid):
  """Check the puzzle for uniqueness.

  Args:
    grid: the puzzle as list of lists.
  Returns:
    boolean: False if any row, column or diagonal is not unique excluding
    zeros AKA missing pieces yet to be filled in.
  """
  assert isinstance(grid, list)
  assert all(isinstance(row, list) for row in grid)
  assert len(grid) == LENGHT
  assert all(len(row) == LENGHT for row in grid)

  puzzle = [digit for row in grid for digit in row]
  puzzle_rows = grid
  puzzle_columns = group_by_columns(puzzle)
  puzzle_diagonals = group_by_main_diagonals(puzzle)

  for grid in puzzle_rows, puzzle_columns, puzzle_diagonals:
    try:
      assert all(digit in range(0, LENGHT+1)
                 for row in grid
                 for digit in row)
      assert all(row.count(digit) == 1
                 for row in grid
                 for digit in row
                 if digit != 0)
    except AssertionError:
      return False
  return True


def fill_in_the_blanks(row):
  """Fill in the missing pieces row by row.

  Args:
    row: list, a row from the puzzle.
  Yeilds:
    list, A row from the puzzle with the missing pieces filled in.
  """
  indexes = [i for i, d in enumerate(row) if d == 0]
  missing_digits = DIGITS - set(row)
  for guesses in itertools.permutations(missing_digits):
    row_copy = list(row)
    for index, digit in zip(indexes, guesses):
      if digit in columns[index]:
        break
      row_copy[index] = digit
    if 0 in row_copy:
      continue
    yield row_copy


def solve_puzzle(puzzle):
  """Find the solution to a given puzzle.

  Args:
    puzzle: list, the puzzle as a list.
  Returns:
    The solved puzzle as a list of lists or Flase if it is a invalid puzzle.
  """
  global columns
  result = check_puzzle(puzzle)
  if not result:
    return result

  columns = group_by_columns([digit for row in puzzle for digit in row])
  return next([A, B, C, D, E]
              for A in fill_in_the_blanks(puzzle[0])
              if check_puzzle([A] + puzzle[1:])
              for B in fill_in_the_blanks(puzzle[1])
              if check_puzzle([A, B] + puzzle[2:])
              for C in fill_in_the_blanks(puzzle[2])
              if check_puzzle([A, B, C] + puzzle[3:])
              for D in fill_in_the_blanks(puzzle[3])
              if check_puzzle([A, B, C, D] + puzzle[4:])
              for E in fill_in_the_blanks(puzzle[4])
              if check_puzzle([A, B, C, D, E] + puzzle[5:])
              )


def parse_raw_puzzle(raw):
  """Make the input string in to a list.

  Args:
    raw: str, The input puzzle to solve as a string.
  Returns:
    the puzzle as a list.
  """
  return [[CHAR_TO_DIGIT.get(c, 0) for c in raw][i*LENGHT:i*LENGHT+LENGHT]
      for i in range(LENGHT)]


def main(arg):
  puzzle = parse_raw_puzzle(arg)
  t1 = time.time()
  result = solve_puzzle(puzzle)
  t2 = time.time()
  if result:
    print 'solved in {:f} : "{}"'.format(t2 - t1, arg)
    answer = [DIGIT_TO_CHAR[item] for each in result for item in each]
    print TEMPLATE.format(*answer)
  else:
    print 'solve_puzzle returned: {}'.format(result)


def tests():
  raw = 'BRAVE EBR   V B BR    EB '
  puzzle = parse_raw_puzzle(raw)
  assert puzzle == [[1, 2, 3, 4, 5], [0, 5, 1, 2, 0], [0, 0, 4, 0, 1],
                    [0, 1, 2, 0, 0], [0, 0, 5, 1, 0]]
  result = solve_puzzle(puzzle)
  assert result == [[1, 2, 3, 4, 5], [4, 5, 1, 2, 3], [2, 3, 4, 5, 1],
                    [5, 1, 2, 3, 4], [3, 4, 5, 1, 2]]
  answer = ''.join([DIGIT_TO_CHAR[item] for each in result for item in each])
  assert answer == 'BRAVEVEBRARAVEBEBRAVAVEBR'


if __name__ == '__main__':
  tests()
  raw =  ''.join(sys.argv[1:])
  if len(raw) == 25:
    main(raw)
  else:
    print 'expected a string of 25 characters.'
    print 'example: {} "BRAVE EBR   V B BR    EB "'.format(sys.argv[0])
