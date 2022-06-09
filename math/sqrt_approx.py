
num = 3
prec = 160
#useful only for precision above 16(IDLE)

len_num = len(str(int(num)))
limit = prec+(len_num//2)

if len_num%2 == 0:
    string = '0'+str(num)
    l0 = 1
else:
    string = str(num)
    l0 = 0

if '.' not in string:
    string = string + '.' + '0'*prec*2
else:
    string = string + '0'*(prec*2-len(string)+len_num+l0+1)

##print('Number is: ',string)

root = list(string)
dot_pos = root.index('.')
root.remove('.')
result = []
##result = list(str(int(int(string)**0.5)))
##result = [result[0]]
##remainder = int(root[0])-int(result[0])**2
#print(root)
#print(result)

if root[0] == 0:
    remainder = 0
else:
    result.append(str(int(int(root[0])**0.5)))
    remainder = int(root[0])-int(result[0])**2
    
w = 1
##print('  '+''.join(root))
##print(' '+'-{0:>{width}}'.format(result[0],width=w))

s_result = ''.join(result)

for i in range(limit):
    w+=2
    operand = ''.join(str(remainder)+str(root[i*2+1])+str(root[i*2+2]))
##    print(' '+'={0:>{width}}'.format(operand,width=w))
    multi = str(int(s_result)*2)
    #print(multi+'\t'+s_result)
    for digit in range(0,11):
        a = multi+str(digit)
        b = int(a)*int(digit)
        if b > int(operand):
            diff = int(multi+str(int(digit)-1))*(int(digit)-1)
            result.append(str(int(digit)-1))
            s_result += str(int(digit)-1)
            break
    #print(digit)
    remainder = int(operand)-int(diff)
##    print(' '+'-{0:>{width}}'.format(str(diff),width=w))#+'\ta:{}\tb:{}'.format(a,b))

print('The square root of {} to the {} digit is:'.format(num,prec))
for x in range(len(result)):
    if x == int(dot_pos/2+0.5):
        print('.'+result[x],end = '',flush=True)
    else:
        print(result[x],end = '', flush=True)

print(dot_pos)

#Ho cambiato questo e si deve vedere su Github

input()
