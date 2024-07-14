# If the following string is given as input to the program:
#
# abcdefgabc
#
# Then, the output of the program should be:
#
# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1

def count_check_character_occurance(string):
    char_count={}
    for char in string:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1

    return char_count
string="abcdefgabc"
occurances=count_check_character_occurance(string)
print(occurances)
for key,value in occurances.items():
 print(f'{key},{value}')

