# 20 EJERCICIOS EXTRA — SEMANA 3

**Curso:** Solución de problemas con programación computacional
**Alcance:** Temas 1 al 8 (Variables, tipos y operadores · Entradas y salidas · Estructuras de decisión · Ciclo `while` · Ciclo `for` · Acumuladores y contadores)

---

## BLOQUE 1 · DECISIONES Y OPERADORES LÓGICOS

### Ejercicio 1: Tarifa de estacionamiento
**Enunciado:** Un estacionamiento cobra las primeras 2 horas a $15.00 cada una y las horas adicionales a $10.00 cada una. El cobro nunca puede exceder los $200.00 del pase diario (tope). Crea un programa que pida el número de horas (entero) y muestre el total a pagar aplicando las reglas.
**Entrada:** `25`
**Proceso:** `(2 * 15) + (23 * 10) = 260`, pero el tope diario es `200`
**Salida:** `Total a pagar: $200.00`

---

### Ejercicio 2: Años bisiestos en un rango
**Enunciado:** Crea un programa que pida dos años (inicio y fin) y muestre en una línea todos los años bisiestos de ese rango. Regla: un año es bisiesto si es divisible entre 4 pero no entre 100, o si es divisible entre 400. Usa el `for` con `range` y operadores lógicos (`and`/`or`).
**Entrada:** `2000` y `2010`
**Proceso:** `2000 % 400 == 0` (bisiesto), `2004 % 4 == 0` y `2004 % 100 != 0` (bisiesto), `2008` (bisiesto)
**Salida:** `Años bisiestos: 2000, 2004, 2008`

---

## BLOQUE 2 · WHILE: DÍGITOS Y DESCOMPOSICIÓN DE NÚMEROS

### Ejercicio 3: Contador de dígitos
**Enunciado:** Crea un programa que pida un número entero positivo y cuántos dígitos tiene, usando `while` con el operador división entera `//` (cada iteración elimina el último dígito).
**Entrada:** `4572`
**Proceso:** `4572 -> 457 -> 45 -> 4 -> 0` (4 eliminaciones)
**Salida:** `El número 4572 tiene 4 dígitos`

---

### Ejercicio 4: Suma de dígitos
**Enunciado:** Crea un programa que pida un número entero positivo y calcule la suma de sus dígitos usando `while`, el módulo `%` para extraer el último dígito y `//` para eliminarlo.
**Entrada:** `4729`
**Proceso:** `4 + 7 + 2 + 9 = 22`
**Salida:** `La suma de los dígitos de 4729 es: 22`

---

### Ejercicio 5: Número invertido
**Enunciado:** Crea un programa que pida un número entero positivo y muestre sus dígitos en orden inverso. Construye el nuevo número en un acumulador con la fórmula `invertido = invertido * 10 + digito`.
**Entrada:** `1234`
**Proceso:** `4`, luego `43`, luego `432`, luego `4321`
**Salida:** `El número invertido de 1234 es 4321`

---

### Ejercicio 6: División con restas sucesivas
**Enunciado:** Sin usar los operadores `/` ni `//`, calcula el cociente y el residuo de una división entre enteros positivos restando el divisor al dividendo con un `while`; el cociente es la cantidad de restas realizadas.
**Entrada:** `17` y `5`
**Proceso:** `17-5=12`, `12-5=7`, `7-5=2` (3 restas, ya no se puede restar más)
**Salida:** `17 ÷ 5 = 3 con residuo 2`

---

### Ejercicio 7: Desglose de billetes
**Enunciado:** Un cajero entrega el monto solicitado con la menor cantidad de billetes posibles. Crea un programa que pida un monto (múltiplo de 10) y muestre cuántos billetes de `$500`, `$200`, `$100`, `$50`, `$20` y monedas de `$10` entregará, usando `//` y `%`.
**Entrada:** `1380`
**Proceso:** `1380 // 500 = 2` (restan 380), `380 // 200 = 1` (restan 180), y así sucesivamente
**Salida:**
```
Billetes de $500: 2
Billetes de $200: 1
Billetes de $100: 1
Billetes de $50: 1
Billetes de $20: 1
Monedas de $10: 1
```

---

## BLOQUE 3 · FOR, ACUMULADORES Y SERIES NUMÉRICAS

### Ejercicio 8: Potencia sin usar **
**Enunciado:** Crea un programa que pida una base y un exponente entero positivo, y calcule la potencia mediante multiplicaciones sucesivas con un `for` y un acumulador (sin usar el operador `**`).
**Entrada:** base `3`, exponente `4`
**Proceso:** `3 * 3 = 9`, `9 * 3 = 27`, `27 * 3 = 81`
**Salida:** `3 elevado a 4 = 81`

---

### Ejercicio 9: El mayor de N números
**Enunciado:** Crea un programa que primero pregunte cuántos números se capturarán y, con un `for`, lea cada uno guardando siempre el mayor visto hasta ese momento en una variable.
**Entrada:** `6`, valores `4`, `15`, `3`, `9`, `21`, `7`
**Proceso:** el máximo parcial va cambiando: `4 -> 15 -> 21`
**Salida:** `El número mayor es: 21`

---

### Ejercicio 10: Múltiplos de K con range y paso
**Enunciado:** Crea un programa que pida dos enteros positivos `k` y `n`, e imprima en una sola línea todos los múltiplos de `k` menores que `n`, generándolos directamente con `range(k, n, k)` (sin usar `if`).
**Entrada:** `k = 4`, `n = 30`
**Proceso:** `range(4, 30, 4)` genera `4, 8, 12, 16, 20, 24, 28`
**Salida:** `4, 8, 12, 16, 20, 24, 28`

---

### Ejercicio 11: Serie alternada
**Enunciado:** Crea un programa que pida un entero positivo `n` y calcule la suma alternada `1 - 2 + 3 - 4 + ...` hasta `n`. Usa un `for` y decide el signo de cada término con el módulo `%`.
**Entrada:** `6`
**Proceso:** `1 - 2 + 3 - 4 + 5 - 6 = -3`
**Salida:** `El resultado de la serie es: -3`

---

### Ejercicio 12: Serie armónica
**Enunciado:** Crea un programa que pida un entero positivo `n` y calcule la suma `1 + 1/2 + 1/3 + ... + 1/n` con un acumulador flotante. Muestra el resultado con 2 decimales.
**Entrada:** `4`
**Proceso:** `1 + 0.5 + 0.3333... + 0.25 = 2.0833...`
**Salida:** `La suma de la serie es: 2.08`

---

### Ejercicio 13: Sucesión de Fibonacci
**Enunciado:** Crea un programa que pida cuántos términos de la sucesión de Fibonacci mostrar. La sucesión comienza con `0` y `1`, y cada término siguiente es la suma de los dos anteriores. Usa dos variables que avancen junto con el `for`.
**Entrada:** `8`
**Proceso:** `0+1=1`, `1+1=2`, `1+2=3`, `2+3=5`, `3+5=8`, `5+8=13`
**Salida:** `Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13`

---

## BLOQUE 4 · PATRONES GRÁFICOS CON CICLOS ANIDADOS

> Para estos patrones, acumula los caracteres en una cadena usando concatenación (`linea = linea + "*"`) e imprime la cadena completa al terminar cada fila.

### Ejercicio 14: Triángulo de asteriscos
**Enunciado:** Crea un programa que pida un número de filas y dibuje un triángulo de asteriscos cuya primera fila tenga 1 asterisco, la segunda 2, y así sucesivamente. Usa ciclos anidados.
**Entrada:** `4`
**Salida:**
```
*
**
***
****
```

---

### Ejercicio 15: Pirámide centrada
**Enunciado:** Crea un programa que pida un número de filas y dibuje una pirámide de asteriscos centrada: la fila `i` lleva `filas - i` espacios seguidos de `2*i - 1` asteriscos. Usa ciclos anidados.
**Entrada:** `5`
**Proceso:** fila 1 = 4 espacios + 1 asterisco, fila 5 = 0 espacios + 9 asteriscos
**Salida:**
```
    *
   ***
  *****
 *******
*********
```

---

## BLOQUE 5 · RETOS DE INTEGRACIÓN (DECISIÓN + CICLOS)

### Ejercicio 16: Adivina el número secreto
**Enunciado:** Define en tu código un número secreto (por ejemplo `42`). El usuario intenta adivinarlo en un ciclo `while`: por cada intento muestra `Muy bajo` si su número es menor, `Muy alto` si es mayor, y al acertar termina indicando en cuántos intentos lo logró (usa un contador).
**Entrada:** `10`, `90`, `40`, `42`
**Proceso:** `10 < 42` (bajo), `90 > 42` (alto), `40 < 42` (bajo), `42 == 42` (correcto)
**Salida:**
```
Muy bajo
Muy alto
Muy bajo
¡Correcto! Lo lograste en 4 intentos
```

---

### Ejercicio 17: Detector de números primos
**Enunciado:** Crea un programa que pida un entero positivo y determine si es primo (solo divisible entre 1 y sí mismo). Recorre los posibles divisores con un `for` desde 2 hasta `n - 1`, cuenta cuántos dividen exactamente con `%` y decide el mensaje.
**Entrada:** `29`
**Proceso:** ningún número de `2` a `28` divide exactamente a `29` (contador de divisores = 0)
**Salida:** `29 es primo`

---

### Ejercicio 18: Número perfecto
**Enunciado:** Un número perfecto es igual a la suma de sus divisores propios (sin contarse a sí mismo). Crea un programa que pida un entero positivo, sume sus divisiores con un `for` y un acumulador, e indique si es perfecto o no.
**Entrada:** `28`
**Proceso:** divisores propios `1, 2, 4, 7, 14`; suma = `28`
**Salida:** `28 es un número perfecto`

---

### Ejercicio 19: Interés compuesto año por año
**Enunciado:** Crea un programa que pida un capital inicial, una tasa de interés anual en porcentaje y un número de años. Con un `for`, muestra el capital al final de cada año aplicando el crecimiento sobre el año anterior, y al final reporta el capital total.
**Entrada:** capital `1000`, tasa `10`, años `3`
**Proceso:** `1000 * 1.10 = 1100`, `1100 * 1.10 = 1210`, `1210 * 1.10 = 1331`
**Salida:**
```
Año 1: $1100.00
Año 2: $1210.00
Año 3: $1331.00
Capital final: $1331.00
```

---

### Ejercicio 20: Simulador de batería
**Enunciado:** Simula la descarga de la batería de un laptop que inicia al 100% y pierde 10 puntos por hora. Con un `while`, muestra el nivel después de cada hora; cuando el nivel llegue a 20% o menos, imprime la advertencia de batería baja y detén la simulación.
**Entrada:** Ninguna (la simulación inicia siempre en 100).
**Proceso:** niveles `90, 80, 70, 60, 50, 40, 30, 20`; al llegar a `20` se dispara la alerta
**Salida:**
```
Hora 1: 90%
Hora 2: 80%
Hora 3: 70%
Hora 4: 60%
Hora 5: 50%
Hora 6: 40%
Hora 7: 30%
Hora 8: 20%
¡Batería baja! Conecta el cargador
```
**Tip:** Usa `time.sleep(10)` para pausar 10 segundos el ciclo simulando que es una hora. Recuerda importar `import time`


