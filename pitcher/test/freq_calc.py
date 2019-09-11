import numpy as np
import wave
import struct
import matplotlib.pyplot as plt


frame_rate = 48000.0
infile = 'test.wav'
num_samples = 48000
wav_file = wave.open(infile, 'r')
data = wav_file.readframes(num_samples)
wav_file.close()

data = struct.unpack('{n}h'.format(n=num_samples), data)
data = np.array(data)
data_fft = np.fft.fft(data)

frequencies = np.abs(data_fft)

print("Frequency: {} Hz".format(np.argmax(frequencies)))