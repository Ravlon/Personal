from matplotlib import pyplot as plt

def retrieve(i):
    while True:
        q = input('Enter the {0}: '.format(i))
        try:
            float(q)
        except:
            print("Not a number!")
            continue
        else:
            break
    return float(q)

alpha = 3
top = int(retrieve("ending number"))
sequence =[]
x = [0 for i in range(top)]
y = x[:]
loop = False

maxi_len = 0 #maxixum lenght's position in array

for i in range(top):
    x[i] = i+1
    n = x[i]
    while True:  #when n is 1 the loop ends
        if n in sequence:
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
    if y[i] > y[maxi_len]: maxi_len=i
    sequence = []
    loop = False

print("End of calculation, graph elaborating")

print("Longest streak is for starting number: ", x[maxi_len]," with lenght: ", y[maxi_len])

plt.plot(x,y,'.', color='black')
plt.show()



input()
