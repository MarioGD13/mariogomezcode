diccionario = {'c1': 'valor1', 'c2': 'valor2'}
print(diccionario)

resultado = diccionario['c2']
print(resultado)

cliente = {'nombre': 'juan', 'apellido': 'gomez', 'peso': 89}
print(cliente['peso'])

dic = {'c1': 55, 'c2': [10, 20, 30], 'c3': {'s1': 100, 's2': 200}}
print(dic['c3'])
dic_inside_dic = dic['c3']  # En lugar de estas 2 líneas
print(dic_inside_dic['s1'])  # Se puede hacer esto:

print(dic['c3']['s1'])
print(dic['c2'][1])

# Mini EJERCICIO:
# Dado el siguiente diccionario, imprime
# la letra E mayuscula
print("\nEJERCICIO")
dic2 = {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}
print(dic2['c2'][1].upper())

print("\nEjemplo3")
dic3 = {1: 'a', 2:'b'}
dic3[3] = 'c'
print(dic3)
dic3[2] = 'B'
print(dic3)
print(dic3.keys())
print(dic3.values())
print(dic3.items())

#  Agregar nueva clave y valor a diccionario
print("\n")
mi_dic4 = {"nombre": "Karen", "apellido": "Jurgens", "edad": 35, "ocupacion": "Periodista"}
mi_dic4["pais"] = "Colombia"
print(mi_dic4)
