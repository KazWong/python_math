import numpy as np
import matplotlib.pyplot as plt

def simple_convo(pdf, offset, kernel):
  N = len(pdf)
  kN = len(kernel)
  width = int((kN - 1) / 2)

  prior = np.zeros(N)
  for i in range(N):
    for k in range (kN):
      index = (i + (width-k) - offset) % N
      prior[i] += pdf[index] * kernel[k]
  return prior

belief = np.array([.05, .05, .05, .05, .55, .05, .05, .05, .05, .05])
prior = simple_convo(belief, offset=3, kernel=[.05, .05, .6, .2, .1])

plt.subplot(121)
plt.title('Before Prediction')
plt.hist([0,1,2,3,4,5,6,7,8,9], bins=[-0.5,0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5], weights=belief, density=1, histtype='bar', rwidth=0.9)
plt.axis([-1, 10, 0, max(belief)*1.2])
plt.grid(True)

plt.subplot(122)
plt.title('After Prediction')
plt.hist([0,1,2,3,4,5,6,7,8,9], bins=[-0.5,0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5], weights=prior, density=1, histtype='bar', rwidth=0.9)
plt.axis([-1, 10, 0, max(belief)*1.2])
plt.grid(True)


plt.show()

# Kalman-and-Bayesian-Filters-in-Python
# https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python
