import control
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
import numpy as np
import cmath, math
import scipy

z = control.TransferFunction.z
H = (0.9474+0.2105*z**-1-0.7368*z**-2)/(1.0-1.579*z**-1+0.7895*z**-2)

omega = np.linspace(0, 100, 500)
mag = []
phase = []
for i in range(0, 500):
  mag = np.append(mag, np.abs( H(np.exp(complex(0, 2.*math.pi*omega[i] / 201.)))))
  phase = np.append(phase, np.angle(H(np.exp(complex(0, 2.*math.pi*omega[i] / 201.)))))
omega = np.linspace(0, 3.1415926, 500)
#mag, phase, omega = control.bode(H, omega=omega, Plot=False)
plt.figure()
plt.subplot(211)
plt.suptitle('Mag H')
plt.grid(True)
plt.xlim(0, 3.5)
plt.plot(omega, mag)
plt.subplot(212)
plt.suptitle('phase H')
plt.grid(True)
plt.xlim(0, 3.5)
plt.plot(omega, phase)


Nt = 50
N = 201
A = 1.0
ohm = 2.*math.pi / N

h = ifft( [H( np.exp( complex(0, ohm*n) ) )  for n in range(0, N-1)] ).real


###############################
#
# Hre = Y / U 
#
###############################

Y = []
U = []
for l in range(0, int((N-1)/2)):
	ohml = ohm*l
	u = A*np.cos([ohml*n for n in range(0, Nt + N - 1)])
	#ye = np.abs( H(np.exp(complex(0, ohml))) )*A*np.cos( [(ohml*n + np.angle(H(np.exp( complex(0, ohml))))) for n in range(0, Nt + N - 1)] )
	ye = scipy.signal.convolve(u, h)
	Y = np.append(Y, np.sum( [ye[n]*np.exp( complex(0, -ohml*n) )  for n in range(Nt, Nt+N-1)] ) )
	U = np.append(U, np.sum( [u[n]*np.exp( complex(0, -ohml*n) )  for n in range(Nt, Nt+N-1)] ) )

H_re = Y / U
mag_H_re = np.abs(H_re)
phase_H_re = np.angle(H_re)
T = np.linspace(0, 3.1415926, int(H_re.size))
plt.figure()
plt.subplot(211)
plt.suptitle('Mag H re')
plt.grid(True)
plt.xlim(0, 3.5)
plt.plot(T, mag_H_re)
plt.subplot(212)
plt.suptitle('Phase H re')
plt.grid(True)
plt.xlim(0, 3.5)
plt.plot(T, phase_H_re)


###############################
#
# ye by convolution and by defination 
#
###############################

l = 7

#convolution for fix l
u = A*np.cos([ohm*l*n for n in range(0, Nt + N - 1)])
ye_f = np.convolve(u, h)
ye_d = np.abs(H( np.exp( complex(0, -ohm*l) ) ) )*A*np.cos( [(ohm*l*n + np.angle(H( np.exp( complex(0, -ohm*l))))) for n in range(0, Nt + N - 1)] )
n1 = range(0, u.size)
n2 = range(0, len(ye_f))
n3 = range(0, len(ye_d))

#print h
h_t = np.linspace(0, Nt+N-1, h.size)
plt.figure()
plt.subplot(211)
plt.grid(True)
plt.xlim(0, 250)
plt.plot(h_t, h)

#print u, ye_f, ye_d
plt.subplot(212)
plt.suptitle('l = ' + str(l))
plt.grid(True)
plt.xlim(0, 250)
plt.ylim(-6, 6)
line_1, = plt.plot(n1, u, label="u")
line_2, = plt.plot(n2, ye_f.real, label="conv y")
line_3, = plt.plot(n3, ye_d.real, label="def y")
plt.legend(handles=[line_1, line_2, line_3])
print("H  : ", np.abs( H(np.exp(complex(0, ohm*l)))), np.angle(H(np.exp(complex(0, ohm*l)))))
print("Hre: ", np.abs(H_re[l]), np.angle(H_re[l]), "\n")


###############################
#
# least squares
#
###############################

A_cos = [[0, 0, 0, 0, 0]]
B_cos = []
A_sin = [[0, 0, 0, 0, 0]]
B_sin = []
L = int((N-1)/2)
for l in range(0, L):
	ohml = 2.*math.pi*l / N
	
	#R = np.abs( H(np.exp(complex(0, ohml))));phi = np.angle(H(np.exp(complex(0, ohml))))
	R = np.abs(H_re[l]);phi = np.angle(H_re[l])
	A_cos = np.concatenate( (A_cos, [[-R*np.cos(phi - ohml), -R*np.cos(phi - 2.*ohml), 1., np.cos(ohml), np.cos(2.*ohml)]]), axis=0 )
	B_cos = np.concatenate( (B_cos, [R*np.cos(phi)]), axis=0 )
	A_sin = np.concatenate( (A_sin, [[-R*np.sin(phi - ohml), -R*np.sin(phi - 2.*ohml), 0., -np.sin(ohml), -np.sin(2.*ohml)]]), axis=0 )
	B_sin = np.concatenate( (B_sin, [R*np.sin(phi)]), axis=0 )
	
A = np.concatenate([np.delete(A_cos, 0, 0), np.delete(A_sin, 0, 0)], axis=0)
B = np.concatenate([B_cos, B_sin], axis=0)

A_T = A.T;
a = np.linalg.inv(A_T.dot(A)).dot(A_T).dot(B)
Hre = (a[2]+a[3]*z**-1+a[4]*z**-2)/(1.0+a[0]*z**-1+a[1]*z**-2)

print("Hre :", Hre)
print("H :", H)

plt.show()
