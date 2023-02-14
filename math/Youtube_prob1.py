"""_summary_
    Youtube link to problme:  https://www.youtube.com/watch?v=pxHd8tLI65Q

Problem: Find all non negative interger a,b solutions a,b >= 0; so that:

    sqrt(a)+sqrt(b) = sqrt(n)

    given n.

    Solution for n = 2023.
    2023 prime factors are 7 and 17**2
    we use this to define   a = 7*(n**2)        for n: 0->17
                            b = 7(17-n)**2      for n: 0->17

    b can also be defined as the reverse set of a.

!!!!Proper generalisation for my solution is:
    Given x = K**2 * L where K and L are products of the factor. 

            K: the product of the prime factors that have a exponent greater or equal to 2, the product is done with the biggest even number less or equal to the exponent.
            L: the product of the prime factors that have an odd exponent. The product is done with exponent 1. Can also be seen as the part of x that can be square rooted to an integer.
            
            K can be also defined as what we get by diving x with L (product of the prime factors with odd exponents) and square rooted.
            
            define  a := L * n**2
                    b := L * (K-n)**2       where n: 0 -> K
            
            It follows that:
            sqrt(x) = sqrt(K**2 * L) = K * sqrt(L) = n*sqrt(L) + (K-n)*sqrt(L) = sqrt(L* n**2) + sqrt(L * (K-n)**2) = sqrt(a) + sqrt(b)
            
            This demonstrate that the given definitions of a and b are the solution for the problem.

Solutions: 2 solutions are presented: mine and one from the Youtube video.
    The solutions are to be benchmarked one against the other.

Third Element: an improvement in my solution has been found and benchmarked. It's 33% faster and most likely can ben improved.
    """

from sympy import factorint
from numpy import prod, arange
from math import sqrt
import matplotlib.pyplot as plt
from time import time

#Personal solution
def luca_solution(n: int) ->list:
    factors = factorint(n)
    non_square = prod([i**(j%2) for (i,j) in factors.items()])
    squared = prod([i**(j//2) for (i,j) in factors.items()])

    return [non_square*(i**2) for i in range(int(squared)+1)]

#Improved algorithm
def luca2_sol(n: int) ->list:
    factors = factorint(n)
    non_square = prod([i**(j%2) for (i,j) in factors.items() if j%2])
    squared = int((n/non_square)**0.5)

    return [non_square*(i**2) for i in range(int(squared)+1)]

#Youtube's solution: two functions.
def calc_b(a,n):
    return n-2*sqrt(n*a)+a

def youtube_solution(n:int) ->list:
    return [a for a in range(0, n+1) if calc_b(a,n).is_integer()]

def timer(func, j):
    start = time()
    for t in range(1000):
        func(j)
    return time()-start

def main():
    luca = []
    #youtube = []
    luca2 =[]

    ranger = int(input("Range: "))+1

    for i in range(1,ranger):
        print(round(100*i/ranger,2),"%", end="\r")
        luca.append(timer(luca_solution,i))
        luca2.append(timer(luca2_sol,i))

    x = arange(1,ranger)
    plt.plot(x,luca, label = "luca")
    plt.plot(x,luca2, label = "luca2")
    plt.legend()
    plt.show()

    print(sum(luca)/len(luca))
    print(sum(luca2)/len(luca2))

    input()


if __name__ == "__main__":
    main()
    