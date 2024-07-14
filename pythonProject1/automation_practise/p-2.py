l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
odd_index_position=l1[1::2]
even_index_position=l2[::2]
l3=sorted(set(odd_index_position+even_index_position),reverse=True)



print("Elements at odd index position from l1\n",odd_index_position)
print("Elements at even index position from l2\n",even_index_position)
print("Printing final third list\n",l3)