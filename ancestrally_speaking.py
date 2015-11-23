#!/usr/bin/env python
"""Ancestrally Speaking Puzzle

Hungry Horace was looking through the family photograph album, which has a photo
of each of his parent, each of his grandparents, all the way up to each of his
great-great-great-grandparents.

How many photos is that?

referance: http://www.mathsisfun.com/puzzles/ancestrally-speaking.html
"""

print __doc__
print 'Answer: {0}'.format(sum(2 ** i for i in range(1, 6)))
