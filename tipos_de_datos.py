Nombre = 'Andersson'
# convierte cualquier tipo de dato a un string
Welcome = f'Hola {Nombre} bienvenido'

# del Nombre #elimina una variable
print(Welcome)


# operadores de pertenencia - in & not in
# dan como resultado un booleano

print("Andersson" in Welcome)  # True
print('Andersson' not in Welcome)  # False


# ..............Datos compuestos..............

# arrays - se pueden modificar
lista = ['Andersson', 'Rincon', True, 31]
print(lista[0])

# tuplas - no se puede modificar
tupla = (1, 2, 3, 4,)


# conjuto -set
conjunto = {"hola", 1.25, True}
# no puede accederse directamente a los elementos por los indices, no almacena datos duplicados

# diccionario -dict  ..... key : value  ((objeto??))
diccionario = {
    'nombre': 'Andersson',
    'apellido': 'Rincon'
}
print(diccionario['nombre'])


print(type(1))
