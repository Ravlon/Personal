from __future__ import division
from math import factorial
from time import time

def wilson_check(n):
    return not((factorial(n-1)+1)%n)

def factors(n):
    for i in range(2,n//2+1):
        if not(n%i): 
            return False
    return True

def timer(func,a):
    start = time()
    func(a)
    return time() - start

def average(array):
     return sum(array)/len(array)

def main(n):
    
    #func_array = [wilson_check]
    func_array = [wilson_check,factors]
    maxi = []

    for i in func_array:
        results = []
        for x in range(1000):
            results.append(timer(i,n))
        #print("{0!s:<15} | {1:<7.5f} - {2:<7.5f} - {3:<7.5f} | {4}".format(str(i.__name__),min(results),average(results),max(results),n))
        maxi.append(max(results))

    if maxi[1]:
        print("{0:>5}.\t{1}".format(n,maxi[0]/maxi[1]))
    else:
        print("{0:>5}.\t{1}".format(n,0))

if __name__ == "__main__":
    limit = int(input("Limit is: "))
    #print(f"Function        | Min     - Avg     - Max     | Check") # 11 e 7
    for n in range(1,limit+1,2):
        main(n)
    input()