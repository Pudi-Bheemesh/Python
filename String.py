class Student:
    
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        
    def __eq__(self, other):
        return self.mark1 == other.mark1 and self.mark2 == other.mark2 and self.mark3 == other.mark3

def compare_students(student1, student2):
    if student1 == student2:
        print(f"{student1.name} and {student2.name} have scored the same marks in all three subjects.")
    else:
        print(f"{student1.name} and {student2.name} have not scored the same marks in all three subjects.")

# Creating two student objects
student1 = Student("Alice", 90, 85, 95)
student2 = Student("Bob", 90, 85, 95)

# Comparing the two student objects
compare_students(student1, student2)
import math as m
num=int(input("enter number"))
def is_perfect(k):
    s=int(m.sqrt(k))
    return s*s==k
def is_Fib(r):
    return is_perfect(5*r*r+4) or is_perfect(5*r*r-4)
if is_Fib(num):
    print("yes")
else:
    print("no")