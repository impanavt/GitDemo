def bar(first,second,third,**options):
    if options.get("action")=="sum":
        print("The sum is :%d"%(first+second+third))
    if options.get("number")=="first":
        return first

result=bar(4,5,6,action='sum',number='first')
print("Result is :%d"%result)

#The "bar" function receives 3 arguments. If an additional "action" argument is received,
# and it instructs on summing up the numbers, then the sum is printed out.
# Alternatively, the function also knows it must return the first argument,
# if the value of the "number" parameter, passed into the function, is equal to "first".