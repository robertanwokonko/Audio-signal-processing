import matplotlib.pyplot as plt 
import numpy as np 
import wave
import sys

from scipy.io.wavfile import write
from scipy.io import wavfile

"""
Showing the use of convolution:

Convolution of an echo filter with a signal
"""


spf = wave.open('/Users...wav', 'r')

signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')
print ("numpy signal shape:", signal.shape[0])

plt.plot(signal)
plt.title("wave signal")
plt.show()

delta = np.array([1, 0, 0])
noecho = np.convolve(signal, delta)
print ("noecho signal", noecho)
assert(np.abs(noecho[:len(signal)]-signal).sum() < 0.0000001)

noecho = noecho.astype(np.int16)
write('noecho.wav', 44100, noecho)

filt = np.zeros(44100)
filt[0] = 1
filt[11025] = 0.6
filt[22050] = 0.3
filt[33075] = 0.2
filt[44099] = 0.1
out = np.convolve(signal, filt)

out = out.astype(np.int16)
write('/Users/..wav', 44100, out)