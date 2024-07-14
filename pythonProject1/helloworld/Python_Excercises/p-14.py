# Perform right and left rotation on list by two positions in Python
#    create a list and rotate the elements stored in the list by two positions
#    a. Right rotation
#    b. Left rotation
def rotated_array(array,rotations):
    rotated_array1=array[-rotations:]+array[:-rotations]
    rotated_array2 = array[rotations:] + array[:rotations]
    return rotated_array1,rotated_array2
array=[1,2,3,4,5,6,7,8,9]
rotations=3
rotated_array=rotated_array(array,rotations)
print(rotated_array)
