import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
from pydle import *


r = range
p = pydle

for x in r(5):
    for y in r(5):
        p(x, y, "", "gray")
        if y < 3:
            p(x, y, "", "white")
            p(2, 1, "", "maroon")
            p(2, 2, "", "gray")
            if 0 < x < 4:
                p(x, 0, "", "zinc")
    for x in r(1, 4, 2):
        p(x, 2, "", "orange")
    for x in r(0, 5, 4):
        p(x, 3, "", "orange")

show()