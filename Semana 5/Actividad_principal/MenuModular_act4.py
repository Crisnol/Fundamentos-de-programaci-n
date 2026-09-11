# Cristian Alejandro Nolasco Vargas
# AL07264144
# 10/09/2026
# Menu Modular para acceder a diferentes funciones.


def sumaTupla (tupla):
    sumaTotal = 0
    for i in range(0, len(tupla)):
        sumaTotal += tupla[i]
    return sumaTotal

def buscarTelefono(contactos, nombre):
    telefono = contactos.get(nombre, "Contacto no encontrado")
    return telefono
        
        
def countPalabras(frase):
    count_mensaje_replace = frase.split()
    total_palabras_replace = len(count_mensaje_replace)
    return total_palabras_replace

while True:
    print("========================================\n")
    print("1) Mostrar tupla ordenada")
    print("2) Buscar telefono")
    print("3) Suma dos Números")
    print("4) Analizar mensaje")
    print("5) Finalizar el programa")
    print("\n========================================")

    
    opcion = int(input("Opción: "))
    
    match opcion:
        case 1:
            print("\n__________ Mostrar tupla ordenada _________\n")
            numeros = (5, 76, 23, 45, 67, 23, 98, 3, 8)
            print(f"El tercer elemento de la tupla es: {numeros[2]}")
                
            newNumero1 = float(input("Ingresa el Primer Nuevo Número: "))
            newNumero2 = float(input("Ingresa el Segundo Nuevo Número: "))
                
            nueva_tupla = numeros + (newNumero1, newNumero2)
            lista_numeros = list(nueva_tupla)                
            lista_numeros.sort()
            print(f"Lista ordenada: {lista_numeros}")
            
            suma = sumaTupla(nueva_tupla)
            print(f"La suma de los numeros en la tupla: {suma}")
        case 2:
            print("\n_______ Buscar telefono ______\n")
            
            contactos = {
                "juan": "342 2344 2344",
                "nose": "943 2345 9822",
                "cr7": "242 8092 8493",
                "messi": "243 7654 3534"
            }
            
            nombre = input("Ingresa el nombre del nuevo contacto: ").lower()
            numero = input("Ingresa su numero: ")

            contactos[nombre] = numero
            
            print("Lista de contacto")
            for c in contactos.keys():
                print(f"--{c}")
            
            nombre = input("Ingresa Nombre a Buscar: ")
            busqueda_telefono = buscarTelefono(contactos,nombre.lower())
            print(f"\nEl teléfono {nombre} es: {busqueda_telefono}")

        case 3:
            print("\n_________ Suma dos Números _________\n")
            while True:
                try:
                    num1 = int(input("Ingrese el primer numero entero: "))
                    num2 = int(input("Ingresa el segundo numero entero: "))
                    try:
                        divicion = num1 / num2      
                        divicion = num2 / num1 
                         
                        suma = num1 + num2
                        print(f"La suma del los numeros: {suma}")    
                        break
                    except ZeroDivisionError:
                        print("----Ingresa un numero diferente a cero para realizar la suma correctamente----") 
                except:
                    print("Se ha ingresado un número incorrecto")   
                
                
        case 4:
            print("\n_________ Analizar Mensaje __________\n")
            mensaje = input("Escribe una mensaje: ")
            
            count_mensaje = len(mensaje)
            mayus_mensaje = mensaje.upper()
            replace_mensaje = mensaje.replace("hola", "(Palabra encriptada)")
        
            print(f"Mensaje Original: {mensaje} - Longitud: {count_mensaje}")
            print(f"mensaje UPPER: {mayus_mensaje}")
            print(f"mensaje con Remplazo: {replace_mensaje} - Cantidad Palabras: {total_palabras_replace}")
            
            countPalabras(mensaje)
        case 5:
            print("______________ Finalizando Programa, Gracias por su preferencia _______________________")
            break
        case _:
            print("-------------------------- Opción no valida ---------------------\n")
