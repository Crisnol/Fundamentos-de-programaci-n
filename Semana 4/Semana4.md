# SEMANA 4: LISTAS, MATRICES (LISTAS DE LISTAS) Y FUNCIONES EN PYTHON

**Curso:** Solución de problemas con programación computacional  
**Institución:** Universidad Tecmilenio  
**Rol:** PyCoach — Guía Docente y Material de Clase  

---

## ÍNDICE DEL MATERIAL
1. **Tema 9:** Listas (creación, indexación, métodos y recorridos)
2. **Tema 10:** Listas de listas (matrices) — Creación, acceso por fila/columna y recorrido
3. **Tema 11:** Funciones que NO regresan valor (`def`, parámetros y procedimientos sin `return`)
4. **Tema 12:** Funciones que regresan valor (`return`, funciones con parámetros y retorno, llamadas)
5. **Actividad Integradora Semanal:** Tabla de Pitágoras en Jupyter + Gestión en GitHub
6. **Desafíos Extras Autoevaluables:** Ejercicios de refuerzo para los alumnos

---

# TEMA 9: LISTAS

### 9.1 ¿Qué es una Lista?
Una **lista** es una estructura de datos en Python que permite almacenar una **colección ordenada y modificable (mutable)** de valores en una sola variable. Cada valor guardado recibe el nombre de **elemento** y ocupa una **posición (índice)** dentro de la lista.

#### Características Clave de una Lista:
1. **Ordenada:** Cada elemento tiene un índice que determina su posición.
2. **Mutable:** Los elementos pueden agregarse, eliminarse o modificarse después de crear la lista.
3. **Heterogénea:** Puede contener valores de distintos tipos (enteros, flotantes, cadenas, booleanos, incluso otras listas).
4. **Indizada desde cero:** El primer elemento se encuentra en el índice `0`.

---

### 9.2 Creación de Listas
Las listas se crean con **corchetes `[]`** separando los elementos con comas.

```python
frutas = ["manzana", "platano", "cereza"]
numeros = [10, 20, 30]
mixta = ["Ana", 25, 1.75, True]   # Python permite mezclar tipos de datos
vacia = []                        # lista sin elementos

print(frutas)    # ['manzana', 'platano', 'cereza']
print(len(frutas))  # 3
```

---

### 9.3 Indexación (Acceso a Elementos)
Cada elemento se accede con su **índice**. Python también permite **índices negativos**, donde `-1` representa el último elemento, `-2` el penúltimo, y así sucesivamente.

```python
frutas = ["manzana", "platano", "cereza"]

print(frutas[0])    # manzana  -> primer elemento
print(frutas[2])    # cereza   -> tercer elemento
print(frutas[-1])   # cereza   -> último elemento
print(frutas[-2])   # platano  -> penúltimo elemento
```

> **IMPORTANTE:** Intentar acceder a un índice que no existe provoca un error `IndexError` (ej. `frutas[3]` o `frutas[5]` en la lista anterior).

---

### 9.4 Métodos y Funciones Esenciales de Listas

| Método / Función | Descripción | Ejemplo |
| :--- | :--- | :--- |
| `lista.append(x)` | Agrega el elemento `x` al final de la lista. | `numeros.append(40)` |
| `lista.remove(x)` | Elimina la **primera aparición** de `x`. | `frutas.remove("cereza")` |
| `lista.sort()` | Ordena la lista de menor a mayor (en el lugar). | `numeros.sort()` |
| `lista.sort(reverse=True)` | Ordena la lista de mayor a menor. | `numeros.sort(reverse=True)` |
| `len(lista)` | Devuelve la cantidad de elementos. | `len(frutas)` |

```python
numeros = [30, 10, 20]
numeros.append(40)      # -> [30, 10, 20, 40]
numeros.sort()          # -> [10, 20, 30, 40]
numeros.remove(20)      # -> [10, 30, 40]
print(numeros)          # [10, 30, 40]
print(len(numeros))     # 3
```

---

### 9.5 Recorridos de Listas con `for`
Para procesar todos los elementos de una lista se utiliza la estructura de repetición `for`.

```python
puntajes = [90, 85, 100]

# Recorrido por valor (lo más común)
for p in puntajes:
    print(p)
# 90
# 85
# 100

# Recorrido por índice usando range() y len()
for i in range(len(puntajes)):
    print(f"Posicion {i}: {puntajes[i]}")
# Posicion 0: 90
# Posicion 1: 85
# Posicion 2: 100
```

---

# TEMA 10: LISTAS DE LISTAS (MATRICES)

### 10.1 ¿Qué es una Matriz en Python?
Una **matriz** es una estructura bidimensional que se representa en Python como una **lista de listas**: cada elemento de la lista externa es, a su vez, otra lista (una **fila**). Esto permite organizar datos en **renglones (filas)** y **columnas**, tal como en una hoja de cálculo.

```
Columna 0    Columna 1    Columna 2
   [1]           [2]          [3]      <- Fila 0
   [4]           [5]          [6]      <- Fila 1
   [7]           [8]          [9]      <- Fila 2
```

---

### 10.2 Creación de una Matriz

```python
matriz = [
    [1, 2, 3],   # fila 0
    [4, 5, 6],   # fila 1
    [7, 8, 9]    # fila 2
]
```

También se puede construir con ciclos `for` y `append()`:

```python
matriz = []
for i in range(3):
    fila = [1, 2, 3]
    matriz.append(fila)

print(matriz)   # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
```

---

### 10.3 Acceso por Fila y por Columna
- Para obtener una **fila completa**: `matriz[índice_fila]`.
- Para obtener un **elemento específico**: `matriz[índice_fila][índice_columna]`.

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[0])      # [1, 2, 3]   -> fila 0 completa
print(matriz[1][2])   # 6           -> fila 1, columna 2
print(matriz[2][0])   # 7           -> fila 2, columna 0
print(matriz[-1][-1]) # 9           -> último elemento (fila 2, columna 2)
```

> **Nota:** `matriz[1][2]` se lee como: "en la fila 1, toma el elemento de la columna 2". El primer índice selecciona la fila y el segundo la columna.

---

### 10.4 Recorrido de una Matriz
Para recorrer todos los elementos se usan **dos ciclos `for` anidados**: el externo recorre las filas y el interno recorre los elementos de cada fila.

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()
```

**Salida en pantalla:**
```
1 2 3 
4 5 6 
7 8 9 
```

---

### 10.5 Número de Filas y Columnas
- **Filas:** `len(matriz)`.
- **Columnas:** `len(matriz[0])` (longitud de la primera fila, asumiendo matriz rectangular).

```python
print(len(matriz))     # 3 filas
print(len(matriz[0]))  # 3 columnas
```

---

# TEMA 11: FUNCIONES QUE NO REGRESAN VALOR

### 11.1 ¿Qué es una Función?
Una **función** es un bloque de código reutilizable con un nombre que ejecuta una tarea específica. Las funciones permiten **organizar el programa en módulos**, evitar la repetición de código y hacer el programa más legible y fácil de mantener.

En Python existen dos grandes familias de funciones:
1. **Funciones que NO regresan valor (procedimientos):** ejecutan una tarea (por ejemplo, imprimir) pero no devuelven un resultado a la parte que las llamó. **No usan `return`.**
2. **Funciones que regresan valor:** calculan un resultado y lo devuelven con la palabra clave `return`.

---

### 11.2 Definición con `def` y Parámetros
La sintaxis general es:

```python
def nombre_de_la_funcion(parametro1, parametro2):
    # cuerpo de la función
    instrucciones...
```

- **`def`:** palabra reservada para definir la función.
- **Parámetros:** valores que la función recibe al ser llamada.
- El cuerpo debe estar **indentado** (4 espacios).

---

### 11.3 Procedimientos sin `return` (Funciones que no regresan valor)
Estas funciones realizan su tarea (generalmente imprimir o modificar estructuras) y **terminan sin devolver nada**. Al llamarlas simplemente se invoca su nombre con los argumentos entre paréntesis.

```python
def imprimir_saludo():
    print("Hola, esto es una funcion sin return")

imprimir_saludo()
# Hola, esto es una funcion sin return
```

```python
def imprimir_suma(a, b):
    suma = a + b
    print(f"La suma de {a} y {b} es: {suma}")

imprimir_suma(5, 7)
# La suma de 5 y 7 es: 12
```

```python
def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
imprimir_matriz(matriz)
# 1	2	3
# 4	5	6
# 7	8	9
```

> **Ejemplo clave de la semana:** la función `imprimir_matriz(matriz)` recibe la matriz como parámetro y la muestra **sin corchetes ni comas**, sin usar `return`. Este patrón es obligatorio en la Actividad 3.

---

# TEMA 12: FUNCIONES QUE REGRESAN VALOR

### 12.1 La Palabra Clave `return`
Las funciones que **regresan valor** devuelven un resultado a la parte del programa que las llamó mediante la palabra reservada `return`. Ese resultado puede asignarse a una variable o usarse directamente en una expresión.

```python
def sumar(a, b):
    return a + b

resultado = sumar(3, 4)   # se guarda el valor devuelto en la variable
print(resultado)          # 7
print(sumar(10, 20))      # 30
```

> **Diferencia clave:** una función con `return` devuelve el resultado para que el programa lo siga utilizando; una función sin `return` solo ejecuta su tarea (como imprimir) y no entrega ningún valor.

---

### 12.2 Funciones con Parámetros y Retorno
La sintaxis es igual a la anterior, pero el cuerpo contiene al menos una instrucción `return`.

```python
def cuadrado(n):
    return n ** 2

print(cuadrado(5))    # 25
print(cuadrado(10))   # 100
```

```python
def factorial(n):
    producto = 1
    for i in range(1, n + 1):
        producto = producto * i
    return producto

print(factorial(5))   # 120  (1 * 2 * 3 * 4 * 5)
```

```python
def promedio(calificaciones):
    suma = 0
    for nota in calificaciones:
        suma = suma + nota
    return suma / len(calificaciones)

print(promedio([7, 8, 9, 10]))   # 8.5
```

---

### 12.3 Llamadas y Composición de Funciones
Una función que regresa valor puede usarse dentro de otra función o expresión, lo que permite **componer** funciones.

```python
def sumar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

# Composición: el resultado de sumar() se usa como argumento de multiplicar()
resultado = multiplicar(sumar(3, 4), 2)
print(resultado)   # 14
```

```python
def consultar_producto(matriz, renglon, columna):
    return matriz[renglon - 1][columna - 1]

tabla = [
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9]
]
print(consultar_producto(tabla, 2, 3))   # 6  (2 x 3)
```

> **Ejemplo clave de la semana:** la función `consultar_producto(matriz, renglon, columna)` regresa el producto **consultando la posición del factor en la matriz**, sin necesidad de usar el operador `*`. Este patrón es obligatorio en la Actividad 3.

---

# ACTIVIDAD INTEGRADORA SEMANAL (PRÁCTICA EN GUÍAS JUPYTER + GIT)

### Consigna para el Estudiante:
Debes crear un Jupyter Notebook llamado `solucion_semana4.ipynb` dentro de tu repositorio local `curso-python-semana4` que contenga:

1. **Celda Markdown:** Un título general, tu nombre completo, matrícula y una explicación breve de qué es una lista de listas (matriz) y para qué sirven las funciones con y sin `return`.
2. **Celda Código:** Un programa en Python que:
   - Construya una **matriz de 5x5** con los productos de la tabla de Pitágoras (renglones y columnas del 1 al 5) usando una **lista de listas**.
   - Defina una **función que NO regresa valor** para imprimir la matriz completa **sin corchetes ni comas** (usando tabulaciones `\t`).
   - Defina una **función que regresa valor** (con `return`) que reciba un renglón y una columna y devuelva el producto **consultando la matriz**, **SIN usar el operador `*`**.
   - Capture por teclado un renglón y una columna, y muestre el resultado de la multiplicación.

3. **Subir los cambios a GitHub:**
```bash
git init
git add solucion_semana4.ipynb
git commit -m "feat: completar actividad integradora semana 4"
git push origin main
```

> **Nota:** La versión completa y oficial de la actividad evaluable (ACTIVIDAD 3 "Tabla de Pitágoras en Matriz y Operaciones Especiales", 6% de la calificación) se encuentra en el archivo `Actividad4_TablaPitagoras.md` de esta misma carpeta, junto con su rúbrica de evaluación y sus ejercicios extras.

---

# DESAFÍOS EXTRAS AUTOEVALUABLES (REFUERZO)

Los siguientes ejercicios extras están diseñados para ser resueltos en tu libreta de Jupyter Notebook para poner a prueba tus habilidades con listas, matrices y funciones.

### Desafío Extra 1: Registro de calificaciones con listas
Crea un programa que pida el número de calificaciones `N`, capture `N` calificaciones y las guarde en una lista con `append()`. Define una función que **regresa valor** para calcular el promedio (con `return`) y una función que **no regresa valor** para mostrar todas las calificaciones. Muestra el promedio con dos decimales.

### Desafío Extra 2: Matriz de ventas semanales
Define una matriz de **3 filas x 7 columnas** con las ventas de tres vendedores durante una semana. Con ciclos `for` calcula la suma de cada fila y el total general de la semana. Usa una función que no regresa valor para imprimir la matriz sin corchetes ni comas.

### Desafío Extra 3: Procedimiento que dibuja un tablero 3x3
Crea una función `mostrar_tablero(tablero)` que **no regrese valor** y que reciba una lista de listas 3x3 de símbolos (ej. `[["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]`) y la imprima en pantalla como un tablero de juego de gato, separando los símbolos con el carácter `|` y las filas con guiones.

### Desafío Extra 4: Potencia con multiplicación repetida
Crea una función `potencia(base, exponente)` que **regrese valor** (con `return`) y calcule `base ** exponente` **sin usar el operador `**`** ni la función `pow`. Debes lograrlo con un ciclo `for` y multiplicaciones acumuladas (ej. `potencia(3, 4)` debe devolver `81`).
- *Pista:* Inicia con `resultado = 1` y multiplica `base` repetidamente, `exponente` veces.

### Desafío Extra 5: Suma de la diagonal principal
Crea una función `suma_diagonal(matriz)` que **regrese valor** (con `return`) y reciba una matriz cuadrada de 3x3. Debe sumar únicamente los elementos donde el índice de fila es igual al índice de columna (la diagonal principal). Usa una función que no regresa valor para mostrar la matriz y el resultado.
- *Pista:* Para la matriz `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`, la suma de la diagonal es `1 + 5 + 9 = 15`.
