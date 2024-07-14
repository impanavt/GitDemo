def merge_arrays(array1,array2):
    return sorted(set(array1+array2))



array1=[1,2,3,9,9,3,8,6,4,2]
array2=[9,2,0,5,5,8,2,7,5,7]
result=merge_arrays(array1,array2)
print(result)