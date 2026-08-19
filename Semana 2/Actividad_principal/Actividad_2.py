# Cristian Alejandro Nolasco Vargas
# AL07264144
# 19/08/2026

import pdb

PRECIO_MAYOR_18 = 45
PRECIO_MENOR_EDAD = 30
PRECIO_MENOR_3 = 0

DESCUENTO_ADULTO = 0.12
DESCUENTO_PROFESOR = 0.1
DESCUENTO_ESTUDIANTE = 0.1


num_visitantes = int(input("Ingresa el número de visitantes:  "))
i = 1
total_general = 0

while (i <= num_visitantes):
    # pdb.set_trace()

    edad = int(input("\nIngrese la edad del visitante: "))

    if (edad >= 18):
        precio_boleto = PRECIO_MAYOR_18
    elif(edad <= 17 and edad >= 3):
        precio_boleto = PRECIO_MENOR_EDAD
    else:
        i += 1
        continue
    
    tipo_visitante = input("Ingresa el tipo de visitante (Adulto mayor / Profesor / Estudiante): ")

    if (tipo_visitante == "Adulto mayor"):
        precio_descuento = precio_boleto * (1 - DESCUENTO_ADULTO)
    elif (tipo_visitante == "Profesor"):
        precio_descuento = precio_boleto * (1 - DESCUENTO_PROFESOR)
    elif (tipo_visitante == "Estudiante"):
            precio_descuento = precio_boleto * (1 - DESCUENTO_ESTUDIANTE)
    else:
        precio_descuento = precio_boleto * 1         

    total_general = total_general + precio_descuento
    i += 1

print(f"\nTotal a pagar con descuento: {total_general}")