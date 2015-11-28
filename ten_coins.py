#!/usr/bin/env python

import random

coins = [random.choice([0,1]) for _ in range(1000)]

random.shuffle(coins)

a, b = coins[:len(coins)/2], coins[len(coins)/2:]

print {id(n) for n in coins}

print len(coins)

a = [abs(x - 1) for x in a]

print a.count(1)
print b.count(1)
