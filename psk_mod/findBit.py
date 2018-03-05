# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 08:24:37 2018

@author: Nick Butts
"""

import numpy as np
import matplotlib.pyplot as plt


def findPreamble(preamble, x):
    for i in range(0, len(x) - len(preamble)):
        check = 0
        for j in range(0, len(preamble)):
            check += x[i + j] - preamble[j]
        if (check == 0):
            print("Found a preamble at {0}".format(i))
            x = x[i + len(preamble)::]
            break
    return check == 0, x

def shiftBits(x):
    for i in range (0, len(x) - 1):
        a = x[i]
        a = a << 1
        if x[i + 1] & 0x80:
            a = a | 1

        x[i] = (a & 0xFF)
    return x

f = open('test.bits', 'rb')
x = f.read();
f.close()

preamble = [0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08]
searchForBit = True
x = np.frombuffer(x, dtype='uint8')
x = x.astype('int')
print(x)

while searchForBit:

    x = shiftBits(x)
    print(x)
    found, y = findPreamble(preamble, x)
    if found:
        searchForBit = False
        y = y.astype('uint8')
        f = open('test.bits', 'wb')
        f.write(y)
        f.close()

