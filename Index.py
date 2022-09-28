mi_texto = "Esto es una prueba"
resultado = mi_texto[2]
resultado2 = mi_texto[-1]
resultado3 = mi_texto.index("prueba") # Es sensible a mayus
resultado4 = mi_texto.index("a", 5, 11) # Desde el 5 hasta el anterior a 10 (no inclusivo) - imprime un 10
resultado5 = mi_texto.rindex("a") # De der a izq


print(resultado)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)
