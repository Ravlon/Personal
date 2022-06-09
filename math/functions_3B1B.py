import luca as l

def f_next(array,check_array):
    for i in range(0,len(array)):
        if False in check_array[i+1:]:
            continue
        else:
            array[i]+=1
            array[i+1:]=f_maximiser(array[i:])
            break
    return array

def f_maximiser(array):
    try:
        for a in range(1,len(array)):
            array[a] = array[a-1]+1
    except:
        return []
    else:
        return array[1:]
    
def f_check(array, max_array):
    """ Check if the elements in array are at the maximum, return check array
    """
    check = [False]*len(array)
    for a in range(0,len(array)):
        check[a] = (array[a]>=max_array[a])
    return check
   
def f_max(pos,len_array,n):
    """ Calculate maximum element from set allowed for the specified position
    """
    max_n = n-len_array+pos+1
    return max_n
    
def f_div5(array):
    """Check if set's sum of elements is divisible by 5, return 1 if true, 0 if not"""
    sum_a = 0
    for element in array:
        sum_a += element
    if sum_a:
        return not(sum_a%3)
    else: #triggered only if all elements in array are = 0
        return False

def f_sum(array):
    sums = 0
    for i in array:
        try:
            sums+=int(i)
        except:
            continue
    return sums

def f3B1B_1(n,current,calculations):
    #n = int(l.retrieve("set lenght"))
    ans = [ 0 for i in range(n+1) ]

    #calculations = 2**n-1  #correct for null set
    #current = 0

    for i in range(1,n+1):
        a_set = [0]*i
        for el in range(0,len(a_set)): 
            a_set[el]=el+1 #fill a_set wih the minimum number for each position
            #print("{0}\t|{1}".format(len(a_set),a_set))
        current += 1
        
        max_a = [0]*i
        for a in range(0,i): 
            max_a[a] = f_max(a,i,n)
        
        while True:
            ans[i] += f_div5(a_set)
            check = f_check(a_set,max_a)
            if not(False in check):
                break            
            else:
                a_set = f_next(a_set,check)
                current += 1
            l.progress(current,calculations)
    return (ans,current)
    
