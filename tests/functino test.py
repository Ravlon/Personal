#define functions

def times(a,b):
    return a*b
    
def retrieve():
    while True:
        q = input("Enter the factor: ")
        try:
            float(q)
        except:
            print("Not a number!")
            continue
        else:
            break
    return float(q)
    
#retrieve values from user and call defined function

x = retrieve()
y = retrieve()
res =times(x,y)

print('The product of {0} & {1} is: {2}'.format(x,y,res))
input()