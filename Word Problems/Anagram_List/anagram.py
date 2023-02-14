
def confronto(anagram, capitals):
    anagram = sorted(anagram)
    print(anagram)
    for cap in capitals:
        #print(sorted(cap))
        if anagram == sorted(cap):
            print("Result is: ", cap)
            return cap

def retrieve_caps():
    cap_list = []
    with open(r"C:\Users\lucas\OneDrive\Code\Altro\Anagram_List\cap.txt","r") as text:
        for line in text:
            cap_list.append(line.rstrip().lower())
    print(cap_list)
    return cap_list

def inserto(anagram, capitals):
    for cap in capitals:
        inside = False
        for i in anagram:
            if i in cap:
                inside = True
            else:
                inside = False    
        if inside: print("Possible: ", cap)
    return 0

def main():
    capitals = retrieve_caps()
    while True:
        anagram = input("Anagram (else stop): ")
        #print(anagram)
        if anagram == "stop":
            break
        confronto(anagram, capitals)
        #inserto(anagram,capitals)
        
        

if __name__ == "__main__":
    main()