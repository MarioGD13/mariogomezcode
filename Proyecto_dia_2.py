nombre = input("Cual es tu nombre: ")
ventas = float(input("Importe de ventas: "))


comision = round((ventas * 13)/100, 2)
print(f"Ok {nombre}. Este mes\nganaste ${comision}")