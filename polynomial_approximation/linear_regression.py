import random
import numpy as np
import matplotlib.pyplot as plt
from ..plant.linear_gaussian import LinearGaussian

resolution = 5
time = 5
sigma = 1.3
o_m = random.uniform(-20, 20)
o_c = random.uniform(-20, 20)
p_x, p_y = LinearGaussian(resolution, sigma, o_m, o_c).Offline(time)
  
  
a = 0.
b = 0.
mean_x = np.mean(p_x)
mean_y = np.mean(p_y)

for i in xrange(len(p_x)):
  a = (p_x[i] - mean_x)*(p_y[i] - mean_y) + a
  b = (p_x[i] - mean_x)*(p_x[i] - mean_x) + b

m = a / b
c = mean_y - m * mean_x


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
