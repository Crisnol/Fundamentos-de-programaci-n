# ACTIVIDAD EVALUABLE 3 — TABLA DE PITÁGORAS EN MATRIZ Y OPERACIONES ESPECIALES

**Curso:** Solución de problemas con programación computacional
**Semana:** 4 · Temas 9 al 12
**Ponderación:** 6% de la calificación total del curso
**Fechas límite:** 04 de septiembre de 2026 (Periodo I) · 06 de noviembre de 2026 (Periodo II)
**Entrega:** Viernes por la noche

---

## 1. Descripción del reto

Desarrollar una **aplicación en Python** que muestre una **tabla de Pitágoras interactiva** para facilitar la multiplicación de dos factores ingresados por el usuario. El programa debe almacenar la tabla en una **lista de listas (matriz)**, imprimirla en pantalla de forma ordenada y permitir que el usuario capture dos factores (renglón y columna) para obtener su producto consultando directamente la información almacenada en la matriz.

Este reto integra las **listas** (Tema 9), las **listas de listas o matrices** (Tema 10), las **funciones que no regresan valor** (Tema 11) y las **funciones que regresan valor** (Tema 12).

---

## 2. Requerimientos técnicos obligatorios

1. **Matriz obligatoria en lista de listas:** La tabla de Pitágoras debe almacenarse obligatoriamente en una **lista de listas (matriz)**, construida con ciclos `for` y `append()`.
2. **Función que no regresa valor para imprimir la matriz:** El programa debe generar e imprimir en pantalla la matriz completa utilizando una **función que no regrese valor** (sin el uso de la palabra clave `return`).
3. **Visualización sin corchetes ni comas:** La salida en pantalla debe mostrar los números tabulados **sin corchetes ni comas** que evidencien la sintaxis de lista interna de Python.
4. **Captura de dos factores:** El usuario debe capturar dos factores numéricos (renglón y columna) para realizar una multiplicación.
5. **Función que regresa valor para multiplicar:** La multiplicación de los dos factores debe realizarse mediante una **función que regresa valor** (con la palabra clave `return`), utilizando la información almacenada en la lista de listas.
6. **Restricción crítica:** Se prohíbe terminantemente el uso de cualquier operador matemático de multiplicación (asterisco `*`) en la función que calcula el resultado. El resultado se debe obtener **consultando la posición de los factores en la matriz de Pitágoras**.

> **Sugerencia de diseño:** Para obtener el producto del factor `renglon` por el factor `columna` (sin usar `*`), la función debe consultar el elemento `matriz[renglon - 1][columna - 1]` de la tabla de Pitágoras.

---

## 3. Estructura del entregable (.py)

Un **archivo de código fuente ejecutable** con extensión **`.py`** libre de errores que contenga las siguientes secciones:

| # | Sección | Detalle |
| :---: | :--- | :--- |
| 1 | **Encabezado y comentarios** | Nombre del alumno, matrícula, fecha y descripción breve del propósito del programa. |
| 2 | **Construcción de la matriz** | Generación de la tabla de Pitágoras (por ejemplo, 10x10) como una **lista de listas**, usando ciclos `for` y `append()`. |
| 3 | **Función sin `return`** | Función `imprimir_tabla(tabla)` que NO regresa valor e imprime la matriz **sin corchetes ni comas**, con los números tabulados (`\t`). |
| 4 | **Función con `return`** | Función `consultar_producto(tabla, renglon, columna)` que regresa valor (con `return`) consultando la matriz y **sin usar el operador `*`**. |
| 5 | **Programa principal** | Captura de los dos factores con `input()` y `int()`, llamada a la función que regresa valor y despliegue del resultado. |

---

## 4. Estrategia de evaluación semanal (80/20)

| Componente | Puntos | Descripción |
| :--- | :---: | :--- |
| **Actividad oficial (archivo .py)** | **80 pts** | Código fuente en Python que cumple los 6 requerimientos obligatorios, evaluado con la rúbrica de la sección 6. |
| **Ejercicios extras en Jupyter** | **15 pts** | Resolución de los 4 ejercicios extras de la sección 5 en un Notebook `.ipynb` con celdas Markdown de explicación. |
| **Uso de Git y GitHub** | **5 pts** | Repositorio público con estructura de carpetas estandarizada e historial mínimo de **3 commits significativos** con mensajes profesionales. |
| **Total semanal** | **100 pts** | |

---

## 5. Ejercicios extras evaluables (15 puntos)

Resuelve los siguientes 4 ejercicios en un Jupyter Notebook (`extras_semana4.ipynb`). Para cada uno documenta en una celda Markdown el procedimiento y la lógica aplicada.

### Extra 1: Suma de todos los elementos de una matriz
**Enunciado:** Crea una función `suma_matriz(matriz)` que **regrese valor** (con `return`) la suma de todos los elementos de una lista de listas, usando ciclos `for` anidados. Define además una función `imprimir_matriz(matriz)` que **no regrese valor** y muestre la matriz sin corchetes ni comas. Aplica ambas funciones a la matriz `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`.
**Entrada:**
```
Matriz: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
**Salida:**
```
1 2 3
4 5 6
7 8 9
La suma de todos los elementos de la matriz es: 45
```

---

### Extra 2: Matriz con suma por fila
**Enunciado:** Crea una función `suma_fila(fila)` que **regrese valor** (con `return`) la suma de los elementos de una lista, y una función `mostrar_tabla(matriz)` que **no regrese valor** e imprima la matriz sin corchetes ni comas. Dada la matriz `[[3, 1, 4], [1, 5, 9], [2, 6, 5]]`, imprime la matriz y la suma de cada fila.
**Entrada:**
```
Matriz: [[3, 1, 4], [1, 5, 9], [2, 6, 5]]
```
**Salida:**
```
3 1 4
1 5 9
2 6 5
Suma de la fila 0: 8
Suma de la fila 1: 15
Suma de la fila 2: 13
```

---

### Extra 3: Producto de una columna sin usar el operador *
**Enunciado:** Crea la matriz `[[1, 2, 3], [4, 5, 6], [7, 8, 9], [2, 4, 6]]` (4 filas y 3 columnas). Define una función `multiplicar_columna(matriz, columna)` que **regrese valor** (con `return`) el producto de los elementos de una columna dada. **Restricción:** dentro de la función está prohibido usar el operador `*`; el producto debe calcularse con sumas repetidas usando un ciclo. Pide al usuario el número de columna (`0`, `1` o `2`) y muestra el resultado.
**Entrada:**
```
Numero de columna: 1
```
**Salida:**
```
El producto de la columna 1 es: 320
```
*(Los elementos de la columna 1 son `2`, `5`, `8` y `4`; su producto es `2 * 5 * 8 * 4 = 320`.)*

---

### Extra 4: Tabla de Pitágoras de tamaño variable
**Enunciado:** Crea una función `generar_tabla(tamano)` que **regrese valor** (con `return`) una lista de listas de `tamano x tamano` con los productos de la tabla de Pitágoras (renglones y columnas del 1 al `tamano`). Dentro de la función de generación está prohibido usar el operador `*`; usa sumas repetidas con ciclos. Define una función `imprimir_tabla(tabla)` que **no regrese valor** e imprima la tabla sin corchetes ni comas, con los números tabulados (`\t`). Pide al usuario un tamaño entre 2 y 5; si ingresa un valor fuera del rango, muestra un mensaje de error. Al final pide un renglón y una columna y muestra el producto consultando la matriz, sin usar `*`.
**Entrada:**
```
Tamano de la tabla: 4
Renglon (factor): 2
Columna (factor): 3
```
**Salida:**
```
1	2	3	4
2	4	6	8
3	6	9	12
4	8	12	16
El producto de 2 x 3 es: 6
```
*(El producto se obtiene consultando `tabla[2 - 1][3 - 1] = tabla[1][2] = 6`.)*

---

## 6. Rúbrica de evaluación (100 puntos)

| Criterio | Puntos | Excelente (100%) | Bueno (75%) | Regular (50%) | Insuficiente (0%) |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Matriz en lista de listas** | 12 | La tabla de Pitágoras se construye correctamente como una lista de listas con ciclos `for` y `append()`, sin errores. | Matriz correcta con detalles menores de formato o tamaño. | Matriz construida de forma incorrecta o con datos incompletos. | No utiliza una lista de listas o no existe. |
| **Función que no regresa valor** | 12 | Función `imprimir_tabla` correcta, sin `return`, que imprime la matriz completa. | Función correcta con detalles menores de estilo. | Función con errores de lógica o que usa `return` indebidamente. | No existe la función sin `return`. |
| **Impresión sin corchetes ni comas** | 12 | Salida perfectamente tabulada (`\t`) y sin corchetes ni comas en toda la matriz. | Salida correcta con una o dos filas con detalle menor de formato. | Varias filas muestran corchetes o comas. | La salida conserva la sintaxis de lista de Python. |
| **Captura de factores** | 10 | Captura correcta de renglón y columna con `input()` y `int()`, con validación de rango. | Captura correcta sin validación de rango. | Captura con errores de conversión o lógica. | No captura los factores. |
| **Función que regresa valor** | 16 | Función con `return` correcta que obtiene el resultado consultando la matriz (renglón y columna). | Función correcta con detalle menor de estilo o sin validación. | Función con errores de índices o que no consulta la matriz. | No existe la función con `return`. |
| **Restricción crítica (sin `*`)** | 18 | La función que calcula el resultado NO usa el operador `*` en ninguna línea; el producto se consulta en la matriz. | La función cumple la restricción pero hay un `*` aislado fuera de la función de cálculo. | Se usa el operador `*` en la función de cálculo para obtener el resultado. | El resultado se calcula directamente con `*` en el programa. |
| **Ejercicios extras (Jupyter)** | 15 | 4 ejercicios resueltos correctamente con explicaciones en Markdown. | 4 ejercicios con errores menores, o 3 resueltos correctamente. | 2 ejercicios resueltos correctamente. | 1 o ningún ejercicio resuelto. |
| **Git y GitHub** | 5 | Repositorio público, estructura de carpetas estandarizada y al menos 3 commits con mensajes profesionales. | Repositorio público con 3 commits pero mensajes poco descriptivos o estructura irregular. | Repositorio con menos de 3 commits. | No entrega liga del repositorio. |
| **TOTAL** | **100** | | | | |

---

## 7. Lista de entregables y fechas

| Entregable | Archivo | Formato | Fecha límite |
| :--- | :--- | :--- | :--- |
| Código fuente de la actividad | `tabla_pitagoras.py` | Python (.py) | 04 de septiembre de 2026 (Periodo I) · 06 de noviembre de 2026 (Periodo II) |
| Ejercicios extras | `extras_semana4.ipynb` | Jupyter Notebook (.ipynb) | 04 de septiembre de 2026 (Periodo I) · 06 de noviembre de 2026 (Periodo II) |
| Repositorio | Liga pública de GitHub | URL | 04 de septiembre de 2026 (Periodo I) · 06 de noviembre de 2026 (Periodo II) |

**Nota de entrega:** Los tres entregables deben subirse al repositorio personal del estudiante (con estructura de carpetas por semana: `semana1/`, `semana2/`, `semana3/`, `semana4/`, etc.) y la liga del repositorio se entrega como evidencia de la actividad. La entrega se realiza el viernes por la noche.
