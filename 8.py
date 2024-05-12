def final_word(string):
    if len(string) < 2:
        return None
    else:
        final = string[0]+string[1]+string[-2]+string[-1]
        return final

string = input("Enter your string: ")
print(final_word(string))
