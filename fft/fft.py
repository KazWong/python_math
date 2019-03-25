from scipy.fftpack import fft,ifft
import numpy as np
import matplotlib.pyplot as plt
from ..plant.sine_gaussian import SineGaussian

sine2 = SineGaussian(0., 2.7, 6.4, 0.)
sine1 = SineGaussian(0., 1.7, 12.3, 0.)
sine = SineGaussian(0., 15.7, 3.3, 0.)

sine1.Cascade(sine2)
sine.Cascade(sine1)

x, y = sine.Offline(1, 1000)

yy = abs(fft(y)/len(x))
yy_half = yy[range(int(len(x)/2))]

xx = np.arange(len(y))
xx_halft = xx[range(int(len(x)/2))]


plt.subplot(211)
plt.plot(x, y)
plt.title("Original")

plt.subplot(212) 
plt.scatter(xx_halft, yy_half, s=0.7) 
plt.title("FFT") 

plt.show()



