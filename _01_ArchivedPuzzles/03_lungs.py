import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from pydle import *


r = range
p = pydle
for x in r(5):
    for y in r(5):
        p(x, y, "", "gray")
for y in r(1, 5):
    for x in r(0, 5, 4):
        if y > 1:
            p(x, y, "", "pink")
            p(4-x, y, "", "pink")
    for x in r(1, 4, 2):
        if 0 < y < 4:
            p(x, y, "", "pink")
            p(4-x, y, "", "pink")
for x in r(5):
    for y in r(5):
        if y < 3 and 0 < x < 4:
                    p(2, y, "", "yellow")
                    p(x, 2, "", "yellow")

show()