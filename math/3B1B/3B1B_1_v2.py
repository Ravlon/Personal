import functions_3B1B as f3b1b
import luca as l

n = int(l.retrieve("set lenght"))
ans = [ [ 0 for i in range(n) ] for j in range(n) ]
calculations = -1*n #correct for null set
#calculations = 0 #do not correcto for null set

for i in range(1,n+1):
    calculations += 2**i
current = 0

for i in range(1,n+1):
    ans[i-1],current = f3b1b.f3B1B_1(i,current,calculations)

print()
for i in range(0,n):
    print("{0:^3,}|{1:<10}\t->{2}".format(i+1,f3b1b.f_sum(ans[i]),ans[i]))
input()
