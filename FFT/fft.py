from scipy.fftpack import fft,ifft
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,1,1000)
y = 3.14*np.sin(2*np.pi*6.6*x) + 2.66*np.sin(2*np.pi*4.3*x)

yy = abs(fft(y)/len(x))
yy_half = yy[range(int(len(x)/2))]

xx = np.arange(len(y))
xx_halft = xx[range(int(len(x)/2))]


plt.subplot(211)
plt.plot(x, y)
plt.title("Original")

plt.subplot(212) 
plt.plot(xx_halft, yy_half) 
plt.title("FFT") 

plt.show()



