# write
# with open('notas.txt', 'w', encoding="utf-8") as f:
#     f.write("Linea 1\n")
#     f.write("Linea 2\n")

# add
# with open('notas.txt', 'a', encoding='utf-8') as f:
#     f.write('Linea 3\n')

# read
with open("notas.txt", "r", encoding="utf-8") as f:
    contenido = f.read()

print(contenido)


with open("notas.txt", "r", encoding="utf-8") as f:
    for linea in f:
        print(linea.strip())  # strip() quita \n y espacios laterales
