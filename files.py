# write
# with open('notas.txt', 'w', encoding="utf-8") as f:
#     f.write("Linea 1\n")
#     f.write("Linea 2\n")

# add
# with open('notas.txt', 'a', encoding='utf-8') as f:
#     f.write('Linea 3\n')

# read
# with open("notas.txt", "r", encoding="utf-8") as f:
#     contenido = f.read()

# print(contenido)

# read all
# with open("notas.txt", "r", encoding="utf-8") as a:
#     for linea in a:
#         print(linea.strip())  # strip() quita \n y espacios laterales


import csv

# with open('files/usuarios.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerow(['name', 'age'])
#     writer.writerow(['andersson', 31])
#     writer.writerow(['Ana', 40])

with open('files/usuarios.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for fila in reader:
        print(fila['name'], '→', fila['age'])
