# 25 EJERCICIOS DE INTEGRACIÓN — SEMANA 3

**Curso:** Solución de problemas con programación computacional
**Alcance:** Temas 1 al 8 (Algoritmos y modelo EPS · PSeInt · Variables, tipos y operadores · Entradas y salidas simples · Estructuras de decisión · Ciclo `while` · *Debugging* con PDB · Ciclo `for`)

**IMPORTANTE:** Estos **25 ejercicios NO son evaluables**. Son ejercicios complementarios de integración para preparar el **Avance del Reto/Proyecto (Fase I)**. Resuélvelos en tu Jupyter Notebook de práctica semanal (`practica_semana3.ipynb`) documentando cada solución con celdas Markdown, y súbelos a tu repositorio de GitHub.

Cada ejercicio combina varios temas (decisiones, ciclos, acumuladores, validaciones, etc.). Incluye el **enunciado**, un **ejemplo de entrada** y la **salida esperada**.

---

## BLOQUE 1 · DISEÑO ALGORÍTMICO, EPS Y PSEINT (TEMAS 1 Y 2)

### Ejercicio 1: Algoritmo con decisión para descuento por monto
**Enunciado:** Escribe en lenguaje natural los pasos del algoritmo (modelo Entrada-Proceso-Salida) para que una tienda aplique un 10% de descuento cuando la compra sea de $300 o más, y muestre el monto del descuento y el total a pagar.
**Entrada:** `monto = 500`
**Proceso:** `descuento = 500 * 0.10`, `total = 500 - 50`
**Salida:** `Monto: 500. Descuento: 50.0. Total a pagar: 450.0`

---

### Ejercicio 2: Pseudocódigo en PSeInt que clasifica un número
**Enunciado:** Escribe el pseudocódigo en PSeInt que lea un número entero y determine si es positivo, negativo o cero, usando una estructura `Si-Entonces-Sino`.
**Entrada:** `-5`
**Salida:** `El número -5 es negativo`

---

### Ejercicio 3: Pseudocódigo en PSeInt con ciclo Mientras y acumulador
**Enunciado:** Escribe el pseudocódigo en PSeInt que sume números enteros hasta que el usuario ingrese `0`, y muestre la suma acumulada.
**Entrada:** `5`, `8`, `3`, `0`
**Proceso:** `suma = 5 + 8 + 3`
**Salida:** `La suma es: 16`

---

### Ejercicio 4: Pseudocódigo en PSeInt con ciclo Para (tabla de multiplicar)
**Enunciado:** Escribe el pseudocódigo en PSeInt que genere la tabla de multiplicar del 7 desde `7 x 1` hasta `7 x 10`.
**Entrada:** `7`
**Salida:** `7 x 1 = 7`, `7 x 2 = 14`, `...`, `7 x 10 = 70`

---

### Ejercicio 5: Algoritmo natural del registro de ventas del día
**Enunciado:** Diseña el algoritmo paso a paso (en lenguaje natural) para registrar ventas del día con un acumulador que se detiene cuando se ingresa `0`, y muestra el total. Identifica las fases Entrada, Proceso y Salida.
**Entrada:** `120`, `80`, `200`, `0`
**Proceso:** `total = 120 + 80 + 200`
**Salida:** `Total de ventas del día: 400`

---

## BLOQUE 2 · DECISIONES, ENTRADAS Y SALIDAS (TEMAS 3, 4 Y 5)

### Ejercicio 6: Calificación con escala de letras
**Enunciado:** Crea un programa que pida una calificación numérica (0 a 10) y la convierta a letra: `A` si es `>= 9`, `B` si es `>= 8`, `C` si es `>= 7`, `D` si es `>= 6`, `F` en otro caso.
**Entrada:** `9`
**Salida:** `Tu calificación es: A`

---

### Ejercicio 7: Número par o impar
**Enunciado:** Crea un programa que pida un número entero y muestre si es par o impar usando el operador módulo `%`.
**Entrada:** `14`
**Proceso:** `14 % 2 = 0`
**Salida:** `14 es un número par`

---

### Ejercicio 8: El mayor de tres números
**Enunciado:** Crea un programa que pida tres números y determine cuál es el mayor, usando decisiones anidadas o comparaciones con `and`.
**Entrada:** `12`, `7`, `9`
**Salida:** `El mayor es: 12`

---

### Ejercicio 9: Descuento escalonado
**Enunciado:** Crea un programa que aplique un descuento según el monto de compra: sin descuento si es menor a $100, 10% si es de $100 a $499, y 20% si es de $500 o más. Muestra el precio final con dos decimales.
**Entrada:** `800`
**Proceso:** `descuento = 800 * 0.20`, `final = 800 - 160`
**Salida:** `Precio final con descuento: $640.00`

---

### Ejercicio 10: Tipo de triángulo por sus lados
**Enunciado:** Crea un programa que pida tres lados y determine si el triángulo es equilátero (tres lados iguales), isósceles (dos iguales) o escaleno (todos distintos).
**Entrada:** `5`, `5`, `5`
**Salida:** `El triángulo es equilátero`

---

## BLOQUE 3 · CICLO `while`, CENTINELAS Y ACUMULADORES (TEMA 6)

### Ejercicio 11: Suma con centinela 0
**Enunciado:** Crea un programa que sume números positivos ingresados por el usuario y se detenga cuando ingrese `0`, mostrando la suma total.
**Entrada:** `4`, `6`, `10`, `0`
**Proceso:** `suma = 4 + 6 + 10`
**Salida:** `La suma es: 20`

---

### Ejercicio 12: Contar números pares
**Enunciado:** Crea un programa que cuente cuántos números pares se ingresan, y se detenga cuando el usuario ingrese un número negativo.
**Entrada:** `2`, `5`, `8`, `10`, `-1`
**Proceso:** pares detectados: `2`, `8`, `10`
**Salida:** `Cantidad de números pares: 3`

---

### Ejercicio 13: Promedio con centinela -1
**Enunciado:** Crea un programa que capture calificaciones y calcule su promedio; se detiene cuando el usuario ingresa `-1`.
**Entrada:** `8`, `9`, `7`, `-1`
**Proceso:** `promedio = (8 + 9 + 7) / 3`
**Salida:** `El promedio es: 8.0`

---

### Ejercicio 14: Menú simple con ciclo while
**Enunciado:** Crea un programa con un menú de opciones: `1` sumar, `2` restar, `3` salir. Para las opciones 1 y 2 pide dos números y muestra el resultado; repite hasta elegir salir.
**Entrada:** opción `1`, números `5` y `3`, luego opción `3`
**Salida:** `Resultado: 8` y `Fin del programa`

---

### Ejercicio 15: Tabla de multiplicar con while
**Enunciado:** Crea un programa que pida un número y muestre su tabla de multiplicar del 1 al 10 usando un ciclo `while`.
**Entrada:** `6`
**Salida:** `6 x 1 = 6`, `6 x 2 = 12`, `...`, `6 x 10 = 60`

---

## BLOQUE 4 · CICLO `for` Y ACUMULADORES (TEMA 8)

### Ejercicio 16: Suma de los primeros N números
**Enunciado:** Crea un programa que pida un entero positivo `n` y calcule la suma de los números del 1 al `n` con un ciclo `for`.
**Entrada:** `5`
**Proceso:** `1 + 2 + 3 + 4 + 5`
**Salida:** `La suma de los primeros 5 números es: 15`

---

### Ejercicio 17: Factorial con for
**Enunciado:** Crea un programa que pida un entero positivo y calcule su factorial (producto de 1 hasta N) usando un ciclo `for`.
**Entrada:** `5`
**Proceso:** `1 * 2 * 3 * 4 * 5`
**Salida:** `El factorial de 5 es: 120`

---

### Ejercicio 18: Números pares del 1 al N
**Enunciado:** Crea un programa que pida un entero `n` e imprima en una sola línea los números pares del 1 al `n`.
**Entrada:** `10`
**Proceso:** pares en `{1,...,10}`: `2, 4, 6, 8, 10`
**Salida:** `2, 4, 6, 8, 10`

---

### Ejercicio 19: Promedio de N calificaciones con for
**Enunciado:** Crea un programa que primero pida cuántas calificaciones se van a capturar y luego las capture con un ciclo `for`, calculando el promedio con dos decimales.
**Entrada:** `3`, calificaciones `7`, `8`, `9`
**Proceso:** `promedio = 24 / 3`
**Salida:** `El promedio es: 8.0`

---

### Ejercicio 20: Cuenta regresiva con for
**Enunciado:** Crea un programa que pida un entero positivo y realice una cuenta regresiva desde ese número hasta `1`, imprimiendo los valores en una línea y el mensaje de despegue al final.
**Entrada:** `5`
**Salida:** `5, 4, 3, 2, 1, ¡Despegue!`

---

## BLOQUE 5 · INTEGRACIÓN AVANZADA: DECISIÓN + CICLOS + VALIDACIÓN + PDB (TEMAS 5 A 8)

### Ejercicio 21: Validación de rango y tabla con for
**Enunciado:** Crea un programa que pida un número entre 1 y 10; si está fuera de rango, muestra un error y vuelve a pedirlo con `while`. Cuando sea válido, imprime su tabla de multiplicar del 1 al 10 con `for`.
**Entrada:** `0` (inválido), luego `5`
**Salida:**
```
Error: número fuera de rango (1-10)
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

---

### Ejercicio 22: Conteo de positivos, negativos y ceros
**Enunciado:** Crea un programa que pida cuántos valores se van a capturar y luego los capture con `for`, contando cuántos son positivos, cuántos negativos y cuántos ceros.
**Entrada:** `5`, valores `3`, `-1`, `0`, `7`, `-2`
**Proceso:** positivos `{3, 7}`, negativos `{-1, -2}`, ceros `{0}`
**Salida:** `Positivos: 2, Negativos: 2, Ceros: 1`

---

### Ejercicio 23: Promedio con validación de rango
**Enunciado:** Crea un programa que capture calificaciones hasta ingresar `-1`. Si una calificación está fuera del rango 0 a 10, muestra un error y no la considera. Al final muestra el promedio de las válidas.
**Entrada:** `8`, `12` (inválida), `9`, `-1`
**Proceso:** válidas `{8, 9}`, `promedio = 17 / 2`
**Salida:**
```
Error: calificación fuera de rango (0-10)
El promedio es: 8.5
```

---

### Ejercicio 24: Minicalculadora con menú y ciclo while
**Enunciado:** Crea un programa con un menú: `1` suma, `2` resta, `3` multiplicación, `4` salir. Para cada operación pide dos números y muestra el resultado; repite hasta elegir salir.
**Entrada:** opción `1` con `10` y `5`, luego opción `3` con `4` y `2`, luego opción `4`
**Proceso:** `10 + 5 = 15`, `4 * 2 = 8`
**Salida:**
```
Suma: 15.0
Multiplicación: 8.0
Fin del programa
```

---

### Ejercicio 25: Depuración de promedio con PDB
**Enunciado:** El siguiente código tiene un error lógico: divide el promedio entre un valor incorrecto. Usa `breakpoint()` y los comandos de PDB (`n`, `p`, `c`) para localizar el error y corregirlo.
```python
suma = 0
contador = 0
for i in range(3):
    cal = float(input("Calificación: "))
    suma = suma + cal
    contador = contador + 1
promedio = suma / 4   # BUG: el divisor debe ser contador
print("El promedio es:", promedio)
```
**Entrada:** `8`, `9`, `10`
**Proceso:** `suma = 27`, `contador = 3`, divisor correcto `3`, `promedio = 27 / 3`
**Salida:** `Con PDB detectaste que el divisor debe ser contador. Promedio corregido: 9.0`

---

## SOLUCIONES RÁPIDAS (VERIFICACIÓN ARITMÉTICA)

| Ejercicio | Verificación |
| :---: | :--- |
| 1 | `500 * 0.10 = 50`, `500 - 50 = 450` |
| 2 | `-5 < 0`, por lo tanto es negativo |
| 3 | `5 + 8 + 3 = 16` |
| 4 | `7 x 10 = 70` (última línea de la tabla) |
| 5 | `120 + 80 + 200 = 400` |
| 6 | `9 >= 9` corresponde a `A` |
| 7 | `14 % 2 = 0`, es par |
| 8 | `12 > 7` y `12 > 9`, el mayor es `12` |
| 9 | `800 * 0.20 = 160`, `800 - 160 = 640` |
| 10 | Tres lados iguales `(5, 5, 5)` → equilátero |
| 11 | `4 + 6 + 10 = 20` |
| 12 | Pares: `2`, `8`, `10` → total `3` |
| 13 | `(8 + 9 + 7) / 3 = 24 / 3 = 8.0` |
| 14 | `5 + 3 = 8` |
| 15 | `6 x 10 = 60` (última línea de la tabla) |
| 16 | `1 + 2 + 3 + 4 + 5 = 15` |
| 17 | `1 * 2 * 3 * 4 * 5 = 120` |
| 18 | Pares de 1 a 10: `2, 4, 6, 8, 10` |
| 19 | `(7 + 8 + 9) / 3 = 24 / 3 = 8.0` |
| 20 | Secuencia `5, 4, 3, 2, 1` |
| 21 | `0` fuera de rango; `5 x 10 = 50` |
| 22 | Positivos `2`, negativos `2`, ceros `1` |
| 23 | Válidas `{8, 9}`: `17 / 2 = 8.5` |
| 24 | `10 + 5 = 15`, `4 * 2 = 8` |
| 25 | `27 / 3 = 9.0` (divisor corregido) |
