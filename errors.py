import math

# interceptar un error en especifico

# try:
#     number = int(input('Add a number: '))
#     print(f'Doble is :{number*2}')
# except ValueError:
#     print('Error: add a valid number')
# else:
#     print('Conversion success')
# finally:
#     print('Program end')


# capturar varios errores

try:
    lista = [1, 2, 3]
    print(lista[5])
    numero = int('abc')
except IndexError:
    print('Error: indice out of range')
except ValueError:
    print('Error: invalid conversion')


try:
    x = int("hola")
except Exception as e:
    print(f"Ocurrió un error: {e}")


while True:
    try:
        edad = int(input('Edad: '))
        if edad < 0:
            # raise lanza un error manual
            raise ValueError('la edad no puede ser negativa')
        break
    except ValueError as e:
        print(f'entrada invalida {e}')


while True:
    try:
        number = int(input('Add the number: '))
        if number < 0:
            print('Add a positive number')
            continue
        sqrt = float(math.sqrt(number))
        print(f'{sqrt:.2f}')
        break
    except ValueError:
        print('Add a number')
