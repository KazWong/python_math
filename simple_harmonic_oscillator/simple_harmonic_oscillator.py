#!/usr/bin/env python

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dy/dt
def model(x,t):
    k = 0.3
    dxdt = -k * x
    return dxdt

# initial condition
x0 = 5

# time points
t = np.linspace(0,20)

# solve ODE
x = odeint(model,x0,t)

# plot results
plt.plot(t,x)
plt.xlabel('time')
plt.ylabel('x(t)')
plt.show()
  
