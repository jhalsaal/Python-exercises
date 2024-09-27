"""Escribir un programa que pregunte al usuario por el número de horas trabajadas y 
el coste por hora. Después debe mostrar por pantalla la paga que le corresponde."""

hour_jop = float(input("¿Cuantas horas trabajaste?"))
price_hour = float(input('¿Cuanto cuestan las horas?'))

result =hour_jop*price_hour
print(f'El valor que deben pagarte por {hour_jop} horas trabajadas es {result}')