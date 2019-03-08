import math
import numpy as np
import random
import matplotlib.pyplot as plt

sample = 5
sigma = 1000
p_x = []
p_y = []
A = np.ndarray(shape=(0, 2))
B = np.ndarray(shape=(0, 1))

o_m = random.uniform(-20, 20)
o_c = random.uniform(-20, 20)

for i in xrange(sample):
  p_x.append( random.uniform(-1000, 1000) )
  p_y.append( random.gauss(o_m * p_x[-1] + o_c, random.uniform(0, sigma)) )
  A = np.append( A, np.array([1., p_x[-1], p_x[-1]*p_x[-1]]) )
  B = np.append( B, np.array(p_y[-1]) )
  
o_x = np.linspace(-1100,1100,100)
o_y = o_m*o_x+o_c


A = A.reshape([-1, 3])
B = B.reshape([-1, 1])
A_t = A.transpose();
A = np.linalg.inv(A_t.dot(A)).dot(A_t)

a = A.dot(B)
a0 = a[0]
a1 = a[1]
a2 = a[2]

x = np.linspace(-1100,1100,100)
y = a2*x*x+a1*x+a0


plt.subplot(111)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(p_x, p_y, c='g')
plt.plot(x, y)
plt.plot(o_x, o_y, 'r--')
plt.show()
