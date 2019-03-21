import random
import numpy as np
import matplotlib.pyplot as plt
from ..plant.linear_gaussian import LinearGaussian
from ..polynomial_approximation import linear_regression as LR
from ..polynomial_approximation import high_order_approximation as HA

resolution = 5
time = 5
sigma = 5

# generate linear point
o_m = random.uniform(-20, 20)
o_c = random.uniform(-20, 20)
p_x, p_y = LinearGaussian(sigma, o_m, o_c).Offline(time, resolution)
o_y = o_m*p_x+o_c

# linear regression
m0, c0 = LR.LeastSquare(p_x, p_y)
m1, c1 = LR.PseudoInverse(p_x, p_y)
a = HA.HighOrderApprox(p_x, p_y, 2)
y0 = m0*p_x+c0
y1 = m1*p_x+c1
y2 = a[2]*p_x*p_x+a[1]*p_x+a[0]


print("Origin\t\t", o_m, o_c)
print("Least Square\t", m0, c0)
print("Pseudo Inverse\t", m1, c1)
print("High Order\t", a[2], a[1], a[0])

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

plt.subplot(313)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(p_x, p_y, c='g')
plt.plot(p_x, o_y, 'r--')
plt.plot(p_x, y2)


plt.show()
