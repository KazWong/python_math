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
p = [0.0]
s = 0.0
last_t = 0.0
count = 0
start_t = 0.0
fix_time = [0]
fix_time_t = [0.0]
v_re = [0.0]
a_re = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

max_count = 200
update_period = 0.1

for i in range(0, len(t)):
	s = v[i]*(t[i] - last_t) + s
	last_t = t[i]
	if (s >= so):
		p = np.append(p, [t[i]])
		s = s - so
		count += 1
	if ((t[i] - start_t) >= update_period):
		fix_time = np.append(fix_time, [count])
		fix_time_t = np.append(fix_time_t, [t[i]])
		v_re = np.append(v_re, [6.5554566704907 * (float(count) / max_count)])
		print(count, v_re[-1], v[i], t[i] - start_t)
		if (len(v_re) > 12):
			#print(v_re[-1] - v_re[-2], fix_time_t[-1] - fix_time_t[-2])
			#a_re = np.append(a_re, [ (v_re[-1] - v_re[-2]) / (fix_time_t[-1] - fix_time_t[-2])])
			#a_re = np.append(a_re, [ ( ((v_re[-1] - v_re[-2]) / (fix_time_t[-1] - fix_time_t[-2]) + (v_re[-2] - v_re[-3]) / (fix_time_t[-2] - fix_time_t[-3]) + (v_re[-3] - v_re[-4]) / (fix_time_t[-3] - fix_time_t[-4]) )/3.0 ) ])
			a_re = np.append(a_re, [ ( ((v_re[-1] - v_re[-2]) / (fix_time_t[-1] - fix_time_t[-2]) + 
			                             (v_re[-2] - v_re[-3]) / (fix_time_t[-2] - fix_time_t[-3]) +
			                             (v_re[-3] - v_re[-4]) / (fix_time_t[-3] - fix_time_t[-4]) +
			                             (v_re[-4] - v_re[-5]) / (fix_time_t[-4] - fix_time_t[-5]) +
			                             (v_re[-5] - v_re[-6]) / (fix_time_t[-5] - fix_time_t[-6]) +
			                             (v_re[-6] - v_re[-7]) / (fix_time_t[-6] - fix_time_t[-7]) +
			                             (v_re[-7] - v_re[-8]) / (fix_time_t[-7] - fix_time_t[-8]) +
			                             (v_re[-8] - v_re[-9]) / (fix_time_t[-8] - fix_time_t[-9]) +
			                             (v_re[-9] - v_re[-10]) / (fix_time_t[-9] - fix_time_t[-10]) +
			                             (v_re[-10] - v_re[-11]) / (fix_time_t[-10] - fix_time_t[-11]) +
			                             (v_re[-11] - v_re[-12]) / (fix_time_t[-11] - fix_time_t[-12]) +
			                             (v_re[-12] - v_re[-13]) / (fix_time_t[-12] - fix_time_t[-13]) )/12.0 ) ])
		start_t = t[i]
		count = 0

l = np.ones(len(p))

#plt.figure()
#plt.stem(p, l, '-', use_line_collection=True)

#plt.figure()
#plt.stem(fix_time_t, fix_time, '-', use_line_collection=True)

plt.figure()

#plt.stem(fix_time_t, v_re, '-', use_line_collection=True)
line_v, = plt.plot(t, v, label='v')
line_v_re, = plt.plot(fix_time_t, v_re, label='v_re')
line_a_re, = plt.plot(fix_time_t, a_re, label='a_re')
line_a, = plt.plot(t, acc, label='a')
plt.legend(handles=[line_v, line_v_re, line_a_re, line_a])
plt.title("Speed-out Simulation Update period=0.0625s, accel 12 value avg") 

plt.show()
