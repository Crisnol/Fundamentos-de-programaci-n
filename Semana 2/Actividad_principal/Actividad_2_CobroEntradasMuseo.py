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

    edad = int(input(f"\nIngrese la edad del visitante {i}: "))

    if (edad >= 18):
        precio_boleto = PRECIO_MAYOR_18
    elif(edad <= 17 and edad >= 3):
        precio_boleto = PRECIO_MENOR_EDAD
    elif(edad < 0):
        print("Edad incorrecta, error en el sistema\nVuelve a ejutar el programa")
        break 
    else:
        precio_boleto = PRECIO_MENOR_3
        print(f"|Visitante|\t|Subtotal|\t|Descuento|\t|Total|\t|Total General|")
        print(f"Visitante {i}\t {precio_boleto}\t\t {0}\t\t {0}\t ${total_general}")
        i += 1
        continue
    
    tipo_visitante = input("Ingresa el tipo de visitante (Adulto mayor / Profesor / Estudiante): ")

    if (tipo_visitante == "Adulto mayor"):
        descuento = precio_boleto * DESCUENTO_ADULTO
    elif (tipo_visitante == "Profesor"):
        descuento = precio_boleto * DESCUENTO_PROFESOR
    elif (tipo_visitante == "Estudiante"):
        descuento = precio_boleto * DESCUENTO_ESTUDIANTE
    else:
        descuento = 0      

    precio_descuento = precio_boleto - descuento
    total_general = total_general + precio_descuento

    print(f"|Visitante|\t|Subtotal|\t|Descuento|\t|Total|\t|Total General|")
    print(f"Visitante {i}\t ${precio_boleto}\t\t -{descuento:.2f}\t\t ${precio_descuento:.2f}\t ${total_general}")
        
    i += 1

    
print(f"\nTotal a pagar es de: ${total_general}")
