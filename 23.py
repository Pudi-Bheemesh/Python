string = input("Enter your string: ")
final_string = ""
for i in range(0, len(string)):
    for j in range(i+1, len(string)):
        if string[i] == string[j]:
            final_string = final_string + string[j]
print(final_string)