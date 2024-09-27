"""Escribir un programa que pida al usuario dos números enteros y muestre por pantalla 
la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números 
introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división 
entera respectivamente."""

print("Ingresa 2 numeros enteros")
num_one = int(input("Ingresa el primer numero entero: \n"))
num_two = int(input("Ingresa el segundo numero entero: \n"))

c = num_one/num_two
r = num_one%num_two

print((f'El cociente de la division entre {num_one} y {num_two}: es {c}'))
print((f'El residuo de la division entre {num_one} y {num_two}: es {r}'))