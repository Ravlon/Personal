from math import log10
from cmath import phase
import matplotlib.pyplot as plt
import numpy as np
import random as rd
from numpy.fft import fft
import sounddevice as sd

"""
Application to generate a sinusoidal and cosoidal wave signal and analyse the result with Fast Discrete Fourier Transform to retrieve the frequencies that compose the signal.
"""

def random_waves(n_waves):
    frequencies = [rd.randint(1,20000) for i in range(n_waves)]
    amplitude = [int(rd.uniform(0,1)*10) for i in range(n_waves)]
    phases = [rd.uniform(0,np.pi) for i in range(n_waves)]
    #offset = rd.uniform (0,1)
    offset = 0

    return frequencies,amplitude,phases,offset

def signal_generation(sampling_rate, frequencies, amplitudes, phases, offset):  
    #sampling interval
    ts = 1.0/sampling_rate
    t = np.arange(0,1,ts)

    #check all arrays are of same lenght raise Exception otherwise
    ...

    #create signal by adding sin waves. Pad amplitudes, phases and offsets if needed
    result = 0
    for i in range(len(frequencies)):
        result += amplitudes[i]*np.sin(2*np.pi*frequencies[i]*t + phases[i]) +offset
    
    #graph of signal
    plt.plot(t, result, 'r')
    plt.ylabel("Amplitude")
    plt.xlabel("Time")
    plt.show()

    return result

def sig_freq(array,sample_rate):
    """Analyse the Discrete Fourier series to retrieve the frequencies composing analysed signal.
    A threshold is used as a certain percentage of contribution to amplitude."""
    res = []
    for i,j in enumerate(array):
        ampl = 10*log10(abs(j)*2) #amplitude in dB compared to amplitude of sin(x)
        if i<sample_rate/2 and ampl>0: #only positive dB amplituted are considered
            #period size check to avoid redundancy of check for subsequent periods !!!MAYBE THIS IS NOT CORRECT
            if i:
                res.append((i,ampl,phase(j)+np.pi/2))
            else:
                res.append((i,j.real/2,0))
    return res

def result(array):
    len_hz = len(str(max(array)[0]))
    if len_hz == 1: len_hz+=1
    header = "[{0:>"+str(len_hz)+"} | {1: ^7"+"} | {2: ^7"+"}]"
    dataline = "[{0:>"+str(len_hz)+"d} | {1:^7.2f"+"} | {2:^+7.2f"+"}]"
    print(header.format("Hz","dB1","Ph.Sh"))
    for hz,amp,ph_sh in array:
        print(dataline.format(int(hz*441/20),amp,ph_sh))

def website(fftransform):
    N = len(fftransform)
    n = np.arange(N)
    T = N/sr
    freq = n/T
    y = [10*log10(i*2) for i in np.abs(fftransform)]
    plt.stem(freq,y,'b', markerfmt= " ", basefmt= "-b")
    plt.xlabel("Freq (Hz)")
    plt.ylabel("FFT Amplitude")
    plt.show()

sr = 44100 #sampling rate
n_waves = 3 #number of waves in signal generation
waves = random_waves(n_waves)
signal = signal_generation(sr,*waves)
fft_tr = fft(signal[:1000])
res = sig_freq(fft_tr,sr)
result(res)
sd.play(signal,samplerate=sr, blocking=True)
website(fft_tr)

