# 40 EJERCICIOS DE REFUERZO — SEMANA 5

**Curso:** Solución de problemas con programación computacional
**Alcance:** Temas 13 al 16 (Tuplas · Diccionarios · Excepciones · Strings)

Resuelve los ejercicios conforme avances en los temas. Cada ejercicio incluye el **enunciado**, un **ejemplo de entrada** y la **salida esperada**. Se recomienda resolverlos en un Jupyter Notebook y subirlos a tu repositorio de GitHub.

---

## BLOQUE 1 · TEMA 13: TUPLAS

### Ejercicio 1: Tercer elemento de una tupla
**Enunciado:** Dada la tupla `colores = ("rojo", "verde", "azul", "amarillo", "naranja")`, imprime el tercer elemento (índice 2) y el primer elemento (índice 0).
**Entrada:** `colores = ("rojo", "verde", "azul", "amarillo", "naranja")`
**Salida:** `El tercer color es: azul` y `El primer color es: rojo`

---

### Ejercicio 2: Longitud de una tupla
**Enunciado:** Dada la tupla `frutas = ("manzana", "plátano", "cereza", "durazno")`, calcula e imprime la cantidad de elementos con la función `len()`.
**Entrada:** `frutas = ("manzana", "plátano", "cereza", "durazno")`
**Salida:** `La tupla tiene 4 elementos`

---

### Ejercicio 3: Índices negativos
**Enunciado:** Dada la tupla `puntos = (5, 10, 15, 20, 25, 30)`, imprime el último elemento usando el índice negativo `-1` y el tercero desde el final usando `-3`.
**Entrada:** `puntos = (5, 10, 15, 20, 25, 30)`
**Salida:** `El último elemento es: 30` y `El tercero desde el final es: 20`

---

### Ejercicio 4: Inmutabilidad de las tuplas
**Enunciado:** Dada la tupla `puntos = (5, 10, 15)`, escribe la línea que intenta modificar el primer elemento (asignar el valor 99) e indica qué excepción se genera al ejecutarla.
**Entrada:** `puntos[0] = 99`
**Salida:** `TypeError: 'tuple' object does not support item assignment`

---

### Ejercicio 5: Desempaquetado de una tupla
**Enunciado:** Desempaqueta la tupla `(7, 8, 9)` en las variables `a`, `b` y `c` en una sola línea e imprime cada una.
**Entrada:** `a, b, c = (7, 8, 9)`
**Salida:** `a = 7, b = 8, c = 9`

---

### Ejercicio 6: Concatenación de tuplas
**Enunciado:** Dadas `t1 = (1, 2, 3)` y `t2 = (4, 5)`, crea una nueva tupla `t3` con el operador `+` e imprímela.
**Entrada:** `t1 = (1, 2, 3)`, `t2 = (4, 5)`
**Salida:** `La nueva tupla es: (1, 2, 3, 4, 5)`

---

### Ejercicio 7: Anexar elementos en una nueva tupla
**Enunciado:** Dada la tupla `numeros = (10, 20, 30)`, crea una nueva tupla que anexe los valores `40` y `50` usando el operador `+`, sin modificar la tupla original.
**Entrada:** `numeros = (10, 20, 30)` más los valores `40` y `50`
**Salida:** `Nueva tupla: (10, 20, 30, 40, 50)`

---

### Ejercicio 8: Conversión a lista y ordenamiento
**Enunciado:** Dada la tupla `desorden = (8, 3, 12, 5, 1)`, conviértela en lista con `list()`, ordénala con `sort()` en orden ascendente y muéstrala.
**Entrada:** `desorden = (8, 3, 12, 5, 1)`
**Salida:** `Lista ordenada: [1, 3, 5, 8, 12]`

---

### Ejercicio 9: Suma de tupla con función que retorna
**Enunciado:** Define una función `suma_tupla(t)` que reciba una tupla, sume todos sus elementos y retorne el resultado. Pruébala con `numeros = (2, 4, 6, 8)`.
**Entrada:** `numeros = (2, 4, 6, 8)`
**Salida:** `La suma de la tupla es: 20`

---

### Ejercicio 10: Contar e indexar elementos
**Enunciado:** Dada la tupla `datos = (3, 7, 3, 9, 3)`, usa `count()` para saber cuántas veces aparece el 3 y `index()` para conocer la posición del 9.
**Entrada:** `datos = (3, 7, 3, 9, 3)`
**Salida:** `El 3 aparece 3 veces` y `El 9 está en el índice 3`

---

## BLOQUE 2 · TEMA 14: DICCIONARIOS

### Ejercicio 11: Acceso a un valor
**Enunciado:** Dado el diccionario `calificaciones = {"Ana": 9, "Luis": 8, "Mía": 10}`, imprime la calificación de Ana y la de Mía usando sus claves.
**Entrada:** `calificaciones = {"Ana": 9, "Luis": 8, "Mía": 10}`
**Salida:** `La calificación de Ana es: 9` y `La calificación de Mía es: 10`

---

### Ejercicio 12: Agregar un nuevo elemento
**Enunciado:** Dado el diccionario `contactos = {"Ana": "555-0101", "Luis": "555-0102"}`, agrega el contacto `"Mía": "555-0103"` y muestra el total de elementos con `len()`.
**Entrada:** `contactos = {"Ana": "555-0101", "Luis": "555-0102"}`
**Salida:** `Contacto agregado. Total de contactos: 3`

---

### Ejercicio 13: Actualizar un valor existente
**Enunciado:** Dado el diccionario `poblaciones = {"México": 126, "España": 47}`, actualiza el valor de México a `130` e imprímelo.
**Entrada:** `poblaciones = {"México": 126, "España": 47}`
**Salida:** `Nueva población de México: 130`

---

### Ejercicio 14: Método keys()
**Enunciado:** Dado el diccionario `contactos = {"Ana": "555-0101", "Luis": "555-0102", "Mía": "555-0103"}`, recorre sus claves con `keys()` e imprime únicamente los nombres.
**Entrada:** `contactos = {"Ana": "555-0101", "Luis": "555-0102", "Mía": "555-0103"}`
**Salida:**
```
Ana
Luis
Mía
```

---

### Ejercicio 15: Método values()
**Enunciado:** Con el mismo diccionario de contactos, recorre sus valores con `values()` e imprime únicamente los teléfonos.
**Entrada:** `contactos = {"Ana": "555-0101", "Luis": "555-0102", "Mía": "555-0103"}`
**Salida:**
```
555-0101
555-0102
555-0103
```

---

### Ejercicio 16: Método items()
**Enunciado:** Con el mismo diccionario de contactos, recorre las parejas clave-valor con `items()` e imprime cada contacto en formato `nombre: teléfono`.
**Entrada:** `contactos = {"Ana": "555-0101", "Luis": "555-0102", "Mía": "555-0103"}`
**Salida:**
```
Ana: 555-0101
Luis: 555-0102
Mía: 555-0103
```

---

### Ejercicio 17: Iteración sobre claves
**Enunciado:** Con el diccionario `contactos = {"Ana": "555-0101", "Luis": "555-0102", "Mía": "555-0103"}`, usa un ciclo `for` sobre las claves que imprima `Contacto: <nombre>` para cada una.
**Entrada:** `contactos = {"Ana": "555-0101", "Luis": "555-0102", "Mía": "555-0103"}`
**Salida:**
```
Contacto: Ana
Contacto: Luis
Contacto: Mía
```

---

### Ejercicio 18: Verificar existencia de una clave
**Enunciado:** Con el diccionario de contactos anterior, verifica con el operador `in` si la clave `"Ana"` existe y si la clave `"Pedro"` existe, imprimiendo el resultado de cada comparación.
**Entrada:** `contactos = {"Ana": "555-0101", "Luis": "555-0102", "Mía": "555-0103"}`
**Salida:** `¿Ana está en los contactos? True` y `¿Pedro está en los contactos? False`

---

### Ejercicio 19: Método get() con valor por defecto
**Enunciado:** Con el diccionario `notas = {"Ana": 9, "Luis": 8}`, usa el método `get()` para consultar la nota de `"Pedro"` usando el valor por defecto `"Sin registro"`.
**Entrada:** `notas = {"Ana": 9, "Luis": 8}`, consulta de `"Pedro"`
**Salida:** `Sin registro`

---

### Ejercicio 20: Función que retorna el teléfono
**Enunciado:** Define la función `buscar_telefono(contactos, nombre)` que retorne el teléfono del contacto o `"Contacto no encontrado"`. Pruébala con el nombre `"Luis"` y con el nombre `"Pedro"`.
**Entrada:** `contactos = {"Ana": "555-0101", "Luis": "555-0102", "Mía": "555-0103"}`, búsqueda de `"Luis"`
**Salida:** `El teléfono de Luis es: 555-0102` y `El teléfono de Pedro es: Contacto no encontrado`

---

## BLOQUE 3 · TEMA 15: EXCEPCIONES

### Ejercicio 21: Capturar ValueError
**Enunciado:** Escribe un bloque `try-except` que intente convertir el texto `"abc"` a entero con `int()` y capture el error mostrando un mensaje controlado.
**Entrada:** `"abc"`
**Salida:** `Error: Debes ingresar un número entero válido`

---

### Ejercicio 22: Capturar ZeroDivisionError
**Enunciado:** Escribe un bloque `try-except` que divida `10` entre `0` y capture el error específico mostrando un mensaje amigable.
**Entrada:** `a = 10`, `b = 0`
**Salida:** `Error: No se puede dividir entre cero`

---

### Ejercicio 23: Suma protegida con try-except
**Enunciado:** Escribe un programa que pida dos números enteros dentro de un `try-except`. Si son válidos, muestra la suma.
**Entrada:** `5` y `3`
**Salida:** `La suma es: 8`

---

### Ejercicio 24: División con bloques específicos
**Enunciado:** Escribe un programa que divida dos números capturados por consola usando un bloque `except ValueError` y otro `except ZeroDivisionError`. Muéstralo con valores válidos.
**Entrada:** `8` y `2`
**Salida:** `El resultado de la división es: 4.0`

---

### Ejercicio 25: Capturar TypeError
**Enunciado:** Escribe un bloque `try-except` que intente ejecutar `"Hola" + 5` y capture el `TypeError` mostrando un mensaje controlado.
**Entrada:** `"Hola" + 5`
**Salida:** `Error: No se pueden sumar texto y número`

---

### Ejercicio 26: Capturar IndexError
**Enunciado:** Escribe un bloque `try-except` que intente acceder al índice `5` de la lista `[10, 20, 30]` y capture el `IndexError`.
**Entrada:** `lista = [10, 20, 30]`, acceso a `lista[5]`
**Salida:** `Error: Índice fuera de rango`

---

### Ejercicio 27: Excepción general
**Enunciado:** Escribe un bloque `try-except` con `except Exception as e` que capture cualquier error y despliegue un mensaje genérico con la descripción del mismo. Pruébalo dividiendo entre cero.
**Entrada:** División `10 / 0`
**Salida:** `Ocurrió un error inesperado: division by zero`

---

### Ejercicio 28: Bloque else
**Enunciado:** Escribe un `try-except-else` que divida `10` entre `2`; el bloque `else` debe ejecutarse solo si no hubo error.
**Entrada:** `10` y `2`
**Salida:** `División exitosa: 5.0`

---

### Ejercicio 29: Bloque finally
**Enunciado:** Escribe un `try-except-finally` que intente dividir `9` entre `0`; el bloque `finally` debe ejecutarse siempre.
**Entrada:** `9` y `0`
**Salida:** `Error: No se puede dividir entre cero` y `El bloque finally siempre se ejecuta`

---

### Ejercicio 30: Ciclo while con validación
**Enunciado:** Escribe un ciclo `while` con `try-except` que repita la solicitud hasta capturar un entero válido. Simula que el usuario escribe `"hola"` y después `7`.
**Entrada:** `"hola"`, luego `7`
**Salida:** `Error: Dato inválido. Inténtalo nuevamente.` y `Número capturado: 7`

---

## BLOQUE 4 · TEMA 16: STRINGS

### Ejercicio 31: upper() y lower()
**Enunciado:** Dado `mensaje = "Hola Mundo"`, imprime el texto convertido a mayúsculas con `upper()` y a minúsculas con `lower()`.
**Entrada:** `mensaje = "Hola Mundo"`
**Salida:** `HOLA MUNDO` y `hola mundo`

---

### Ejercicio 32: Longitud con len()
**Enunciado:** Dado `texto = "Tecmilenio"`, calcula e imprime la cantidad de caracteres con `len()`.
**Entrada:** `texto = "Tecmilenio"`
**Salida:** `El texto tiene 10 caracteres`

---

### Ejercicio 33: Método replace()
**Enunciado:** Dado `frase = "El gato duerme"`, reemplaza la palabra `"gato"` por `"perro"` con `replace()` e imprime el resultado.
**Entrada:** `frase = "El gato duerme"`
**Salida:** `El perro duerme`

---

### Ejercicio 34: Método split()
**Enunciado:** Dado `frase = "Hola mundo Python"`, usa `split()` para dividir el texto y muestra cuántas palabras contiene.
**Entrada:** `frase = "Hola mundo Python"`
**Salida:** `La frase tiene 3 palabras`

---

### Ejercicio 35: Método find()
**Enunciado:** Dado `frase = "Programación en Python"`, usa `find("Python")` para conocer el índice inicial de la palabra.
**Entrada:** `frase = "Programación en Python"`
**Salida:** `La palabra "Python" inicia en el índice 16`

---

### Ejercicio 36: Slicing
**Enunciado:** Dado `texto = "Hola Mundo"`, extrae la primera palabra con `[0:4]`, la segunda con `[5:]` e imprime el texto invertido con `[::-1]`.
**Entrada:** `texto = "Hola Mundo"`
**Salida:** `Primera palabra: Hola`, `Segunda palabra: Mundo` y `Texto invertido: odnuM aloH`

---

### Ejercicio 37: Formato con f-strings
**Enunciado:** Dadas las variables `nombre = "Ana"` y `edad = 20`, imprime una frase que las integre usando un f-string.
**Entrada:** `nombre = "Ana"`, `edad = 20`
**Salida:** `Ana tiene 20 años`

---

### Ejercicio 38: Función que cuenta palabras
**Enunciado:** Define una función `contar_palabras(texto)` que retorne la cantidad de palabras de un string y pruébala con `"Aprender programación es divertido"`.
**Entrada:** `"Aprender programación es divertido"`
**Salida:** `La frase tiene 4 palabras`

---

### Ejercicio 39: replace() y upper() combinados
**Enunciado:** Dado `mensaje = "me gusta python"`, reemplaza `"python"` por `"Python"` con `replace()` y convierte el resultado a mayúsculas con `upper()`.
**Entrada:** `mensaje = "me gusta python"`
**Salida:** `ME GUSTA PYTHON`

---

### Ejercicio 40: strip() y len()
**Enunciado:** Dado `texto = "  hola  "`, elimina los espacios iniciales y finales con `strip()` y muestra el texto limpio junto con su longitud con `len()`.
**Entrada:** `texto = "  hola  "`
**Salida:** `El texto limpio es "hola" y tiene 4 caracteres`
