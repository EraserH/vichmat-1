import math
from scipy import integrate


def f(x, y):
    return y**2


result, err = integrate.dblquad(f, -1, 2, lambda y: y**2, lambda y: y+2)
print(result)