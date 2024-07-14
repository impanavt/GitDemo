# def calculate_sum(dictionery):
#     if not dictionery:
#         return "Dictionery is empty"
#     else:
#         sum_values = sum(dictionery.values())
#         return sum_values
#
#
# my_dict = {'a': 5, 'b': 10, 'c': 15, 'd': 20}
# sum_values = calculate_sum(my_dict)
# print(sum_values)

# students=[]
# def insert_student_properties(name,age,marks):
#     std=dict()
#     std['name']=name
#     std['age']=age
#     std['marks']=marks
#     students.append(std)
#     return students
# students=insert_student_properties('impana','23','100')
# students=insert_student_properties('pavan','21','120')
# students=insert_student_properties('impanavt','20','180')
# students=insert_student_properties('impanagowda','27','190')
# print(students)



# def get_dict_from_array(arr):
#     d=dict()
#     for i in range(len(arr)):
#       key=arr[i]
#       value=i
#       d[key]=value
#     return d
# arr=[23,78,9,56]
# res=get_dict_from_array(arr)
# print(res)

# def remove_duplicates(lst):
#     return list(set(lst))
#
# my_list=[1,2,3,3,4,5,6]
# unique_list=remove_duplicates(my_list)
# print(unique_list)


# def merge_dictioneries(dict1,dict2):
#      merged_dict={**dict1,**dict2}
#      return merged_dict
# dict1={'a':1,'b':2}
# dict2={'c':3,'d':4}
# merged_dict=merge_dictioneries(dict1,dict2)
# print(merged_dict)

# def animal(name:str):
#      print(name)
#      return animal

# animal("cat")("dog")("elephant")

#
#

#
#

s = 'My name is viper'
print(s.replace('viper','vishalaaaa'))
import re
print(re.sub('viper','ryder', s))
