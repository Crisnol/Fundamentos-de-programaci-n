# 35 EJERCICIOS DE REFUERZO — SEMANA 4

**Curso:** Solución de problemas con programación computacional
**Alcance:** Temas 9 al 12 (Listas · Listas de listas (matrices) · Funciones que no regresan valor · Funciones que regresan valor)

Resuelve los ejercicios conforme avances en los temas. Cada ejercicio incluye el **enunciado**, un **ejemplo de entrada** y la **salida esperada**. Se recomienda resolverlos en un Jupyter Notebook y subirlos a tu repositorio de GitHub.

---

## BLOQUE 1 · TEMA 9: LISTAS

### Ejercicio 1: Crear y mostrar una lista de frutas
**Enunciado:** Crea una lista llamada `frutas` con los elementos `"manzana"`, `"banana"`, `"cereza"` y `"durazno"`, y muéstrala en pantalla con `print()`.
**Entrada:** Ninguna (valores fijos en el código).
**Salida:** `['manzana', 'banana', 'cereza', 'durazno']`

---

### Ejercicio 2: Primer y último elemento
**Enunciado:** Dada la lista `colores = ["rojo", "verde", "azul", "amarillo"]`, accede al primer elemento con el índice `0` y al último con el índice `-1`, e imprime ambos.
**Entrada:** Ninguna (valores fijos).
**Salida:**
```
rojo
amarillo
```

---

### Ejercicio 3: Índices negativos
**Enunciado:** Dada la lista `letras = ["a", "b", "c", "d", "e"]`, imprime los elementos que se encuentran en las posiciones `-2` y `-5`.
**Entrada:** Ninguna (valores fijos).
**Salida:**
```
d
a
```

---

### Ejercicio 4: Agregar elementos con append
**Enunciado:** Crea una lista vacía `numeros = []` y agrega con `append()` los valores `10`, `20` y `30`, en ese orden. Muestra la lista final.
**Entrada:** Ninguna (valores fijos).
**Salida:** `[10, 20, 30]`

---

### Ejercicio 5: Eliminar elementos con remove
**Enunciado:** Dada la lista `nombres = ["Ana", "Luis", "Carmen", "Luis"]`, elimina la primera aparición de `"Luis"` con `remove()` y muestra la lista resultante.
**Entrada:** Ninguna (valores fijos).
**Salida:** `['Ana', 'Carmen', 'Luis']`

---

### Ejercicio 6: Ordenar con sort
**Enunciado:** Dada la lista `edades = [34, 12, 8, 21, 15]`, ordénala de menor a mayor con `sort()` y muéstrala. Luego ordénala de mayor a menor con `sort(reverse=True)` y muéstrala nuevamente.
**Entrada:** Ninguna (valores fijos).
**Salida:**
```
[8, 12, 15, 21, 34]
[34, 21, 15, 12, 8]
```

---

### Ejercicio 7: Longitud de una lista con len
**Enunciado:** Dada la lista `paises = ["Mexico", "Canada", "Brasil", "Chile"]`, muestra con `len()` cuántos países contiene.
**Entrada:** Ninguna (valores fijos).
**Salida:** `4`

---

### Ejercicio 8: Recorrido con for
**Enunciado:** Dada la lista `materias = ["Matematicas", "Fisica", "Programacion"]`, recórrela con un ciclo `for` e imprime cada materia junto con su posición, usando `range()` y `len()`.
**Entrada:** Ninguna (valores fijos).
**Salida:**
```
Posicion 0: Matematicas
Posicion 1: Fisica
Posicion 2: Programacion
```

---

### Ejercicio 9: Suma de elementos de una lista
**Enunciado:** Dada la lista `ventas = [120, 85, 200, 45]`, calcula la suma de todos sus elementos con un ciclo `for` e imprime el total.
**Entrada:** Ninguna (valores fijos).
**Salida:** `La suma de las ventas es: 450`

---

## BLOQUE 2 · TEMA 10: LISTAS DE LISTAS (MATRICES)

### Ejercicio 10: Crear una matriz 3x3
**Enunciado:** Crea una lista de listas que represente la siguiente matriz de 3 filas y 3 columnas:
```
1 2 3
4 5 6
7 8 9
```
Muestra la matriz con `print()`.
**Entrada:** Ninguna (valores fijos).
**Salida:** `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`

---

### Ejercicio 11: Acceder a una fila completa
**Enunciado:** Dada la matriz del ejercicio 10, imprime la **segunda fila completa** (índice `1`).
**Entrada:** Ninguna (valores fijos).
**Salida:** `[4, 5, 6]`

---

### Ejercicio 12: Acceder a un elemento por fila y columna
**Enunciado:** Dada la matriz del ejercicio 10, imprime el elemento que se encuentra en la **fila 2, columna 0** (índices `[2][0]`).
**Entrada:** Ninguna (valores fijos).
**Salida:** `7`

---

### Ejercicio 13: Número de filas y columnas
**Enunciado:** Dada la matriz del ejercicio 10, muestra con `len()` el número de filas y el número de columnas (longitud de la primera fila).
**Entrada:** Ninguna (valores fijos).
**Salida:**
```
Filas: 3
Columnas: 3
```

---

### Ejercicio 14: Recorrido e impresión sin corchetes ni comas
**Enunciado:** Dada la matriz `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`, recórrela con dos ciclos `for` anidados e imprime cada fila con los elementos separados por un espacio, **sin corchetes ni comas**.
**Entrada:** Ninguna (valores fijos).
**Salida:**
```
1 2 3
4 5 6
7 8 9
```

---

### Ejercicio 15: Suma de una fila
**Enunciado:** Dada la matriz del ejercicio 14, calcula con un ciclo `for` la suma de los elementos de la **fila 0** (`1 + 2 + 3`) y muestra el resultado.
**Entrada:** Ninguna (valores fijos).
**Salida:** `La suma de la fila 0 es: 6`

---

### Ejercicio 16: Suma de una columna
**Enunciado:** Dada la matriz del ejercicio 14, calcula la suma de los elementos de la **columna 1** (`2 + 5 + 8`) recorriendo las filas con un ciclo `for` y muestra el resultado.
**Entrada:** Ninguna (valores fijos).
**Salida:** `La suma de la columna 1 es: 15`

---

### Ejercicio 17: Matriz identidad 3x3
**Enunciado:** Crea con listas anidadas la **matriz identidad** de 3x3 (unos en la diagonal principal y ceros en el resto de posiciones).
**Entrada:** Ninguna (valores fijos).
**Salida:** `[[1, 0, 0], [0, 1, 0], [0, 0, 1]]`

---

### Ejercicio 18: Diagonal principal
**Enunciado:** Dada la matriz del ejercicio 14, recórrela con ciclos anidados e imprime únicamente los elementos donde el índice de fila es igual al índice de columna (la diagonal principal).
**Entrada:** Ninguna (valores fijos).
**Salida:**
```
1
5
9
```

---

## BLOQUE 3 · TEMA 11: FUNCIONES QUE NO REGRESAN VALOR

### Ejercicio 19: Procedimiento sin parámetros
**Enunciado:** Define una función `saludar()` que no reciba parámetros, **no regrese valor** e imprima `"Bienvenido al curso de programacion"`. Llámala.
**Entrada:** Ninguna (llamada directa).
**Salida:** `Bienvenido al curso de programacion`

---

### Ejercicio 20: Procedimiento con un parámetro
**Enunciado:** Define una función `mostrar_nombre(nombre)` que **no regrese valor** e imprima `Hola {nombre}`. Llámala con `"Ana"`.
**Entrada:** Ninguna (llamada directa).
**Salida:** `Hola Ana`

---

### Ejercicio 21: Procedimiento que suma y muestra
**Enunciado:** Define una función `sumar(a, b)` que calcule la suma y la **imprima**, sin usar `return`. Llámala con los valores `5` y `7`.
**Entrada:** Ninguna (llamada directa).
**Salida:** `La suma de 5 y 7 es: 12`

---

### Ejercicio 22: Procedimiento que imprime la tabla de multiplicar
**Enunciado:** Define una función `tabla(numero)` que **no regrese valor** e imprima la tabla de multiplicar del número del 1 al 10 (formato `numero x i = resultado`). Llámala con `3`.
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

### Ejercicio 23: Procedimiento que recorre una lista
**Enunciado:** Define una función `mostrar_lista(lista)` que **no regrese valor**, recorra e imprima cada elemento de la lista en una línea. Llámala con `["lunes", "martes", "miercoles"]`.
**Entrada:** Ninguna (llamada directa).
**Salida:**
```
lunes
martes
miercoles
```

---

### Ejercicio 24: Procedimiento que calcula y muestra el promedio
**Enunciado:** Define una función `promedio(c1, c2, c3)` que **no regrese valor**, calcule el promedio de 3 calificaciones y lo imprima con dos decimales usando f-strings. Llámala con `(8, 9, 7)`.
**Entrada:** Ninguna (llamada directa).
**Salida:** `El promedio es: 8.00`

---

### Ejercicio 25: Procedimiento de descuento
**Enunciado:** Define una función `aplicar_descuento(precio)` que **no regrese valor**, calcule el precio con un 10% de descuento y lo imprima. Llámala con `250`.
**Entrada:** `250`
**Salida:** `Precio con 10% de descuento: $225.0`

---

### Ejercicio 26: Procedimiento que usa append
**Enunciado:** Define una función `agregar_nota(lista, nota)` que **no regrese valor**, agregue la nota a la lista con `append()` e imprima la lista actualizada. Llámala con la lista `[8, 9]` y la nota `10`.
**Entrada:** Ninguna (llamada directa).
**Salida:** `[8, 9, 10]`

---

### Ejercicio 27: Analizar qué hace la función
**Enunciado:** Dado el siguiente código, indica si la función regresa valor y qué imprime al ser llamada:
```python
def misterio(a, b, c):
    resultado = (a + b + c) / 3
    print(f"Resultado: {resultado}")

misterio(6, 7, 11)
```
**Entrada:** Ninguna (ejercicio de análisis).
**Salida:**
```
No regresa valor (no usa return)
Resultado: 8.0
```

---

## BLOQUE 4 · TEMA 12: FUNCIONES QUE REGRESAN VALOR

### Ejercicio 28: Función que regresa una suma
**Enunciado:** Define una función `sumar(a, b)` que **regrese valor** con `return` la suma de `a + b`. Llámala con `(4, 9)` y muestra el resultado.
**Entrada:** `4`, `9`
**Salida:** `La suma de 4 y 9 es: 13`

---

### Ejercicio 29: Función que regresa el cuadrado
**Enunciado:** Define una función `cuadrado(numero)` que **regrese valor** con `return` el resultado de `numero ** 2`. Llámala con `7` y muestra el resultado.
**Entrada:** `7`
**Salida:** `El cuadrado de 7 es: 49`

---

### Ejercicio 30: Función que regresa el mayor de dos números
**Enunciado:** Define una función `mayor(a, b)` que **regrese valor** con `return` el más grande entre dos números, usando una estructura `if-else`. Llámala con `(12, 8)`.
**Entrada:** `12`, `8`
**Salida:** `El mayor es: 12`

---

### Ejercicio 31: Función que regresa el promedio de una lista
**Enunciado:** Define una función `promedio(calificaciones)` que **regrese valor** con `return` el promedio de los elementos de una lista, usando un ciclo `for` para sumarlos. Llámala con `[7, 8, 9, 10]`.
**Entrada:** `[7, 8, 9, 10]`
**Salida:** `El promedio es: 8.5`

---

### Ejercicio 32: Función que regresa el factorial
**Enunciado:** Define una función `factorial(n)` que **regrese valor** con `return` el factorial de un número usando un ciclo `for` y una variable acumuladora que inicie en `1`. Llámala con `5`.
**Entrada:** `5`
**Salida:** `El factorial de 5 es: 120`

---

### Ejercicio 33: Función que regresa el área de un círculo
**Enunciado:** Define una función `area_circulo(radio)` que **regrese valor** con `return` el resultado de `3.1416 * radio ** 2`. Llámala con `5` y muestra el resultado redondeado a dos decimales.
**Entrada:** `5`
**Salida:** `El area del circulo es: 78.54`

---

### Ejercicio 34: Función que regresa la cantidad de pares
**Enunciado:** Define una función `contar_pares(lista)` que **regrese valor** con `return` la cantidad de números pares de una lista, usando el operador módulo `%`. Llámala con `[2, 5, 8, 11, 14]`.
**Entrada:** `[2, 5, 8, 11, 14]`
**Salida:** `La lista tiene 3 numeros pares`

---

### Ejercicio 35: Composición de funciones
**Enunciado:** Define dos funciones: `sumar(a, b)` que **regrese valor** `a + b`, y `multiplicar(a, b)` que **regrese valor** `a * b`. Llama a `multiplicar(sumar(3, 4), 2)` y muestra el resultado.
**Entrada:** Ninguna (llamada directa).
**Salida:** `El resultado es: 14`
