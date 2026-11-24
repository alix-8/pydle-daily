import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
from pydle import *

r = range
p = pydle
g = "gray"
z = "zinc"
w = "white"


for x in r(5):
    for y in r(5):
        p(x, y, "", g)

for x in r(1, 4):
    for y in r(3, 5):
        p(x, y, "", z)
    for y in r(1, 3):
        p(x, y, "", w)

for x in r(1, 4, 2):
    p(x, 1, "🥟", w)

for x in range(0, 5, 4):
    for y in range(2, 4):
        pydle (x, y, "", z)

for x in range(2, 3):
    pydle (x, 0, "🥟", w)

show()