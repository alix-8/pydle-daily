import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
from pydle import *

r = range
p = pydle
v = "purple"
for x in r(5):
    for y in r(5):
        p(x, y, "", "zinc")
        if y in r(0, 2):
            if 0 == x % 2: 
                p(x, y, "", "blue")
                p(0, 0, ">", "blue")
                p(2, 0, "<", "blue")
                p(4, 0, "🫀", "zinc")
        elif y in r(3, 5):
            if x != 3:
                p(x, 2, "", v)
            if x == 1 or x == 4:
                p(x, 3, "", v)
            if x in r(1, 4):
                p(x, 4, "", v)

show()