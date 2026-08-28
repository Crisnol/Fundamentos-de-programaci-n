#Cristian Alejandro Nolasco Vargas

while True:
    #Primer menu registro
    print("1) Iniciar Sesión")
    print("2) Crear Cuenta")
    print("3) Salir del programa")
    opcion = int(input("Opción: "))

    if(opcion == 1):
        #if para inciar sesion
        while True:
            print("Para Iniciar Sesion Ingresa tu matricula")
            matricula = input("Matricula: ") 
            
            if(matricula == ""):
                print("Matricula incorrecta") 
            else:
                break          
    elif(opcion == 2):
        # if para crear cuenta
        while True:
            print("Para crear una nueva cuenta ingresa los siguientes datos.")
            matricula = input("Matricula: ")
            nombre = input("Nombre: ")
            carrera = input("Carrera: ")
        
            if ((matricula == "" and  len(matricula) !=  10) and nombre == "" and carrera == ""):
                print("Algun dato incorrecto, porfavor ingresa correctamente.")
            else:
                break
    
    elif(opcion == 3):
        break
    else:
        print("Ingrese una opción valida")
        continue
    
    #while para el menu dentro de la app
    while True: 
        #Rol hardcodeado pero lo debe recuperar con la cuenta
        rol = "Alumno"
        if(rol == "Alumno"):
            print("\nBienvenido al sistema")
            print("1) Organizaciones")
            print("2) Mi servicio")
            print("3) Salir de la cuenta")
            opcion = int(input("Opción: "))
            
            if(opcion == 1):
                #Opcion para ver las organizaciones en un listado
                while True:
                    print("Organización Socias")
                    cantOrganizaciones = 5
                    for i in range (1,cantOrganizaciones + 1):
                        cupos = 5
                        print(f"{i}) #Nombre de la organización (Cupos: {cupos}): ")
                    
                    opcionOrg = int(input("Elije una organizaciones para ver su información:"))
                    #ToDo: Falta organizar la recuperación de datos de cada organizaicion para imprimir
            
            elif(opcion == 2):
                #Opción para ver el servicio social del alumno
                #Variables harcodeadas para el avance, ToDo: recuperar de manera dinamica
                orgAlumno = "Perritos A Salvo"
                horasAcumuladas = 140
                
                while True:
                    print("Mi servicio")
                    print(f"Organización actual: {orgAlumno}")
                    print(f"Horas acumuladas: {horasAcumuladas} hrs")
                    
                    print("1) Registrar un nuevo dia")
                    print("2) Ver detalles de mi servicio")
                    
                    opcionServicio = int(input("Opción: "))
                    
                    if(opcionServicio == 1):
                        #opción para ver registrar
                        print("Bitacora")
                        fecha = int(input("Ingresa la fecha: "))
                        horas = int(input("Ingresa las horas acumuladas: "))
                        descripcion = input("Ingresa las actividades realizadas: ")
                        
                    elif(opcionServicio == 2):
                        #ToDo: Muestreo de datos especificios del servicio
                        print
                    else:
                        print("Ingrese una opción valida")
                        continue
                    
                    
            elif(opcion == 3):
                print("Saliendo de la cuenta...")
                break
            else:
                print("Ingrese una opción valida")
                continue
            
        elif(rol == "Organización"):
            #ToDo: Menu de org
            print()
        elif(rol == "Admin"): 
            #ToDo: Menu de admin
            print()
        
        
        