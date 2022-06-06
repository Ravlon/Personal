#define functions

# def retrieve(i):
    # while True:
        # q = input('Enter the {0}: '.format(i))
        # try:
            # float(q)
        # except:
            # print("Not a number!")
            # continue
        # else:
            # break
    # return float(q)

# def recursion(x,top,step):

    # a = x + step
    
    # if a<top:
        # a = recursion(a,top,step)
    
    # return a

    
    
#main

import luca

luca.retrieve('test')

# while True:
    # start = retrieve('start')
    # top = retrieve('top')
    # step = retrieve('step')
    
    # if step>=top:
        # print('step needs to be less than top')
        # continue
    # else:
        # res = recursion(start,top,step)
        # break

# print('Start @ {0} increase to {1} up to {2}: result is {3}'.format(start,step,top,res))

input()
