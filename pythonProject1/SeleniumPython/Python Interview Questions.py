# grades = [ ('Raju', 91),  ('Ram', 98),  ('Raju', 81),  ('Megha', 88) , ('Ram', 78), ('Raju', 88)]
4)
 def average_scores(input_list):
    data_scores = {}
    for name, score in input_list:
        if name in data_scores:
            data_scores[name].append(score)
        else:
            data_scores[name] = [score]

    average_scores = {}

    for name, scores in data_scores.items():
        average = sum(scores) / len(scores)
        average_scores[name] = average

    return average_scores

input_list = [('Raju', 91), ('Ram', 98), ('Raju', 81), ('Megha', 88), ('Ram', 78), ('Raju', 88)]
output_dict = average_scores(input_list)

for name, average in output_dict.items():
    print(f"{name}: {average:.2f}")

# 1)X1Y2A1B2A2X1- Expected o/p XYYABBAAX
  def convert_string(input_str):
    result = ""
    i = 0

    while i < len(input_str):
        char = input_str[i]
        i += 1

        if i < len(input_str) and input_str[i].isdigit():
            count = int(input_str[i])
            result += char * count
            i += 1
        else:
            result += char

    return result
input_str = "X1Y2A1B2A2X1"
output_str = transform_string(input_str)
print(output_str)

5)def remove_consecutive_duplicates(input_str):
    if not input_str:
        return ""

    result = input_str[0]
    for i in range(1, len(input_str)):
        if input_str[i] != input_str[i - 1]:
            result += input_str[i]

    return result

input_str = "HAAPPYYAAY"
output_str = remove_consecutive_duplicates(input_str)
print(output_str)

or using enumerate where index and respective characters  are taken as consideration if character repeates then that is removed

input_str = "HAAPPYYAAY"
output_str = ''.join(char for i, char in enumerate(input_str) if i == 0 or char != input_str[i - 1])
print(output_str)

# 2)Here reversed function is used to craete the sample in reversed order from last.It starts from last element and remove last occuring repeating elements
def remove_last_occurrence_of_repeating_elements(sample_list):
    seen = {}
    result = []

    for item in reversed(sample_list):
        if item not in seen:
            seen[item] = True
            result.append(item)

    return list(reversed(result))
sample_list = [3, 2, 1, 3, 3, 5, 4, 5]
output_list = remove_last_occurrence_of_repeating_elements(sample_list)
print(output_list)


# 6)Here we defined longest vowels sequence function and we are iterating over the  characters for each char in vowels we are adding to current sequence and then when atlast where current sequence vowels count is exceeding the previous length of vowels then the ouptput of longest vowesl length is printed
def longest_vowel_sequence(input_str):
    vowels = "aeiouAEIOU"
    current_sequence = ""
    longest_sequence = ""

    for char in input_str:
        if char in vowels:
            current_sequence += char
        else:
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence
            current_sequence = ""


    if len(current_sequence) > len(longest_sequence):
        longest_sequence = current_sequence

    return longest_sequence

input_str = 'xcaeduoimnooonioeauizvaeiuof'
output_sequence = longest_vowel_sequence(input_str)
print(output_sequence)

# 7) Unpack the data into a dictionary format as below.
#     input_data = {'Name': ['John', 'Ravi'], 'Age': [25, 35], 'City': ['New York', 'Gudur']}
# 	output_dict = {'John': {'Age': 25, 'City': 'New York'}, 'Ravi': {'Age': 35, 'City': 'Gudur'}}
#     Here we need to unpack the dictionery items so we are iterating over the length so it can be of Name,age or city as all of them  are having the same number of elements

input_data = {'Name': ['John', 'Ravi'], 'Age': [25, 35], 'City': ['New York', 'Gudur']}
output_dict = {}

for i in range(len(input_data['Name'])):
    name = input_data['Name'][i]
age = input_data['Age'][i]
city = input_data['City'][i]

output_dict[name] = {'Age': age, 'City': city}

print(output_dict)


or
for unpacking we can use the ZIP inbuilt dictionery function .where the Name Age and City are unzipped so indivisually there are printed with corresponding values

input_data = {'Name': ['John', 'Ravi'], 'Age': [25, 35], 'City': ['New York', 'Gudur']}

output_dict = {}
for name, age, city in zip(input_data['Name'], input_data['Age'], input_data['City']):
    output_dict[name] = {'Age': age, 'City': city}

print(output_dict)


# 3) input_ip = 'fd18:0e00:0083::/48'. Truncate leading 0's in each octet. Exp o/p -  'fd18:e00:83::/48'
# here we are using inbuilt function lstrip to remove all the leading zeroes

input_ip='fd18:0e00:0083::/48'
split_input_ip=input_ip.split(':')
for i in range(len(split_input_ip)):
    split_input_ip[i]=split_input_ip[i].lstrip('0')
output=':'.join(split_input_ip)
print(output)














