import statistics
def mean_median_mode(list1):
    return statistics.mean(list1),statistics.median(list1),statistics.mode(list1)
# After return it's end of function 
a,b,c=mean_median_mode([3,5,45,3,2,1,89])
print(f"Mean is {a}\n Median is {b}\n Mode is {c}")