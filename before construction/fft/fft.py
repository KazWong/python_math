from scipy.fftpack import fft,ifft
import numpy as np
import matplotlib.pyplot as plt
from ..signal import Time
from ..signal.pulse import Square, PWM

# clock
sampling_rate = 1000.;end_time = 2.
clock = Time(sampling_rate)
clock.Offline(end_time)

sigma = 0.01; terms = 40;A = 1.5;f = 1.;d = 0.5
y = Square(clock, sigma, terms, A, f).Offline()
y2 = PWM(clock, sigma, terms, A, f, d).Offline()

l = clock.Len()
yy = abs(fft(y)/l)
yy_half = yy[range(int(l/2))]

xx = np.arange(len(y))
xx_halft = xx[range(int(l/2))]

yy2 = abs(fft(y2)/l)
yy_half2 = yy2[range(int(l/2))]

xx2 = np.arange(len(y2))
xx_halft2 = xx2[range(int(l/2))]


plt.subplot(221)
plt.plot(clock.timespace, y)
plt.title("Squre")

plt.subplot(223) 
plt.plot(xx_halft, yy_half) 
plt.title("FFT Square") 

plt.subplot(222)
plt.plot(clock.timespace, y2)
plt.title("PWM")

plt.subplot(224) 
plt.plot(xx_halft2, yy_half2) 
plt.title("FFT PWM") 

plt.show()



