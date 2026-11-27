import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
from pydle import *


r = range
p = pydle

for y in r(5):
    for x in r(1, 4):
        if y == 0 or y == 4:
            p(x, y, "", "red")
    for x in r(0, 5):
        if  x != 2:
            if y == 1 or y == 3:
                p(x, y, "🤍", "red")

show()