mi_set = set([1, 2, 3, 4, 5])  # Una manera de crearlo
print(type(mi_set))
print(mi_set)

otro_set = {1, 2, 3}  # Otra manera de crearlo
print(type(otro_set))
print(otro_set)

mi_set2 = set((1,2,3,4,5,1,2,3,4,5))
print(mi_set)  # Solo imprime del 1 al 5 ya que un set
# solo contiene valores únicos

# Tampoco puedo incluir una lista ni un diccionario
# en un set, pero si un tupple ya que es un elemento
# inmmutable (que no cambia) y eso es lo que un set requiere

mi_set3 = set((1,2,3,4,5))
print(len(mi_set3))
print(2 in mi_set3)
print(6 not in mi_set3)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

s1.add(4)
print(s1)
s1.remove(2)
print(s1)
s1.discard(6)  # La unica diferencia entre remove y
# discard es que remove devuelve error si le pides que
# elimine un elemento que no existe, y discard simplemente
# no haria nada

sorteo = s1.pop()  # Elimina un elemento aleatorio
print(sorteo)
print(s1)

s1.clear()  # Vacía el set
print(s1)
