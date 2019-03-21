import random
import numpy as np
import matplotlib.pyplot as plt
from ..plant.linear_gaussian import LinearGaussian
from ..polynomial_approximation import linear_regression as LR

resolution = 5
time = 5
sigma = 1.3

o_m = random.uniform(-20, 20)
o_c = random.uniform(-20, 20)

p_x, p_y = LinearGaussian(sigma, o_m, o_c).Offline(time, resolution)

m0, c0 = LR.LeastSquare(p_x, p_y)
m1, c1 = LR.PseudoInverse(p_x, p_y)


o_y = o_m*p_x+o_c
y0 = m0*p_x+c0
y1 = m1*p_x+c1

print(o_m, o_c)
print(m0, c0)
print(m1, c1)

plt.subplot(211)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(p_x, p_y, c='g')
plt.plot(p_x, o_y, 'r--')
plt.plot(p_x, y0)

plt.subplot(212)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(p_x, p_y, c='g')
plt.plot(p_x, o_y, 'r--')
plt.plot(p_x, y1)
plt.show()
