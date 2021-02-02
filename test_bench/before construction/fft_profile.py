from scipy.fftpack import fft,ifft
import numpy as np
import matplotlib.pyplot as plt
#from ..signal import Time
#from ..signal.pulse import Square, PWM

# clock
sampling_rate = 1000.;end_time = 2.
#clock = Time(sampling_rate)
#clock.Offline(end_time)
sample = 1000
t = np.linspace(0, 3, int(30*sample + 1))

y=[]
yj=[]

for i in t:
	if (i <= 0.4):
		y.append(0)
	if (0.4 < i <= 2.4):
		y.append(1.5*i - 0.6)
	if (i > 2.4):
		y.append(3)
		
for i in t:
	yj.append(0)
yj[4000] = 1000
yj[4001] = 1000
yj[24000] = -1000
yj[24001] = -1000


a = [0.0, 0.0, 1.0, -0.22222222222222222]
y2 = a[0] + a[1]*t + a[2]*t**2 + a[3]*t**3
y2j = 2*a[2] + 6*a[3]*t

l = len(t)
yy = abs(fft(yj)/l)
yy_half = yy[range(int(l/100))]

xx = np.arange(len(yj))
xx_halft = xx[range(int(l/100))]

l = len(t)
yy2 = abs(fft(y2j)/l)
yy_half2 = yy2[range(int(l/100))]

xx2 = np.arange(len(y2j))
xx_halft2 = xx2[range(int(l/100))]


plt.subplot(221)
plt.plot(t, y)
plt.title("Trapezoidal")

plt.subplot(223) 
plt.plot(xx_halft, yy_half) 
plt.title("FFT Trapezoidal jerk") 

plt.subplot(222)
plt.plot(t, y2)
plt.title("S-Curve")

plt.subplot(224) 
plt.plot(xx_halft2, yy_half2) 
plt.title("FFT S-Curve jetk") 

plt.show()



