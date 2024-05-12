test = input("Enter the String: ")
test_list = test.split()
res = ""
max_len = 0
for ele in test_list:
    vow_len = len([el for el in ele if el in ['a','e','i','o','u']])
    if vow_len > max_len:
        max_len = vow_len
        res = ele

print(res)