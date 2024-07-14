try:
    age=int(input('Age: '))
    income=200000
    risk=income/age
    print(Age)
except ZeroDivisionError:
   print('income cannot be divided by zero')
except ValueError:
   print('Invalid entry')