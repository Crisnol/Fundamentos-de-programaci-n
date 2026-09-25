#Cristian Alejandro Nolasco Vargas

import time
import json
from pathlib import Path

DIR_BASE = Path(__file__).resolve().parent
RUTA_ARCHIVO_USERS = DIR_BASE / "data" / "Usuarios.json"
RUTA_ARCHIVO_ORGS = DIR_BASE / "data" / "Organizaciones.json"
RUTA_ARCHIVO_ADMINS = DIR_BASE / "data" / "Administradores.json"
RUTA_ARCHIVO_BITACORAS = DIR_BASE / "data" / "Bitacoras Usuarios.json"
CARPETA_REPORTES = DIR_BASE / "reportes"

boolSalir = False
matricula = ""

# Funciones Para acceder / Crear Cuenta
def inicioMenu():
    print("""
           ████  ████    ████  ████   ███   ███  ████  █████ █████ ███  ███  █   █   
          █ ░░░░█ ░░░░   █░░░█ █░░░█ █ ░░█ █ ░░░ █░░░█ █░░░░░ ░█░░░ █░░█ ░░█ ██  █░  
           ███░░░███░░░  ████░░████░░█░ ░█░█░ ██░████░░████░░░ █░░░░█░░█░ ░█░█░█ █░░ 
            ░░█   ░░█    █░░░░ █░░█░ █░░ █░█░░ █░█░░█░ █░░░░   █░░  █░░█░░ █░█░░██░░ 
          ████░░████░░   █░░░░░█░░░█░ ███ ░░███ ░█░░░█░█████░  █░░ ███░ ███ ░█░░ █░░ 
           ░░░░ ░░░░░ ░   ░░    ░░  ░  ░░░ ░ ░░░ ░░░  ░ ░░░░░   ░░  ░░░  ░░░ ░░░  ░░ 
            ░░░░  ░░░░     ░     ░   ░  ░░░   ░░░  ░   ░ ░░░░░   ░   ░░░  ░░░  ░   ░ 
          """)
    
    
    
    print("1) Iniciar Sesión")
    print("2) Crear Cuenta")
    print("3) Salir del programa")
    opcion = int(input("Opción: "))
    return opcion

def iniciarSesion():
    with open(RUTA_ARCHIVO_USERS, mode="r") as archivo:
            usuarios = json.load(archivo)
            
    while True:
        global matricula
        
        print("\nIniciar Sesion")

        matricula = input("Ingresa tu matricula: ")
        pantalla_carga("Verificando datos")
        # Comprobación de la matricula
        if matricula == "":
            print("Matricula incorrecta")
        elif len(matricula) != 10:
            print("La matrícula debe tener 10 dígitos.")
        elif not(matricula in usuarios):
            print("El usuario no existe, crea una cuenta")
        else:
            break
        
def crearCuenta():
    global matricula
    usuarios = {}
    
    with open(RUTA_ARCHIVO_USERS, mode="r") as archivo:
        try:
            usuarios = json.load(archivo)
        except json.JSONDecodeError:
            usuarios = {}
    
    while True:
        print("Para crear una nueva cuenta ingresa los siguientes datos.")
        matricula = input("Matricula: ")
        nombre = input("Nombre: ")
        carrera = input("Carrera: ")
        correo = input("Correo Institucional: ")
        rol = input("Rol (Alumno / Organización):")
    
        # Validar si la matrícula ya existe
        if matricula in usuarios:
            print("Esa matrícula ya está registrada en el sistema.")
            continue
    
        # Comprobación de datos ingresado correctamente
        if ((matricula == "" or  len(matricula) !=  10) or nombre == "" or carrera == ""):
            print("Algun dato incorrecto, porfavor ingresa correctamente.")
        else: 
            usuarios[matricula] = {
                "matricula": matricula,
                "nombre": nombre,
                "carrera": carrera,
                "correo": correo,
                "rol": rol
            }
            with open(RUTA_ARCHIVO_USERS, mode="w") as archivo:
                json.dump(usuarios, archivo, indent=4, ensure_ascii=False)

            break

def registro_acceso_cuenta():
    while True:
        global boolSalir
        # Primer menú de registro
        opcion = inicioMenu()

        match opcion:
            case 1:
                # Inicio de sesión
                iniciarSesion()
                break
            case 2:
                # Crear cuenta
                crearCuenta()
                break
            case 3:
                # Salir del programa
                boolSalir = True
                break
            case _:
                print("Ingrese una opción valida")
                continue

# Funciones General
## Funcion Pantalla de Carga
def pantalla_carga(mensaje="Cargando"):
    
    print(mensaje, end="", flush=True)
    
    for i in range(3):
        time.sleep(0.6)
        print(".", end="", flush=True)
        
    print(" ¡Listo!\n")

## Funcion Inactividad
def controlInactividad():
    print()

## Funcion Obtener Datos del usuario
def loadDataUser(matricula):
    with open(RUTA_ARCHIVO_USERS, mode="r") as archivo:
        usuarios = json.load(archivo)

    userData = usuarios[matricula]
    return userData

# Funciones Acciones Programa
## Funciones Rol Alumno ----------------
def impresionOrganizaciones():
    while True:
        print("Organización Socias")
        
        cantOrganizaciones = 5
        
        # for para recorrer la lista de las organizaciones
        for i in range(1, cantOrganizaciones + 1):
            cupos = 5
            print(f"{i}) #Nombre de la organización (Cupos: {cupos})")
        
        print(f"{cantOrganizaciones + 1}) Salir")
        opcionOrg = int(input("Elije una organización para ver su información: "))

        # Seleccion de opciones para ver las organizaciones o salir
        if opcionOrg == cantOrganizaciones + 1:
            break
        elif 1 <= opcionOrg <= cantOrganizaciones:
            print(f"Mostrando información de la organización {opcionOrg}...")
        else:
            print("Ingrese una opción válida.")

def servicioSocial():
    
    orgAlumno = "Perritos A Salvo"
    horasAcumuladas = 140
    
    while True:
        print("\nMi servicio")
        print(f"Organización actual: {orgAlumno}")
        print(f"Horas acumuladas: {horasAcumuladas} hrs")

        print("1) Registrar un nuevo dia")
        print("2) Ver detalles de mi servicio")
        print("3) Regresar")

        opcionServicio = int(input("Opción: "))

        match opcionServicio:
        # 1 Ingresa un nuevo registro en la bitacora
            case 1:
                registro_bitacora()
        
        # 2 Ver detalles del servicio
            case 2:
                print("Detalles de mi servicio")
                print(f"Organización: {orgAlumno}")
                print(f"Horas acumuladas: {horasAcumuladas} hrs")

            case 3:
                break
            case _:
                print("Ingrese una opción valida")

def registro_bitacora():
    print("Bitacora")
    fecha = input("Ingresa la fecha: ")
    horas = int(input("Ingresa las horas acumuladas (entero): "))
    descripcion = input("Ingresa las actividades realizadas: ")

    if fecha == "" or descripcion == "":
        print("La fecha y la descripción no pueden estar vacías.")
    else:
        print("Registro guardado exitosamente.")
        print(f"Fecha: {fecha}")
        print(f"Horas: {horas}")
        print(f"Descripción: {descripcion}")
    
def acciones_alumno():
    while True:
        print("\nBienvenido " + nombre)
        print("1) Organizaciones")
        print("2) Mi servicio")
        print("3) Salir de la cuenta")
        opcion = int(input("Opción: "))
        
        match opcion:
            case 1:
                # Opción para ver las organizaciones en un listado
                impresionOrganizaciones()
            case 2:
                # Menú del Servicio social
                servicioSocial()            
            case 3:
                print("Saliendo de la cuenta...")
                return
            case _:
                print("Ingrese una opción valida")
                continue
# -------------------------------------    

## Funciones Rol Admin ----------------
def vistaArchivos():
    print("\nLista de los Archivos Existentes")
    print("1. Organizaciones.txt")
    print("2. Usuarios.json")
    print("3. Bitacoras Usuarios.txt")
    print("4. Administradores.txt\n")

def lecturaArchivo():
      while True:
        nombre_archivo = input("Ingresa el nombre del archivo para leer: ")
        ruta_archivo = DIR_BASE / "data" / nombre_archivo

        try:
            with open(ruta_archivo, "r") as archivo:
                data = json.load(archivo)
                
            for key, content in data.items():
                print("\n_________________________________________")
                print(f"Matricula: {key}")
                print(f"Nombre: {content["nombre"]}")
                print(f"Carrera: {content["carrera"]}")
                print(f"Correo: {content["correo"]}")
                print(f"Rol: {content["rol"]}")
                print("_________________________________________")    
            break
        except FileNotFoundError:
            print(f"Error: no se encontro el archivo '{nombre_archivo}'.")
        except PermissionError:
            print(f"Error: no tienes permisos para abrir '{nombre_archivo}'.")                       

def escrituraArchivo():
    while True:
            nombre_archivo = input("Ingresa el nombre del archivo para leer: ")
            ruta_archivo = DIR_BASE / "data" / nombre_archivo
    
            try:
                with open(ruta_archivo, "r") as archivo:
                    data = json.load(archivo)
            
                match nombre_archivo:
                    case "Usuarios.json":
                         creaCuentaUsuario()        
                    case "Organizaciones.json":
                        crearOrganizacion()        
                    case "Bitacoras Usuarios.json":
                        crearBitacoraUsuario()        
                    case "Administradores.json":
                        crearAdministrador()        
                    case _:
                        print("Error inesperado")
                   
                break
            except FileNotFoundError:
                print(f"Error: no se encontro el archivo '{nombre_archivo}'.")
            except PermissionError:
                print(f"Error: no tienes permisos para abrir '{nombre_archivo}'.") 

def crearOrganizacion():
    organizaciones = {}
        
    try:
        with open(RUTA_ARCHIVO_ORGS, mode="r") as archivo:
            organizaciones = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        organizaciones = {}
    
    while True:
        print("\n--- Crear Nueva Organización ---")
        id_org = input("ID o RFC de la Organización: ")
        nombre = input("Nombre de la Organización: ")
        sector = input("Sector: ")
        correo = input("Correo de contacto: ")
    
        if id_org in organizaciones:
            print("Esa organización ya está registrada en el sistema.")
            continue
    
        if id_org == "" or nombre == "" or correo == "":
            print("Algún dato está vacío. Por favor ingresa los datos correctamente.")
        else: 
            organizaciones[id_org] = {
                "id_org": id_org,
                "nombre": nombre,
                "sector": sector,
                "correo": correo
            }
            with open(RUTA_ARCHIVO_ORGS, mode="w") as archivo:
                json.dump(organizaciones, archivo, indent=4, ensure_ascii=False)
            
            print("Organización registrada exitosamente.")
            break

def crearAdministrador():
    administradores = {}
        
    try:
        with open(RUTA_ARCHIVO_ADMINS, mode="r") as archivo:
            administradores = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        administradores = {}
    
    while True:
        print("\n--- Crear Nuevo Administrador ---")
        id_admin = input("ID de Administrador (ej. número de nómina): ").strip()
        nombre = input("Nombre completo: ").strip()
        departamento = input("Departamento: ").strip()
        correo = input("Correo Institucional: ").strip()
    
        if id_admin in administradores:
            print("Ese administrador ya está registrado en el sistema.")
            continue
    
        if id_admin == "" or nombre == "" or correo == "":
            print("Algún dato está incompleto. Reintenta.")
        else: 
            administradores[id_admin] = {
                "id_admin": id_admin,
                "nombre": nombre,
                "departamento": departamento,
                "correo": correo,
                "rol": "Administrador"
            }
            with open(RUTA_ARCHIVO_ADMINS, mode="w") as archivo:
                json.dump(administradores, archivo, indent=4, ensure_ascii=False)
            
            print("Administrador creado exitosamente.")
            break
 
def creaCuentaUsuario():
    usuarios = {}
        
    with open(RUTA_ARCHIVO_USERS, mode="r") as archivo:
        try:
            usuarios = json.load(archivo)
        except json.JSONDecodeError:
            usuarios = {}
    
    while True:
        print("Para crear una nueva cuenta ingresa los siguientes datos.")
        matricula = input("Matricula: ")
        nombre = input("Nombre: ")
        carrera = input("Carrera: ")
        correo = input("Correo Institucional: ")
        rol = input("Rol (Alumno / Organización):")
    
        # Validar si la matrícula ya existe
        if matricula in usuarios:
            print("Esa matrícula ya está registrada en el sistema.")
            continue
    
        # Comprobación de datos ingresado correctamente
        if ((matricula == "" or  len(matricula) !=  10) or nombre == "" or carrera == ""):
            print("Algun dato incorrecto, porfavor ingresa correctamente.")
        else: 
            usuarios[matricula] = {
                "matricula": matricula,
                "nombre": nombre,
                "carrera": carrera,
                "correo": correo,
                "rol": rol
            }
            with open(RUTA_ARCHIVO_USERS, mode="w") as archivo:
                json.dump(usuarios, archivo, indent=4, ensure_ascii=False)
            print("Usuario creado exitosamente.")
            break
    
def crearBitacoraUsuario():
    bitacoras = []
        
    try:
        with open(RUTA_ARCHIVO_BITACORAS, mode="r") as archivo:
            bitacoras = json.load(archivo)
            
    except (FileNotFoundError, json.JSONDecodeError):
        bitacoras = []
    
    while True:
        print("\n--- Registro de Bitácora ---")
        matricula = input("Ingresa la matrícula del usuario: ")
        fecha = input("Ingresa la fecha (ej. DD/MM/AAAA): ")
        
        # Validar entrada numérica para evitar que el programa truene
        try:
            horas = int(input("Ingresa las horas acumuladas (entero): "))
        except ValueError:
            print("Error: Las horas deben ser un número entero válido.")
            continue

        descripcion = input("Ingresa las actividades realizadas: ")

        # Validaciones de campos obligatorios
        if matricula == "" or fecha == "" or descripcion == "":
            print("La matrícula, fecha y descripción no pueden estar vacías.")
            continue
            
        if horas <= 0:
            print("Las horas deben ser un número entero mayor a cero.")
            continue

        # Crear estructura de registro
        bitacoras[f"{matricula} - {fecha}"] = {
            "matricula": matricula,
            "fecha": fecha,
            "horas": horas,
            "descripcion": descripcion
        }
        
        # Escritura física en JSON
        with open(RUTA_ARCHIVO_BITACORAS, mode="w", encoding="utf-8") as archivo:
            json.dump(bitacoras, archivo, indent=4, ensure_ascii=False)

        print(f"Registro guardado exitosamente para la matrícula {matricula}.")
        break

def generarReporteAlumno():
    try:
        with open(RUTA_ARCHIVO_USERS, mode="r", encoding="utf-8") as archivo:
            usuarios = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error: No se pudo abrir o leer 'Usuarios.json'.")
        return

    print("\n--- Exportar Reporte de Alumno a TXT ---")
    matricula = input("Ingresa la matrícula del alumno a consultar: ").strip()

    if matricula not in usuarios:
        print(f"Error: La matrícula '{matricula}' no se encuentra registrada.")
        return

    alumno = usuarios[matricula]

    registros_alumno = []
    try:
        with open(RUTA_ARCHIVO_BITACORAS, mode="r", encoding="utf-8") as archivo:
            bitacoras = json.load(archivo)
            if isinstance(bitacoras, dict):
                # Filtramos iterando sobre los valores del diccionario
                registros_alumno = [
                    reg for reg in bitacoras.values() 
                    if isinstance(reg, dict) and reg.get("matricula") == matricula
                ]
    except (FileNotFoundError, json.JSONDecodeError):
        registros_alumno = []

    total_horas = sum(registro.get("horas", 0) for registro in registros_alumno)
    total_registros = len(registros_alumno)

    CARPETA_REPORTES.mkdir(parents=True, exist_ok=True)
    ruta_txt = CARPETA_REPORTES / f"Reporte_{matricula}.txt"

    lineas = [
        "=" * 55,
        "               REPORTE DETALLADO DE ALUMNO               ",
        "=" * 55,
        f"Matrícula: {alumno.get('matricula', 'N/A')}",
        f"Nombre:    {alumno.get('nombre', 'N/A')}",
        f"Carrera:   {alumno.get('carrera', 'N/A')}",
        f"Correo:    {alumno.get('correo', 'N/A')}",
        f"Rol:       {alumno.get('rol', 'N/A')}",
        "-" * 55,
        f"Total de entradas registradas: {total_registros}",
        f"Total de horas acumuladas:    {total_horas} hrs",
        "-" * 55
    ]

    if not registros_alumno:
        lineas.append("El alumno no cuenta con actividades en su bitácora.")
    else:
        lineas.append("HISTORIAL DE ACTIVIDADES:")
        for i, reg in enumerate(registros_alumno, start=1):
            lineas.append(f"  [{i}] Fecha: {reg.get('fecha')} | Horas: {reg.get('horas')}")
            lineas.append(f"      Descripción: {reg.get('descripcion')}")
            lineas.append("-" * 40)

    lineas.append("=" * 55)

    try:
        with open(ruta_txt, mode="w", encoding="utf-8") as archivo_txt:
            archivo_txt.write("\n".join(lineas))
        print(f"\nReporte generado con éxito en: {ruta_txt}")
    except OSError as e:
        print(f"Error al escribir el archivo de reporte: {e}")

def acciones_admin():
    while True:
            print("\nBienvenido " + nombre)
            print("1) Vista y lectura Archivos")
            print("2) Escritura Archivo")
            print("3) Crear Reporte Alumno")
            print("4) Salir Cuenta\n")
            opcion = int(input("Opción: "))
            
            match opcion:
                case 1:
                    # Lectura archivo
                    vistaArchivos()
                    lecturaArchivo()
                case 2:
                    # Escritura archivo
                    vistaArchivos()
                    escrituraArchivo()          
                case 3:
                    # Crear archivo reporte alumno
                    generarReporteAlumno()
                case 4:
                    print("Saliendo de la Cuenta")
                    return
                case _:
                    print("Ingrese una opción valida")
                    continue
# -------------------------------------     

# Menú dentro de la app
while True:
    #Uso de la funcion para el Registro / iniciar sesion de la cuenta
    registro_acceso_cuenta()
    if boolSalir == True:
        break
    
    datosUsuario = loadDataUser(matricula = matricula)
    
    # Rol y nombre hardcodeado, pero lo debe recuperar con la cuenta
    rol = datosUsuario["rol"]
    nombre = datosUsuario["nombre"]

    match rol:
        case "Alumno":
            # Menu con todas las acciones para ALUMNOS
            acciones_alumno()
        case"Organización":
            # TODO: Menu de org
            print()
        case "Admin":
            acciones_admin()

print("Agradesemos su Preferencia")





