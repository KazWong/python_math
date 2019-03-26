import numpy as np
import matplotlib.pyplot as plt
from ..signal.pwm import PWM


x, y = PWM(24, 0, 6, 3).Offline(18, 100)

plt.subplot(111)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(x, y, c='g')
plt.show()
