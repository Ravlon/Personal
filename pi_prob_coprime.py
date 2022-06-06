import random as r

attempts = 10000
r_max = 1200000 #maximum range for random integer generation
real = 0    #realisatio of coprimes
stat_bar = 75
print('Status:')
i=0

for i in range(attempts): 
    a=r.randint(1,r_max)
    b=r.randint(1,r_max)
    coprime = True
    for j in range(2,r_max):
        if a%j==0 and b%j==0:
            coprime = False
            break
    if coprime == True:
        real += 1
    completion = float(i)*100.0/float(attempts)
    seg_fill = (int(stat_bar*(completion/100))+1)
    if i >= attempts:
        seg_fill = stat_bar
    seg_null = stat_bar-seg_fill
    print('['+'*'*(seg_fill)+' '*(seg_null)+']'+'{0:>6.2f}%\t'.format(completion), end = '\r', flush = True)

approx = (6.0/(real/attempts))**0.5
print('\nPi = '+str(approx))
input()
