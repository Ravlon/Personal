size = 1000
mininum = 7
factors = [6,9,20]
for i in range(size,mininum,-1):
    if all((i%f for f in factors)):
        print(i)
        break
    else:
        continue


#completely wrong and botched
#https://en.wikipedia.org/wiki/Frobenius_formula