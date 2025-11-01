list_a = [10, 20, 25, 20, 5]
list_b = [10, 20, 24, 19, 4]

set_a = set(list_a)
set_b = set(list_b)

print(set_a | set_b)
print(set_a & set_b)
print(set_a - set_b)
print(set_a ^ set_b)
print(len(set_a | set_b))
