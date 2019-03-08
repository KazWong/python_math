import math
import numpy as np
import random
import matplotlib.pyplot as plt

sample = 100
order = 20
sigma = 1000000

if (not sample > order):
  order = sample - 1
  
p_x = []
p_y = []
A = np.ndarray(shape=(0, order))
B = np.ndarray(shape=(0, 1))

o_m = random.uniform(-20, 20)
o_c = random.uniform(-20, 20)

for i in xrange(sample):
  p_x.append( random.uniform(-1000, 1000) )
  p_y.append( random.gauss(o_m * p_x[-1] + o_c, random.uniform(0, sigma)) )
  
  order_array = [1.]
  for j in xrange(order):
    order_array.append( math.pow(p_x[-1], j+1) )
  A = np.append( A, np.array(order_array) )
  B = np.append( B, np.array(p_y[-1]) )
  
o_x = np.linspace(-1100,1100,100)
o_y = o_m*o_x+o_c


A = A.reshape([-1, order+1])
B = B.reshape([-1, 1])
A_t = A.transpose();
A = np.linalg.inv(A_t.dot(A)).dot(A_t)
a = A.dot(B)


x = np.linspace(-800,800,100)
y = []
for i in xrange(len(x)):
  tmp = 0.
  for j in xrange(order + 1):
    tmp = a[j, 0] * math.pow(x[i], j) + tmp
  y.append(tmp)

for i in xrange(order + 1):
  print "a" + str(i) + " =", a[i, 0]

plt.subplot(111)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(p_x, p_y, c='g')
plt.plot(x, y)
plt.plot(o_x, o_y, 'r--')
plt.show()
