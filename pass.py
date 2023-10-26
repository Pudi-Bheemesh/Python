pasw = input("Enter your new password: ")
a=A=d=sp=0
salp="abcdefghijklmnopqrstuvwxyz"
lalp="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
spchar="$@_<*&^%:>#!?"
dgt="0123456789"
if (len(pasw)>=6) and (len(pasw)<=8):
    for i in pasw:
        if i in salp:
            a+=1       
        if i in lalp:
            A+=1
        if i in dgt:
            d+=1          
        if(i in spchar):
            sp+=1       
if (a>=1 and A>=1 and sp>=1 and d>=1):
    print("Valid Password")
else:
    print("Invalid Password")
    if len(pasw) > 8:
        print("Reason: Too long")
    if len(pasw) < 6:
        print("Reason: Too short")
    if A == 0:
        print("Reason: No capital Alphabets found")    
    if a == 0:
        print("Reason: No small Alphabets found")
    if d == 0:
        print("Reason: No Digits found")
    if sp == 0:
        print("Reason: No Special character found")