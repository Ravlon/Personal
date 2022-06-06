def retrieve(i):
    while True:
        q = input('Enter the {0}: '.format(i))
        try:
            float(q)
        except:
            print("Not a number!")
            continue
        else:
            break
    return float(q)
  
def luca():
    print("module successful")
    

def progress(status,terms):
    stat_bar = 75
    completion = float(status)*100.0/float(terms)
    if status%7==0:
        blink = 0
    else:
        blink = 1
    seg_fill = (int(stat_bar*(completion/100))+1)*blink
    if status >= terms:
        seg_fill = stat_bar
    seg_null = stat_bar-seg_fill
    print('['+'*'*(seg_fill)+' '*(seg_null)+']'+'{0:>6.2f}%\t'.format(completion), end = '\r', flush = True)
    return 0