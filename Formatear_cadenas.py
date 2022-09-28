x=10
y=5

print("Mis numeros son " + str(x) + " y " + str(y))

#Para evitar esto poco practico, lo haríamos así con
#el método antiguo:

print("Mis numeros son {} y {}".format(x,y))

print("La suma de {} y {} es igual a {}".format(x,y,x+y))

#Pero con el nuevo método y más legible, sería así:

color = "Azul"
matricula = 7569

print(f"Mi coche es {color} y su matrícula es {matricula}")