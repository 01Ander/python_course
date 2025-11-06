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


# import json
# write
# usuario = {
#     "nombre": "Andersson",
#     "edad": 30,
#     "skills": ["Python", "Data", "QA"]
# }

# with open("usuario.json", "w", encoding="utf-8") as f:
#     json.dump(usuario, f, indent=4, ensure_ascii=False)

# read
# with open("usuario.json", "r", encoding="utf-8") as f:
#     data = json.load(f)

# print(data["skills"])


# from pathlib import Path

# # Carpeta
# ruta_carpeta = Path("data")
# ruta_carpeta.mkdir(exist_ok=True)  # la crea si no existe

# # Archivo dentro de la carpeta
# ruta_archivo = ruta_carpeta / "ejemplo.txt"

# # Escribir
# ruta_archivo.write_text("Hola desde pathlib", encoding="utf-8")

# # Leer
# print(ruta_archivo.read_text(encoding="utf-8"))
