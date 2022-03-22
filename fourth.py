import math
from scipy import integrate


def f(x):
    return 1/(1 + 2 * math.sin(x)**2)


result, err = integrate.quad(f, 0, math.pi/4)
print(result)
