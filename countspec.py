'''
   Retrieving the frequencies from the given files

   Thanks to Fred, Ben and Hubert
'''
import numpy as np
import matplotlib.pyplot as plt
import sys

#todo: refactor into real code
# add in duration
filename = sys.argv[1]

if not filename:
    print "Need a file name :("
    sys.exit()

# Time series setup
sample_length_s = 4.0  # s
sample_rate = 44.0e3  # Hz
num_samples = int(sample_length_s * sample_rate)
dt = 1.0 / sample_rate  # s

times = np.arange(num_samples) * int(dt)

max_freq = 0.5 / dt  # Maximum frequency
freq_inc = max_freq / (num_samples / 2)
# Spectrum frequencies (spectrum x-axis), in Hz
freqs = np.arange(num_samples / 2) * freq_inc

data = np.memmap(filename, dtype='h', mode='r')

spectrum = np.fft.ifft(data) * 2.0
#spec = defaultdict(int)

flux = []
flux.append(0)
flux.append(spectrum[0])

fluxsum = 0.0
last_spec = spectrum[0]
for i in range(1,(len(spectrum))):
    #print np.abs(spectrum[i])
    fluxsum = abs(spectrum[i]) - abs(last_spec)
    last_spec = spectrum[i]
    print fluxsum
    if fluxsum  > 0.0:
        flux.append(fluxsum)
    else:
        flux.append(0.0)

#print flux
