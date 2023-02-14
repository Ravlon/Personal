import matplotlib.pyplot as plt
import numpy as np

def collatz_conj(n):
    array = [n]
    while (n-1):
        if n%2:
            n = 3*n+1
            array.append(n)
        else:
            n//=2
            array.append(n)
    return array

def path_plot(ran:int):
    plt.ion()
    plt.figure()
    ax = plt.subplot(111)
    for i in range(1,ran):
        y = collatz_conj(i)
        x = np.arange(len(y))
        print(y)
        ax.plot(x,y)
        plt.pause(0.5)
    input()

if __name__ == "__main__":
    path_plot(50)



    
