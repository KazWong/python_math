import random
import numpy as np
import matplotlib.pyplot as plt
from ..signal import Time
from ..signal.linear_gaussian import LinearGaussian
from ..polynomial_approximation import linear_regression as LR
from ..polynomial_approximation import high_order_approximation as HA

sigma = 1.3

# clock
sampling_rate = 1000.;end_time = 2.
clock = Time(sampling_rate)
clock.Offline(end_time)

# generate linear point
o_m = random.uniform(-20, 20)
o_c = random.uniform(-20, 20)
p_x = clock.timespace 
p_y = LinearGaussian(clock, sigma, o_m, o_c).Offline()
o_y = o_m*p_x+o_c

# linear regression
m0, c0 = LR.LeastSquare(p_x, p_y)
m1, c1 = LR.PseudoInverse(p_x, p_y)
a = HA.HighOrderApprox(p_x, p_y, 1)
y0 = m0*p_x+c0
y1 = m1*p_x+c1
y2 = a[1]*p_x+a[0]


print("Origin\t\t", o_m, o_c)
print("Least Square\t", m0, c0)
print("Pseudo Inverse\t", m1, c1)
print("High Order\t", a[1], a[0])

plt.subplot(311)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(p_x, p_y, c='g', s=0.5)
plt.plot(p_x, o_y, 'r--')
plt.plot(p_x, y0)

plt.subplot(312)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(p_x, p_y, c='g', s=0.5)
plt.plot(p_x, o_y, 'r--')
plt.plot(p_x, y1)

plt.subplot(313)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(p_x, p_y, c='g', s=0.5)
plt.plot(p_x, o_y, 'r--')
plt.plot(p_x, y2)


plt.show()
