import difflib

def string_similarity(string_1, string_2):
    Stringmatch_ratio = difflib.SequenceMatcher(a=string_1.lower(),b=string_2.lower())
    return  Stringmatch_ratio.ratio()


string_1 = "Python Exercises"
string_2 = "Python Exercises"

print("Given Strings: ",end=" ")
print(string_1,end=", ")
print(string_2)
print("Similarity is equal to: ",end=" ")
print(string_similarity(string_1,string_2))

string_1 = "Python Exercises"
string_2 = "Python Exercise"

print("\nGiven Strings: ",end=" ")
print(string_1,end=", ")
print(string_2)
print("Similarity is equal to: ",end=" ")
print(string_similarity(string_1,string_2))