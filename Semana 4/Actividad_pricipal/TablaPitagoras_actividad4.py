# Cristian Alejandro Nolasco Vargas
# AL07264144
# 03/09/2026
# Progama para generar la matriz de la tabla pitagorica, imprimirla y obtener una intersección

# Función que genera todos los valores para guardarlo en una matriz
def generacionTabla():
    matriz_tablaPitagorica = []
    
    for f in range (1,11):
        fila_actual = []
        for c in range (1,11):
            num = f * c
            fila_actual.append(num)
        matriz_tablaPitagorica.append(fila_actual)
    
    return matriz_tablaPitagorica

# Función que imprime la tabla con formato
def printTabla(matriz_tablaPitagorica):
    
    # Impresion columnas 1-10
    print("\t", end="")
    for i in range(1,11):
        print(f"{i}", end= "\t")
    print()
    
    # Ciclo for para imprimir la tabla
    for f in range(len(matriz_tablaPitagorica)):
        #Impresion filas 1-10
        print(f + 1, end="\t|")
        for c in range(len(matriz_tablaPitagorica)):
                print(matriz_tablaPitagorica[f][c], end= "\t")
        print()

# Función para obtner el valor de la interseccion de la columna y fila 
def consultar_producto(matriz_tablaPitagorica, num1, num2):
    valor = matriz_tablaPitagorica[num1 - 1][num2-1]
    return valor

# llamado de funciones genera e imprime la tabla
matriz_tablaPitagorica = generacionTabla()
printTabla(matriz_tablaPitagorica)

# Ciclo para la comprobacion de datos sin finalizar el programa
while True:
    num1 = int(input("Ingresa el primer factor (Columna) (1-10): "))
    num2 = int(input("Ingresa el segundo fator (Fila) (1-10): "))
    
    # Comprobación de rango de los 2 numero ingresados por el usuario
    if (num1 > 0 and num1<= 10) and (num2 > 0 and num2<= 10):
        break
    else:
        print("Valores incorrectos asegurate de ingresar los datos correctamente\n")

valor = consultar_producto(matriz_tablaPitagorica, num1, num2)

print(f"La multiplicación {num1} x {num2} = {valor}")