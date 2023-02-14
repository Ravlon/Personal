import math
from math import factorial
from fractions import Fraction
from time import time
from matplotlib.pyplot import plot,show

def gen_func_2(n):
    for i in range(1,n+1):
        if Fraction(factorial(i-1)+1,i).denominator == 1:
            yield i

def prime_list(maxi):
    array = []
    with open(r"C:\Users\lucas\OneDrive\Code\Altro\Temp\prime_list.txt","r") as f:
        for line in f:
            if int(line.rstrip()) <= maxi:
                array.append(int(line.rstrip()))
    return array

def timer(func,n):
    start = time()
    func(n)
    return time()-start

def wilson_prime_check(n):
    """Check if the number is a prime with wilsons formula"""
    return not((factorial(n-1)+1)%n)

def main(limit):
    # start = time()
    result = list(gen_func_2(limit))[-1]
    # total = time()-start
    # print("Execution time: {:<7}".format(total))
    # primes = prime_list(limit)
    # check  = all([j in primes for j in result])
    # print("All primes found: {}".format(check))
    print(result)

if __name__ == "__main__":
    while True:
        n = int(input("Check if prime: "))
        start = time()
        check = wilson_prime_check(n)
        print(time()-start)
        if check: 
            print("Number is a prime")
        else:
            print("Not a prime")


    # time_array = []
    # while True:
    #     a = 50000
    #     # try:
    #     #     int(a)
    #     # except:
    #     #     continue
    #     # else:
    #     for i in range(1,int(a),100):
    #         time_array.append(timer(main,i))
    #     x = list(range(1,int(a),100))
    #     plot(x,time_array, 'o', color = 'black')
    #     show()
    #     time_array = []
    #     input()




# def benchmark():
#     rep = 10
#     func_array = [list_func_1,gen_func_2]
#     limit = 10000

#     primes = prime_list(limit)

#     print(f"Function    | Min     - Avg     - Max     | Check") # 11 e 7

#     for i in func_array:
#         result=list(i(limit))[1:]
#         if len(result) == len(primes):
#             check = all([j in primes for j in result])
#         else:
#             check = False
#             #print(len(result),";",len(primes))
        
#         timed = [timer(i,limit) for j in range(rep)]
#         print("{0!s:<11} | {1:<7.5f} - {2:<7.5f} - {3:<7.5f} | {4}".format(str(i.__name__),min(timed),average(timed),max(timed),check))
#         #print(result)

# def average(array):
#     return sum(array)/len(array)



# def list_func_1(n):
#     return [i for i in range(1,n+1) if Fraction(factorial(i-1)+1,i).denominator == 1]

# def list_func_2(n):
#     return [i for i in range(1,n+1) if Fraction(factorial(i-1)+1,i).denominator == 1]

# def gen_func_1(n):
#     yield (i for i in range(1,n+1) if Fraction(factorial(i-1)+1,i).denominator == 1)

# def w3(j):
#     stuff = math.factorial(j-1)+1
#     term = math.pi*stuff/j
#     res = math.cos(term)
#     return pow(res,2)

# def w2(i):
#     res=[math.floor(w3(j)) for j in range(1,i+1)]
#     return sum(res)

# def w1(x):
#     range_max = 2**x+1
#     exp=1/x
#     res = [math.floor(pow(x/w2(i),exp)) for i in range(1,range_max)]
#     return sum(res)

# def willans(x):
#     return 1+w1(x)

# for i in range(1,n):
#     print(i,". ",willans(i))