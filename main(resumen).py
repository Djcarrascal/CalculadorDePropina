#Aqui solicitamos los datos y valor de la compra del cliente.

nombre = input("\nIngrese su nombre: ")
while True:
    try:
       precio = float(input("\nIngrese el valor de su compra: "))
       break
    except ValueError:
        print("\nERROR.Solo se pueden ingresar numeros enteros")        

#Aqui definimos que el valor debe calcular la propina segun el valor de la compra:

if precio < 20:
    propina = precio * 0.10
elif precio >= 20 and precio < 50:
    propina = precio * 0.15
else:
    propina = precio * 0.20

#Aqui realizamos los prints que mostará el detalle de la compra
print("\nResumen de la compra")
print("\nCliente: ", nombre)
print("Valor bruto: ", precio)
print("Propina: ", propina)
print("Valor total: ", precio + propina)