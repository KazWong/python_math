#A universal velocity profile generation approach for high-speedmachining of small line segments with look-ahead

import matplotlib.pyplot as plt
import numpy as np
import math



#Eficient acceleration and deceleration techniquefor short distance movement in industrial robots and CNC machinetools.
#Arbitrary acceleration and deceleration formulationbased on coefficients

sample = 1000
t = np.linspace(0, 10, int(10*sample)+1)
t1 = np.linspace(0, 2, int(2*sample))
t2 = np.linspace(2, 10, int(8*sample)+1)
#a = [0.0, 2.220446049250313e-16, -1.1102230246251565e-16, 0.05000000000000003, -0.007500000000000002, 0.0003000000000000001]
#vel = np.ceil( (a[0] + a[1]*t + a[2]*t**2 + a[3]*t**3 + a[4]*t**4 + a[5]*t**5) * 10.0 ) / 10.0
#acc = np.ceil( (a[1] + 2*a[2]*t + 3*a[3]*t**2 + 4*a[4]*t**3 + 5*a[5]*t**4) * 10.0 ) / 10.0
a = [-1.0, 0.1]
vel = a[0] + a[1]*t1
acc = a[1]*(t*0.0+1)
vel = np.append(vel, (a[0] + a[1]*t1[-1])+(t2-t2))
#vel = np.ceil( (a[0] + a[1]*t) * 10.0 ) / 10.0
#acc = np.ceil( (a[1]*(t*0.0+1)) * 10.0 ) / 10.0

MAX_ACC = 0.38
MAX_DEC = 0.87
MAX_ACC_VEL = MAX_ACC / sample
MAX_DEC_VEL = MAX_DEC / sample
w = [a[0]]
dv = [0.0]
sel = [0]

for i in range(1, len(vel)):
	dv.append(vel[i] - w[i-1])
	
	if ( w[-1] >= 0.0 and dv[-1] > MAX_ACC_VEL ):
		w.append(w[-1] + MAX_ACC_VEL)
		sel.append(0)
	elif ( w[-1] >= 0.0 and dv[-1] < -MAX_DEC_VEL ):
		w.append(w[-1] - MAX_DEC_VEL)
		sel.append(1)
	elif ( w[-1] < 0.0 and dv[-1] > MAX_DEC_VEL ):
		w.append(w[-1] + MAX_DEC_VEL)
		sel.append(2)
	elif ( w[-1] < 0.0 and dv[-1] < -MAX_ACC_VEL ):
		w.append(w[-1] - MAX_ACC_VEL)
		sel.append(3)
	else:
		w.append(w[-1] + dv[-1])
		sel.append(4)



plt.subplot(211)
plt.xlabel('t')
plt.ylabel('vel')
plt.plot(t, vel)
plt.plot(t, w)
plt.subplot(212)
plt.xlabel('t')
plt.ylabel('if-case')
plt.plot(t, sel)
plt.show()
