import scipy.signal as sig
import matplotlib.pyplot as plt
import numpy as np
from math import pi
import scipy.fftpack as sf


plt.close('all')

# generate a signal
Fs = 100
t = 4
n = np.arange(0, t, 1/Fs)
f = 10
x = np.sin(2*pi*f*n)

# Generate noisy signal, if you increase the variance is increases the noise
y = np.random.normal(0, 0.2, np.size(x)) #AWGN: Additive white Gaussian noise (AWGN) is a basic noise model used in information theory to mimic the effect of many random processes that occur in nature. 
                                         #The modifiers denote specific characteristics: Additive because it is added to any noise that might be intrinsic to the information system
x = x+y 

plt.figure(1)
plt.subplot(2, 1, 1)
plt.plot(n,x); plt.title('Noisy Sinusodial Wave')
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')

# take spectral analysis
X_f = abs(sf.fft(x))
l = np.size(x)
fr = (Fs/2)*np.linspace(0,1,1/2)
xl_m = (2/1)*abs(X_f[0:np.size(fr)])

plt.subplot(2,1,2)
plt.plot(fr,20*xl_m)
plt.title('Spectrum of Noisy signal')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Magnitude')
plt.tight_layout()

# create a BPF
o = 5
fc = np.array([8,12])
wc = 2*fc/Fs
[b,a] = sig.butter(o,wc, btype = 'bandpass')

# filter response
[W,h] = sig.freqz(b,a,worN = 1024)

W =Fs * W/(2*pi)

plt.figure(2)
plt.subplot(2,1,2)
plt.plot(W, 20*np.log10(h))
plt.title('Filter Freq. Response')

# filter signal
x_filt = sig.lfilter(b,a,x)

plt.subplot(2,1,2)
plt.plot(n, x_filt)
plt.title('Filtered Signal')
plt.tight_layout()