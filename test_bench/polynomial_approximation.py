import random
import numpy as np
import matplotlib.pyplot as plt
from ..plant.linear_gaussian import LinearGaussian
from ..polynomial_approximation import linear_regression as LR
from ..polynomial_approximation import high_order_approximation as HA

resolution = 5
time = 5
sigma = 1.3

# generate linear point
o_m = random.uniform(-20, 20)
o_c = random.uniform(-20, 20)
p_x, p_y = LinearGaussian(sigma, o_m, o_c).Offline(time, resolution)
o_y = o_m*p_x+o_c

# linear regression
m0, c0 = LR.LeastSquare(p_x, p_y)
m1, c1 = LR.PseudoInverse(p_x, p_y)
m2, c2 = HA.HighOrderApprox(p_x, p_y, 1)
y0 = m0*p_x+c0
y1 = m1*p_x+c1
y2 = m2*p_x+c2


print(o_m, o_c)
print(m0, c0)
print(m1, c1)
print(m2, c2)

plt.subplot(311)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(p_x, p_y, c='g')
plt.plot(p_x, o_y, 'r--')
plt.plot(p_x, y0)

plt.subplot(312)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(p_x, p_y, c='g')
plt.plot(p_x, o_y, 'r--')
plt.plot(p_x, y1)
plt.show()

plt.subplot(313)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(p_x, p_y, c='g')
plt.plot(p_x, o_y, 'r--')
plt.plot(p_x, y3)
plt.show()
