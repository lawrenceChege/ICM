import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft,fftfreq, ifft

#number of points
n = 1000

#Distance (meters) or time period(seconds)
Lx = 100

#angular freq

ang = 2.0*np.pi/Lx

#Creating individual signals
x = np.linspace(0, Lx, n)
y1 = 1.0*np.cos(5.0*ang*x)
y2 = 2.0*np.sin(10.0*ang*x)
y3 = 0.5*np.sin(20*ang*x)

#full signal
y = y1+y2+y3

#create all necessary frequencies
freqs = fftfreq(n)

#ignore half the values
mask = freqs>0

#ftt values
fft_vals = fft(y)

#true theoretical fft
fft_theo = 2.0*np.abs(fft_vals/n)

plt.figure(1)
plt.title('Original Signal')
plt.plot(x,y, color='xkcd:salmon', label='original')
plt.legend()

plt.figure(2)
plt.plot(freqs, fft_vals, label='raw fft values')
plt.title('Raw FFt values')
plt.show()

plt.figure(3)
plt.plot(freqs[mask], fft_theo[mask], label='True fft values')
plt.title('True fft values')
plt.show()
