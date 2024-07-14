# Write a program that accepts input in this form: m3a1h5e4s2h6.
#    Here any character is followed by a number. The program should return a string where the character is repeated for the corresponding number of times.
#    Input: m3a1h5e4s2h6
#    Output: mmmahhhhheeeesshhhhhh

def input_output(input_string):
    i = 0
    result = ""
    while i < len(input_string):
        char = input_string[i]
        i += 1

        if i < len(input_string) and input_string[i].isdigit():
            count = int(input_string[i])
            result += char * count
            i += 1
        else:
            result += char
    return result

input_string = "m3a1h5e4s2h6"
output_string = input_output(input_string)
print(output_string)


