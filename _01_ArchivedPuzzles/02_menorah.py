import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from pydle import *

r = range
p = pydle

for x in r(5):
    for y in r(0, 3):
        if x % 2 == 0:
            p(x, y, "", "orange")
            p(x, 1, "^", "")
            p(x, 2, "", "yellow")
    for y in r(3, 4):
        p(x, 3, "", "yellow")
p(2, 4, "", "yellow")

show()