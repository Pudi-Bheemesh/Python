import os.path
import sys

fileName = input("Enter your filename: ")
if not os.path.isfile(fileName):
    print("the file '",fileName,"' Does not Exist")
    sys.exit(0)
infile = open(fileName,"r")
linelist = infile.readlines()

for i in range(2):
    print(i+1, ":", lineList[i])
input_word = input("Enter a word : ")
countWord = 0

for line in lineList:
    countWord += line.count(input_word)
print("The word", input_word, "appears", countWord, "times in the file")
