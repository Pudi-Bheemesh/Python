year = int(input("Enter year: "))
leap_year = []
while(len(leap_year)<15):
    if(year % 4 == 0 or year %100 == 0) or (year % 400 == 0):
        leap_year.append(year)
    year += 1

print("Leap years are: ",leap_year)

str = input("Enter a string: ")
str1 = str[::-1]
if str == str1:
    print("Palidrome")
else:
    print("Not Palidrome")