"""Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual 
y el número de años, y muestre por pantalla el capital obtenido en la inversión."""

cantidad = float(input('Ingresa la cantidad a invertir: \n'))
interes = float(input('Ingresa el interes anual: \n'))
anios = float(input('Ingresa los años que vas a invertir: \n'))

intereses = cantidad * interes * anios

print(f'Los intereses generados seran {intereses}')