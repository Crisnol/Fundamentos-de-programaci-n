# SEMANA 3: INTEGRACIÓN DE LOS TEMAS 1 AL 8 Y GUÍA DEL AVANCE DEL RETO/PROYECTO (FASE I)

**Curso:** Solución de problemas con programación computacional  
**Institución:** Universidad Tecmilenio  
**Rol:** PyCoach — Guía Docente y Material de Clase  

**Actividad de la semana:** Avance del Reto/Proyecto (Fase I) — **25%** de la calificación total del curso  
**Fechas límite:** 28 de agosto de 2026 (Periodo I) · 30 de octubre de 2026 (Periodo II)  
**Temas integrados:** Temas 1 al 8 (esta semana **no hay temas nuevos**: el contenido es de integración y guía del avance)

---

## ÍNDICE DEL MATERIAL
1. **¿Por qué una semana de integración?** (Qué se evalúa y por qué no hay temas nuevos)
2. **Recorrido Rápido — Tema 1:** Algoritmos y modelo Entrada-Proceso-Salida (EPS)
3. **Recorrido Rápido — Tema 2:** PSeInt y pseudocódigo
4. **Recorrido Rápido — Tema 3:** Variables, tipos de datos y operadores
5. **Recorrido Rápido — Tema 4:** Entradas y salidas simples (`input`, `print`, conversiones)
6. **Recorrido Rápido — Tema 5:** Estructuras de decisión (`if`, `elif`, `else`)
7. **Recorrido Rápido — Tema 6:** Estructura de repetición `while`
8. **Recorrido Rápido — Tema 7:** *Debugging* (depuración de código con PDB)
9. **Recorrido Rápido — Tema 8:** Estructura de repetición `for`
10. **Problemas Integradores:** Ejemplos prácticos que combinan varios temas
11. **Guía paso a paso para el AVANCE DEL PROYECTO (Fase I):** Los 8 requerimientos
12. **Actividad de la Semana y Entregables**

---

# 1. ¿POR QUÉ UNA SEMANA DE INTEGRACIÓN?

El plan del curso está alineado a las entregas del sistema institucional. La **Semana 3** está reservada para la entrega del **Avance del Reto/Proyecto (Fase I)**, que pondera el **25%** de la calificación total del curso. Por ello, en esta semana **no se introduce ningún tema nuevo**: los ocho temas ya vistos (Temas 1 al 8) se convierten en las herramientas que deberás combinar para diseñar la solución técnica de tu proyecto.

El objetivo de esta semana es triple:

1. **Recapitular** los conceptos esenciales de los Temas 1 al 8.
2. **Integrarlos** en ejemplos prácticos que combinan decisión, ciclos y acumuladores.
3. **Guiarte paso a paso** en los **8 requerimientos** del Avance del Proyecto (Fase I), tal como lo exige la agenda oficial del curso (sección 4).

> **NOTA CLAVE:** Esta semana **NO tiene ejercicios extra evaluables**. Los únicos componentes que se evalúan son la **actividad oficial del avance**, el **Jupyter de práctica semanal** y el **uso de Git/GitHub**.

---

# 2. RECORRIDO RÁPIDO — TEMA 1: ALGORITMOS Y MODELO ENTRADA-PROCESO-SALIDA (EPS)

Un **algoritmo** es una secuencia finita, ordenada y no ambigua de pasos que resuelve un problema. Todo programa opera bajo el modelo **Entrada - Proceso - Salida (EPS)**:

```
[ Entrada de Datos ]  --->  [ Proceso / Transformación ]  --->  [ Salida de Resultados ]
```

**Recordatorio clave para el avance del proyecto:** Antes de escribir una sola línea de código, debes definir con precisión cuáles son los datos de entrada, qué transformaciones se les aplica y qué resultados se entregan.

**Ejemplo integrado (EPS + decisión):** Determinar si una compra de $500 o más recibe el 10% de descuento.

```
ENTRADA: monto = 500
PROCESO: si monto >= 500, entonces descuento = monto * 0.10, si no descuento = 0
         total = monto - descuento
SALIDA:  total = 450.0
```

Verificación: `500 * 0.10 = 50`, `500 - 50 = 450`. Correcto.

---

# 3. RECORRIDO RÁPIDO — TEMA 2: PSEINT Y PSEUDOCÓDIGO

**PSeInt** es la herramienta educativa que permite escribir y probar algoritmos en **pseudocódigo en español** antes de traducirlos a Python. La estructura general usa `Algoritmo`, `Escribir`, `Leer`, `<-` y `FinAlgoritmo`.

**Ejemplo integrado (PSeInt + ciclo + acumulador):** Sumar números hasta que el usuario ingrese `0`.

```text
Algoritmo SumaHastaCero
    Definir numero, suma Como Entero
    suma <- 0
    Escribir "Ingrese un numero (0 para terminar):"
    Leer numero
    Mientras numero <> 0 Hacer
        suma <- suma + numero
        Escribir "Ingrese un numero (0 para terminar):"
        Leer numero
    FinMientras
    Escribir "La suma es: ", suma
FinAlgoritmo
```

**Traducción directa a Python:**

```python
suma = 0
numero = int(input("Ingrese un numero (0 para terminar): "))
while numero != 0:
    suma = suma + numero
    numero = int(input("Ingrese un numero (0 para terminar): "))
print("La suma es:", suma)
```

Verificación con entradas `5, 8, 3, 0`: `5 + 8 + 3 = 16`. La salida es `La suma es: 16`.

---

# 4. RECORRIDO RÁPIDO — TEMA 3: VARIABLES, TIPOS DE DATOS Y OPERADORES

Una **variable** es un espacio en memoria con un nombre que almacena un valor cambiante. Python infiere el tipo automáticamente (tipado dinámico).

| Tipo de Dato | Tipo en Python (`type`) | Ejemplo |
| :--- | :--- | :--- |
| **Entero** | `int` | `cantidad = 3` |
| **Flotante** | `float` | `precio = 35.50` |
| **Cadena** | `str` | `nombre = "Ana"` |
| **Booleano** | `bool` | `es_estudiante = True` |

**Operadores que ya dominas (y usarás en el avance):**

```python
a = 10
b = 3

print(a + b)    # Suma           -> 13
print(a - b)    # Resta          -> 7
print(a * b)    # Multiplicación -> 30
print(a / b)    # División       -> 3.333...
print(a // b)   # División entera -> 3
print(a % b)    # Módulo         -> 1
print(a ** b)   # Potencia       -> 1000
```

Operadores **relacionales**: `==`, `!=`, `>`, `<`, `>=`, `<=`.  
Operadores **lógicos**: `and`, `or`, `not`.

**Ejemplo integrado (tipos + operadores relacionales y lógicos):**

```python
es_estudiante = True
monto = 150
descuento_valido = es_estudiante and monto >= 150   # True and True -> True
print(descuento_valido)                              # True
```

---

# 5. RECORRIDO RÁPIDO — TEMA 4: ENTRADAS Y SALIDAS SIMPLES

> **¡REGLA DE ORO DE PYTHON!** Todo dato capturado con `input()` se recibe como cadena (`str`); se debe convertir con `int()` o `float()` para operar numéricamente.

**Ejemplo integrado (input + casting + f-string + operador):**

```python
nombre = input("Nombre del cliente: ")
platillos = int(input("Cantidad de platillos: "))
precio_unitario = float(input("Precio unitario: "))
total = platillos * precio_unitario
print(f"Cliente {nombre}, total a pagar: ${total:.2f}")
```

Verificación con `nombre = "Ana"`, `platillos = 3`, `precio_unitario = 45.0`: `3 * 45.0 = 135.00`. Salida: `Cliente Ana, total a pagar: $135.00`.

---

# 6. RECORRIDO RÁPIDO — TEMA 5: ESTRUCTURAS DE DECISIÓN (`if`, `elif`, `else`)

Las estructuras de decisión permiten que el programa elija caminos distintos según una condición.

**Ejemplo integrado (decisión + clasificación de datos):**

```python
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 12:
    print("Eres adolescente")
else:
    print("Eres menor de edad")
```

| Entrada | Proceso | Salida |
| :--- | :--- | :--- |
| `20` | `20 >= 18` es `True` | `Eres mayor de edad` |
| `14` | `20 >= 18` es `False`, `14 >= 12` es `True` | `Eres adolescente` |
| `8` | ambas condiciones son `False` | `Eres menor de edad` |

---

# 7. RECORRIDO RÁPIDO — TEMA 6: ESTRUCTURA DE REPETICIÓN `while`

El ciclo `while` repite un bloque **mientras** una condición sea verdadera. Es ideal cuando no sabemos de antemano cuántas veces se repetirá (menús, validaciones, acumuladores con centinela).

**Ejemplo integrado (while + acumulador + decisión):** Registrar ventas del día hasta que el monto sea `0`.

```python
total = 0
contador = 0
venta = float(input("Monto de la venta (0 para terminar): "))
while venta != 0:
    total = total + venta
    contador = contador + 1
    venta = float(input("Monto de la venta (0 para terminar): "))
if contador > 0:
    promedio = total / contador
    print(f"Total de ventas: ${total:.2f}")
    print(f"Numero de ventas: {contador}")
    print(f"Ticket promedio: ${promedio:.2f}")
else:
    print("No se registraron ventas.")
```

Verificación con entradas `120, 80, 200, 0`: `total = 400`, `contador = 3`, `promedio = 400 / 3 = 133.33`. Salidas: `Total de ventas: $400.00`, `Numero de ventas: 3`, `Ticket promedio: $133.33`.

> **RIESGO A EVITAR:** Si olvidas actualizar la variable de la condición dentro del ciclo, se genera un ciclo infinito. Siempre asegúrate de que la condición pueda volverse falsa.

---

# 8. RECORRIDO RÁPIDO — TEMA 7: *DEBUGGING* (DEPURACIÓN DE CÓDIGO CON PDB)

El **debugging** es el proceso de encontrar y corregir errores. El módulo estándar **PDB** permite ejecutar el programa paso a paso e inspeccionar variables.

**Comandos esenciales de PDB:**

| Comando | Acción |
| :--- | :--- |
| `breakpoint()` | Inserta un punto de interrupción (Python 3.7+). |
| `n` (next) | Ejecuta la siguiente línea. |
| `p variable` | Imprime el valor actual de una variable. |
| `l` (list) | Muestra el código alrededor de la línea actual. |
| `c` (continue) | Continúa la ejecución normal. |
| `q` (quit) | Sale del depurador. |

**Ejemplo integrado (error lógico detectado con PDB):** El siguiente código calcula el promedio de 3 calificaciones, pero divide entre `4` en lugar de `3`.

```python
suma = 0
contador = 0
breakpoint()                      # El programa se pausa aquí
for i in range(3):
    cal = float(input("Calificación: "))
    suma = suma + cal
    contador = contador + 1
promedio = suma / 4               # BUG: debería ser contador
print("El promedio es:", promedio)
```

**Sesión típica de depuración (entradas `8, 9, 10`):**

```text
> (Pdb) p suma          # Tras cargar 8, 9 y 10
27.0
> (Pdb) p contador
3
> (Pdb) c
El promedio es: 6.75     # Salida incorrecta (27 / 4)
```

Con PDB se observa que `suma = 27` y `contador = 3`, por lo que el divisor debe ser `contador` y no `4`. Corregido: `promedio = suma / contador` produce `27 / 3 = 9.0`. La salida correcta es `El promedio es: 9.0`.

---

# 9. RECORRIDO RÁPIDO — TEMA 8: ESTRUCTURA DE REPETICIÓN `for`

El ciclo `for` recorre una secuencia conocida de valores (`range(n)` genera los valores de `0` a `n-1`). Es ideal cuando se conoce de antemano cuántas veces se repetirá.

**Ejemplo integrado (for + acumulador + decisión):** Calcular cuántos números pares hay del 1 al N.

```python
n = int(input("Hasta que numero: "))
pares = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        pares = pares + 1
print(f"Del 1 al {n} hay {pares} numeros pares")
```

Verificación con `n = 10`: pares `{2, 4, 6, 8, 10}` → `pares = 5`. Salida: `Del 1 al 10 hay 5 numeros pares`.

**Uso de `range` (repaso):**

```python
for i in range(1, 6):     # 1, 2, 3, 4, 5
    print(i)

for i in range(2, 11, 2): # 2, 4, 6, 8, 10 (paso 2)
    print(i)
```

---

# 10. PROBLEMAS INTEGRADORES: EJEMPLOS QUE COMBINAN VARIOS TEMAS

## Problema Integrador 1: Promedio con validación y nivel (Temas 2, 3, 4, 5, 6 y 8)

Captura N calificaciones (0 a 10), valida cada una con `while`, acumula con `for`, calcula el promedio y muestra un nivel con `if/elif/else`.

**Pseudocódigo en PSeInt:**

```text
Algoritmo PromedioValidado
    Definir n, i Como Entero
    Definir cal, suma, promedio Como Real
    Escribir "Numero de calificaciones:"
    Leer n
    suma <- 0
    Para i <- 1 Hasta n Hacer
        Escribir "Calificacion ", i, ":"
        Leer cal
        Mientras cal < 0 O cal > 10 Hacer
            Escribir "Invalida. Reingrese (0-10):"
            Leer cal
        FinMientras
        suma <- suma + cal
    FinPara
    promedio <- suma / n
    Si promedio >= 9 Entonces
        Escribir "Nivel: Excelente"
    Sino Si promedio >= 8 Entonces
        Escribir "Nivel: Bueno"
    Sino Si promedio >= 7 Entonces
        Escribir "Nivel: Aprobado"
    Sino
        Escribir "Nivel: Reprobado"
    FinSi
    Escribir "Promedio: ", promedio
FinAlgoritmo
```

**Código en Python:**

```python
n = int(input("Numero de calificaciones: "))
suma = 0
for i in range(1, n + 1):
    cal = float(input(f"Calificacion {i}: "))
    while cal < 0 or cal > 10:
        print("Calificacion invalida. Reingrese (0-10).")
        cal = float(input(f"Calificacion {i}: "))
    suma = suma + cal
promedio = suma / n
if promedio >= 9:
    nivel = "Excelente"
elif promedio >= 8:
    nivel = "Bueno"
elif promedio >= 7:
    nivel = "Aprobado"
else:
    nivel = "Reprobado"
print(f"Promedio: {promedio:.2f}")
print(f"Nivel: {nivel}")
```

**Verificación:** Entrada `n = 3`, calificaciones `8, 9, 7`. `suma = 24`, `promedio = 24 / 3 = 8.00`, `nivel = Bueno` (porque `8.00 >= 8`). Salida:

```text
Promedio: 8.00
Nivel: Bueno
```

## Problema Integrador 2: Resumen de ventas del día (Temas 1, 3, 4, 5 y 6)

Aplica el modelo EPS para registrar ventas, acumular totales y reportar el resumen diario.

**Código en Python:**

```python
total = 0
contador = 0
mayor = 0
venta = float(input("Monto de la venta (0 para terminar): "))
while venta != 0:
    total = total + venta
    contador = contador + 1
    if venta > mayor:
        mayor = venta
    venta = float(input("Monto de la venta (0 para terminar): "))
if contador > 0:
    promedio = total / contador
    print(f"Total de ventas: ${total:.2f}")
    print(f"Numero de ventas: {contador}")
    print(f"Ticket promedio: ${promedio:.2f}")
    print(f"Venta mayor: ${mayor:.2f}")
else:
    print("No se registraron ventas.")
```

**Verificación:** Entradas `120, 80, 200, 0`. `total = 400`, `contador = 3`, `mayor = 200`, `promedio = 400 / 3 = 133.33`.

```text
Total de ventas: $400.00
Numero de ventas: 3
Ticket promedio: $133.33
Venta mayor: $200.00
```

## Problema Integrador 3: Tabla de multiplicar con rango personalizado (Temas 4, 5, 6 y 8)

**Código en Python:**

```python
n = int(input("De que numero quieres la tabla: "))
inicio = int(input("Desde que multiplicador: "))
fin = int(input("Hasta que multiplicador: "))
while inicio > fin:
    print("El inicio no puede ser mayor que el fin.")
    inicio = int(input("Desde que multiplicador: "))
    fin = int(input("Hasta que multiplicador: "))
for i in range(inicio, fin + 1):
    print(f"{n} x {i} = {n * i}")
```

**Verificación:** Entradas `n = 7`, `inicio = 1`, `fin = 5`.

```text
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
```

---

# 11. GUÍA PASO A PASO PARA EL AVANCE DEL PROYECTO (FASE I)

El Avance del Proyecto (Fase I) representa el **25%** de la calificación total. Consiste en diseñar la **arquitectura conceptual, las reglas de negocio y la lógica base** de una solución de software para una problemática real de una organización. A continuación, los **8 requerimientos exactos** de la sección 4 de la agenda, con una guía práctica. Para ilustrar cada paso se usa un ejemplo guía: la **cafetería universitaria "Sabor TEC"** (área de caja y control de pedidos).

### Requerimiento 1: Análisis Organizacional
**Exigencia de la agenda:** Identificar una empresa u organización real, seleccionar un área específica de impacto operativo y describir sus necesidades.

- Elige una empresa/organización real (pequeño negocio, departamento, asociación, etc.).
- Selecciona **un área** de impacto: caja, inventario, control de citas, ventas, etc.
- Describe sus necesidades operativas actuales.

**Ejemplo guía (cafetería "Sabor TEC"):**
> *"La cafetería Sabor TEC es un negocio real de servicio de alimentos dentro del campus. El área de impacto es la caja: la persona encargada calcula cada cuenta de forma manual y con frecuencia se equivoca al aplicar descuentos y al sumar los productos. La necesidad es automatizar el registro de pedidos, el cálculo de totales y el reporte de ventas del día."*

### Requerimiento 2: Definición del Problema
**Exigencia de la agenda:** Formular con precisión la problemática técnica a resolver y delimitar las **reglas de negocio** (cómo opera actualmente el área y bajo qué restricciones).

- Escribe el problema en una o dos oraciones claras.
- Define las **reglas de negocio**: precios, descuentos, horarios, condiciones, restricciones.

**Ejemplo guía:**
> *"El problema es que el cálculo manual de cuentas en caja genera errores en subtotales, descuentos e IVA, y no existe un resumen confiable de las ventas diarias."*
> **Reglas de negocio:** el menú es fijo (café $35, sándwich $45, jugo $25); los estudiantes reciben 10% de descuento en compras de $150 o más; el IVA es del 16%; el horario de operación es de 8:00 a 18:00.

### Requerimiento 3: Listado de Requerimientos
**Exigencia de la agenda:** Detallar los requerimientos funcionales que el software debe realizar para solucionar el problema.

- Escribe cada función con un identificador y una descripción verificable.

**Ejemplo guía:**
> - R1: Registrar el nombre del cliente y si es estudiante.
> - R2: Mostrar el menú con precios.
> - R3: Capturar la cantidad de cada producto del pedido.
> - R4: Calcular subtotal, descuento (si aplica), IVA y total.
> - R5: Aplicar el descuento solo si se cumple la regla de negocio.
> - R6: Repetir el proceso para varios clientes.
> - R7: Mostrar el resumen de ventas del día.

### Requerimiento 4: Clasificación de Datos
**Exigencia de la agenda:** Identificar y documentar los tipos de datos requeridos por la solución (enteros, flotantes, cadenas, booleanos).

- Documenta cada variable con su tipo y su uso.

**Ejemplo guía:**

| Variable | Tipo | Uso |
| :--- | :--- | :--- |
| `nombre` | `str` | Nombre del cliente |
| `es_estudiante` | `bool` | `True`/`False` para aplicar descuento |
| `cantidad_cafe`, `cantidad_sandwich`, `cantidad_jugo` | `int` | Cantidad de cada producto |
| `precio_cafe`, `precio_sandwich`, `precio_jugo` | `float` | Precios del menú |
| `subtotal`, `descuento`, `iva`, `total` | `float` | Resultados del cálculo |
| `total_dia` | `float` | Acumulador de ventas del día |

### Requerimiento 5: Operadores del Lenguaje
**Exigencia de la agenda:** Identificar y justificar los operadores matemáticos, relacionales y lógicos que serán clave en el código.

- Lista cada operador y explica por qué es necesario.

**Ejemplo guía:**

| Operador | Tipo | Justificación |
| :--- | :--- | :--- |
| `*` | Matemático | Calcular el importe de cada producto (`cantidad * precio`). |
| `+` | Matemático | Sumar los importes para obtener el subtotal. |
| `>=` | Relacional | Verificar la regla de negocio del descuento (`subtotal >= 150`). |
| `==` | Relacional | Comparar la opción del menú elegida. |
| `and` | Lógico | Combinar condiciones (ser estudiante **y** cumplir el monto mínimo). |
| `/` | Matemático | Calcular el ticket promedio del día. |

### Requerimiento 6: Estructuras de Control
**Exigencia de la agenda:** Enumerar las estructuras condicionales (ej. `if-else`) e iterativas (ej. `while`, `for`) que dirigirán el flujo del programa.

**Ejemplo guía:**
- **`if-elif-else`:** elegir el producto del menú y decidir si aplica el descuento.
- **`while`:** mantener activo el menú principal hasta que el cajero seleccione la opción de cierre del día.
- **`for`:** recorrer los productos del pedido para sumar los importes.

### Requerimiento 7: Diseño Algorítmico
**Exigencia de la agenda:** Elaborar el diagrama de flujo detallado en **PSeInt** con el flujo de trabajo funcional y exportar el **pseudocódigo formal** de trabajo.

- Crea el diagrama de flujo en PSeInt (símbolos de inicio/fin, proceso, decisión, entrada/salida).
- Exprésalo también como pseudocódigo formal y **exporta la imagen** del diagrama.

**Ejemplo guía (pseudocódigo formal en PSeInt):**

```text
Algoritmo AvanceCafeteria
    Definir nombre Como Cadena
    Definir es_estudiante Como Logico
    Definir c_cafe, c_sandwich, c_jugo Como Entero
    Definir precio_cafe, precio_sandwich, precio_jugo Como Real
    Definir subtotal, descuento, iva, total, total_dia Como Real
    Definir opcion Como Entero
    precio_cafe <- 35
    precio_sandwich <- 45
    precio_jugo <- 25
    total_dia <- 0
    Repetir
        Escribir "--- MENU ---"
        Escribir "1. Registrar pedido"
        Escribir "2. Resumen del dia"
        Escribir "3. Salir"
        Leer opcion
        Si opcion = 1 Entonces
            Escribir "Nombre del cliente:"
            Leer nombre
            Escribir "Es estudiante (V/F):"
            Leer es_estudiante
            Escribir "Cantidad de cafes:"
            Leer c_cafe
            Escribir "Cantidad de sandwiches:"
            Leer c_sandwich
            Escribir "Cantidad de jugos:"
            Leer c_jugo
            subtotal <- (c_cafe * precio_cafe) + (c_sandwich * precio_sandwich) + (c_jugo * precio_jugo)
            descuento <- 0
            Si es_estudiante Y subtotal >= 150 Entonces
                descuento <- subtotal * 0.10
            FinSi
            iva <- (subtotal - descuento) * 0.16
            total <- subtotal - descuento + iva
            total_dia <- total_dia + total
            Escribir "Cliente: ", nombre
            Escribir "Subtotal: ", subtotal
            Escribir "Descuento: ", descuento
            Escribir "IVA: ", iva
            Escribir "Total: ", total
        FinSi
    Hasta Que opcion = 3
    Escribir "Ventas del dia: ", total_dia
FinAlgoritmo
```

### Requerimiento 8: Prototipo de Código
**Exigencia de la agenda:** Desarrollar la versión inicial (prototipo ejecutable) en Python que refleje la lógica base y corra de forma correcta en consola.

- Traduce el pseudocódigo a un archivo `.py` y pruébalo en consola.

**Ejemplo guía (prototipo en Python):**

```python
precio_cafe = 35.0
precio_sandwich = 45.0
precio_jugo = 25.0
total_dia = 0.0

while True:
    print("--- MENU DE SABOR TEC ---")
    print("1. Registrar pedido")
    print("2. Resumen del dia")
    print("3. Salir")
    opcion = int(input("Selecciona una opcion: "))

    if opcion == 1:
        nombre = input("Nombre del cliente: ")
        es_estudiante = input("Es estudiante (si/no): ").lower() == "si"
        c_cafe = int(input("Cantidad de cafes: "))
        c_sandwich = int(input("Cantidad de sandwiches: "))
        c_jugo = int(input("Cantidad de jugos: "))

        subtotal = (c_cafe * precio_cafe) + (c_sandwich * precio_sandwich) + (c_jugo * precio_jugo)
        descuento = 0.0
        if es_estudiante and subtotal >= 150:
            descuento = subtotal * 0.10
        iva = (subtotal - descuento) * 0.16
        total = subtotal - descuento + iva
        total_dia = total_dia + total

        print(f"Cliente: {nombre}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Descuento: ${descuento:.2f}")
        print(f"IVA (16%): ${iva:.2f}")
        print(f"Total: ${total:.2f}")

    elif opcion == 2:
        print(f"Ventas acumuladas del dia: ${total_dia:.2f}")

    elif opcion == 3:
        print("Cerrando el sistema del dia.")
        break
    else:
        print("Opcion invalida.")
```

**Verificación del prototipo (dos clientes):**

*Cliente 1:* `nombre = "Ana"`, no estudiante, `2` cafés, `1` sándwich, `0` jugos.
`subtotal = (2 * 35) + (1 * 45) + (0 * 25) = 115`. No aplica descuento (`115 < 150`). `iva = 115 * 0.16 = 18.40`. `total = 115 + 18.40 = 133.40`.

*Cliente 2:* `nombre = "Luis"`, estudiante, `3` cafés, `2` sándwiches, `0` jugos.
`subtotal = (3 * 35) + (2 * 45) + (0 * 25) = 105 + 90 = 195`. Aplica descuento (`estudiante` y `195 >= 150`): `descuento = 195 * 0.10 = 19.50`. `iva = (195 - 19.50) * 0.16 = 175.50 * 0.16 = 28.08`. `total = 195 - 19.50 + 28.08 = 203.58`. `total_dia = 133.40 + 203.58 = 336.98`.

Verificación aritmética: `2*35 = 70`, `70 + 45 = 115`, `115*0.16 = 18.40`, `115 + 18.40 = 133.40`. `3*35 = 105`, `2*45 = 90`, `105 + 90 = 195`, `195*0.10 = 19.50`, `195 - 19.50 = 175.50`, `175.50*0.16 = 28.08`, `175.50 + 28.08 = 203.58`, `133.40 + 203.58 = 336.98`. Correcto.

---

# 12. ACTIVIDAD DE LA SEMANA Y ENTREGABLES

El detalle completo de la actividad (estructura del entregable, rúbrica y fechas) se encuentra en **`Actividad3_AvanceProyecto.md`**.

| Entregable | Descripción | Formato |
| :--- | :--- | :--- |
| **Avance del Proyecto (Fase I)** | Documento Word con los 8 requerimientos del avance. | `.docx` |
| **Diagrama de flujo** | Imagen del diagrama exportado desde PSeInt (Requerimiento 7). | Imagen (`.png`) |
| **Prototipo de código** | Prototipo ejecutable de Python (Requerimiento 8). | `.py` |
| **Jupyter de práctica semanal** | Práctica de integración en Notebook (ver `Ejercicios_Semana3.md`). | `.ipynb` |
| **Repositorio en GitHub** | Liga pública con la estructura de carpetas semanales. | URL |

**Fecha límite:** Viernes por la noche — **28 de agosto de 2026** (Periodo I) · **30 de octubre de 2026** (Periodo II).

Recuerda: esta semana **NO tiene ejercicios extra evaluables**; los 25 ejercicios complementarios de `Ejercicios_Semana3.md` son para practicar la integración y pueden resolverse en tu Jupyter de práctica semanal.

---

# DESAFÍOS DE INTEGRACIÓN (AUTOEVALUABLES, NO EVALUABLES)

Practica la combinación de los Temas 1 al 8 con los **25 ejercicios** del archivo **`Ejercicios_Semana3.md`**. Resuélvelos en tu Jupyter Notebook de práctica y consérvalos en tu repositorio como evidencia de tu avance.

--- 
