def OctToHex(octal_num):
    return hex(int(octal_num, 8))
def BinToDec(binary_num):
    return int(binary_num, 2)

binary_num = input("Enter the Binary Number= ")
decimal_num = BinToDec(binary_num)
print("\nEquivalent Decimal Value = ", decimal_num)

octal_num = input("Enter Octal Number: ")
hexa_num = OctToHex(octal_num)
print("\nEquivalent Hexadecimal Value =", hexa_num.upper())
