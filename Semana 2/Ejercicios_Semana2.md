# 35 EJERCICIOS DE REFUERZO — SEMANA 2

**Curso:** Solución de problemas con programación computacional
**Alcance:** Temas 5 al 8 (Estructuras de decisión · Estructura de repetición `while` · Debugging con PDB · Estructura de repetición `for`)

Resuelve los ejercicios conforme avances en los temas. Cada ejercicio incluye el **enunciado**, un **ejemplo de entrada** y la **salida esperada**. Se recomienda resolverlos en un Jupyter Notebook y subirlos a tu repositorio de GitHub.

---

## BLOQUE 1 · TEMA 5: ESTRUCTURAS DE DECISIÓN (if, else, elif y operadores lógicos)

### Ejercicio 1: Mayor de edad
**Enunciado:** Crea un programa que pida la edad de una persona y muestre si es mayor de edad (18 años o más) o menor de edad.
**Entrada:** `17`
**Salida:** `Eres menor de edad`

---

### Ejercicio 2: Número par o impar
**Enunciado:** Crea un programa que pida un número entero y determine si es par o impar usando el operador módulo `%`.
**Entrada:** `7`
**Salida:** `7 es un número impar`

---

### Ejercicio 3: Calificación aprobatoria
**Enunciado:** Crea un programa que pida una calificación de 0 a 10 y muestre si la materia está aprobada (mayor o igual a 6) o reprobada.
**Entrada:** `7`
**Salida:** `Aprobado`

---

### Ejercicio 4: Clasificación por rango de edad con elif
**Enunciado:** Crea un programa que clasifique a una persona según su edad: menor de 3 años "Bebé", de 3 a 12 "Niño", de 13 a 17 "Adolescente" y de 18 en adelante "Adulto". Usa `elif`.
**Entrada:** `15`
**Salida:** `Adolescente`

---

### Ejercicio 5: Descuento por tipo de visitante
**Enunciado:** Crea un programa que pida el tipo de visitante (`adulto_mayor`, `profesor`, `estudiante` u `otro`) y calcule el precio de un boleto base de $45 aplicando solo un descuento: adulto mayor 12%, profesor 10%, estudiante 10%, otro 0%.
**Entrada:** `estudiante`
**Salida:** `Precio final: $40.50`

---

### Ejercicio 6: Acceso con operador and
**Enunciado:** Crea un programa que pida la edad y si la persona tiene credencial vigente (`si`/`no`). Solo se permite el acceso si la edad es mayor o igual a 18 y la credencial es `si`.
**Entrada:** `20` y `si`
**Salida:** `Acceso permitido`

---

### Ejercicio 7: Detección de número negativo con or
**Enunciado:** Crea un programa que pida dos números y muestre una alerta si alguno de ellos es negativo, usando el operador `or`.
**Entrada:** `5` y `-3`
**Salida:** `Hay un número negativo`

---

### Ejercicio 8: Positivo y par con anidamiento
**Enunciado:** Crea un programa que pida un número entero y, si es positivo, verifique además si es par usando un `if` anidado.
**Entrada:** `8`
**Salida:** `El número es positivo y par`

---

### Ejercicio 9: Salir del proceso con not
**Enunciado:** Crea un programa que pregunte si desea continuar. Si la respuesta NO es `si` (usa el operador `not`), el proceso finaliza.
**Entrada:** `no`
**Salida:** `Proceso finalizado`

---

## BLOQUE 2 · TEMA 6: ESTRUCTURA DE REPETICIÓN - WHILE (contadores, acumuladores, break y continue)

### Ejercicio 10: Contador del 1 al 5
**Enunciado:** Escribe un programa que imprima los números del 1 al 5 usando un ciclo `while` y una variable contador.
**Entrada:** Ninguna.
**Salida:**
```
1
2
3
4
5
```

---

### Ejercicio 11: Suma de los primeros N números
**Enunciado:** Crea un programa que pida un número entero positivo N y calcule con `while` la suma de los números del 1 al N.
**Entrada:** `5`
**Salida:** `La suma del 1 al 5 es: 15`

---

### Ejercicio 12: Tabla de multiplicar con while
**Enunciado:** Crea un programa que pida un número y muestre su tabla de multiplicar del 1 al 10 usando `while`.
**Entrada:** `3`
**Salida:**
```
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
```

---

### Ejercicio 13: Cuenta regresiva
**Enunciado:** Crea un programa que imprima los números del 5 al 1 con `while` y después el mensaje "Despegue".
**Entrada:** Ninguna.
**Salida:**
```
5
4
3
2
1
Despegue
```

---

### Ejercicio 14: Salir del ciclo con break
**Enunciado:** Crea un programa que capture textos con `input()` dentro de un `while True`. Si el usuario escribe `salir`, el ciclo se interrumpe con `break`.
**Entrada:** `hola`, `mundo`, `salir`
**Salida:**
```
hola
mundo
Fin del ciclo
```

---

### Ejercicio 15: Promedio con acumulador
**Enunciado:** Crea un programa que capture calificaciones hasta que el usuario escriba `fin` y calcule el promedio con un acumulador y un contador.
**Entrada:** `8`, `9`, `10`, `fin`
**Salida:** `El promedio es: 9.0`

---

### Ejercicio 16: Validación de contraseña
**Enunciado:** Crea un programa que pida una contraseña repetidamente hasta que el usuario escriba la contraseña correcta `secreto`, momento en el que se muestra "Acceso concedido".
**Entrada:** `1234`, `abcd`, `secreto`
**Salida:** `Acceso concedido`

---

### Ejercicio 17: Suma de pares con continue
**Enunciado:** Crea un programa que capture 5 números y sume únicamente los pares, ignorando los impares con `continue`.
**Entrada:** `1`, `2`, `3`, `4`, `5`
**Salida:** `La suma de los pares es: 6`

---

### Ejercicio 18: Detener la suma con break
**Enunciado:** Crea un programa que sume números capturados con `input()`; si el acumulado alcanza o supera 100, el ciclo se detiene con `break` y se muestra el total.
**Entrada:** `50`, `30`, `25`
**Salida:** `Total: 105`

---

## BLOQUE 3 · TEMA 7: DEBUGGING CON PDB (errores de sintaxis, lógica y ejecución)

### Ejercicio 19: Identificar un error de sintaxis
**Enunciado:** El código `print("Hola` presenta un error. Indica qué tipo de error es y cuál es la corrección.
**Entrada:** Ninguna (ejercicio de análisis).
**Salida:** `Error de sintaxis: falta la comilla de cierre en la cadena; corregir a print("Hola")`

---

### Ejercicio 20: Error de lógica en un promedio
**Enunciado:** El código `promedio = a + b + c / 3` con `a = 8`, `b = 9`, `c = 10` produce un resultado incorrecto. Identifica el error y calcula el promedio correcto.
**Entrada:** `a = 8`, `b = 9`, `c = 10`
**Salida:** `Error de lógica: falta agrupar la suma con paréntesis; promedio correcto = 9.0`

---

### Ejercicio 21: Insertar un punto de interrupción
**Enunciado:** Indica qué línea debes agregar y en qué lugar del código `x = 5` / `x = x + 3` para inspeccionar el valor de `x` con `pdb`.
**Entrada:** Ninguna (ejercicio de análisis).
**Salida:** `Agregar "import pdb" al inicio y "pdb.set_trace()" entre ambas líneas`

---

### Ejercicio 22: Comandos del depurador PDB
**Enunciado:** Explica brevemente qué hace cada comando de PDB: `n`, `c`, `p`, `l`, `q`.
**Entrada:** Ninguna (ejercicio de análisis).
**Salida:** `n: ejecuta la siguiente línea; c: continúa hasta el final; p: imprime el valor de una expresión; l: lista el código actual; q: sale del depurador`

---

### Ejercicio 23: Error de ejecución al convertir
**Enunciado:** El código `edad = int(input("Edad: "))` falla cuando el usuario escribe un texto. Indica el tipo de error que se genera.
**Entrada:** `veinte`
**Salida:** `ValueError: invalid literal for int() (error de ejecución)`

---

### Ejercicio 24: Corregir un ciclo infinito
**Enunciado:** El siguiente código genera un ciclo infinito. Depúralo y corrígelo para que imprima los números del 1 al 5:
```python
i = 1
while i <= 5:
    print(i)
```
**Entrada:** Ninguna.
**Salida:** `Corrección: agregar "i = i + 1" dentro del ciclo para que imprima 1 2 3 4 5`

---

### Ejercicio 25: División entre cero
**Enunciado:** El código `division = a / b` con `b = 0` produce un error de ejecución. Indica el nombre del error.
**Entrada:** `a = 10`, `b = 0`
**Salida:** `ZeroDivisionError: division by zero`

---

### Ejercicio 26: Rastreo de variables con while
**Enunciado:** Sigue el rastro de las variables en el siguiente código e indica los valores finales de `total` e `i`:
```python
total = 0
i = 1
while i <= 4:
    total = total + i
    i = i + 1
```
**Entrada:** Ninguna.
**Salida:** `Al terminar el ciclo: total = 10, i = 5`

---

## BLOQUE 4 · TEMA 8: ESTRUCTURA DE REPETICIÓN - FOR (range, sumas, acumuladores y patrones)

### Ejercicio 27: range() básico
**Enunciado:** Escribe un programa que imprima los números del 1 al 5 usando `for` y `range(1, 6)`.
**Entrada:** Ninguna.
**Salida:**
```
1
2
3
4
5
```

---

### Ejercicio 28: Suma con for
**Enunciado:** Crea un programa que sume los números del 1 al 10 con un acumulador dentro de un `for`.
**Entrada:** Ninguna.
**Salida:** `La suma del 1 al 10 es: 55`

---

### Ejercicio 29: Tabla de multiplicar con for
**Enunciado:** Crea un programa que pida un número y muestre su tabla de multiplicar del 1 al 10 usando `for`.
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

### Ejercicio 30: Acumulador de pares con for
**Enunciado:** Crea un programa que sume los números pares del 1 al 10 usando un `for` y una condición `i % 2 == 0`.
**Entrada:** Ninguna.
**Salida:** `La suma de los pares del 1 al 10 es: 30`

---

### Ejercicio 31: Triángulo numérico
**Enunciado:** Crea un programa que pida un número de filas y dibuje un triángulo con los números 1, 12, 123... usando `for` anidados.
**Entrada:** `4`
**Salida:**
```
1
12
123
1234
```

---

### Ejercicio 32: Cuenta regresiva con range
**Enunciado:** Escribe un programa que imprima los números del 5 al 1 usando `for` con `range(5, 0, -1)`.
**Entrada:** Ninguna.
**Salida:**
```
5
4
3
2
1
```

---

### Ejercicio 33: Factorial con for
**Enunciado:** Crea un programa que pida un número entero positivo y calcule su factorial (producto de los números del 1 al N) con un acumulador.
**Entrada:** `5`
**Salida:** `El factorial de 5 es: 120`

---

### Ejercicio 34: Promedio de N calificaciones
**Enunciado:** Crea un programa que pida cuántas calificaciones se capturarán y, con un `for`, pida cada una para calcular y mostrar el promedio.
**Entrada:** `3` y `8`, `9`, `10`
**Salida:** `El promedio es: 9.0`

---

### Ejercicio 35: Cuadrados del 1 al N
**Enunciado:** Crea un programa que pida un número N y muestre el cuadrado de cada entero del 1 al N con un `for`.
**Entrada:** `4`
**Salida:**
```
1
4
9
16
```
