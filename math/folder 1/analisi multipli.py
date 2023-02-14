
try:
    x = 'luca'
    import luca as l
    x = 'string'
    import string
    x = 'base_conv'
    import base_conv as b
except:
    print("Error occured while importing module: ", str(x))
else:
    while True:
        x = int(l.retrieve('decimal number for the table'))
        base = int(l.retrieve('base'))
        top = int(l.retrieve('max factor'))
        
        print ("|Fact.\t|Decim.\t|Base{0}\t\t|Sum_digits\t|{1} is divisor".format(base,x))
        for i in range(0,top):
            a = i*x
            [new_base,sums] = b.rebase(base,a)
            divisor = not(bool(sums%x))
            print("|{0}*{1}:\t|{2}\t|{3}\t\t|{4}\t\t{5}".format(i,x,a,new_base,sums,divisor))
        if input("Ripeti [Enter]: ") in ['y','\n','yes','YES','Yes','y\n']: continue
        else: break
