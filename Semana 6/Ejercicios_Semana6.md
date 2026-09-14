# 25 EJERCICIOS DE REPASO INTEGRAL — SEMANA 6

**Curso:** Solución de problemas con programación computacional
**Alcance:** Temas 1 al 16 (Repaso integral: Algoritmos y modelo EPS · PSeInt · Variables, tipos y operadores · Entrada/salida · Decisiones · Ciclos · Debugging · Listas · Matrices · Funciones · Tuplas · Diccionarios · Excepciones · Strings)

Estos ejercicios **no son evaluables**; son de repaso y consolidación previos a la **ACTIVIDAD 5 (Certificación de Cisco Networking Academy)**. Cada ejercicio combina varios temas del curso e incluye el **enunciado**, la **entrada** y la **salida esperada**. Resuélvelos en un Jupyter Notebook y súbelos a tu repositorio.

---

## BLOQUE 1 · TEMAS 1 Y 2: ALGORITMOS, MODELO EPS Y PSEINT

### Ejercicio 1: Modelo EPS del área de un triángulo
**Enunciado:** Identifica las fases del modelo Entrada-Proceso-Salida para calcular el área de un triángulo (`area = (base * altura) / 2`) y escribe el código Python equivalente con `input()`, `float()` y `print()`.
**Entrada:** `base = 8`, `altura = 5`
**Salida:** `El área del triángulo es: 20.0`

---

### Ejercicio 2: EPS para convertir Celsius a Fahrenheit
**Enunciado:** Plantea el modelo Entrada-Proceso-Salida para convertir grados Celsius a Fahrenheit (`F = C * 9/5 + 32`), indicando qué datos son entrada, qué operaciones son el proceso y qué resultado es la salida.
**Entrada:** `celsius = 30`
**Proceso:** `fahrenheit = celsius * 9/5 + 32`
**Salida:** `30 grados Celsius equivalen a 86.0 grados Fahrenheit`

---

### Ejercicio 3: Interés simple en PSeInt
**Enunciado:** Escribe el pseudocódigo en PSeInt (`Algoritmo`, `Escribir`, `Leer`, `<-`, `FinAlgoritmo`) que calcule el interés simple con la fórmula `interes = capital * (tasa / 100) * tiempo`.
**Entrada:** `capital = 2000`, `tasa = 6`, `tiempo = 2`
**Proceso:** `interes = 2000 * (6 / 100) * 2`
**Salida:** `El interés simple es: 240`

---

## BLOQUE 2 · TEMAS 3 Y 4: VARIABLES, OPERADORES Y ENTRADA/SALIDA

### Ejercicio 4: Precedencia combinada de operadores
**Enunciado:** Calcula el resultado de la expresión `4 * 3 + 10 // 3 - 8 % 5` e indica el orden de evaluación aplicado.
**Entrada:** Ninguna (ejercicio de análisis).
**Salida:** `4 * 3 + 10 // 3 - 8 % 5 = 12 + 3 - 3 = 12`

---

### Ejercicio 5: Tipo de dato tras `input()` y casting
**Enunciado:** Dado el código `x = input("Número: ")` con la entrada `"25"`, indica el tipo de dato de `x`, qué ocurre al ejecutar `x + 1` y cómo corregirlo para obtener `26`.
**Entrada:** `"25"`
**Salida:** `type(x) es <class 'str'>`, `x + 1` genera `TypeError`, corregido con `int(x)` se obtiene `26`

---

### Ejercicio 6: Conversión de horas a segundos
**Enunciado:** Crea un programa que pida una cantidad de horas (`float`) y la convierta a segundos (1 hora = 3600 segundos), mostrando el resultado formateado.
**Entrada:** `3`
**Proceso:** `segundos = 3 * 3600`
**Salida:** `3 horas equivalen a 10800 segundos`

---

### Ejercicio 7: Descuento del 15% con f-strings
**Enunciado:** Crea un programa que pida el precio de un artículo y aplique un 15% de descuento, mostrando el monto del descuento y el precio final con dos decimales usando f-strings.
**Entrada:** `460`
**Proceso:** `descuento = 460 * 0.15`, `final = 460 - 69`
**Salida:**
```
Descuento (15%): $69.00
Precio final: $391.00
```

---

## BLOQUE 3 · TEMAS 5, 6, 7 Y 8: DECISIONES, CICLOS Y DEBUGGING

### Ejercicio 8: Número par o impar
**Enunciado:** Crea un programa que pida un número entero y determine con `if-else` y el operador `%` si es par o impar.
**Entrada:** `17`
**Proceso:** `17 % 2 = 1`
**Salida:** `17 es un número impar`

---

### Ejercicio 9: Mayor de tres números
**Enunciado:** Crea un programa que pida tres números y determine cuál es el mayor usando `if-elif-else`.
**Entrada:** `12`, `45`, `23`
**Salida:** `El mayor de los tres números es: 45`

---

### Ejercicio 10: Suma acumulada con `while`
**Enunciado:** Crea un programa que sume números ingresados por el usuario mientras el número sea distinto de `0` (el `0` no se suma y termina el ciclo).
**Entrada:** `5`, `8`, `2`, `0`
**Proceso:** `5 + 8 + 2 = 15`
**Salida:** `La suma de los números es: 15`

---

### Ejercicio 11: Tabla de multiplicar con `for`
**Enunciado:** Crea un programa que pida un número entero y muestre su tabla de multiplicar del 1 al 10 usando un ciclo `for` y `range()`.
**Entrada:** `6`
**Salida:**
```
6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 30
6 x 6 = 36
6 x 7 = 42
6 x 8 = 48
6 x 9 = 54
6 x 10 = 60
```

---

### Ejercicio 12: Suma de pares del 1 al 20 con `for` y `continue`
**Enunciado:** Crea un programa que sume los números pares del 1 al 20 usando un ciclo `for`, la instrucción `continue` (para saltar impares) y el operador `%`.
**Entrada:** Ninguna (valores fijos).
**Proceso:** `2 + 4 + 6 + 8 + 10 + 12 + 14 + 16 + 18 + 20`
**Salida:** `La suma de los números pares del 1 al 20 es: 110`

---

## BLOQUE 4 · TEMAS 9, 10, 11 Y 12: LISTAS, MATRICES Y FUNCIONES

### Ejercicio 13: Suma de una lista con función que regresa valor
**Enunciado:** Escribe una función que reciba una lista de números y **regrese** la suma de sus elementos (sin usar la función integrada `sum()`). Muestra el resultado.
**Entrada:** `lista = [10, 20, 30, 40]`
**Proceso:** `10 + 20 + 30 + 40 = 100`
**Salida:** `La suma de los elementos es: 100`

---

### Ejercicio 14: Máximo de una lista con función que regresa valor
**Enunciado:** Escribe una función que reciba una lista de números y **regrese** el valor máximo recorriéndola con un ciclo (sin usar `max()`).
**Entrada:** `lista = [7, 3, 9, 2]`
**Salida:** `El elemento máximo es: 9`

---

### Ejercicio 15: Matriz y suma de la diagonal principal
**Enunciado:** Dada la matriz `[[1,2,3],[4,5,6],[7,8,9]]`, escribe un programa que la recorra con ciclos anidados y calcule la suma de la diagonal principal (posiciones donde el renglón es igual a la columna).
**Entrada:** `matriz = [[1,2,3],[4,5,6],[7,8,9]]`
**Proceso:** `1 + 5 + 9 = 15`
**Salida:** `La suma de la diagonal principal es: 15`

---

### Ejercicio 16: Promedio con función que no regresa valor
**Enunciado:** Escribe una función que reciba una lista de calificaciones y **no regrese valor**, sino que imprima directamente el promedio con dos decimales.
**Entrada:** `calificaciones = [8, 9, 10, 7]`
**Proceso:** `(8 + 9 + 10 + 7) / 4 = 34 / 4 = 8.5`
**Salida:** `El promedio es: 8.50`

---

### Ejercicio 17: Invertir una lista con slicing
**Enunciado:** Crea un programa que invierta una lista de números usando *slicing* (`lista[::-1]`) y muestre el resultado.
**Entrada:** `lista = [1, 2, 3, 4, 5]`
**Salida:** `Lista invertida: [5, 4, 3, 2, 1]`

---

### Ejercicio 18: Factorial con función recursiva
**Enunciado:** Escribe una función recursiva que calcule el factorial de un número (`n! = n * (n-1) * ... * 1`) y regrese el resultado. Considera que `0! = 1`.
**Entrada:** `5`
**Proceso:** `5 * 4 * 3 * 2 * 1 = 120`
**Salida:** `El factorial de 5 es: 120`

---

## BLOQUE 5 · TEMAS 13, 14, 15 Y 16: TUPLAS, DICCIONARIOS, EXCEPCIONES Y STRINGS

### Ejercicio 19: Tupla: acceso y suma con función
**Enunciado:** Dada la tupla `numeros = (4, 8, 15, 16, 23, 42)`, imprime el tercer elemento y escribe una función que reciba la tupla y regrese la suma de todos sus elementos.
**Entrada:** `numeros = (4, 8, 15, 16, 23, 42)`
**Proceso:** `4 + 8 + 15 + 16 + 23 + 42 = 108`
**Salida:**
```
El tercer elemento es: 15
La suma de la tupla es: 108
```

---

### Ejercicio 20: Diccionario: buscar teléfono de un contacto
**Enunciado:** Dado el diccionario `contactos = {"Ana": 5551234, "Beto": 5555678, "Carla": 5559012}`, pide un nombre al usuario y muestra su teléfono consultando la clave del diccionario.
**Entrada:** `Beto`
**Salida:** `El teléfono de Beto es: 5555678`

---

### Ejercicio 21: Diccionario de calificaciones y promedios
**Enunciado:** Dado el diccionario `calif = {"Ana": [8, 9, 10], "Beto": [7, 7, 8]}`, recorre sus claves y calcula el promedio de cada estudiante, mostrándolo con dos decimales.
**Entrada:** `calif = {"Ana": [8, 9, 10], "Beto": [7, 7, 8]}`
**Proceso:** `Ana: 27 / 3 = 9.00`, `Beto: 22 / 3 = 7.33`
**Salida:**
```
Ana: 9.00
Beto: 7.33
```

---

### Ejercicio 22: Excepción de división entre cero
**Enunciado:** Crea un programa que pida dos números enteros y los divida dentro de un bloque `try-except`, capturando `ZeroDivisionError` para mostrar un mensaje amigable si el divisor es cero.
**Entrada:** `10`, `0`
**Salida:** `Error: No se puede dividir entre cero.`

---

### Ejercicio 23: Excepción de valor no numérico
**Enunciado:** Crea un programa que pida un número entero y lo convierta con `int()` dentro de un bloque `try-except`, capturando `ValueError` para mostrar un mensaje amigable si el usuario escribe algo que no es un número.
**Entrada:** `"abc"`
**Salida:** `Error: Debes ingresar un número entero.`

---

### Ejercicio 24: Contar palabras de un string
**Enunciado:** Escribe un programa que cuente cuántas palabras tiene un mensaje usando el método `.split()` y la función `len()`.
**Entrada:** `"Python es un lenguaje de programacion"`
**Proceso:** `len("Python es un lenguaje de programacion".split()) = 6`
**Salida:** `El mensaje tiene 6 palabras.`

---

### Ejercicio 25: Longitud, mayúsculas y reemplazo de un string
**Enunciado:** Dado el mensaje `"aprende python"`, muestra su longitud con `len()`, su versión en mayúsculas con `.upper()` y el resultado de reemplazar `"python"` por `"programacion"` con `.replace()`.
**Entrada:** `"aprende python"`
**Proceso:** `len("aprende python") = 14`, `.upper()` = `"APRENDE PYTHON"`, `.replace("python", "programacion")` = `"aprende programacion"`
**Salida:**
```
Longitud: 14
En mayúsculas: APRENDE PYTHON
Reemplazo: aprende programacion
```
