mi_texto = "HolA qUe Tal"
print(mi_texto.upper())
print(mi_texto.lower())
print(mi_texto[3].lower())
print(mi_texto.split()) # Separa palabras en lista
print(mi_texto.split("a")) # Utiliza la A como separador
# Es sensible de mayus por eso solo me separa la ultima a

a = "aprender"
b = "python"
c = "es"
d = "genial"
e = "-".join([a,b,c,d])
print(e)

print(mi_texto.find("Z"))
print(mi_texto.replace("HolA", "Adios"))

lista = ["La","legibilidad","cuenta"]
print(" ".join(lista))

print(mi_texto.replace("HolA", "Adios").replace("Tal", "mal"))