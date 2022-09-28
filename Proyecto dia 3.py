#  Ejercicio: Pedir al usuario que introduzca
#  un texto, y después 3 letras, y que el
#  programa analice:
#  1.- Cuantas veces aparece cada letra
#  2.- Cuantas palabras hay en total
#  3.- Primera y ultima letra
#  4.- Palabras en orden inverso
#  5.- ¿Aparece la palabra "python"?

texto = input("Introduce un texto: ")
letras = input("Introduce 3 letras juntas para buscar"
               "en el texto: ")
texto = texto.lower()
letras = letras.lower()

letra1 = letras[0]
letra2 = letras[1]
letra3 = letras[2]
lista_letras = [letra1, letra2, letra3]
lista_texto = texto.split()
lista_texto.reverse()
python_aparece = "python" in lista_texto
print("\n RESULTADOS EJERCICIO")
print("1.- La letra '" + letra1 + "' aparece " + str(texto.count(letra1)) + " veces, la '" + letra2 + "' "
      + str(texto.count(letra2)) + " veces y la '" + letra3 + "' " + str(texto.count(letra3)) + " veces.")
print("2.- En total hay " + str(len(texto.split())) + " palabras")
print("3.- La primera letra del texto es una '" + texto[0] + "' y la última una '" + texto[-1] + "'.")
print("4.- Las palabras en orden inverso serían: " + " ".join(lista_texto))
print("5.- ¿Aparece la palabra 'python'?: " + str(python_aparece))

# OTRA MANERA DE HACERLO

print("\n")
print("OTRA FORMA DE HACERLO")
texto_ej_2 = input("Introduce un texto: ").lower()
letras_ej_2 = []
letras_ej_2.append(input("Introduce la primera letra: ").lower())
letras_ej_2.append(input("Introduce la segunda letra: ").lower())
letras_ej_2.append(input("Introduce la segunda letra: ").lower())
cantidad_letras_1 = texto_ej_2.count(letras_ej_2[0])
cantidad_letras_2 = texto_ej_2.count(letras_ej_2[1])
cantidad_letras_3 = texto_ej_2.count(letras_ej_2[2])
print(f"La letra '{letras_ej_2[0]}' aparece {cantidad_letras_1} "
      f"veces, la letra '{letras_ej_2[1]}' aparece {cantidad_letras_2} veces, "
      f"y la letra '{letras_ej_2[2]}' aparece {cantidad_letras_3} veces")
print("\nCantidad de palabras")
palabras_ej_2 = texto_ej_2.split()
print(f"Hay {len(palabras_ej_2)} palabras en tu texto")
print("\nTexto invertido")
palabras_ej_2.reverse()
texto_invertido = " ".join(palabras_ej_2)
print(f"El texto al reves es: {texto_invertido}")
print("\nBuscando 'python")
buscar_python_ej_2 = 'python' in texto_ej_2
dic = {True:"si", False:"no"}
print(f"La palabra 'Python' {dic[buscar_python_ej_2]} se encuentra en el texto")
