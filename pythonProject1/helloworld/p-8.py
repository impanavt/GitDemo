# Python program to display all numbers within a range except the prime numbers
l=[]
c=[]
for num in range(0,20):
    for i in range(2,num):
        if num%i==0:
         c.append(num)
    else:
        l.append(num)
# for num in range(20,50):
#     if num not in l:
#         c.append(num)
# print(list(set(l)))
print(list(set(c)))
