from math import sin, cos, log10
from cmath import exp, phase
from math import pi as mpi
import matplotlib.pyplot as plt

"""
Application to generate a sinusoidal and cosoidal wave signal and analyse the result with Discrete Fourier Transform to retrieve the frequencies that compose the signal.
"""

def waves_selection():
    """Insert type of Wave: SIN of COS wave. Number of waves each needed, their frequency, their amplitude, their phase shift."""
    n_waves = int(input("Number of sin waves: "))
    waves = [0.0 for j in range(n_waves)]
    amplitude = [0.0 for j in range(n_waves)]
    phase_shift = [0.0 for j in range(n_waves)]
    phase_bool = input("Phase shift to be inserted [y/n]: ")
    for j in range(n_waves):
        waves[j]=float(input("Frequency of wave {0}: ".format(j+1)))
        amplitude[j]=float(input("Amplitude of wave {0}: ".format(j+1)))
        if phase_bool == "y": phase_shift[j]=float(input("Phase shift of wave {0}: ".format(j+1)))
    # norm = sum(amplitude)
    # weighted = [i/norm for i in amplitude]
    return waves, amplitude, phase_shift

def data_size():
    """Size of the dataset to be created and accuracy of it (datapoints per period)"""
    bins_n = int(input("Number of data points: "))
    details = int(input("How many datapoints per unit: "))
    offset = float(input("Offset: "))
    # offset = 0
    return bins_n,details,offset

def sig_create(data_size,point_unit,frequencies,amplitude,phase_shift,offset):
    """Signal creation as sum of sin and cos waves"""
    data = []
    for x in range(0,data_size):
        i = x/point_unit                #correction of data point provided. Each point become the actual position on x axis (phase point)
        a = 0
        for j in range(len(frequencies)):   #add the sin waves
            a += amplitude[j]*sin(frequencies[j]*2*mpi*i+phase_shift[j])+offset
        data.append(a)
    # with open(r"C:\Users\lucas\OneDrive\Code\Altro\Temp\signal Fourier\signal_data.txt", "w") as f:
    #     for i in data:
    #         f.writelines(str(i)+"\n")
    return data

def dft(data,hz,detail) -> complex:
    """Discrete Fourier Transform: calculates amplituted from data point /data/ for the frequency /hz/ in Hertz"""
    result = []
    constant = 2*mpi*hz/detail
    for n,j in enumerate(data):
        trig = constant*n
        result.append((j*(cos(trig)+1j*sin(trig)))) 
        #DFT w/out the complex number structure. "detail" is used instead of "big_n" as the DFT use of N is that of "number of observations in a period" not the total amount of observations. Link:https://wikimedia.org/api/rest_v1/media/math/render/svg/18b0e4c82f095e3789e51ad8c2c6685306b5662b
        #Wikipedia link: https://en.wikipedia.org/wiki/Discrete_Fourier_transform ||| Youtube link: https://youtu.be/nmgFG7PUHfo?t=778
        #confront both to understand this function
    return sum(result)/len(data) #corrects the result (integral under the signal wave) making it a "fraction" of the signal's amplitude.

def dft_3B1B(data,hz,detail) -> complex:
    """Discrete Fourier Transfomr: use the euler formula
    See: https://www.youtube.com/watch?v=spUNpyF58BY"""
    result = []
    for n,j in enumerate(data):
        result.append(j*exp(complex(0,-2*mpi*hz*n/detail)))
        #result.append((j*(cos(2*mpi*hz*n/detail)-sin(2*mpi*hz*n/detail))))
    return sum(result)/len(data) #complex number

def sig_anal(bins_n, detail,data,mode_3b1b=True):
    """Use the dataset to create a Discrete Fourier Series that can be used to retrieve frequencies composing the signal"""
    # data = []
    # with open(r"C:\Users\lucas\OneDrive\Code\Altro\Temp\signal Fourier\signal_data.txt", "r") as f:
    #     for i in f:
    #         data.append(float(i.rstrip()))
    if mode_3b1b:
        #3Blue1Brown version using dft_3B1B function
        hz_step = 1 #reciprocal of actual number you want: 10 is for 0.1
        hz_range = 20000
        hz_array = [i/hz_step for i in range(hz_range*hz_step+1)]
        dft_array = []
        for i in hz_array:
            dft_array.append(dft_3B1B(data,i,detail))
        return hz_array,dft_array
    else:
        #Veritasium version using dft function
        dft_array = [0.0 for i in range(0,bins_n)]
        x = [i for i in range(bins_n)]
        for i in range(len(dft_array)):
            dft_array[i] = dft(data,i,detail)
        return x,dft_array   

def sig_freq(array,percentage:int,period_size):
    """Analyse the Discrete Fourier series to retrieve the frequencies composing analysed signal.
    A threshold is used as a certain percentage of contribution to amplitude."""
    res = []
    for i,j in enumerate(array):
        ampl = 10*log10(abs(j)*2) #amplitude in dB compared to amplitude of sin(x)
        if i<period_size and ampl>0: #only positive dB amplituted are considered
            #period size check to avoid redundancy of check for subsequent periods !!!MAYBE THIS IS NOT CORRECT
            if i:
                res.append((i,ampl,phase(j)+mpi/2))
            else:
                res.append((i,j.real/2,0))
    return res

def sig_show(x,amplitude):
    """Show the Amplitude Graphic of the signal"""
    y = []
    temp = [i[0] for i in amplitude]
    for i in range(len(x)):
        if not(i in temp):
            y.append(0)
        else:
            for n,j in enumerate(temp):
                if j == i:
                    y.append(amplitude[n][1])
                    break

    plt.plot(x,y)
    plt.show()
    return 0

def result(array):
    len_hz = len(str(max(array)[0]))
    if len_hz == 1: len_hz+=1
    header = "[{0:>"+str(len_hz)+"} | {1: ^7"+"} | {2: ^7"+"}]"
    dataline = "[{0:>"+str(len_hz)+"d} | {1:^7.2f"+"} | {2:^+7.2f"+"}]"
    print(header.format("Hz","dB1","Ph.Sh"))
    for hz,amp,ph_sh in array:
        print(dataline.format(hz,amp,ph_sh))

bis,det,offs = data_size()
freq,ampl,phases = waves_selection()
signal_data = sig_create(data_size=bis,point_unit=det,offset=offs,frequencies=freq,amplitude=ampl,phase_shift=phases)
x,array = sig_anal(bis,det,signal_data,True)
res = sig_freq(array,percentage=1,period_size=det)
result(res)
sig_show(x,res)
input()
