#!/usr/bin/env python
"""Alphabet Spaghetti Puzzle.

Spaghetti is famous for the way it all gets tangled up on the plate. Those of
you who think they know their alphabet are bound to get all tangled up with this
puzzle too, unless you read it and think about it very carefully!

What letter of the alphabet is the one which comes eight letters before the
letter which comes five letters after the fourth appearance of the first letter
to occur four times in this sentence?

referance: http://www.mathsisfun.com/puzzles/alphabet-spaghetti.html
"""

import string

sentence = ('What letter of the alphabet is the one which comes eight letters '
            'before the letter which comes five letters after the fourth '
            'appearance of the first letter to occur four times in this '
            'sentence?')
characters = ''.join(c for c in sentence.lower() if c in string.ascii_lowercase)


def occur_atleast_four_times(characters):
  """Find the letters that appear four or more times.

  Args:
    characters: str, a string of letters from the sentence.
  Yields:
    a single letter from the string.
  """
  for c in set(characters):
    if characters.count(c) >= 4:
      yield c


def indexes_of_character(character):
  """Find the indexes in the string for a given character.

  Args:
    character: a single letter.
  Returns:
    list of index numbers.
  """
  return [i for i in range(len(characters))
          if characters[i] == character][:4]


def main():
  """Find the answer."""
  minimum = len(characters)
  index = None

  for c in occur_atleast_four_times(characters):
    indexes = indexes_of_character(c)
    if sum(indexes) < minimum:
      minimum = sum(indexes)
      index = indexes[-1]

  print sentence
  print 'The Answer is: ' + characters[index + 5 - 8]


if __name__ == '__main__':
  main()
