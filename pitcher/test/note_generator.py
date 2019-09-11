import numpy as np
import wave
import struct
import matplotlib.pyplot as plt


#----------- Clean 1000 Hz wave ----------#

freq = 1000
num_samples = 48000
sampling_rate = 48000.0
amp = 16000

file = 'test_clean.wav'

sine_wave = [np.sin(2 * np.pi * freq * x/sampling_rate) for x in range(num_samples)]

nframe = num_samples
comptype = "NONE"
compname = "not compressed"
nchannels = 1
sampwidth = 2

wav_file = wave.open(file, 'w')
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframe, comptype, compname))

for s in sine_wave:
    wav_file.writeframes(struct.pack('h', int(s*amp)))


#----------- Noisy 1000 Hz wave ----------#

noise_freq = 50

sine_noise = [np.sin(2 * np.pi * noise_freq * x/sampling_rate) for x in range(num_samples)]

sine_wave = np.array(sine_wave)
sine_noise = np.array(sine_noise)

combined_signal = sine_wave + sine_noise

file = 'test_noise.wav'

wav_file = wave.open(file, 'w')
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframe, comptype, compname))

for s in combined_signal:
    wav_file.writeframes(struct.pack('h', int(s*amp)))




