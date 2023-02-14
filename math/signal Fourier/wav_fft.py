import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft
from math import log10,sin
from scipy.io import wavfile
import sounddevice as sd
from time import time

"""
Application to generate a sinusoidal and cosoidal wave signal and analyse the result with Fast Discrete Fourier Transform to retrieve the frequencies that compose the signal.
"""
def wav_file():
    # file = wavfile.read(r"C:\Users\lucas\OneDrive\Code\Altro\Temp\signal Fourier\audio.wav")
    file = wavfile.read(r"C:\Users\lucas\OneDrive\Code\Altro\music\15,684kg Bell ringing (320 kbps).wav")
    sample_rate = file[0]
    data = [i[0] for i in file[1]]
    return sample_rate,data

sr,data = wav_file()
spectrum, freq, times, im = plt.specgram(x=data, cmap="Greys", NFFT=2**10, Fs = sr)
plt.show()

frequencies = np.zeros(np.shape(spectrum))
new_signal = np.zeros(int(times[-1]*sr))

for f in range(len(freq)):
    for t in range(len(times)):
        ampl = spectrum[f][t]
        if ampl<100:
            spectrum[f][t] = 0
            frequencies[f][t] = 0.0
        else:                                         
        #     spectrum[f][t] = 10*log10(abs(ampl)*2)        #enable to have dB in heatmap for better visibility
            frequencies[f][t] = 2*np.pi*freq[f]
        # spectrum[f][t]=10*log10(abs(spectrum[f][t]*2))  #heatmap becomes proper spectogrm

spectrum = np.transpose(spectrum)
frequencies = np.transpose(frequencies)

preceding = 0

start = time()
print("Time:",start)

for t_pos in range(len(times)):
    ranger = int(times[t_pos]*sr)
    for x in range(ranger-preceding):
        if t_pos:
            t = times[t_pos-1]+x/sr
        else:
            t = x/sr
        for f in range(len(freq)):
            if spectrum[t_pos][f]:
                new_signal[preceding+x]+=spectrum[t_pos][f]*sin(frequencies[t_pos][f]*t)
    preceding = ranger

print("Time elapsed: ",time()-start )

plt.plot(np.arange(0,times[-1],1/sr),new_signal)
plt.show()

sd.play(new_signal,samplerate=sr,blocking=True)
spectrum, freq, times, im =plt.specgram(new_signal, cmap="Greys", NFFT = 2**10, Fs = sr)

for f in range(len(freq)):
    for t in range(len(times)):
        if spectrum[f][t]:
            spectrum[f][t]=10*log10(abs(spectrum[f][t]*2))  #heatmap becomes proper spectogrm

# plt.imshow(spectrum, cmap="Greys")
plt.show()

# input()
