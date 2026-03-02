#Aqui solicitamos los datos y valor de la compra del cliente.

nombre = input("\nIngrese su nombre: ")
while True:
    try:
       precio = int(input("\nIngrese el valor de su compra: "))
       break
    except ValueError:
        print("\nERROR.Solo se pueden ingresar numeros enteros")

        

#Aqui definimos que el valor debe calcular la propina segun el valor de la compra:

total1 = precio * 0.10
total2 = precio * 0.15
total3 = precio * 0.20


if precio < 20:
    print(f"\nEl valor de su compra con propia es de: {precio + total1}\n")          
if precio >= 20 and precio < 50:
    print(f"\nEl valor de su compra con propia es de: {precio + total2}\n")
if precio >= 50:
    print(f"\nEl valor de su compra con propia es de: {precio + total3}\n")

print("\nResumen de la compra")
print("\nCliente: ", nombre)
print("Valor bruto: ", precio)
print("Propina: ", )