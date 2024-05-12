import re
def is_phonenumber(ph_num):
    if len(ph_num) != 12:
       return False
    for i in range(len(ph_num)):
        if i==3 or i==7:
            if ph_num[i] != "-":
               return False
            else:
                if ph_num[i].isdigit() == False:
                    return False
            return True

def ch_kphonenumber(ph_num):
    ph_no_pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    if ph_no_pattern.match(ph_num):
        return True
    else:
        return False
ph_num = input("Enter a phone number :")
print("Without using Regular Expression")
if is_phonenumber(ph_num):
   print("valid phone number")
else:
    print("Invalid phone number")
print("Using Regular Expression")
if ch_kphonenumber(ph_num):
    print("valid phone number")
else:
    print("Invalid phone number")
