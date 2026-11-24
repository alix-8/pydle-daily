import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
from pydle import *


r = range
p = pydle
for y in r(5):
    for x in r(5):
        p(x, y, "", "zinc")
    if x == 4:
        p(x, y, "", "gray")
for x in r(1, 4):
    for y in r(1, 4):
        if y == 1:
            p(x, y, "", "yellow")
            if x <= 2:
                p(x, 1, "🧊", "yellow")
        elif y == 2:
            p(x, y, "", "orange")
        else:
            p(x, y, "", "brown")


show()