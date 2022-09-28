num1 = 5.8
print(num1)
print(type(num1))

num2 = int(num1) #Elimina decimales forzosamente al convertirlo en entero
print(num2)
print(type(num2))

edad = input("Dime tu edad: ")
print(type(edad))
edad = int(edad)
print(type(edad))
nueva_edad = 1 + edad
nueva_edad = str(nueva_edad)
print("El año que viene cumples " + nueva_edad)