from luca import retrieve
from matplotlib import pyplot as plt

alpha = int(retrieve("multiplier"))
top = int(retrieve("starting number"))
sequence =[]
x = [0 for i in range(top)]
y = x[:]
loop = False

for i in range(top):
    x[i] = i+1
    n = x[i]
    while True:  #when n is 1 the loop ends
        if n in sequence:
            #print("Loop reached!!!!")
            #print(i,".\n")
            #print(', '.join(list(map(str,sequence))))
            loop = True
            break
        sequence.append(n)
        if n%2:
            n*=alpha
            n+=1
        else:
            n//=2
        print(x[i],end='\r',flush=True)
    
    y[i] = len(sequence)
    sequence = []
    loop = False

print("End of calculation, graph elaborating")

#for n in range(top):
    #print(sequence[i], end=',')
    #print((x[n],y[n]))

plt.plot(x,y,'.', color='black')
plt.show()


input()
