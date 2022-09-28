#  Los tuples no son modificables
#  por tanto, son a prueba de daños
#  y ocupan menos espacio en memoria

mi_tuple = (1, 2, 3, 4)  # Puede hacerse sin ()
print(type(mi_tuple))

print(mi_tuple[0])
mi_tuple2 = (1, 2, (10, 20), 4)  # tupple dentro de otro
print(mi_tuple2[2][1])

mi_tuple3 = (1,2,3)
x, y, z = mi_tuple3
print(x, y, z)
print(mi_tuple3.count(1))  # El metodo count permite contar
# el nº de veces que aparece el elemento del argumento

print(mi_tuple3.index(2))  # Metodo index para consultar
# en que numero de indice se encuentra el elemento
