def rebase(base, num):

    """
        rebase(base, numero decimale)
            Converte il numero inserito nella base desirata (binario, oct, hex e qualsiasi altro numero entro le digits possibili (62 o 92)
            Returns a string
        
            Per Luca:
            Da aggiungere: possibilità di aggiungere scelta di numero di caratteri tra 62 o 92 con default 62
            Da vedere: estensione dei caratteri disponibili
    """
    #import luca as l #ignora in quanto specifico per il debug personale
    import string
    
    digit = list(string.printable) 

    #digit = digit[:-7] #digits used are all printable characters
    digit = digit[0:62] #digits used are aritmeci digits and letters


    # while True:      #ignora in quanto specifico per il debug personale
        # base = int(l.retrieve("base"))
        # if base>len(digit):
            # print("Too big, max is {0}".format(len(digit)-1))
            # continue
        # else:
            # num = int(l.retrieve("number"))
            # break

    factor = []

    for i in range(0,num+1):
        factor.append(base**i)
        if factor[i]>num:
            break

    factor = factor[::-1]

    ans = [0]*len(factor)
    sums = 0

    while num:
        for i in range(0,len(factor)):
            if num>=factor[i]:
                num -= factor[i]
                ans[i] += 1
                break
    
    for i in range(0,len(ans)):
        #print("{0}:{1},{2}".format(i,ans[i],digit[ans[i]]))
        sums += ans[i] 
        ans[i] = digit[ans[i]]

    #print("\n The number {0} in base {1} is: '".format(num,base),"".join(ans),"'")

    return(["".join(ans),sums])
