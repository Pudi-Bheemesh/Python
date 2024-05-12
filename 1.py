marks_1_test = int (input("Enter the marks in the first test: "))
marks_2_test = int (input("Enter the marks in second test: "))
marks_3_test = int (input("Enter the marks in third test: "))

if(marks_1_test > marks_2_test):
    if(marks_2_test > marks_3_test):
        totalofBest2 = marks_1_test + marks_2_test
    else:
        totalofBest2 = marks_1_test + marks_3_test
elif (marks_1_test > marks_3_test):
    totalofBest2 = marks_1_test + marks_2_test
else:
    totalofBest2 = marks_2_test + marks_3_test

AverageofBest2 = totalofBest2/2

print(AverageofBest2)