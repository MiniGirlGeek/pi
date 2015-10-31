#!/usr/bin/python3
"""
pi.py - an algorithm to calculate Pi
The MIT License (MIT)

Copyright (c) 2015 Joe Glancy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from mpmath import *
# use the mpmath's real floats:
a = mpf(1)
x = mpf(1)
b = mpf(1 / sqrt(2))
c = mpf(1 / 4)

# output the result to this file
f = open("pi.txt", "w")

# set the decimal precision to 10000 (so ~10000 decimal places). the size of
# the resulting text file should be this + 2.
mp.dps=10000

# the more this loop loops, the more precise the result will be (up to a point
# which depends on the decimal precision)
for z in range(0, 10000):
    y = a
    a = (a + b) / 2
    b = sqrt(b * y)
    c = c - x * ((a - y) *  (a - y))
    x = x * 2

f.write(str(((a + b) * (a + b)) / (4 * c)) + "\n")
f.close()

