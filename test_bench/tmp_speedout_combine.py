import math
import numpy as np
#from . import Dynsys
import matplotlib.pyplot as plt

sample = 100000
t = np.linspace(0, 10, int(10*sample)+1)
a = [0.0, 2.220446049250313e-16, -1.1102230246251565e-16, 0.05000000000000003, -0.007500000000000002, 0.0003000000000000001]
v = a[0] + a[1]*t + a[2]*t**2 + a[3]*t**3 + a[4]*t**4 + a[5]*t**5
acc = a[1] + 2*a[2]*t + 3*a[3]*t**2 + 4*a[4]*t**3 + 5*a[5]*t**4
#v = 1.5*np.cos(2*np.pi*t)
#acc = -1.5*np.sin(2*np.pi*t)

so = np.pi*0.1565/150.
p = []
s = 0.0
dt = t[1]

for i in range(0, len(t)):
	ds = v[i]*dt
	if ((s + ds) == so):
		p = np.append(p, [t[i]])
		s = 0.0
		ds = 0.0
	elif ((s + ds) > so):
		p = np.append(p, [t[i-1] + (so - s)/ds * dt])
		s = (ds + s) - so
		ds = 0.0
	s = s + ds

#Combine
start_i = 0
start_t = 0.0
j = 0
tick_count = []
pulse_count = []
v_re = []
a_re = []
t_re = []

fc = 50000000.
update_period = 0.01
avg_size = 5

K = so*fc
clock = np.linspace(0, 10, int(10*fc)+1)
for i in range(0, len(p)):
	if ((p[i] - start_t) >= update_period):
		tc = 0
		while (clock[j] < p[i]):
			j += 1
			tc += 1
		if (clock[j] > p[i]):
			j -= 1
			tc -= 1
		tick_count = np.append(tick_count, [tc])
		pulse_count = np.append(pulse_count, [i-start_i])
		v_re = np.append(v_re, [ K*pulse_count[-1] / tick_count[-1] ])
		t_re = np.append(t_re, [p[i]])
		
		start_i = i
		start_t = p[i]
		
		#accel
		k = 2
		sum_ = 0.0
		while ( k < len(v_re) and (k-1) < avg_size ):
			sum_ += (v_re[-(k-1)] - v_re[-k] ) / ( t_re[-(k-1)] - t_re[-k] )
			k += 1
		if ((k-2)>0):
			a_re = np.append(a_re, [sum_/(k-2)])
		else:
			a_re = np.append(a_re, [0.0])

plt.figure()
plt.stem(t_re, tick_count, '-', use_line_collection=True)
plt.title("Combine, tick_count = " + str(fc/1.e6) + "MHz")

plt.figure()
plt.stem(t_re, pulse_count, '-', use_line_collection=True)
plt.title("Combine, pulse_count = " + str(update_period) +"s") 

plt.figure()
#plt.stem(fix_time_t, v_re, '-', use_line_collection=True)
line_v, = plt.plot(t, v, label='v')
line_v_re, = plt.plot(t_re, v_re, label='v_re')
line_a_re, = plt.plot(t_re, a_re, label='a_re')
line_a, = plt.plot(t, acc, label='a')
plt.legend(handles=[line_v, line_v_re, line_a_re, line_a])
plt.title("Combine, sampling clock = " + str(fc/1.e6) + "MHz, Update period = "+ str(update_period) +"s, accel "+ str(avg_size) +" value avg") 

plt.show()
