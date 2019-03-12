import numpy as np
import random
import matplotlib.pyplot as plt
from ..plant.linear_gaussian import LinearGaussian

resolution = 5
time = 5
sigma = 2
o_m = random.uniform(-20, 20)
o_c = random.uniform(-20, 20)
p_x, p_y = LinearGaussian(resolution, sigma, o_m, o_c).Offline(time)
A = np.ndarray(shape=(0, 2))
B = np.ndarray(shape=(0, 1))


for i in xrange(len(p_x)):
  A = np.append( A, np.array([1., p_x[i]]) )
  B = np.append( B, np.array(p_y[i]) )

A = A.reshape([-1, 2])
B = B.reshape([-1, 1])
A_t = A.transpose();
A = np.linalg.inv(A_t.dot(A)).dot(A_t)

a = A.dot(B)
a0 = a[0]
a1 = a[1]


y = a1*p_x+a0
o_y = o_m*p_x+o_c

print o_m, o_c
print a1, a0

plt.subplot(111)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(p_x, p_y, c='g')
plt.plot(p_x, y)
plt.plot(p_x, o_y, 'r--')
plt.show()
