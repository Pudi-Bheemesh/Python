class int_conversion:
    def roman_to_int(self, input_value):
        romon_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_value = 0
        for val in range(len(input_value)):
            if val > 0 and romon_values[input_value[val]] > romon_values[input_value[val - 1]]:
                int_value += romon_values[input_value[val]] - 2 * romon_values[input_value[val - 1]]
            else:
                int_value += romon_values[input_value[val]]
        return int_value

print(int_conversion().roman_to_int('MMMCMLXXXVI'))
print(int_conversion().roman_to_int('MMMM'))
print(int_conversion().roman_to_int('C'))

