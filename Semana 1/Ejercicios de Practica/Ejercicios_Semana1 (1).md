# 50 EJERCICIOS DE REFUERZO — SEMANA 1

**Curso:** Solución de problemas con programación computacional
**Alcance:** Temas 1 al 4 (Algoritmos y modelo EPS · PSeInt y pseudocódigo · Variables, tipos de datos y operadores · Entradas y salidas simples)

Resuelve los ejercicios conforme avances en los temas. Cada ejercicio incluye el **enunciado**, un **ejemplo de entrada** y la **salida esperada**. Se recomienda resolverlos en un Jupyter Notebook y subirlos a tu repositorio de GitHub.

---

## BLOQUE 1 · TEMA 1: ALGORITMOS Y MODELO ENTRADA-PROCESO-SALIDA

### Ejercicio 1: Algoritmo para preparar café
**Enunciado:** Escribe en lenguaje natural los pasos (algoritmo) para preparar una taza de café instantáneo. Deben ser precisos, definidos y finitos.
**Entrada:** Temperatura del agua, cantidad de café en cucharadas, presencia de azúcar.
**Salida:** Lista ordenada de pasos que termina con la taza de café lista para beber.

---

### Ejercicio 2: Identificar las fases del modelo EPS
**Enunciado:** Para el problema "calcular el Índice de Masa Corporal (IMC) de una persona", identifica qué datos son **Entrada**, qué operaciones son el **Proceso** y qué resultados son la **Salida**.
**Entrada:** `peso = 70`, `altura = 1.75`
**Proceso:** `imc = peso / (altura ** 2)`
**Salida:** `El IMC es: 22.86`

---

### Ejercicio 3: Características de un algoritmo
**Enunciado:** El siguiente algoritmo no es correcto: "Mueve el mouse un poco. Haz clic varias veces hasta que pase algo". Señala cuál(es) de las tres características de un algoritmo (Preciso, Definido, Finito) se viola(n) y escribe una versión mejorada.
**Entrada:** Descripción textual del algoritmo deficiente.
**Salida:** Explicación de la(s) característica(s) violada(s) y versión corregida.

---

### Ejercicio 4: Algoritmo del cajero automático
**Enunciado:** Escribe el algoritmo paso a paso para retirar dinero de un cajero automático (identificación, selección de monto, dispensación y retiro de la tarjeta).
**Entrada:** Usuario con tarjeta y NIP.
**Salida:** Secuencia de pasos que finaliza con el dinero entregado y la tarjeta recuperada.

---

### Ejercicio 5: EPS del área de un círculo
**Enunciado:** Plantea el modelo Entrada-Proceso-Salida para calcular el área de un círculo. Escribe también los pasos en lenguaje natural.
**Entrada:** `radio = 5`
**Proceso:** `area = 3.1416 * radio ** 2`
**Salida:** `El área del círculo es: 78.54`

---

### Ejercicio 6: Algoritmo del sándwich
**Enunciado:** Diseña el algoritmo para preparar un sándwich de jamón y queso. Incluye al menos 6 pasos claros y sin ambigüedad.
**Entrada:** Ingredientes disponibles (pan, jamón, queso).
**Salida:** Pasos ordenados que terminan con el sándwich armado.

---

### Ejercicio 7: Algoritmo para saber si un número es par
**Enunciado:** Escribe los pasos del algoritmo (en lenguaje natural) que reciba un número entero y determine si es par o impar. La paridad se verifica con la operación `numero % 2`.
**Entrada:** `numero = 8`
**Salida:** `8 es un número par`

---

### Ejercicio 8: EPS para convertir kilómetros a millas
**Enunciado:** Identifica Entrada, Proceso y Salida del problema "convertir kilómetros a millas" (1 km = 0.621371 millas).
**Entrada:** `kilometros = 10`
**Proceso:** `millas = kilometros * 0.621371`
**Salida:** `10 km equivalen a 6.21 millas`

---

### Ejercicio 9: EPS del promedio de calificaciones
**Enunciado:** Escribe los pasos del algoritmo para calcular el promedio de 3 calificaciones parciales y el modelo EPS correspondiente.
**Entrada:** `cal1 = 8`, `cal2 = 9`, `cal3 = 10`
**Proceso:** `promedio = (cal1 + cal2 + cal3) / 3`
**Salida:** `El promedio es: 9.0`

---

### Ejercicio 10: Algoritmo para entrada a una película
**Enunciado:** Diseña un algoritmo que reciba la edad de una persona y decida si puede entrar a una película para mayores de 18 años. (Comparación: `edad >= 18`.)
**Entrada:** `edad = 18`
**Salida:** `Puedes entrar a la película`

---

## BLOQUE 2 · TEMA 2: PSEINT Y PSEUDOCÓDIGO

### Ejercicio 11: Suma de dos números en PSeInt
**Enunciado:** Escribe el pseudocódigo en PSeInt (`Algoritmo`, `Escribir`, `Leer`, `<-`, `FinAlgoritmo`) que sume dos números.
**Entrada:** `5`, `7`
**Salida:** `La suma es: 12`

---

### Ejercicio 12: Área de un rectángulo en PSeInt
**Enunciado:** Escribe el pseudocódigo que calcule el área de un rectángulo a partir de su base y su altura.
**Entrada:** `base = 4`, `altura = 6`
**Salida:** `El área del rectángulo es: 24`

---

### Ejercicio 13: Promedio de 3 notas en PSeInt
**Enunciado:** Escribe el pseudocódigo que capture 3 calificaciones y calcule su promedio.
**Entrada:** `7`, `8`, `9`
**Salida:** `El promedio es: 8`

---

### Ejercicio 14: Convertidor de grados en PSeInt
**Enunciado:** Escribe el pseudocódigo que convierta una temperatura en grados Celsius a Fahrenheit (`F = C * 9/5 + 32`).
**Entrada:** `25`
**Salida:** `25 grados Celsius equivalen a 77 grados Fahrenheit`

---

### Ejercicio 15: Descuento en PSeInt
**Enunciado:** Escribe el pseudocódigo que aplique un 10% de descuento a un precio y muestre el precio final.
**Entrada:** `precio = 200`
**Proceso:** `descuento = precio * 0.10`, `final = precio - descuento`
**Salida:** `Precio final con 10% de descuento: 180`

---

### Ejercicio 16: Intercambio de variables en PSeInt
**Enunciado:** Escribe el pseudocódigo que lea dos valores y los intercambie usando una variable temporal.
**Entrada:** `a = 3`, `b = 8`
**Salida:** `a = 8`, `b = 3`

---

### Ejercicio 17: Perímetro de un cuadrado en PSeInt
**Enunciado:** Escribe el pseudocódigo que calcule el perímetro de un cuadrado a partir de su lado.
**Entrada:** `lado = 6`
**Proceso:** `perimetro = lado * 4`
**Salida:** `El perímetro del cuadrado es: 24`

---

### Ejercicio 18: Propina en PSeInt
**Enunciado:** Escribe el pseudocódigo que calcule la propina del 15% de una cuenta de restaurante.
**Entrada:** `cuenta = 300`
**Salida:** `La propina del 15% es: 45`

---

### Ejercicio 19: Velocidad media en PSeInt
**Enunciado:** Escribe el pseudocódigo (versión PSeInt) del ejemplo de la velocidad media: distancia y tiempo como entrada, velocidad como salida.
**Entrada:** `distancia = 150`, `tiempo = 3`
**Salida:** `La velocidad promedio es: 50 km/h`

---

### Ejercicio 20: Descomposición de segundos en PSeInt
**Enunciado:** Escribe el pseudocódigo que convierta una cantidad entera de segundos en horas, minutos y segundos restantes (`//` y `%`).
**Entrada:** `3665`
**Proceso:** `horas = 3665 // 3600`, `minutos = (3665 % 3600) // 60`, `segundos = 3665 % 60`
**Salida:** `3665 segundos = 1 hora(s), 1 minuto(s), 5 segundo(s)`

---

## BLOQUE 3 · TEMA 3: VARIABLES, TIPOS DE DATOS Y OPERADORES

### Ejercicio 21: Identificar tipos de datos
**Enunciado:** Indica el tipo de dato en Python (`int`, `float`, `str` o `bool`) de cada uno de los siguientes valores: `10`, `3.14`, `"Hola"`, `True`.
**Entrada:** Ninguna (ejercicio de análisis).
**Salida:** `10 -> int`, `3.14 -> float`, `"Hola" -> str`, `True -> bool`

---

### Ejercicio 22: Nombres de variables válidos
**Enunciado:** De la siguiente lista, indica cuáles son nombres de variables válidos en Python siguiendo PEP 8 y cuáles no, y por qué: `precio_total`, `2valor`, `_contador`, `nombre-alumno`, `class`.
**Entrada:** Ninguna (ejercicio de análisis).
**Salida:** `precio_total (válido)`, `2valor (inválido, inicia con número)`, `_contador (válido)`, `nombre-alumno (inválido, usa guion medio)`, `class (inválido, palabra reservada)`

---

### Ejercicio 23: Precedencia de operadores
**Enunciado:** Calcula mentalmente y luego verifica en Python el resultado de la expresión `2 + 3 * 4`.
**Entrada:** Ninguna.
**Salida:** `14`

---

### Ejercicio 24: División entera y módulo
**Enunciado:** Calcula el resultado de `10 // 3` y `10 % 3`. Explica qué representa cada operador.
**Entrada:** Ninguna.
**Salida:** `10 // 3 = 3 (cociente entero)`, `10 % 3 = 1 (residuo)`

---

### Ejercicio 25: Potencia
**Enunciado:** Calcula el resultado de la operación `2 ** 5` y explica qué operador se usa.
**Entrada:** Ninguna.
**Salida:** `32`

---

### Ejercicio 26: Operadores relacionales
**Enunciado:** Evalúa las siguientes comparaciones e indica si el resultado es `True` o `False`: `7 > 3`, `7 == 3`, `7 <= 7`.
**Entrada:** Ninguna.
**Salida:** `True`, `False`, `True`

---

### Ejercicio 27: Comparación de cadenas
**Enunciado:** Evalúa la comparación `"ana" < "beto"` y explica por qué el resultado es así (orden alfabético).
**Entrada:** Ninguna.
**Salida:** `True (a está antes que b en el abecedario)`

---

### Ejercicio 28: Precedencia combinada
**Enunciado:** Calcula el resultado de la expresión `(2 + 3) * 4 - 6`.
**Entrada:** Ninguna.
**Salida:** `14`

---

### Ejercicio 29: Rastreo de variables
**Enunciado:** Sigue el rastro de la variable `x` en el siguiente código e indica el valor final:
```python
x = 5
x = x + 3
x = x * 2
```
**Entrada:** Ninguna.
**Salida:** `x = 16`

---

### Ejercicio 30: Intercambio con variable temporal
**Enunciado:** Escribe el código en Python que intercambie los valores de dos variables `a` y `b` usando una variable temporal `temp`.
**Entrada:** `a = 5`, `b = 9`
**Salida:** `Después del intercambio: a = 9, b = 5`

---

### Ejercicio 31: Cálculo del IMC
**Enunciado:** Escribe las instrucciones en Python que calculen el IMC usando la fórmula `peso / (altura ** 2)`.
**Entrada:** `peso = 70`, `altura = 1.75`
**Salida:** `El IMC es: 22.857142857142858`

---

### Ejercicio 32: Área de un círculo con constante
**Enunciado:** Escribe el código que calcule el área de un círculo con `pi = 3.1416` y lo muestre redondeado a 2 decimales.
**Entrada:** `radio = 7`
**Proceso:** `area = 3.1416 * radio ** 2`
**Salida:** `El área del círculo es: 153.94`

---

### Ejercicio 33: IVA
**Enunciado:** Escribe el código que calcule el IVA (16%) de una cantidad y el total con IVA.
**Entrada:** `monto = 500`
**Salida:** `IVA (16%): 80.0` y `Total con IVA: 580.0`

---

### Ejercicio 34: Promedio con decimales
**Enunciado:** Escribe el código que calcule el promedio de `9`, `8.5` y `7.5`, mostrando el resultado con 2 decimales.
**Entrada:** Ninguna (valores fijos en el código).
**Salida:** `El promedio es: 8.33`

---

### Ejercicio 35: Variable booleana
**Enunciado:** Declara una variable `es_mayor` que sea `True` si la edad es mayor o igual a 18 y `False` en caso contrario. Usa el operador relacional adecuado.
**Entrada:** `edad = 20`
**Salida:** `es_mayor = True`

---

## BLOQUE 4 · TEMA 4: ENTRADAS Y SALIDAS SIMPLES (input, print y casting)

### Ejercicio 36: Saludo personalizado
**Enunciado:** Crea un programa que pida el nombre del usuario y lo salude con un mensaje de bienvenida usando `input()` y `print()`.
**Entrada:** `Ana`
**Salida:** `Hola Ana, bienvenido al curso de programación`

---

### Ejercicio 37: Suma de dos enteros
**Enunciado:** Crea un programa que pida dos números enteros y muestre su suma. Recuerda convertir con `int()`.
**Entrada:** `5` y `3`
**Salida:** `La suma de 5 y 3 es: 8`

---

### Ejercicio 38: Suma de dos flotantes
**Enunciado:** Crea un programa que pida dos números con decimales y muestre su suma usando `float()`.
**Entrada:** `2.5` y `1.25`
**Salida:** `La suma es: 3.75`

---

### Ejercicio 39: Promedio formateado con f-string
**Enunciado:** Crea un programa que pida 3 calificaciones y muestre el promedio con dos decimales usando f-strings.
**Entrada:** `8`, `9`, `10`
**Salida:** `Tu promedio es: 9.00`

---

### Ejercicio 40: Convertidor de temperatura (Desafío Extra 1)
**Enunciado:** Crea un programa que pida una temperatura en grados Celsius (`float`) y la convierta a Fahrenheit y Kelvin. Fórmulas: `F = (C * 9/5) + 32` y `K = C + 273.15`.
**Entrada:** `25`
**Salida:** `25 °C = 77.0 °F = 298.15 K`

---

### Ejercicio 41: Calculadora de edad
**Enunciado:** Crea un programa que pida el año de nacimiento del usuario y calcule su edad aproximada (año actual: 2026).
**Entrada:** `2006`
**Salida:** `Tienes aproximadamente 20 años`

---

### Ejercicio 42: Ticket con subtotal, IVA y total
**Enunciado:** Crea un programa que pida el costo de dos productos, calcule el subtotal, el IVA (16%) y el total general, e imprima un ticket formateado con f-strings.
**Entrada:** `50` y `30`
**Salida:**
```
Subtotal: $80.00
IVA (16%): $12.80
Total a pagar: $92.80
```

---

### Ejercicio 43: Precio con descuento
**Enunciado:** Crea un programa que pida un precio y aplique un 10% de descuento, mostrando el precio final con formato de moneda.
**Entrada:** `250`
**Salida:** `Precio final con 10% de descuento: $225.00`

---

### Ejercicio 44: Propina de restaurante
**Enunciado:** Crea un programa que pida el total de la cuenta y calcule una propina del 15%, mostrando ambos montos.
**Entrada:** `200`
**Salida:** `Propina (15%): $30.00` y `Total con propina: $230.00`

---

### Ejercicio 45: Conversión de kilómetros a millas
**Enunciado:** Crea un programa que pida una distancia en kilómetros y la convierta a millas (1 km = 0.621371 millas), redondeada a 2 decimales.
**Entrada:** `5`
**Salida:** `5 km equivalen a 3.11 millas`

---

### Ejercicio 46: Área y perímetro de un rectángulo
**Enunciado:** Crea un programa que pida la base y la altura de un rectángulo y calcule su área y su perímetro.
**Entrada:** `base = 8`, `altura = 5`
**Salida:** `Área: 40` y `Perímetro: 26`

---

### Ejercicio 47: Descomposición de tiempo (Desafío Extra 3)
**Enunciado:** Crea un programa que pida una cantidad entera de segundos y la exprese en horas, minutos y segundos restantes usando `//` y `%`.
**Entrada:** `3665`
**Salida:** `3665 segundos = 1 hora(s), 1 minuto(s), 5 segundo(s)`

---

### Ejercicio 48: Calculadora de tiempo digital (preparación Actividad 1)
**Enunciado:** Crea un programa que pida el tiempo diario (en horas) dedicado a 3 plataformas digitales, calcule el total y el porcentaje del día (24 h) usado en actividades digitales.
**Entrada:** `2`, `1.5`, `1` (total `4.5`)
**Salida:** `Tiempo total en pantalla: 4.5 horas` y `Porcentaje del día: 18.75%`

---

### Ejercicio 49: Conocer el tipo de dato
**Enunciado:** Crea un programa que pida un valor al usuario y muestre con `type()` el tipo de dato con el que se recibe, y luego el tipo tras convertirlo a `int`.
**Entrada:** `42`
**Salida:** `Recibido como: <class 'str'>` y `Convertido a: <class 'int'>`

---

### Ejercicio 50: Minicalculadora de 4 operaciones
**Enunciado:** Crea un programa que pida dos números y muestre el resultado de sumarlos, restarlos, multiplicarlos y dividirlos (con `float()`).
**Entrada:** `10` y `4`
**Salida:**
```
Suma: 14.0
Resta: 6.0
Multiplicación: 40.0
División: 2.5
```
