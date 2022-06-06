from fractions import Fraction
import decimal as d
d.getcontext().prec = 25
i = 1
terms = 1500000
stat_bar = 75
pi = Fraction(0,1)
print('Status:')
sign = 4
while i<=terms:
    pi+=Fraction(sign,i)
    completion = float(i)*100.0/float(terms)
    if i%7==0:
        blink = 0
    else:
        blink = 1
    seg_fill = (int(stat_bar*(completion/100))+1)*blink
    if i >= terms:
        seg_fill = stat_bar
    seg_null = stat_bar-seg_fill
    print('['+'*'*(seg_fill)+' '*(seg_null)+']'+'{0:>6.2f}%\t'.format(completion)+'pi:'+str(float(pi)), end = '\r', flush = True)
    sign*=-1
    i+=2

print('\nProcessing...')
pi = pi.as_integer_ratio()
#print(pi)
num = d.Decimal(pi[0])
den = d.Decimal(pi[1])
res = num/den
print('\nEstimate of Pi:\n'+str(res))#+'\a'*10)
input()
