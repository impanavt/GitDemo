# f=open('impana.txt','w')
# print(f)
# text=f.write("you deserve the best l ")
# # f.close()

# with open('impana.txt','a') as f:
#     f.write('you are genious')

# f


# f=open('impana.txt','w')
# lines=['line1\n' ,'line2\n','line3\n']
# f.writelines(lines)
# f.close
# from functools import reduce
# # from itertools import zip_longest
# # list1=[1,2,3,4,5,67]
# list2=[3,4,5,8,9,34,89]
# result=reduce(lambda x,y:x+y ,list2)
# print(result)
#

# from itertools import zip_longest
#
# list1 = [1, 2, 3]
# list2 = [4, 5, 6, 7]
#
# # Using map with zip_longest to handle lists of different lengths
# summed_lists = map(lambda x, y: x + y, list1, list2)
#
# # Convert the result to a list and print it
# print(list(summed_lists))  # Output: [5, 7, 9]
#
# # Using zip_longest to fill missing values with 0
# summed_lists_with_fill = map(lambda x, y: x + y, zip_longest(list1, list2, fillvalue=0))
# print(list(summed_lists_with_fill))  # Output: [5, 7, 9, 7]




# def starts_with(string,prefix):
#     if string.startswith('prefix'):
#         return True
#     else:
#         return False
#
# user_input=input('Enter a string')
# converted-string[:4].uppe()+user_input[4:]


# def count_occurances(string,substring):
#     count=string.count(substring)
#     return count
#
# string='I love music,I love painting,I love Art'
# substring='love'
# res=count_occurances(string,substring)
# print(res)

# list1=[1,3,5,6,7,9]
# list2=[2,3,5,6,8]
# list1[-1:]=list2
# print(list1)


# def sum_even():
#     total_sum=0
#
#     for num in range(2,100):
#         if num%2==0:
#             total_sum+=num
#     return total_sum
#
# print(sum_even())
#
# def shift_zeroes(string):
#     for i in string:
#         if i==0:
#             string.remove(i)
#             string.append(i)
#     return string
#
# string=[5,6,0,1,0,10,0,2,0]
# res=shift_zeroes(string)
# print(res)

# if a string contains a given string
# def check_contain(string,substring):
#     # string=string.split('')
#     if  substring in string:
#         return True
#     return False
#
# string='Hello how are you '
# substring='how'
# res=check_contain(string,substring)
# print(res)

# merge two list

# def merge_list(list1,list2):
#     list1.extend(list2)
#     return list1
#
# list1=[2,3,4,5,6]
# list2=[2,5,6,7,8]
# res=merge_list(list1,list2)
# print(res)

#
# def count_occurances(string):
#     dict={}
#     words=string.split()
#     for word in words:
#          if word in dict:
#             dict[word]+=1
#
#          else:
#             dict[word]=1
#     return dict
#
# string='cat cat dog cat hen hen'
# res=count_occurances(string)
# # print(res)
#
# for key,value in res.items():
#      print(f'{key}{value}', end=' ')  o/p-cat3 dog1 hen2

# def string_in_list(list,string):
#     if string in list:
#         return True
#     return False
#
#
#
#
# list=['aaa','a','xyz']
# string='kj'
# res=string_in_list(list,string)
# print(res)


def count_unique_characters(s):
    # Initialize an empty set to store unique characters
    unique_chars = set()

    # Iterate through each character in the string
    for char in s:
        # Add character to the set
        unique_chars.add(char)

    # Return the number of unique characters
    return len(unique_chars)


# Example usage:
input_string = 'FUNNY'
result = count_unique_characters(input_string)
print(f"Number of unique characters in '{input_string}' is: {result}")



