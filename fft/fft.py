from scipy.fftpack import fft,ifft
import numpy as np
import matplotlib.pyplot as plt
from ..signal.square import Square
from ..signal.pwm import PWM

x, y = Square(0., 100, 1., 1.).Offline(1, 1000)
x2, y2 = PWM(0., 2., 1., shift=0.5).Offline(1, 1000)

yy = abs(fft(y)/len(x))
yy_half = yy[range(int(len(x)/2))]

xx = np.arange(len(y))
xx_halft = xx[range(int(len(x)/2))]

yy2 = abs(fft(y2)/len(x2))
yy_half2 = yy2[range(int(len(x2)/2))]

xx2 = np.arange(len(y2))
xx_halft2 = xx2[range(int(len(x2)/2))]


plt.subplot(221)
plt.plot(x, y)
plt.title("Original")

plt.subplot(223) 
plt.plot(xx_halft, yy_half) 
plt.title("FFT sine Square") 

plt.subplot(222)
plt.plot(x2, y2)
plt.title("Original")

plt.subplot(224) 
plt.plot(xx_halft2, yy_half2) 
plt.title("FFT PWM") 

plt.show()



