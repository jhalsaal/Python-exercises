"""Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable, y muestre por 
pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa 
corporal calculado redondeado con dos decimales."""

peso= float(input("Ingresa tu peso en kilogramos: \n"))
estatura = float(input("Ingresa tu estatura en metros"))

imc = peso/(estatura**2)

print(f'Tu imc calculado es: {imc:.2f}')