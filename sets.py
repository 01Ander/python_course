list_a = [10, 20, 25, 20, 5]
list_b = [10, 20, 24, 19, 4]

set_a = set(list_a)
set_b = set(list_b)

print(set_a | set_b)
print(set_a & set_b)
print(set_a - set_b)
print(set_a ^ set_b)
print(len(set_a | set_b))


# # Unión (valores de ambos)
# print(a | b)   # {1, 2, 3, 4, 5, 6}

# # Intersección (valores en común)
# print(a & b)   # {3, 4}

# # Diferencia (valores solo en 'a')
# print(a - b)   # {1, 2}

# # Diferencia simétrica (valores que están en uno u otro, pero no en ambos)
# print(a ^ b)   # {1, 2, 5, 6}
