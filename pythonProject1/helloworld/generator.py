# Generators in Python provide an efficient way to iterate over sequences without the overhead of storing the entire sequence in memory.
#
# The yield keyword in Python is used to create generators


# def create1():
#     i=1
#     list=[]
#     while i<=200:
#         i+=1
#         list.append(i)
#     return list
#
# print(create1())
#
# Without creating a list to store entire sequence in memory use yield (to utilize memory at best)-which stops the value gets genearted only when called

def create1():
    i=1
    while i<=200:
        yield i
        i+=1
# print(create1())
x=create1()
print(next(x))
print(next(x))
print(list(x))