# Input as a single line
# input_line = "[[1,2,3],[4,5,6],[7,8,9]]"
#
# # Remove the outer brackets and split the string at commas
# inner_lists = input_line[1:-1].split(",")
# print(inner_lists)
# #
# # # Parse the elements of each inner list
# # array_2d = [list(map(int, inner_list.strip("[]").split(","))) for inner_list in inner_lists]
# #
# # # Print row-wise
# # for row in array_2d:
# #     print(row)


# primes = (x for x in range(2, 100) if all(x % y != 0 for y in range(2, x)))
#
# # Printing the prime numbers
# print(list(primes))
#

# l=[]
# for num in range (100,200):
#     for j in range(2,num):
#         if num%j==0:
#             print("Not prime")
#         break
#     else:
#         l.append(num)
# print(l)


# my_list=[1,2,3]
# n_string=' '.join(str(item) for item in my_list)
# print(n_string)
#
# from functools import reduce
# numbers=[1,3,4,6,7,3,9]
# # # squared_numbers=map(lambda x:x**2 ,numbers)
# # # print(squared_numbers)
# print(reduce(lambda x ,y : x if x>y else y,numbers))


# add=lambda x,y:x+y
# result=add(2,5)
# print(result)

#
# numbers=[1,3,4,6,7,3,9]
# squared_dict={num:num*2 for num in numbers}
# print(squared_dict)
from itertools import zip_longest
def merge_dictioneries_alternatively(word1, word2):
    return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue=""))


word1 = 'a b c'
word2 = 'p q r'
res=merge_dictioneries_alternatively(word1, word2)
print(res)

# n=5
# from functools import reduce
# factorial=reduce(lambda x,y:x*y,range(1,n+1))
# print(factorial)

# #
# lst=[1,2,3,"viper","dboss",25,"viper",100,"viper"]
# index=[i for i in range(len(lst)) if lst[i]=='viper']
# print(index)

# print("even",list(filter(lambda x:x%2==0,range(10))))
# print("even: " ,[x for x in range(20) if x%2==0])
#
# print("odd: ",[x for x in range(25) if x%2!=0])
# print("odd: ",list(filter(lambda x:x%2!=0,range(20))))
#
# print("even_squares: ",[x*2 for x in range(10) if x%2==0] )
#
# list=[1,2,3,4,5]
# squared_dict={x:x*2 for x in list}
# print(squared_dict)
#
# print("odd_squares:",[x*2 for x in range(20) if x%2!=0])
#
# print("prime_no",[x for x  in range(2,100) if all (x%y!=0 for y in range(2,x))])
#
# print("even_squares:",[x*2 for x in range(20) if x%2==0])

# print("impana"[::-1])
#
# from functools import reduce
# print("sum",reduce(lambda x,y:x+y,range(10)))
#
# txt="i am creating powerful python one liners"
# print([x for x in txt.split() if len(x)>4])

# from datetime import datetime
# now=datetime.now()
# print(now.strftime ("%D-%M-%Y %H:%M:%S"))

# s='impana' 'is' 'beautiful'
# print(s.replace('impana', 'inchara'))

# lst=[1,2,3,"a","b","c",2,"a",1,"c",3]
# # st="abcd acdddd aaaabbbbcccdddd"
# seen=set()
# res=[]
# dup=[]
# for i in lst:
#     if i not in seen:
#         res.append(i)
#         seen.add(i)
#     else:
#         dup.append(i)
#
# print(res)



# class MyClass:
#     def __init__(self):
#         self._protected_var = "I am a protected variable"
#
#     def _protected_method(self):
#         return "I am a protected method"
#
# class SubClass(MyClass):
#     def access_protected(self):
#         return self._protected_var, self._protected_method()
#
# # Usage
# obj = SubClass()
# print(obj.access_protected())   # Accessing protected members from subclass
# print(obj._protected_var)


# def my_decorator(func):
#     def wrapper():
#         print("something is printed before a function is called")
#         func()
#         print('Something is printed after a function is called')
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print('Hello')
#
# say_hello()



# def sum(arr):
#     total_sum=0
#     n=len(arr)
#     for i in range(n):
#         total_sum+=i
#     return total_sum
# arr=[1,2,3,4,5]
# res=sum(arr)
# print(res)

