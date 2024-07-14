# squares=[]
# for i in range(10):
#     squares.append(i**2)
# print("Squares is: ",squares)

#
# sum from 1 to 100#
# sum = 0
# num = 0
# while num <= 100:
#     sum += num
#     num += 1
# print(sum)


# string = "Python Programming"
# vowels = 'aeiouAEIOU'
# char_count = {}
#
# for char in string:
#     if char in vowels:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
#
# print(char_count)

# to multiply all the numbers in the list using for loop [1,2,3,4,5]
# list=[1,2,3,4,5]
# product=1
# for num in list:
#     product*=num
# print(product)

# list=[1,2,3,4,5]
# sum=0
# for num in list:
#     sum+=num
# print(sum)

# reverse a string

# string="Impana is beautiful"
# reversed_string=[]
# words=string.split()
# for word in words:
#     reversed_word=""
#     i=len(word)-1
#     while i>=0:
#         reversed_word+=word[i]
#         i-=1
#     reversed_string.append(reversed_word)
# reversed_string=" ".join(reversed_string)
# print(reversed_string)



# string='impana'
# reversed_string=[]
# i=len(string)-1
# while i>=0:
#     reversed_string+=string[i]
#     i-=1
#     reversed_string=''.join(reversed_string)
# print(reversed_string)

# to print each item and it's corresponding type

# list=[1,2.2,'python']
# for item in list:
#     print(type(item))


# while True:
#  user_input=input("enter the text: ")
#  if user_input=='quit':
#   break

# p=[]
# for num in range(2,50):
#     for i in range(2,num):
#         if num%i==0:
#           print("Not prime")
#           break
#     else:
#          p.append(num)
# print(p)

# fibonacci series
# def generate_fibonacci_series(n):
#     series=[0,1]
#     while len(series)<n:
#         next_num=series[-1]+series[-2]
#         series.append(next_num)
#     return  series
# n=10
# fibonacci_series=generate_fibonacci_series(n)
# print(fibonacci_series)

# dict={'ran'=12,'raju'=89,'reena'=67}
# for key,value in dict.items():
#     print(f'{key}:{value}')

# factorial
# def factorial (n):
#     result=1
#     for i in range(1,n+1):
#         result=result*i
#     return result
# n=10
# fact=factorial(n)
# print(fact)

# greatest number in list
# def find_max(nums):
#     if not nums:
#         return None
#
#     max_value=nums[0]
#
#     for num in nums:
#         if num>max_value:
#             max_value=num
#     return max_value
#
# nums=[12,45,89,23,70,67]
# res=find_max(nums)
# print(res)

# use a while loop to print all numbers from 10 to 1 in reverse order
# num=10
# while num>=1:
#     print(num)
#     num-=1

# python program to find the smallest number in a fiven list

# def smallest_number(nums):
#     if not nums:
#         return None
#
#     min_value=nums[0]
#
#     for num in nums:
#         if num<min_value:
#             min_value=num
#     return min_value
#
# nums=[2,4,67,89,12,8]
# res=smallest_number(nums)
# print (res)

# to print the elements of a list in revesre order

# array=[23,56,78,12,78]
# i=len(array)-1
# reversed_array=[]
# while i>=0:
#     reversed_array.append(array[i])
#     i-=1
# print(reversed_array)

# print the sum of all even numbers and odd numbers seperately in the range 1 and 50

# def total_sum():
#     even_sum=0
#     odd_sum=0
#     for number in range(1,51):
#         if number%2==0:
#             even_sum+=number
#
#         else:
#             odd_sum+=number
#
#     return even_sum,odd_sum
#
# result=total_sum()
# print(result)
#
# or for number in range(1,51,2):
#     even_sum+=number

# use a for loop to print each eleemnts in tuple

# tuple=(1,2,3,4,5)
# list=list(tuple)
# print(list)
# for item in list:
#  print(item)

# Using a loop write a srcipt to convert a number [1,2,3,4,5]  to string list ['1','2','3','4','5']

# list=[1,2,3,4,5]
# string_list=[]
# for num in list:
#     string_list.append(str(num))
# print(string_list)


# to check if a number is palindrome or not

# number


# using loop print python 10 times

# for i in range(10):
#     print("python")

# to iterate over a string and print each letter on a seperate line

# string="Impana"
# for char in string:
#     print(char)


# to check if a number is palindrome or not ?

# def check_palindrome(number):
#     original_number=number
#     reverse_number=0
#
#     while number>0:
#      digit=number%10
#      reverse_number=reverse_number*10+digit
#      number=number//10
#
#     return original_number==reverse_number
#
# number=int(input("Enter a number to check if it's palindrome: "))
# if check_palindrome(number):
#     print(number,"Palindrome")
# else:
#     print(number,'is not palindrome')
#
#



# leap year between 2000 and 2020 ?

# def is_leap_year(year):
#     return (year%4 and year%100!=0)or (year%400==0)
#
# print("Leap year between 2000 and 2020")
# for year in range(2000,2020):
#     if is_leap_year(year):
#         print(year)

# length of each word in string
# string="python is fun"
# words=string.split()
# for word in words:
#     print(len(word))


# to print all numbers from 1 to 100 having 3 in them
# result=[]
# for number in range(100):
#     if '3' in str(number) :
#         result.append(number)
#
# print(result)



# countdown from 10

# count=10
# while count>=0:
#     print(count)
#     count-=1


# calculate average of all numbers in a list

list=[12,34,25,78,67]
total=0
count=0
for num in list:
    total+=num
    count+=1

average=total/count

print("Average:",average)












