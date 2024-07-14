# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

sentence=input("Enter a sentence: ")
upper_count=0
lower_count=0
for char in sentence:
    if char.isupper():
        upper_count+=1
    elif char.islower():
        lower_count+=1
print("UPPER CASE", upper_count)
print("LOWER CASE", lower_count)
