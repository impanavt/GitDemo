# Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list

# Given:
# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
# sample_dict = {'Mahesh':47, 'Suresh':69, 'Lokesh':76, 'Venkatesh':97}

# Expected:
# After removing unwanted elements from list [47, 69, 76, 97]

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Mahesh': 47, 'Suresh': 69, 'Lokesh': 76, 'Venkatesh': 97}
list = []
for key, value in sample_dict.items():
    if value in roll_number:
        list.append(value)
print("After removing unwanted elements from list", list)