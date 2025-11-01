fruits = ["apple", "banana", "apple", "orange", "banana"]

fruits_set = set(fruits)
print(fruits_set, type(fruits_set))

fruits_list = list(fruits_set)
print(fruits_list, type(fruits_list))

fruits_tuple = tuple(fruits_list)
print(fruits_tuple, type(fruits_tuple))

fruits_dict = {i: fruit for i, fruit in enumerate(fruits_list)}
print(fruits_dict, type(fruits_dict))
