import matplotlib.pyplot as plt
import numpy as np
import pyaudio
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import struct
from scipy.fftpack import fft
import sys
import time
import wave
import sounddevice as sd 
from scipy.io.wavfile import write 


class RecordAudio(object):
    def __init__(self):

        # stream constants
        self.CHUNK = 1024 * 2
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 16000
        self.pause = False
        self.RECORD_SECONDS = 10
        self.pause = False

    # stream object
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            output=False,
            frames_per_buffer=self.CHUNK
            )

    def record(self):
        print('recording...')
        self.record_voice = sd.rec(int(self.RECORD_SECONDS * self.RATE), samplerate= self.RATE, channels=self.CHANNELS)
        sd.wait()
        write('/Users../output.wav', self.RATE, self.record_voice)


    # def playback(self):
    #     print('playing back')
    #     sd.play(self.record_voice, self.RATE)


if __name__ == '_main_':
    A = RecordAudio()
    A.record()