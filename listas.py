mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']
resultado = len(mi_lista)
resultado2 = mi_lista[2]
print(type(mi_lista))
print(resultado)
print(resultado2)
print(mi_lista + mi_lista2)

mi_lista3 = mi_lista + mi_lista2
mi_lista3.append('g')
print(mi_lista3)
mi_lista3.pop(6)
print(mi_lista3)

mi_lista4 = ['g','o','f','l']
mi_lista4.sort()
print(mi_lista4)
mi_lista4.reverse()
print(mi_lista4)