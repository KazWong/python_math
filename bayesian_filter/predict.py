import numpy as np
import matplotlib.pyplot as plt

def simple_convo(belief, offset, kernel):
  for i in 

# belief = np.array([0.1]*10)
belief = np.array([.35, .1, .2, .3, 0, 0, 0, 0, 0, .05])

plt.subplot(121)
plt.title('Before Prediction')
plt.hist([0,1,2,3,4,5,6,7,8,9], bins=[-0.5,0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5], weights=belief, density=1, histtype='bar', rwidth=0.9)
plt.axis([-1, 10, 0, max(belief)*1.2])
plt.grid(True)

plt.subplot(122)
plt.title('After Prediction')
plt.hist([0,1,2,3,4,5,6,7,8,9], bins=[-0.5,0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5], weights=belief, density=1, histtype='bar', rwidth=0.9)
plt.axis([-1, 10, 0, max(belief)*1.2])
plt.grid(True)


plt.show()
