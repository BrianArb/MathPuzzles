#!/usr/bin/env python
"""
According to the traditional song, on the first day of Christmas (25th
December), my true love sent to me:

. A partridge in a pear tree

On the second day of Christmas (26th December), my true love sent to me THREE
presents:

. Two turtle doves
. A partridge in a pear tree

On the third day of Christmas (27th December and so on) my true love sent to me
SIX presents:

. Three French hens
. Two turtle doves
. A partridge in a pear tree

This carries on until the the twelfth day of Christmas, when my true love
sends me:

Twelve drummers drumming
Eleven pipers piping
Ten lords a-leaping
Nine ladies dancing
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five gold rings
Four calling birds
Three French hens
Two turtle doves
A partridge in a pear tree

After the twelve days of Christmas are over, how many presents has my true love
sent me altogether?
"""

template = ("After the twelve days of Christmas are over, "
            "my true love sent {0} presents altogether.")

total = sum(x * y for x, y in zip(range(1, 12+1), range(12, 0, -1)))
print template.format(total)
