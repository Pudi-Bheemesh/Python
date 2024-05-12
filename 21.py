class Palindrome_String:
    def __init__(self):
        self.is_Palindrome = False

#check whether given string is plaindrome         
    def check_Palindrome(self, myStr):
        if myStr == myStr[::-1]:
            self.is_Palindrome = True
        else:
            self.is_Palidrome = False
            
        return self.is_Palindrome
    
#Implementation of inheritance           
class Palidrome_Intger(Palindrome_String):
    def __init__(self):
        self.is_Palindrome = False

#Implementation of Polymorphism and check whether given integer is palindrome
        
    def check_Palindrome(self, value):
        tempValue = value
        rev = 0
        while tempValue != 0:
            dig = tempValue % 10
            rev = (rev*10) + dig
            tempValue = tempValue //10
            
        if value == rev:
            self.is_Palidrome = True
        else:
            self.is_Palidrome = False
        
        return self.is_Palindrome

input_string = input("Enter a string : ")
string_Obj = Palindrome_String()
if string_Obj.check_Palindrome(input_string):
    print("Given string is a Palindrome")
else:
    print("Given string is not a Palindrome")

integer_value = int(input("Enter a integer : "))    
intger_Obj = Palidrome_Intger()
if intger_Obj.check_Palindrome(integer_value):
    print("Given integer is a Palindrome")
else:
    print("Given integer is not a Palindrome")
