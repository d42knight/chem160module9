import math
a=3
if math.sqrt(a)**2 != a:
    print("WTH??")
from numpy import isclose
if isclose(math.sqrt(a)**2,a):
    print("Close enough!")
