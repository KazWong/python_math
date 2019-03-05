import math
import numpy as np
import random
import matplotlib.pyplot as plt

sample = 200
sigma = 100000
a = 0.
b = 0.
p_x = []
p_y = []

o_m = random.uniform(-20, 20)
o_c = random.uniform(-20, 20)

for i in xrange(sample):
  p_x.append( random.uniform(-1000, 1000) )
  p_y.append( random.gauss(o_m * p_x[-1] + o_c, random.uniform(0, sigma)) )

mean_x = np.mean(p_x)
mean_y = np.mean(p_y)

for i in xrange(sample):
  a = (p_x[i] - mean_x)*(p_y[i] - mean_y) + a
  b = (p_x[i] - mean_x)*(p_x[i] - mean_x) + b

m = a / b
c = mean_y - m * mean_x

x = np.linspace(-1100,1100,100)
y = m*x+c

o_x = np.linspace(-1100,1100,100)
o_y = o_m*o_x+o_c


plt.subplot(111)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(p_x, p_y, c='g')
plt.plot(x, y)
plt.plot(o_x, o_y, 'r--')
plt.show()
