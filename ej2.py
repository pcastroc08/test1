# Introducir dos números, visualizar primero el menor y luego el mayor
# Pedir el primer número
n1 = int(input("IIntroduce un número: "))
# Pedir el segundo número
n2 = int(input("Introduce otro número: "))
# Comprobar cuál es el menor y cuál es el mayor
if n1 < n2 :
    print(f"El número menor es: {n1}")
    print(f"El número mayor es: {n2}")
else : 
    print(f"El número menor es el {n2}")
    print(f"El número mayor es el {n1}")