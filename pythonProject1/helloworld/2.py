s=input()
print(any(filter(lambda x: x.isalnum(), s)))
print(any(filter(lambda x: x.isalpha(), s)))
print(any(filter(lambda x: x.isdigit(), s)))
print(any(filter(lambda x: x.islower(), s)))
print(any(filter(lambda x: x.isupper(), s)))