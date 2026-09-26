#Cristian Alejandro Nolasco Vargas
# Importacion de librerias necesarios para el programa
import msvcrt
import time
import json
from pathlib import Path
from datetime import datetime
import pdb

# Constantes de Colores
RESET = "\033[0m"
AZUL = "\033[34m"

# Constantes de las direcciones de los archivos ya establecidos
DIR_BASE = Path(__file__).resolve().parent
RUTA_ARCHIVO_USERS = DIR_BASE / "data" / "Usuarios.json"
RUTA_ARCHIVO_ORGS = DIR_BASE / "data" / "Organizaciones.json"
RUTA_ARCHIVO_ADMINS = DIR_BASE / "data" / "Administradores.json"
RUTA_ARCHIVO_BITACORAS = DIR_BASE / "data" / "Bitacoras Usuarios.json"
CARPETA_REPORTES = DIR_BASE / "reportes"

# Variables de control y generales
boolSalir = False
matricula = ""

# Funciones Para acceder / Crear Cuenta
# Muestra el menú inicial y devuelve la opción seleccionada por el usuario
def inicioMenu():
    # Representación en matriz de las opciones del menú
    matriz_inicio = [
        ["1) Iniciar Sesión", "2) Crear Cuenta"],
        ["3) Salir del programa", ""]
    ]
    
    # Impresion de logo con la implementacion del cambio de color
    print(f"""{AZUL}
           ████  ████    ████  ████   ███   ███  ████  █████ █████ ███  ███  █   █   
          █ ░░░░█ ░░░░   █░░░█ █░░░█ █ ░░█ █ ░░░ █░░░█ █░░░░░ ░█░░░ █░░█ ░░█ ██  █░  
           ███░░░███░░░  ████░░████░░█░ ░█░█░ ██░████░░████░░░ █░░░░█░░█░ ░█░█░█ █░░ 
            ░░█   ░░█    █░░░░ █░░█░ █░░ █░█░░ █░█░░█░ █░░░░   █░░  █░░█░░ █░█░░██░░ 
          ████░░████░░   █░░░░░█░░░█░ ███ ░░███ ░█░░░█░█████░  █░░ ███░ ███ ░█░░ █░░ 
           ░░░░ ░░░░░ ░   ░░    ░░  ░  ░░░ ░ ░░░ ░░░  ░ ░░░░░   ░░  ░░░  ░░░ ░░░  ░░ 
            ░░░░  ░░░░     ░     ░   ░  ░░░   ░░░  ░   ░ ░░░░░   ░   ░░░  ░░░  ░   ░ 
          {RESET}""")
    
    print("=== MENÚ PRINCIPAL ===")
    # Renderizado iterativo de la matriz
    for i in range(len(matriz_inicio)):
        for j in range(len(matriz_inicio[i])):
            print(f"{matriz_inicio[i][j]}")
            
    print("** Si desea crear una cuenta de organización o administrador contacte con soporte técnico.\n")
    
    # try-except control errores si no se coloca bien la opcion
    try:
        opcion = int(input("Opción: "))
        return opcion
    except ValueError:
        print("Error: Debes ingresar una opcion valida.")   

# Busca la matrícula o ID en los archivos de usuarios, administradores y organizaciones
def iniciarSesion():
    # acceso al archivo usuarios.json para ver si hay usuarios, con su respectivo control de errores
    try:
        with open(RUTA_ARCHIVO_USERS, mode="r", encoding="utf-8") as archivo:
            usuarios = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        usuarios = {}
        
    # acceso al archivo administradores.json para ver si hay admis, con su respectivo control de errores
    try:
        with open(RUTA_ARCHIVO_ADMINS, mode="r", encoding="utf-8") as archivo:
            administradores = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        administradores = {}
    
    # acceso al archivo organizaciones.json para ver si hay orgs, con su respectivo control de errores
    try:
        with open(RUTA_ARCHIVO_ORGS, mode="r", encoding="utf-8") as archivo:
            organizaciones = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        organizaciones = {}

    if not usuarios and not administradores:
        print("\nNo es posible ejecutar el programa")
        print("Porfavor intentalo mas tarde")
        return

    # ciclo while para la lectura de la matricula con su respecto control de errores y verificaciones
    while True:
        global matricula

        print("\nIniciar Sesión")
        matricula = input("Ingresa tu matricula o ID (0 para cancelar): ")

        if matricula == "0":
            return "cancelar"

        pantalla_carga("Verificando datos")

        if matricula == "":
            print("Matricula incorrecta")
        elif matricula in usuarios:
            return
        elif matricula in administradores:
            return
        elif matricula in organizaciones:
            return
        else:
            print("El usuario no existe, crea una cuenta")
                      
## Funcion ocupada en Rol Alumno / Admin        
# Solicita los datos de una cuenta, los valida y la guarda en Usuarios.json
def crearCuenta(rolUsuario):
    if rolUsuario == "Alumno":
        global matricula
    usuarios = {}
    
    with open(RUTA_ARCHIVO_USERS, mode="r", encoding="utf-8") as archivo:
        try:
            usuarios = json.load(archivo)
        except json.JSONDecodeError:
            usuarios = {}
            
    print("------ Crear Cuenta ------")
    
    while True:
        print("Para crear una nueva cuenta ingresa los siguientes datos.")
        matricula = input("Matricula (10 caracteres): ")
        nombre = input("Nombre: ")
        carrera = input("Carrera: ")
        correo = input("Correo Institucional: ")
        rol = input("Rol (Alumno): ").capitalize()
        servicio = ""
        fecha = estructuraFecha()
        
        # Validar si la matrícula ya existe
        if matricula in usuarios:
            print("Esa matrícula ya está registrada en el sistema.")
            continue
                
        # Comprobación de datos ingresado correctamente
        if matricula == "":
            print("Se necesita una matricula para continuar.")
            continue
        elif len(matricula) != 10:
            print("La matricula no cumple con los requrimentos")
            print("Debe de ser de 10 caracteres")
            continue
        elif nombre == "":
            print("Se necesita un nombre para continuar")
            continue
        elif carrera == "":
            print("Se necesita un carre para continuar")
            continue
        elif correo == "":
            print("Error: Ingresa un correo institucional válido.")
            continue
        elif "@tecmilenio.mx" not in correo:
            print("Error: Ingresa un correo institucional válido.")
            continue
        elif(rol != "Alumno" and rol != "Organización"):
            print("No seleccionaste correctamente el rol")
            print("Ingresa correctamente el rol")
            continue
        else: 
            usuarios[matricula] = {
                "matricula": matricula,
                "nombre": nombre,
                "carrera": carrera,
                "correo": correo,
                "rol": rol,
                "Servicio Social": servicio,
                "fecha_creacion": fecha
            }
            try:
                with open(RUTA_ARCHIVO_USERS, mode="w", encoding="utf-8") as archivo:
                    json.dump(usuarios, archivo, indent=4, ensure_ascii=False)
                pantalla_carga("Creando cuenta")
                print("Usuario Creado Correctamente")
                break
            except OSError as e:
                print(f"Error al escribir el archivo de reporte: {e}")
       
# Controla el flujo inicial para iniciar sesión, crear una cuenta o salir
def registro_acceso_cuenta():
    while True:
        global boolSalir
        # Primer menú de registro
        opcion = inicioMenu()

        match opcion:
            case 1:
                # Inicio de sesión
                if iniciarSesion() != "cancelar":
                    break
            case 2:
                # Crear cuenta
                if crearCuenta(rolUsuario = "Alumno") != "cancelar":
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
# Simula una pantalla de carga para indicar que una operación está en proceso
def pantalla_carga(mensaje="Cargando"):
    
    print(f"\n{mensaje}", end=" - ", flush=True)
    # calculo de tiemp en segundo con la cantidad de cuadro que quieres que aparescan 
    for i in range(20):
        time.sleep(0.2)
        print("█", end="", flush=True)
        
    print("\n¡Listo!\n")

## Funcion Inactividad
# Lee la entrada del teclado durante un tiempo límite y detecta la inactividad
def controlInactividad(mensaje, mins_limite = 10):
    print(mensaje, end="", flush=True)
    entrada = ""
    
    # Calculamos tiemp. 
    # 10 minutos * 60 segundos * 10 décimas de segundo por iteración
    iteraciones = int(mins_limite * 60 * 10)
    
    for i in range(iteraciones):
        # kbhit verifica si hay una tecla presionada en la consola
        if msvcrt.kbhit():
            # getwche lee la tecla y la imprime en pantalla
            char = msvcrt.getwche()
            
            if char in ('\r', '\n'):  # El usuario presionó Enter
                print()
                return entrada
            elif char == '\b':  # El usuario presionó Retroceso (borrar)
                entrada = entrada[:-1]
                print(" \b", end="", flush=True) 
            else:
                entrada += char
                
        # Pausa de 0.1 segundos por ciclo
        time.sleep(0.1)
        
    print("\nTiempo agotado.")
    return "inactividad"   
         
# Pregunta si el usuario desea continuar después de superar el tiempo de inactividad
def respuestaInactividad():
    # ciclo para solicitar la respuesta si/no por si hay algun error tipografico del usuario
    while True:
        print("\nSe ha detectado inactividad en el menú.")
        confirmacion = controlInactividad("¿Desea continuar? Escriba 'si' o 'no': ", mins_limite=1)

        match confirmacion.strip().lower(): 
            case "si":
                return "si"
            case "no":
                print("Cerrando sesión. Regresando al inicio...")
                return "no"
            case _:
                print("Ingresa correctamente una opcionn")
                continue
             
## Funcion Obtener Datos del usuario
# Recupera los datos de una cuenta buscando la matrícula en los archivos disponibles
def loadDataUser(matricula):
    # Cargar el archivo usuarios y pasarlo a una varible
    try:
        with open(RUTA_ARCHIVO_USERS, mode="r", encoding="utf-8") as archivo:
            usuarios = json.load(archivo)
            if matricula in usuarios:
                return usuarios[matricula]
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    # Cargar el archivo admins y pasarlo a una varible
    try:
        with open(RUTA_ARCHIVO_ADMINS, mode="r", encoding="utf-8") as archivo:
            administradores = json.load(archivo)
            if matricula in administradores:
                return administradores[matricula]
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    
    # Cargar el archivo orgs y pasarlo a una varible
    try:
        with open(RUTA_ARCHIVO_ORGS, mode="r", encoding="utf-8") as archivo:
            organizaciones = json.load(archivo)
            if matricula in organizaciones:
                datos = organizaciones[matricula]
                datos["rol"] = "Organización"
                return datos
    except (FileNotFoundError, json.JSONDecodeError):
        pass

    print("\nNo es posible ejecutar el program")
    print("Porfavor intentalo mas tarde")
    return None
            
## Funcion obtener nombre org atra vez id
# Obtiene el nombre de una organización a partir de su identificador
def obtenerNombreOrganizacion(id_org):
    # Cargar el archivo orgs y pasarlo a una varible
    try:
        with open(RUTA_ARCHIVO_ORGS, "r", encoding="utf-8") as archivo:
            orgs = json.load(archivo)
            # Verificar que exista y buscar la organizacion con el id
            if id_org in orgs:
                return orgs[id_org].get("nombre", id_org)
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return id_org

## Funcion para crear la fecha estructura
# Solicita una fecha válida y la devuelve como una tupla (día, mes, año)
def estructuraFecha():
    while True:
        try:
            dia = int(input("Ingresa el dia: "))
            mes = int(input("Ingresa el mes (numero): "))
            año = int(input("Ingresa el año (AAAA): "))

            if año != 2026:
                print("\nAño incorrecto, ingresa uno valido.")
                continue
            # Verifica que la fecha exista realmente en el calendario
            datetime(año, mes, dia)
            
            fecha_tupla = (dia, mes, año)
            return fecha_tupla
            
        except ValueError:
            print("Entrada invalida. Asegurate de ingresar numeros y una fecha real.\n")
    
# Funciones Acciones Programa
## Funciones Rol Alumno ----------------
# Suma las horas registradas de una matrícula en todas sus bitácoras.
def calcularHorasAcumuladas(matricula):
    #Suma dinámicamente las horas del alumno desde Bitacoras Usuarios.json
    try:
        with open(RUTA_ARCHIVO_BITACORAS, "r", encoding="utf-8") as archivo:
            bitacoras = json.load(archivo)
            if isinstance(bitacoras, dict):
                return sum(
                    reg.get("horas", 0) 
                    for reg in bitacoras.values() 
                    if isinstance(reg, dict) and reg.get("matricula") == matricula
                )
        #pdb.set_trace() 
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return 0

# Lee Organizaciones.json y muestra la información de las organizaciones registradas.
def impresionOrganizaciones():
    # declaracion ruta
    ruta_archivo = DIR_BASE / "data" / "Organizaciones.json"
    
    pantalla_carga("Obteniendo Datos")

    try:
        # abrir archivo con la ruta para cargar los datos del json
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            data = json.load(archivo)
            
        if not data:
            print("No hay organizaciones registradas actualmente.")
        
        # Impresion del listado de las organizacion con un ciclo for obteniendo los items
        print("\n=== LISTADO DE ORGANIZACIONES ===")
        for key, content in data.items():
            print("\n_________________________________________")
            print(f"ID Org:      {key}")
            print(f"Nombre:      {content.get('nombre', 'N/A')}")
            print(f"Sector:      {content.get('sector', 'N/A')}")
            print(f"Correo:      {content.get('correo', 'N/A')}")
            print(f"Descripción: {content.get('descripcion', 'N/A')}")
            print(f"Página Web:  {content.get('pagina_web', 'N/A')}")
            print("_________________________________________")
        
    except FileNotFoundError:
        print(f"Error: no se encontro el archivo 'Organizaciones.json'.")
    except json.JSONDecodeError:
        print(f"Error: El archivo 'Organizaciones.json' está corrupto o no tiene un formato JSON válido.")
    except PermissionError:
        print(f"Error: no tienes permisos para abrir 'Organizaciones.json'.")                       
        
# Permite al alumno inscribirse a una organización y consultar su servicio social
def servicioSocial():
    global matricula
    
    # Se abre el archivo usuarios para obtner la informacion
    try:
        with open(RUTA_ARCHIVO_USERS, "r", encoding="utf-8") as archivo:
            usuarios = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error: No se pudo cargar 'Usuarios.json'.")
        return


    alumno = usuarios.get(matricula)

    # Si NO tiene servicio social asignado, mostrar formulario de inscripción
    if not alumno.get("Servicio Social"):
        print("\n--------------------------------------------------")
        print("Aún no tienes asignada una organización de Servicio Social.")
        print("--------------------------------------------------")
        
        impresionOrganizaciones()

        print("\n--- Registro a Servicio Social ---")
        id_org = input("Ingresa el ID de la organización a la que te deseas unir (o '0' para cancelar): ")

        if id_org == "0" or id_org == "":
            print("Operación cancelada.")
            return

        # Validar que el ID exista en Organizaciones.json
        try:
            with open(RUTA_ARCHIVO_ORGS, "r", encoding="utf-8") as archivo:
                orgs = json.load(archivo)
        except (FileNotFoundError, json.JSONDecodeError):
            orgs = {}

        if id_org not in orgs:
            print(f"Error: El ID '{id_org}' no coincide con ninguna organización válida.")
            return
        print("\nPara completar la inscripción, confirma la fecha de la operación:")
        fecha_asignacion = estructuraFecha()

        # Guardar la asignación en Usuarios.json
        alumno["Servicio Social"] = id_org
        alumno["fecha_asignacion_servicio"] = fecha_asignacion
        
        try:
            with open(RUTA_ARCHIVO_USERS, "w", encoding="utf-8") as archivo:
                json.dump(usuarios, archivo, indent=4, ensure_ascii=False)
            print(f"\n¡Te has inscrito con éxito a '{orgs[id_org].get('nombre')}' el día {fecha_asignacion}!")
        except OSError as e:
            print(f"Error al guardar los cambios: {e}")
            return

    # Menú principal del Servicio Social (cuando ya cuenta con organización)
    id_org = alumno["Servicio Social"]

    while True:
        nombre_org = obtenerNombreOrganizacion(id_org)
        horas_acumuladas = calcularHorasAcumuladas(matricula)
        meta_horas = 480  # Horas requeridas estándar para servicio social

        print("\n__________________________________________")
        print("             MI SERVICIO SOCIAL           ")
        print("____________________________________________")
        print(f"Organización:   {nombre_org} (ID: {id_org})")
        print(f"Horas acumuladas: {horas_acumuladas} / {meta_horas} hrs")
        print("------------------------------------------")
        print("1) Registrar un nuevo día en la bitácora")
        print("2) Ver detalles de mi servicio")
        print("3) Regresar")

        try:
            opcionServicio = int(input("Opción: "))
        except ValueError:
            print("Error: Debes ingresar un número entero.")
            continue

        match opcionServicio:
            case 1:
                # Llamada funcion crear bitacora con arg rol alumno
                crearBitacoraUsuario(rol="Alumno")
            case 2:
                pantalla_carga("Obteniendo Datos")
                print("\n--- DETALLES DE MI SERVICIO SOCIAL ---")
                print(f"Alumno:           {alumno.get('nombre')}")
                print(f"Matrícula:        {matricula}")
                print(f"Carrera:          {alumno.get('carrera')}")
                print(f"Organización:     {nombre_org} ({id_org})")
                print(f"Horas acumuladas: {horas_acumuladas} hrs")
                print(f"Horas pendientes: {max(0, meta_horas - horas_acumuladas)} hrs")
                print(f"Estatus:          {'Completado' if horas_acumuladas >= meta_horas else 'En progreso'}")
            case 3:
                break
            case _:
                print("Opción no válida. Intenta de nuevo.")

# Muestra el menú del alumno y ejecuta la acción elegida
def acciones_alumno():
    # opciones en formato de matriz 
    matriz_alumno = [
        ["1) Organizaciones", "2) Mi servicio"],
        ["3) Salir de la cuenta", ""]
    ]
    
    # Menu con todas la opciones que puede hacer el rol alumno
    while True:
        print(f"\nBienvenido Alumno {nombre}")
        
        # Recorrido dinámico de la matriz de opciones
        for i in range(len(matriz_alumno)):
            for j in range(len(matriz_alumno[i])):
                print(f"{matriz_alumno[i][j]}") 
    
        
        # peticion para el control de incatividad
        respuesta = controlInactividad("Opción: ", mins_limite=10)
        
        # lectura de la respuesta si es incactivo
        if respuesta == "inactividad":
            confirmacion = respuestaInactividad()
            if confirmacion == "si":
                continue
            elif confirmacion == "no":
                return
            
        try:
            # Conversion a int para que conicida con el case
            opcion = int(respuesta)
        except ValueError:
            print("Error: Debes ingresar una opcion valida.")
            continue
        
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
# Muestra los archivos JSON que el administrador puede consultar o modificar
def vistaArchivos():
    # Lista de archivos para imprimir
    print("\nLista de los Archivos Existentes")
    print("1. Organizaciones.json")
    print("2. Usuarios.json")
    print("3. Bitacoras Usuarios.json")
    print("4. Administradores.json\n")

# Lee el archivo seleccionado y presenta sus registros según el tipo de información
def lecturaArchivo():
    # Ciclo para el control de errores tipograficos al escribir el nombre del archivo
      while True:
        nombre_archivo = input("Ingresa el nombre del archivo para leer (0 para cancelar): ")
        
        # condicion para salir de la opcion
        if nombre_archivo == "0":
            break
        
        # Creacion dinamica, dependiendo de lo ingresado
        ruta_archivo = DIR_BASE / "data" / nombre_archivo
        # try-except para resolver los posibles escenarios ejemplo no exite, sin permisos, etc
        try:
            # Abrir archivo
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                data = json.load(archivo)
            # Comprombacion por si esta vacio, con su respectivo manejo
            if not data:
                print(f"El archivo '{nombre_archivo}' está vacío.")
                break
            
            pantalla_carga("Obteniendo Datos")
            
            # match para conocer que estructura se tiene que llevar acabo dependiendo el archivo
            match nombre_archivo:
                case "Usuarios.json":
                    print("\n=== LISTADO DE USUARIOS ===")
                    for key, content in data.items():
                        print("\n_________________________________________")
                        print(f"Matrícula: {key}")
                        print(f"Nombre:    {content.get('nombre', 'N/A')}")
                        print(f"Carrera:   {content.get('carrera', 'N/A')}")
                        print(f"Correo:    {content.get('correo', 'N/A')}")
                        print(f"Rol:       {content.get('rol', 'N/A')}")
                        print(f"Servicio Social:    {content.get('Servicio Social', 'N/A')}")
                        print("_________________________________________")

                case "Organizaciones.json":
                    print("\n=== LISTADO DE ORGANIZACIONES ===")
                    for key, content in data.items():
                        print("\n_________________________________________")
                        print(f"ID Org:      {key}")
                        print(f"Nombre:      {content.get('nombre', 'N/A')}")
                        print(f"Sector:      {content.get('sector', 'N/A')}")
                        print(f"Correo:      {content.get('correo', 'N/A')}")
                        print(f"Descripción: {content.get('descripcion', 'N/A')}")
                        print(f"Página Web:  {content.get('pagina_web', 'N/A')}")
                        print("_________________________________________")

                case "Administradores.json":
                    print("\n=== LISTADO DE ADMINISTRADORES ===")
                    for key, content in data.items():
                        print("\n_________________________________________")
                        print(f"ID Admin:     {key}")
                        print(f"Nombre:       {content.get('nombre', 'N/A')}")
                        print(f"Departamento: {content.get('departamento', 'N/A')}")
                        print(f"Correo:       {content.get('correo', 'N/A')}")
                        print(f"Rol:          {content.get('rol', 'N/A')}")
                        print("_________________________________________")

                case "Bitacoras Usuarios.json":
                    print("\n=== LISTADO DE BITÁCORAS ===")
                    for key, content in data.items():
                        print("\n_________________________________________")
                        print(f"Registro:    {key}")
                        print(f"Matrícula:   {content.get('matricula', 'N/A')}")
                        print(f"Fecha:       {content.get('fecha', 'N/A')}")
                        print(f"Horas:       {content.get('horas', 'N/A')} hrs")
                        print(f"Descripción: {content.get('descripcion', 'N/A')}")
                        print("_________________________________________")

                case _:
                    print(f"Error: No existe un formato de lectura definido para '{nombre_archivo}'.")

            break
        
        except FileNotFoundError:
            print(f"Error: no se encontro el archivo '{nombre_archivo}'.")
        except json.JSONDecodeError:
            print(f"Error: El archivo '{nombre_archivo}' está corrupto o no tiene un formato JSON válido.")
        except PermissionError:
            print(f"Error: no tienes permisos para abrir '{nombre_archivo}'.")                       

# Dirige al administrador hacia la función que crea el tipo de registro elegido
def menuEscrituraArchivo():
    # Ciclo control de errore tipograficos la ingresasr el nombre archivo
    while True:
        nombre_archivo = input("Ingresa el nombre del archivo para la nueva entrada (0 para cancelar): ")
        
        # Cancelacion de la opcion
        if nombre_archivo == "0":
            break
        
        ruta_archivo = DIR_BASE / "data" / nombre_archivo

        # try-except para abrir y controlar errores al abrir archivo
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                data = json.load(archivo)
            # match para identificar que funcion hay que llamar para mejora de estrucutura
            match nombre_archivo:
                case "Usuarios.json":
                    crearCuenta(rolUsuario="Admin")        
                case "Organizaciones.json":
                    crearOrganizacion()        
                case "Bitacoras Usuarios.json":
                    crearBitacoraUsuario(rol = "Admin")        
                case "Administradores.json":
                    crearAdministrador()        
                case _:
                    print("Error inesperado")
                
            break
        except FileNotFoundError:
            print(f"Error: no se encontro el archivo '{nombre_archivo}'.")
        except PermissionError:
            print(f"Error: no tienes permisos para abrir '{nombre_archivo}'.") 

# Solicita los datos de una organización y los guarda en Organizaciones.json
def crearOrganizacion():
    organizaciones = {}
    
    # try-except para abrir organizacione.json y su manejo de errores        
    try:
        with open(RUTA_ARCHIVO_ORGS, mode="r", encoding="utf-8") as archivo:
            organizaciones = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        organizaciones = {}
    
    # estructura while para la facilidad de crecion si se llega a cometer un error tipografico
    while True:
        # peticiones necesarias para crear organizacion
        print("\n--- Crear Nueva Organización ---")
        id_org = input("ID o RFC de la Organización: ")
        nombre = input("Nombre de la Organización: ")
        sector = input("Sector: ")
        correo = input("Correo de contacto: ")
        descp = input("Descripcion de la Organización: ")
        web = input("Pagina web de la Organización: ")
        fechaTupla = estructuraFecha()
    
        if id_org in organizaciones:
            print("Esa organización ya está registrada en el sistema.")
            continue
    
        if id_org == "" or nombre == "" or correo == "":
            print("Algún dato está vacío. Por favor ingresa los datos correctamente.")
        else: 
            # estructura diciconario para pasarlo a json
            organizaciones[id_org] = {
                "id_org": id_org,
                "nombre": nombre,
                "sector": sector,
                "correo": correo,
                "descripcion": descp,
                "pagina_web": web,
                "fecha creacion": fechaTupla
            }
            
            #pdb.set_trace() 
            
            # try-except para guardar el nuevo archivo organizaciones
            try:
                with open(RUTA_ARCHIVO_ORGS, mode="w", encoding="utf-8") as archivo:
                    json.dump(organizaciones, archivo, indent=4, ensure_ascii=False)
                pantalla_carga("Escribiendo los datos")
                print("Organización registrada exitosamente.")
                break
            except OSError as e:
                print(f"Error al escribir el archivo de reporte: {e}")

# Solicita los datos de un administrador y los guarda en Administradores.json
def crearAdministrador():
    administradores = {}
    # abrir y controlar errores del admins json    
    try:
        with open(RUTA_ARCHIVO_ADMINS, mode="r", encoding="utf-8") as archivo:
            administradores = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        administradores = {}
    
    # ciclo para el manejor de errores tipograficos
    while True:
        # todos los campos necesario para crear admin
        print("\n--- Crear Nuevo Administrador ---")
        id_admin = input("ID de Administrador (ej. número de nómina): ")
        nombre = input("Nombre completo: ")
        departamento = input("Departamento: ")
        correo = input("Correo Institucional: ")
        fechaTupla = estructuraFecha()
        
        # comprobaciones de informacion ingresada
        if id_admin in administradores:
            print("Ese administrador ya está registrado en el sistema.")
            continue
    
        if id_admin == "" or nombre == "" or correo == "":
            print("Algún dato está incompleto. Reintenta.")
        else:
            # adicion del dicionario con el nuevo admin
            administradores[id_admin] = {
                "id_admin": id_admin,
                "nombre": nombre,
                "departamento": departamento,
                "correo": correo,
                "rol": "Admin",
                "fecha creacion": fechaTupla
            }
            # control de errores y abri escritura archivo para guardado del nuevo diccionario admins
            try:
                with open(RUTA_ARCHIVO_ADMINS, mode="w", encoding="utf-8") as archivo:
                    json.dump(administradores, archivo, indent=4, ensure_ascii=False)
                pantalla_carga("Escribiendo los datos")
                print("Administrador creado exitosamente.")
                break
            except OSError as e:
                print(f"Error al escribir el archivo de reporte: {e}")
 
### Funcion reutilizable dentro de los do roles Alumno / Admin
# Registra las horas y actividades de un alumno en Bitacoras Usuarios.json
def crearBitacoraUsuario(rol):
    
    # deficion del min y max de hora diarias
    max_horas_diarias = 8  
    min_horas_diarias = 1
    
    bitacoras = {}
    
    # abrir archivo de bitacoras json con manejo de errores
    try:
        with open(RUTA_ARCHIVO_BITACORAS, mode="r", encoding="utf-8") as archivo:
            bitacoras = json.load(archivo)
            
    except (FileNotFoundError, json.JSONDecodeError):
        bitacoras = {}
    
    # ciclo para ingresar datos aunque haya un error tipografico
    while True:
        print("\n--- Registro de Bitácora ---")
        print("Advertencia solo se puede añadir un registro por día")
        if rol == "Alumno":
            global matricula
        else:
            matricula = input("Ingresa la matrícula del usuario: ")
        
        # formacion estructura tupla con la funicon   
        fechaTupla = estructuraFecha() 
        
        # Validar entrada numérica para evitar que el programa falle
        while True:
            try:
                # Usando la función auxiliar de entrada descrita anteriormente
                horas = int(input("Ingresa las horas acumuladas (entero): "))

                if horas < min_horas_diarias:
                    print(f"Error: Debes registrar al menos {min_horas_diarias} hora.")
                    continue
                    
                if horas > max_horas_diarias:
                    print(f"Error: No puedes registrar más de {max_horas_diarias} horas en un solo día.")
                    continue

                break
            except ValueError:
                print("Error: Ingresa un número entero válido.")

        descripcion = input("Ingresa las actividades realizadas: ")

        # Validaciones de campos obligatorios
        if matricula == "" or descripcion == "":
            print("La matrícula, fecha y descripción no pueden estar vacías.")
            continue
            
        if horas <= 0:
            print("Las horas deben ser un número entero mayor a cero.")
            continue

        # Crear estructura de registro
        bitacoras[f"{matricula} - {fechaTupla}"] = {
            "matricula": matricula,
            "fecha": fechaTupla,
            "horas": horas,
            "descripcion": descripcion
        }
        
        # Escritura física en JSON
        with open(RUTA_ARCHIVO_BITACORAS, mode="w", encoding="utf-8") as archivo:
            json.dump(bitacoras, archivo, indent=4, ensure_ascii=False)

        print(f"Registro guardado exitosamente para la matrícula {matricula}.")
        break

# Genera un reporte de texto con los datos y las horas registradas de un alumno
def generarReporteAlumno():
    # abrir archivo usuario para conocer a quien identificar en los demas archivos
    try:
        with open(RUTA_ARCHIVO_USERS, mode="r", encoding="utf-8") as archivo:
            usuarios = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error: No se pudo abrir o leer 'Usuarios.json'.")
        return

    # entrada de datos
    print("\n--- Exportar Reporte de Alumno ---")
    matricula = input("Ingresa la matrícula del alumno a consultar: ")
    fechaTupla = estructuraFecha()
    
    # comprobacion de datos
    if matricula not in usuarios:
        print(f"Error: La matrícula '{matricula}' no se encuentra registrada.")
        return

    alumno = usuarios[matricula]

    # try-except manejo de errores al abrir y leer bitacoras
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

    # generacion de horas y lectra de los registro por el alumno
    total_horas = sum(registro.get("horas", 0) for registro in registros_alumno)
    total_registros = len(registros_alumno)
    
    #pdb.set_trace() 
    
    # generacion de ruta para el guardado del reporte
    CARPETA_REPORTES.mkdir(parents=True, exist_ok=True)
    ruta_txt = CARPETA_REPORTES / f"Reporte_{matricula}.txt"

    # esquema del reporte para el txt
    lineas = [
        "_" * 55,
        "               REPORTE DETALLADO DE ALUMNO               ",
        "_" * 55,
        f"Matrícula: {alumno.get('matricula', 'N/A')}",
        f"Nombre:    {alumno.get('nombre', 'N/A')}",
        f"Carrera:   {alumno.get('carrera', 'N/A')}",
        f"Correo:    {alumno.get('correo', 'N/A')}",
        f"Rol:       {alumno.get('rol', 'N/A')}",
        f"Fecha Creacion reporte:   {fechaTupla}",
        "-" * 55,
        f"Total de entradas registradas: {total_registros}",
        f"Total de horas acumuladas:    {total_horas} hrs",
        "-" * 55
    ]
    # comprobacion de registro en la bitacora
    if not registros_alumno:
        lineas.append("El alumno no cuenta con actividades en su bitácora.")
    else:
        lineas.append("HISTORIAL DE ACTIVIDADES:")
        # ciclo for para ver todas los regitros del estudiante
        for i, reg in enumerate(registros_alumno, start=1):
            lineas.append(f"  [{i}] Fecha: {reg.get('fecha')} | Horas: {reg.get('horas')}")
            lineas.append(f"      Descripción: {reg.get('descripcion')}")
            lineas.append("-" * 40)

    lineas.append("=" * 55)
    
    #pdb.set_trace() 
    
    pantalla_carga("Generando el Archivo (～￣▽￣)～")
    # control y manejo de errores al escribir el txt
    try:
        with open(ruta_txt, mode="w", encoding="utf-8") as archivo_txt:
            archivo_txt.write("\n".join(lineas))
        print(f"\nReporte generado con éxito en: {ruta_txt}")
    except OSError as e:
        print(f"Error al escribir el archivo de reporte: {e}")

# Muestra el menú del administrador y ejecuta las operaciones disponibles
def acciones_admin():
    
    # matriz opciones
    matriz_menu = [
    ["1) Vista y lectura Archivos", "2) Escritura Archivo"],
    ["3) Crear Reporte Alumno",     "4) Salir Cuenta"]
]
    
    while True:
        # impresion de la matriz con un ciclo for
        print("\nBienvenido Administrador " + nombre)
        for i in range(len(matriz_menu)):
            for j in range(len(matriz_menu[i])):
                print(f"{matriz_menu[i][j]}") 
        
        # monitoreo respuesta con la funicon controlInactividad
        respuesta = controlInactividad("Opción: ", mins_limite=10)
        # comprobracion de resultado = inactividad        
        if respuesta == "inactividad":
            confirmacion = respuestaInactividad()
            if confirmacion == "si":
                continue
            elif confirmacion == "no":
                return
        # manejo de una opcion invalida
        try:
            opcion = int(respuesta)
        except ValueError:
            print("Error: Debes ingresar una opcion valida.")
            continue
            
        # match para leer los archivo
        match opcion:
            case 1:
                # Lectura archivo
                vistaArchivos()
                lecturaArchivo()
            case 2:
                # Escritura archivo
                vistaArchivos()
                menuEscrituraArchivo()          
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

## Funciones Rol Organizacion
# Informa que las funciones para el rol de organización aún no están disponibles
def menuOrganizacion():
    # impresion aviso de que aun no esta listo el programa
    print("\n___________________________________\n")
    print("Por le momento, las funciones de organizacin no se encuetra disponible")
    print("Agradecemos su atención")
    print("ヾ(⌒ー⌒)ノ")
    print("\n___________________________________\n")
    return
# -------------------------------------  
  
# Menú dentro de la app
while True:
    #Uso de la funcion para el Registro / iniciar sesion de la cuenta
    registro_acceso_cuenta()
    if boolSalir == True:
        break
    
    datosUsuario = loadDataUser(matricula = matricula)
    # si falla el cargado de datos de la persona 
    if not datosUsuario:
        print("Error: No se encontraron los datos del usuario. Verifica la matrícula.")
        continue
    
    # Rol y nombre recuperado con la cuenta
    rol = datosUsuario["rol"]
    nombre = datosUsuario["nombre"]
    #pdb.set_trace() 
    match rol:
        case "Alumno":
            # Menu con todas las acciones para ALUMNOS
            acciones_alumno()
        case"Organización":
            menuOrganizacion()
        case "Admin":
            acciones_admin()

print("Agradecemos Su Preferencia")
