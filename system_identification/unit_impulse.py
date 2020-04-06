import control
import matplotlib.pyplot as plt
import numpy as py

z = control.TransferFunction.z
H = (0.9474+0.2105*z**-1-0.7368*z**-2)/(1.0-1.579*z**-1+0.7895*z**-2)
control.bode_plot(H)

T, yout = control.impulse_response(H, range(0, 201))
plt.figure()
plt.plot(T, yout)

plt.show()
