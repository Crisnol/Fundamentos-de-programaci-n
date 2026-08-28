# Reporte Prototipo

## Análisis Organizacional

**Institución:** Universidad Tecmilenio.

**Área de impacto operativo:** Coordinación de Servicio Social y Vinculación Estudiantil.

**Necesidad:** Esta área es encargada de vincular a los estudiantes con las organizaciones y supervisar el avance del estudiante y el cumplimiento de las organizaciones. Este departamento requiere una mejor gestión en cuanto a compartir información clara de cada organización, así como los cupos por cada una, además de mantener un correcto seguimiento de cada estudiante.

## Definición del Problema

La falta de información accesible y rápida al empezar el servicio social hace que surjan dudas que pueden ser clave para una buena estancia, es por eso que tener la información clara y precisa, hacen tomar una mejor decisión.

Además el seguimiento del Servicio Social depende actualmente de un sistema manual basado en formatos impresos, firmas físicas y entregas de reportes en papel. Esto tiene puntos críticos como la pérdida o deterioro de comprobantes de evidencia, inconsistencia en el conteo de horas acumuladas, incapacidad de consultar en tiempo real la disponibilidad de vacantes en las organizaciones aliadas lo que provoca riesgo de sobrecupo.

Para resolver esto se propone un sistema de gestión de servicio social en Python que centralice el catálogo de organizaciones socio-formadoras, automatice la inscripción según cupos disponibles y administre una bitácora digital de horas trabajadas con aprobación de estados.

## Listado de Requerimientos

### Gestión de usuarios y expedientes

- **Identificación de rol**: Permitir diferentes puestos (Alumno/Organización/Administrador), para asignar funciones especiales para cada rol.
- **Registro de estudiantes:** Registrar nuevos alumnos capturando matrícula, nombre completo y carrera.
- **Consulta de avance:** El alumno debe poder visualizar su expedientes, asi como organización asignada, el total de horas validadas y el porcentaje completado respecto a la meta institucional (480 horas).

### Catálogo de Organizaciones y Cupos

- **Registro de organizaciones:** Registrar nuevas organizaciones, pidiendo datos como nombre, información de la organización y cupos.
- **Visualización de organizaciones:** Despliegue de todas las organizaciones para acceder a su explicación, así como las vacantes disponibles.
- **Registro de alumnos a las organizaciones:** Poder registrarte a las vacantes disponibles y hacer la lógica del llenado de los cupos para que conforme se registren vayan disminuyendo.

### Registro de Bitácora y Evidencias

- **Captura de actividades:** El alumno podrá registrar la fecha, hora de inicio y fin y descripción de las actividades realizadas.
- **Asignación de estado:** Asignar diferentes estados (Pendiente/Firmado/Revisión) por cada nuevo día registrado para la revisión por su supervisor.

### Validación Administrativa y Persistencia

- **Revisión de entregas:** La organización podrá ver y revisar todas las nuevas peticiones de firma para su validación.
- **Actualización de acumulado:** El sistema debe recalcular el total de horas del alumnos por cada petición aceptada.

## Clasificación de Datos

Para este sistema se plantea usar los siguientes tipos de datos.

### Estudiantes

Se necesitan datos básicos para su asignación y su continuo registro.

- Matrícula / str / Cadena
- Nombre / str / Cadena
- Carrera / str / Cadena
- org_asignada / str / Cadena
- horas_acumuladas / float / Flotante

### Organización

Para el nuevo ingreso de organizaciones se necesitan sus datos principales a mostrar y un conteo de sus lugares disponibles.

- Nombre / str / Cadena
- área / str / Cadena
- Cupos totales / int / Entero
- Cupos disponibles / int / Entero

### Bitácora

Para una correcta estructuración de cada entrada se necesitan datos primordiales y datos para su validación, para un conteo de horas exitoso.

- Fecha / str / Cadena
- Horas reportadas / float / Flotante
- Descripción / str / Cadena
- Estado / str / Cadena
- Validado / bool / Booleano

## Operadores del Lenguaje

### Operadores Matemáticos

| Símbolo | Operación | Aplicación en el código | Justificación |
|---|---|---|---|
| + | Suma | Acumulación de horas en el expediente. | Incrementa el total con cada jornada validada (horas_acumuladas += horas_reportadas) para mantener el avance actualizado |
| - | Resta | Control de vacantes | Decrementa la disponibilidad (cupos_disponibles -= 1) tras una inscripción |
| / y * | División y multiplicación | Cálculo del porcentaje de avance. | Avance del estudiante mediante la expresión (horas_acumuladas / meta_horas) * 100 |

### Operadores Relacionales

| Símbolo | Comparación | Aplicación en el código | Justificación |
|---|---|---|---|
| == | igual a | Autenticación y filtrado de datos. | Compara cadenas para validar el rol ingresado (rol == "Alumno") o filtrar la bitácora (estado == "Pendiente") |
| >= | Mayor o igual | Comprobación de liberación de servicio. | Evalúa si el estudiante alcanzó o superó la cuota institucional (horas_acumuladas >= 480) |
| > | Mayor | Control de cupos en la organización. | Evalúa si la entidad socio-formadora cuenta con plazas libres (cupos_disponibles > 0) antes de procesar una inscripción |

### Operadores Lógicos y de Pertenencia

| Símbolo | Lógica | Aplicación en el código | Justificación |
|---|---|---|---|
| and | Conjunción | Validación de reglas compuestas. | El cumplimiento del llenado de todos los datos para la creación de cuentas de alumnos, organizaciones y registro de bitácora |
| or | Disyunción | Tolerancia en las entradas del menú | Permite validar múltiples opciones válidas ingresadas por el usuario (ejemplo: opcion == '1' or opcion == 'a') |
| not | Negación | Detección de ausencia de datos. | Invierte la evaluación para controlar errores de búsqueda cuando un registro no existe |

## Estructuras de Control

### Estructuras Condicionales

#### if - elif - else — Navegación y selección de rol

Evalúa el tipo de rol para mostrar un menú dedicado con funciones especiales para cada uno.

- Ejemplo: Si el rol es 'Alumno', invoca las funciones del estudiante; si es 'Organización', abre el panel de la organización; si no coincide con ninguna, despliega un mensaje de comando inválido.

#### if - else — Validación estricta de vacantes

Comprueba la disponibilidad de cupos para cada organización cuando se quiera hacer el registro.

- Ejemplo: Evalúa `if cupos_disponibles > 0:` para restar una plaza y vincular la matrícula. Si la condición falla, salta al bloque `else` notificando que la entidad seleccionada carece de espacios libres.

#### if - elif - else — Dictamen de reportes de bitácora

Permite mostrar las diferentes opción al cambio de estado de cada registro de la bitácora.

- Ejemplo: Si el estado es "Rechazado", poder revisar y cambiar porque fue rechazado y con esto no contabilizar las horas.

#### if simple — Verificación de meta alcanzada

Evalúa si el alumno completó las horas programadas (480 hrs), con esto cambiar el estado del alumno y poder obtener funciones como la generación de reportes.

### Estructuras Iterativas

#### while True — Bucle principal de la aplicación

Mantiene la interfaz de consola activa y receptiva a comandos hasta que el usuario ejecute la instrucción de salida.

Envuelve todo el flujo del programa. Solo se rompe mediante una sentencia break cuando se elige la opción "Salir" en el menú principal, asegurando que el sistema no se cierre tras completar una sola tarea.

#### while — Validación y reintento de entradas

Obliga a ingresar datos válidos cuando el usuario comete errores de sintaxis al teclear por consola.

Encierra las capturas de datos numéricos (como las horas trabajadas). Si el alumno ingresa texto en lugar de un valor flotante, la excepción ValueError es capturada dentro del ciclo, solicitando el dato nuevamente sin que el programa colapse.


#### for en listas de diccionarios

Recorre colecciones de datos para extraer, filtrar o mostrar información en pantalla, como por ejemplo, recorrer el arreglo de organizaciones para imprimir el listado, nombre y vacantes restantes.

# Pseudocódigo Formal - Sistema de Gestión de Servicio Social
 
## 1. Algoritmo principal
 
```
INICIO
 
    MIENTRAS Verdadero HACER
 
        MOSTRAR "1) Iniciar Sesión"
        MOSTRAR "2) Crear Cuenta"
        MOSTRAR "3) Salir del programa"
        LEER opcion
 
        SI opcion NO ES ENTERO ENTONCES
            MOSTRAR "Ingrese un número válido"
            CONTINUAR
        FIN SI
 
        SEGÚN opcion HACER
 
            CASO 1:
                cuentaActiva = IniciarSesion()
                SI cuentaActiva == NULO ENTONCES
                    CONTINUAR
                FIN SI
 
            CASO 2:
                cuentaActiva = CrearCuenta()
 
            CASO 3:
                SALIR DEL PROGRAMA
 
            OTRO CASO:
                MOSTRAR "Ingrese una opción válida"
                CONTINUAR
 
        FIN SEGÚN
 
        MenuPrincipal(cuentaActiva)
 
    FIN MIENTRAS
 
FIN
```
 
---
 
## 2. Iniciar sesión
 
 
``` 
    MIENTRAS Verdadero HACER
        MOSTRAR "Para iniciar sesión ingresa tu matrícula"
        LEER matricula
 
        SI matricula == "" ENTONCES
            MOSTRAR "Matrícula incorrecta"
            CONTINUAR
        FIN SI
 
        cuenta = BUSCAR matricula EN listaCuentas
 
        SI cuenta == NULO ENTONCES
            MOSTRAR "No existe una cuenta con esa matrícula"
        SINO

        FIN SI
  
    FIN MIENTRAS
```
 
---
 
## 3. Crear cuenta
 
 
```
    MIENTRAS Verdadero HACER
        MOSTRAR "Para crear una nueva cuenta ingresa los siguientes datos"
        LEER matricula
        LEER nombre
        LEER carrera
 
        SI matricula == "" O LONGITUD(matricula) != 10 ENTONCES
            MOSTRAR "La matrícula debe tener 10 caracteres"
            CONTINUAR
        FIN SI
 
        SI nombre == "" O carrera == "" ENTONCES
            MOSTRAR "Nombre y carrera son obligatorios"
            CONTINUAR
        FIN SI
 
        nuevaCuenta = NUEVA Cuenta(matricula, nombre, carrera, rol = "Alumno")
 
    FIN MIENTRAS
```
 
---
 
## 4. Menú principal (según rol)
 
``` 
    MIENTRAS Verdadero HACER
 
        SEGÚN cuenta.rol HACER
 
            CASO "Alumno":
                salir = MenuAlumno(cuenta)
                SI salir ENTONCES ROMPER FIN SI
 
            CASO "Organización":
                salir = MenuOrganizacion(cuenta)
                SI salir ENTONCES ROMPER FIN SI
 
            CASO "Admin":
                salir = MenuAdmin(cuenta)
                SI salir ENTONCES ROMPER FIN SI
 
        FIN SEGÚN
 
    FIN MIENTRAS
```
 
---
 
## 5. Menú Alumno
 
``` 
    MOSTRAR "Bienvenido al sistema"
    MOSTRAR "1) Organizaciones"
    MOSTRAR "2) Mi servicio"
    MOSTRAR "3) Salir de la cuenta"
    LEER opcion
 
    SEGÚN opcion HACER
 
        CASO 1:
            VerOrganizaciones()
            DEVOLVER Falso
 
        CASO 2:
            MenuServicio(cuenta)
            DEVOLVER Falso
 
        CASO 3:
            MOSTRAR "Saliendo de la cuenta..."
            DEVOLVER Verdadero
 
        OTRO CASO:
            MOSTRAR "Ingrese una opción válida"
            DEVOLVER Falso
 
    FIN SEGÚN
 
 
FUNCION VerOrganizaciones()
 
    MOSTRAR "Organizaciones Socias"
    PARA CADA org EN listaOrganizaciones HACER
        MOSTRAR org.nombre, " (Cupos: ", org.cupos, ")"
    FIN PARA
 
    LEER opcionOrg
    
FIN FUNCION
 
 
FUNCION MenuServicio(cuenta: Cuenta)
 
    MOSTRAR "Mi servicio"
    MOSTRAR "Organización actual: ", cuenta.organizacionActual
    MOSTRAR "Horas acumuladas: ", cuenta.horasAcumuladas, " hrs"
    MOSTRAR "1) Registrar un nuevo día"
    MOSTRAR "2) Ver detalles de mi servicio"
    LEER opcionServicio
 
    SEGÚN opcionServicio HACER
 
        CASO 1:
            LEER fecha
            LEER horas
            LEER descripcion
            registro = NUEVO RegistroBitacora(fecha, horas, descripcion)
            AGREGAR registro A cuenta.bitacora
            cuenta.horasAcumuladas = cuenta.horasAcumuladas + horas
 
        CASO 2:
            PARA CADA registro EN cuenta.bitacora HACER
                MOSTRAR registro.fecha, " - ", registro.horas, "hrs - ", registro.descripcion
            FIN PARA
 
        OTRO CASO:
            MOSTRAR "Ingrese una opción válida"
 
    FIN SEGÚN
 
FIN FUNCION
```
 