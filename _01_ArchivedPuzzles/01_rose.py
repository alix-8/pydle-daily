import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from pydle import *


r = range
d = "red"
m = "maroon"
p = pydle



for x in r(5):
    for y in r(5):
        p(x, y, "", "white")
    for y in r(0,3):
        p(x, y, "", d)
        if 2 < x < 5:
            p(x, y, "", "maroon")
        if y == 0:
            if 0 == x % 2:
                p(x, y, "", "white")


for  x in r(1, 4):
    for y in r(3, 5):
        p(x, y, "", "green")

for y in r(4, 5):
    for x in r(1, 4, 2):
        p(x, y, "", "white")


show()