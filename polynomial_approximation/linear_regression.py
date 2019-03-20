import random
import numpy as np
import matplotlib.pyplot as plt
from ..plant.linear_gaussian import LinearGaussian

resolution = 5
time = 5
sigma = 1.3
o_m = random.uniform(-20, 20)
o_c = random.uniform(-20, 20)
p_x, p_y = LinearGaussian(sigma, o_m, o_c).Offline(time, resolution)

cov_m = np.cov(p_x, p_y, bias=1)
a = cov_m[0][1] * len(p_x)
b = cov_m[0][0] * len(p_x)

m = a / b
c = np.mean(p_y) - m * np.mean(p_x)


o_y = o_m*p_x+o_c
y = m*p_x+c

print o_m, o_c
print m, c

plt.subplot(111)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(p_x, p_y, c='g')
plt.plot(p_x, y)
plt.plot(p_x, o_y, 'r--')
plt.show()
