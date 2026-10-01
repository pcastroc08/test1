# Introducir una letra y visualizar si es vocal o consonante
# Pedir una letra
letra = input("Introduce una letra: ")
# Comprobar si la letra es vocal o consonante
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u' :
    print(f"La letra {letra} es una vocal")
else :
    print(f"La letra {letra} es una consonante")