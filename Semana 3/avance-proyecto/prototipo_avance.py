#Cristian Alejandro Nolasco Vargas

while True:
    # Primer menú de registro
    print("1) Iniciar Sesión")
    print("2) Crear Cuenta")
    print("3) Salir del programa")
    opcion = int(input("Opción: "))

    if opcion == 1:
        # Inicio de sesión
        while True:
            print("Para Iniciar Sesion Ingresa tu matricula")
            matricula = input("Matricula: ")

            # Comprobación de la matricula
            if matricula == "":
                print("Matricula incorrecta")
            elif len(matricula) != 10:
                print("La matrícula debe tener 10 dígitos.")
            else:
                break

    elif opcion == 2:
        # Crear cuenta
        while True:
            print("Para crear una nueva cuenta ingresa los siguientes datos.")
            matricula = input("Matricula: ")
            nombre = input("Nombre: ")
            carrera = input("Carrera: ")
        
            # Comprobación de datos ingresado correctamente
            if ((matricula == "" or  len(matricula) !=  10) or nombre == "" or carrera == ""):
                print("Algun dato incorrecto, porfavor ingresa correctamente.")
            else:
                break

    elif opcion == 3:
        break
    else:
        print("Ingrese una opción valida")
        continue

    # Menú dentro de la app
    while True:
        # Rol hardcodeado, pero lo debe recuperar con la cuenta
        rol = "Alumno"

        if rol == "Alumno":
            print("\nBienvenido al sistema")
            print("1) Organizaciones")
            print("2) Mi servicio")
            print("3) Salir de la cuenta")
            opcion = int(input("Opción: "))
            
            if(opcion == 1):
                # Opción para ver las organizaciones en un listado
                while True:
                    print("Organización Socias")
                    
                    cantOrganizaciones = 5
                    
                    # for para recorrer la lista de las organizaciones
                    for i in range(1, cantOrganizaciones + 1):
                        cupos = 5
                        print(f"{i}) #Nombre de la organización (Cupos: {cupos})")
                   
                    print(f"{cantOrganizaciones + 1}) Salir")
                    opcionOrg = int("Elije una organización para ver su información: ")

                    # Seleccion de opciones para ver las organizaciones o salir
                    if opcionOrg == cantOrganizaciones + 1:
                        break
                    elif 1 <= opcionOrg <= cantOrganizaciones:
                        print(f"Mostrando información de la organización {opcionOrg}...")
                    else:
                        print("Ingrese una opción válida.")

            elif opcion == 2:
                # Opción para ver el servicio social del alumno
                orgAlumno = "Perritos A Salvo"
                horasAcumuladas = 140

                # Menú del Servicio social
                while True:
                    print("\nMi servicio")
                    print(f"Organización actual: {orgAlumno}")
                    print(f"Horas acumuladas: {horasAcumuladas} hrs")

                    print("1) Registrar un nuevo dia")
                    print("2) Ver detalles de mi servicio")
                    print("3) Regresar")

                    opcionServicio = int("Opción: ")

                    #if para las opciones del servico
                    # 1 Ingresa un nuevo registro en la bitacora
                    if opcionServicio == 1:
                        print("Bitacora")
                        fecha = input("Ingresa la fecha: ")
                        horas = int("Ingresa las horas acumuladas (entero): ")
                        descripcion = input("Ingresa las actividades realizadas: ")

                        if fecha == "" or descripcion == "":
                            print("La fecha y la descripción no pueden estar vacías.")
                        else:
                            print("Registro guardado exitosamente.")
                            print(f"Fecha: {fecha}")
                            print(f"Horas: {horas}")
                            print(f"Descripción: {descripcion}")
                    
                    # 2 Ver detalles del servicio
                    elif opcionServicio == 2:
                        print("Detalles de mi servicio")
                        print(f"Organización: {orgAlumno}")
                        print(f"Horas acumuladas: {horasAcumuladas} hrs")

                    elif opcionServicio == 3:
                        break
                    else:
                        print("Ingrese una opción valida")

            elif opcion == 3:
                print("Saliendo de la cuenta...")
                break
            else:
                print("Ingrese una opción valida")
                continue
        
        elif rol == "Organización":
            # ToDo: Menu de org
            print()
        elif rol == "Admin":
            # ToDo: Menu de admin
            print()
