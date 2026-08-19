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

while (i <= num_visitantes):
    edad = int(input("Ingrese la edad del visitante: "))
    tipo_visitante = input("Ingresa el tipo de visitante (Adulto mayor / Profesor / Estudiante): ")

    if (edad >= 18):
        precio_boleto = PRECIO_MAYOR_18
    elif(edad <= 17 and edad >= 3):
        precio_boleto = PRECIO_MENOR_EDAD
    else:
       continue

    if (tipo_visitante == "Adulto mayor"):
        precio_descuento = precio_boleto * (1 - DESCUENTO_ADULTO)
    elif (tipo_visitante == "Profesor"):
        precio_descuento = precio_boleto * (1 - DESCUENTO_PROFESOR)
    elif (tipo_visitante == "Estudiante"):
            precio_descuento = precio_boleto * (1 - DESCUENTO_ESTUDIANTE)
    else:
        precio_descuento = precio_boleto * 1         
    


    i += 1