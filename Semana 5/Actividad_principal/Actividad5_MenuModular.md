# ACTIVIDAD EVALUABLE 4 — CONSOLIDACIÓN DE ESTRUCTURAS AVANZADAS DE DATOS Y MENÚ MODULAR

**Curso:** Solución de problemas con programación computacional
**Semana:** 5 · Temas 13 al 16
**Ponderación:** 6% de la calificación total del curso
**Fechas límite:** 11 de septiembre de 2026 (Periodo I) · 13 de noviembre de 2026 (Periodo II)
**Entrega:** Viernes por la noche

---

## 1. Descripción del reto

Crear una **aplicación interactiva en Python** que demuestre el uso integral de **tuplas**, **diccionarios**, **manipulación de cadenas de texto (strings)** y **manejo robusto de excepciones**, estructurada a través de un **menú principal modular** controlado por un ciclo. El usuario debe poder seleccionar por número qué sección desea ejecutar (Tuplas, Diccionarios, Excepciones, Strings o Finalizar) y el programa debe delegar cada tarea a funciones modulares.

Este reto integra la creación y manipulación de **tuplas** (Tema 13), los **diccionarios** con claves y valores (Tema 14), los bloques **try-except** con excepciones específicas (Tema 15) y los **métodos de strings** con conteo de palabras (Tema 16), además de consolidar las funciones con y sin retorno vistas en semanas anteriores.

---

## 2. Requerimientos técnicos obligatorios

### 2.1 Uso de tuplas
1. Crear una tupla llamada `numeros` con un mínimo de **cinco elementos numéricos** de partida.
2. Acceder e imprimir en pantalla el **tercer elemento** de la tupla.
3. Capturar **dos números adicionales** ingresados por el usuario mediante `input()` y anexarlos para crear una **nueva tupla**.
4. Convertir la tupla en **lista**, aplicar un **ordenamiento** a sus elementos y mostrarla.
5. Diseñar una **función** que tome la tupla de números como parámetro, realice la **suma** de todos sus elementos y **retorne** dicho valor para mostrarlo en pantalla.

### 2.2 Uso de diccionarios
1. Crear un diccionario llamado `contactos` con al menos **tres registros iniciales** (clave: nombre del contacto, valor: número de teléfono).
2. Permitir la **captura y adición de un nuevo contacto** al diccionario mediante la consola.
3. **Iterar sobre las claves** del diccionario e imprimir en pantalla exclusivamente los **nombres** de los contactos registrados.
4. Diseñar una **función** que reciba como parámetro el diccionario de contactos y un nombre ingresado, y **retorne el número de teléfono** correspondiente. Si el nombre se localiza, mostrar el teléfono obtenido en consola.

### 2.3 Uso de excepciones
1. Solicitar al usuario ingresar **dos números enteros** en consola.
2. Implementar un bloque **`try-except`** para capturar cualquier excepción que ocurra en caso de que el usuario ingrese caracteres no numéricos o vacíos, desplegando un **mensaje de error controlado**. De lo contrario, imprimir la **suma** de ambos.
3. Agregar un bloque de excepción **específico** para controlar de forma personalizada el error de **división entre cero** (capturando el evento si el segundo número ingresado es cero) y mostrando un **mensaje amigable** al usuario.

### 2.4 Uso de strings
1. Crear una variable de texto llamada `mensaje`.
2. Imprimir en pantalla la **longitud** del string utilizando la función `len()`.
3. Utilizar un método de strings para transformar la totalidad del mensaje a **mayúsculas**.
4. Utilizar un método de strings para **buscar y reemplazar** una palabra clave del mensaje por otra palabra de tu elección.
5. Diseñar una **función** que reciba un string como parámetro y retorne de forma correcta la **cantidad de palabras** que contiene, mostrando el resultado final.

### 2.5 Menú principal interactivo
1. Construir una interfaz de consola con un **ciclo controlado** y un menú de **opciones numéricas** que permita al usuario seleccionar qué sección ejecutar (**Tuplas, Diccionarios, Excepciones, Strings o Finalizar**).
2. Al seleccionar una opción, se debe **llamar de forma modular** a las funciones correspondientes.
3. El ciclo debe permitir regresar al menú tras cada ejecución y **finalizar** únicamente cuando el usuario seleccione la opción correspondiente.

---

## 3. Estructura del entregable principal (80%)

La actividad se compone de un **archivo de código fuente ejecutable** y un **documento anexo con capturas de pantalla**:

| # | Entregable | Detalle |
| :---: | :--- | :--- |
| 1 | **Código fuente `actividad4_menu_modular.py`** | Archivo de código ejecutable con extensión `.py`, con el **menú y funciones modulares** correspondientes a tuplas, diccionarios, excepciones y strings. |
| 2 | **Documento anexo con capturas de pantalla** | Documento en Word (.docx) con capturas nítidas de la consola que demuestren la **ejecución correcta de cada una de las opciones** del menú y la **activación controlada de las excepciones** (valor no numérico, valor vacío y divisor cero). |

---

## 4. Estrategia de evaluación semanal (80/20)

| Componente | Puntos | Descripción |
| :--- | :---: | :--- |
| **Actividad oficial (código .py + documento anexo)** | **80 pts** | Código fuente con menú modular y requerimientos técnicos de tuplas, diccionarios, excepciones, strings y menú, evaluados con la rúbrica de la sección 6, más el documento anexo con capturas. |
| **Ejercicios extras en Jupyter** | **15 pts** | Resolución de los 4 ejercicios extras de la sección 5 en un Notebook `.ipynb` con celdas Markdown de explicación. |
| **Uso de Git y GitHub** | **5 pts** | Repositorio público con estructura de carpetas estandarizada e historial mínimo de **3 commits significativos** con mensajes profesionales. |
| **Total semanal** | **100 pts** | |

---

## 5. Ejercicios extras evaluables (15 puntos)

Resuelve los siguientes 4 ejercicios en un Jupyter Notebook (`extras_semana5.ipynb`). Para cada uno documenta en una celda Markdown el procedimiento aplicado y el porqué de la estructura de datos elegida.

### Extra 1: Sistema de calificaciones con tuplas
**Enunciado:** Crea una tupla `calificaciones = (7.5, 9.0, 8.0, 6.5, 10.0)`. Imprime la tercera calificación, captura dos calificaciones nuevas con `input()` y anéxalas en una nueva tupla. Convierte la nueva tupla en lista, ordénala **de mayor a menor** y muestra la suma de todos los elementos usando una función que retorne el valor.
**Entrada:**
```
Nueva calificación 1: 8.5
Nueva calificación 2: 9.5
```
**Salida:**
```
Tercera calificación: 8.0
Nueva tupla: (7.5, 9.0, 8.0, 6.5, 10.0, 8.5, 9.5)
Lista ordenada (mayor a menor): [10.0, 9.5, 9.0, 8.5, 8.0, 7.5, 6.5]
Suma total: 59.0
```

---

### Extra 2: Agenda de contactos con búsqueda
**Enunciado:** Crea un diccionario `agenda` con tres contactos iniciales (`"Ana": "555-0101"`, `"Luis": "555-0102"`, `"Mía": "555-0103"`). Captura un nuevo contacto (nombre y teléfono) con `input()` y agrégalo al diccionario. Luego imprime todos los nombres con `keys()` en una sola línea y, con una función que retorne el valor, busca y muestra el teléfono del nuevo contacto.
**Entrada:**
```
Nombre del nuevo contacto: Pedro
Teléfono del nuevo contacto: 555-0140
Nombre a buscar: Pedro
```
**Salida:**
```
Contactos registrados: Ana, Luis, Mía, Pedro
El teléfono de Pedro es: 555-0140
```

---

### Extra 3: Calculadora segura con manejo de excepciones
**Enunciado:** Escribe un programa que pida dos números enteros. Implementa un bloque `try-except` que capture `ValueError` (caracteres no numéricos o vacíos) con un mensaje controlado y un bloque específico `except ZeroDivisionError` que muestre un mensaje amigable si el segundo número es cero. En caso exitoso, muestra la división del primero entre el segundo.
**Entrada:**
```
Primer número entero: 20
Segundo número entero: 4
```
**Salida:**
```
20 dividido entre 4 es: 5.0
```
**Caso de error (divisor cero):**
```
Primer número entero: 10
Segundo número entero: 0
```
**Salida:**
```
Error: No es posible dividir entre cero. Ingresa un divisor distinto de 0.
```

---

### Extra 4: Analizador de mensajes con strings
**Enunciado:** Crea una variable `mensaje = "Python es un lenguaje poderoso"`. Imprime su longitud con `len()`, conviértelo a mayúsculas, reemplaza la palabra `"Python"` por `"programación"` y, con una función que retorne el conteo, muestra cuántas palabras contiene el mensaje original.
**Entrada:**
```
mensaje = "Python es un lenguaje poderoso"
```
**Salida:**
```
Longitud del mensaje: 30
En mayúsculas: PYTHON ES UN LENGUAJE PODEROSO
Texto reemplazado: programación es un lenguaje poderoso
Palabras totales: 5
```

---

## 6. Rúbrica de evaluación (100 puntos)

| Criterio | Puntos | Excelente (100%) | Bueno (75%) | Regular (50%) | Insuficiente (0%) |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Código fuente en Python (.py)** | 14 | Código funcional, libre de errores, correctamente formateado y con funciones modulares coherentes con el menú. | Código funcional con detalles menores de estilo o formato. | Código con errores de ejecución o que no cumple todos los módulos. | No incluye código o no funciona. |
| **Uso de tuplas** | 14 | Cumple los 5 requerimientos: tupla `numeros` (5+), tercer elemento, dos números con `input()` en nueva tupla, conversión a lista ordenada y función que suma y retorna. | Cumple 4 de 5 requerimientos. | Cumple 2-3 requerimientos. | Cumple 1 o ninguno. |
| **Uso de diccionarios** | 12 | Cumple los 4 requerimientos: diccionario `contactos` (3+), adición de contacto por consola, iteración de claves con nombres y función que retorna el teléfono. | Cumple 3 de 4 requerimientos. | Cumple 2 requerimientos. | Cumple 1 o ninguno. |
| **Uso de excepciones** | 10 | Cumple los 3 requerimientos: dos enteros, `try-except` con mensaje controlado y bloque específico `ZeroDivisionError`. | Cumple 2 de 3 requerimientos. | Cumple 1 requerimiento. | No implementa excepciones. |
| **Uso de strings** | 12 | Cumple los 5 requerimientos: variable `mensaje`, `len()`, mayúsculas, `replace()` y función que cuenta palabras. | Cumple 4 de 5 requerimientos. | Cumple 2-3 requerimientos. | Cumple 1 o ninguno. |
| **Menú principal interactivo** | 10 | Menú con ciclo controlado, 5 opciones numéricas, llamadas modulares a funciones y finalización correcta del programa. | Menú funcional con detalles menores (mensajes o formato). | Menú incompleto o con opciones que no llaman a las funciones. | No incluye menú. |
| **Documento anexo con capturas** | 8 | Capturas nítidas de las 5 opciones del menú y de la activación de las excepciones, correctamente ordenadas y etiquetadas. | Capturas completas con detalles menores de orden o nitidez. | Capturas incompletas o sin etiquetar. | No incluye documento anexo. |
| **Ejercicios extras (Jupyter)** | 15 | 4 ejercicios resueltos correctamente con explicaciones en Markdown. | 4 ejercicios con errores menores, o 3 resueltos correctamente. | 2 ejercicios resueltos correctamente. | 1 o ningún ejercicio resuelto. |
| **Git y GitHub** | 5 | Repositorio público, estructura de carpetas estandarizada y al menos 3 commits con mensajes profesionales. | Repositorio público con 3 commits pero mensajes poco descriptivos o estructura irregular. | Repositorio con menos de 3 commits. | No entrega liga del repositorio. |
| **TOTAL** | **100** | | | | |

---

## 7. Lista de entregables y fechas

| Entregable | Archivo | Formato | Fecha límite |
| :--- | :--- | :--- | :--- |
| Código fuente de la actividad | `actividad4_menu_modular.py` | Python (.py) | Viernes por la noche |
| Documento anexo de capturas | `actividad4_capturas.docx` | Word (.docx) | Viernes por la noche |
| Ejercicios extras | `extras_semana5.ipynb` | Jupyter Notebook (.ipynb) | Viernes por la noche |
| Repositorio | Liga pública de GitHub | URL | Viernes por la noche |

**Nota de entrega:** Los entregables deben subirse al repositorio personal del estudiante (con estructura de carpetas por semana: `semana5/`, etc.) y la liga del repositorio se entrega como evidencia de la actividad.
