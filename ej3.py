# Leer un número entero y decir si es positivo, negativo o nulo
# Pedir un número entero
n = int(input("Dame un número: "))
# Comprobar si el número es positivo, negativo o nulo
if n == 0 :
    print("El número es nulo")
elif n > 0 :
    print("El número es positivo")
else :
    print("El número es negativo")
