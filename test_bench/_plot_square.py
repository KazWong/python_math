import numpy as np
import matplotlib.pyplot as plt
from ..signal.square import Square


x, y = Square(0., 40, 1., 1.).Offline(5, 100)

plt.subplot(111)
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y, 'g')
plt.show()
