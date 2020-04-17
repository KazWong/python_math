import math
import numpy as np
#from . import Dynsys
import matplotlib.pyplot as plt

sample = 100000
t = np.linspace(0, 10, sample+1)
a = [0.0, 2.220446049250313e-16, -1.1102230246251565e-16, 0.05000000000000003, -0.007500000000000002, 0.0003000000000000001]
v = a[0] + a[1]*t + a[2]*t**2 + a[3]*t**3 + a[4]*t**4 + a[5]*t**5
acc = a[1] + 2*a[2]*t + 3*a[3]*t**2 + 4*a[4]*t**3 + 5*a[5]*t**4


so = np.pi*0.1565/150.
p = []
s = 0.0
dt = t[1]
fix_pos = [0]
fix_pos_t = [0.0]
v_re = [0.0]
a_re = [0.0]
t_a = [0.0]
count = 0

for i in range(0, len(t)):
	ds = v[i]*dt
	if ((s + ds) == so):
		p = np.append(p, [t[i]])
		s = 0.0
		ds = 0.0
		count += 1
	elif ((s + ds) > so):
		p = np.append(p, [t[i-1] + (so - s)/ds * dt])
		s = (ds + s) - so
		ds = 0.0
		count += 1
	s = s + ds
#fix time
Hz = 2000000.#1000000.
clock = np.linspace(0, 10, int(10*Hz + 1))
j = 0
count = 0
for i in range(0, len(p)):
	while (clock[j] < p[i]):
		j += 1
		count += 1
	v_re = np.append(v_re, [ so / (count*(1./Hz)) ])
	fix_pos_t = np.append(fix_pos_t, [clock[j]])
	k = 2
	while ((fix_pos_t[-1] - fix_pos_t[-k]) < 0.1):
		k += 1
	a_re = np.append(a_re, [(v_re[-1] - v_re[-k]) / (fix_pos_t[-1] - fix_pos_t[-k])])
	count = 0

l = np.ones(len(p))

#plt.figure()
#plt.stem(p, l, '-', use_line_collection=True)

#plt.figure()
#plt.stem(fix_pos_t, fix_pos_t, '-', use_line_collection=True)

plt.figure()

#plt.stem(fix_pos_t, v_re, '-', use_line_collection=True)
line_v, = plt.plot(t, v, label='v')
line_v_re, = plt.plot(fix_pos_t, v_re, label='v_re')
line_a_re, = plt.plot(fix_pos_t, a_re, label='a_re')
line_a, = plt.plot(t, acc, label='a')
plt.legend(handles=[line_v, line_v_re, line_a_re, line_a])
plt.title("Speed-out Simulation Fix time, sampling clock=2MHz") 

plt.show()
