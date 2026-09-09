# ENTREGABLES SEMANA 5 — INSTRUCCIONES DE ENTREGA

**Curso:** Solución de problemas con programación computacional
**Semana:** 5 · Temas 13 al 16
**Fechas límite:** 11 de septiembre de 2026 (Periodo I) · 13 de noviembre de 2026 (Periodo II)
**Entrega:** Viernes por la noche

> **⚠️ AVISO IMPORTANTE:** A partir de esta semana, los **5 Desafíos Extras Autoevaluables (Refuerzo)** que originalmente aparecían en el material de clase como ejercicios de autoestudio **pasan a ser de entrega OBLIGATORIA y evaluable**, como consecuencia de un tema de disciplina/castigo en clase. Esto significa que el Notebook de ejercicios extras ya **no contiene 4, sino 9 ejercicios en total** (los 4 ejercicios extras evaluables originales + los 5 desafíos de refuerzo). Para que la rúbrica siga sumando **100 puntos**, el peso de la actividad principal se ajustó de **80 a 70 puntos**, y el 10% restante se redistribuyó como el nuevo criterio obligatorio de la sección 7. **No entregar los 5 desafíos extra afectará la calificación de la semana.**

---

## 1. Descripción del reto

Crear una **aplicación interactiva en Python** que demuestre el uso integral de **tuplas**, **diccionarios**, **manipulación de cadenas de texto (strings)** y **manejo robusto de excepciones**, estructurada a través de un **menú principal modular** controlado por un ciclo. El usuario debe poder seleccionar por número qué sección desea ejecutar (Tuplas, Diccionarios, Excepciones, Strings o Finalizar) y el programa debe delegar cada tarea a funciones modulares.

Este reto integra la creación y manipulación de **tuplas** (Tema 13), los **diccionarios** con claves y valores (Tema 14), los bloques **try-except** con excepciones específicas (Tema 15) y los **métodos de strings** con conteo de palabras (Tema 16), además de consolidar las funciones con y sin retorno vistas en semanas anteriores.

---

## 2. Requerimientos técnicos obligatorios (Actividad principal — 80%)

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

## 3. Estructura del entregable principal (70%)

La actividad se compone de un **archivo de código fuente ejecutable** y un **documento anexo con capturas de pantalla**:

| # | Entregable | Detalle |
| :---: | :--- | :--- |
| 1 | **Código fuente `actividad4_menu_modular.py`** | Archivo de código ejecutable con extensión `.py`, con el **menú y funciones modulares** correspondientes a tuplas, diccionarios, excepciones y strings. |
| 2 | **Documento anexo con capturas de pantalla** | Documento en Word (.docx) con capturas nítidas de la consola que demuestren la **ejecución correcta de cada una de las opciones** del menú y la **activación controlada de las excepciones** (valor no numérico, valor vacío y divisor cero). |

---

## 4. Ejercicios extras evaluables (4 ejercicios — originales)

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

## 5. Desafíos extras de refuerzo — AHORA DE ENTREGA OBLIGATORIA (5 ejercicios adicionales)

> Estos 5 ejercicios aparecían en el material de clase (`Semana5.md`) como **"Desafíos Extras Autoevaluables (Refuerzo)"**, es decir, de resolución voluntaria y sin evaluación. **Debido a un tema de disciplina/castigo en clase, estos 5 desafíos dejan de ser autoevaluables y se convierten en entregables obligatorios y evaluados**, junto con los 4 ejercicios de la sección 4. Resuélvelos en el mismo Notebook `extras_semana5.ipynb`, agregándolos como continuación de los 4 anteriores (es decir, el Notebook final debe contener los **9 ejercicios en total**), cada uno con su celda Markdown de explicación.

### Desafío Extra 1: Lista de espera con tuplas
Crea una tupla `espera = ("María", "José", "Carlos", "Lucía", "Pedro")`. Imprime el tercer elemento, captura dos nombres nuevos con `input()`, anéxalos en una nueva tupla, conviértela en lista, ordénala alfabéticamente y muestra la cantidad total de personas.

### Desafío Extra 2: Contador de votos con diccionario
Crea un diccionario `votos = {"Rojo": 0, "Azul": 0, "Verde": 0}`. Pide al usuario el color de su voto cinco veces, suma uno al valor correspondiente en cada ocasión y, al final, imprime con `items()` el color ganador junto con su total.

### Desafío Extra 3: Validación robusta de entrada
Escribe un programa que pida al usuario dos números enteros dentro de un bloque `try-except`. Si el usuario ingresa texto o un valor vacío, muestra un mensaje controlado y repite la solicitud con un ciclo `while`. Luego pide la división del primero entre el segundo, con un bloque específico para `ZeroDivisionError`.

### Desafío Extra 4: Analizador de textos
Crea un programa que reciba una frase, imprima su longitud con `len()`, la convierta a mayúsculas, reemplace la palabra "Python" por "programación" y muestre cuántas palabras contiene usando una función que retorne el conteo.

### Desafío Extra 5: Minimenú modular integrador
Construye un menú con un ciclo `while` y opciones numéricas que permita ejecutar de forma modular: (1) mostrar la tupla de números ordenada, (2) buscar un teléfono en el diccionario `contactos`, (3) dividir dos números con manejo de `ZeroDivisionError` y (4) analizar un mensaje de texto. La opción (5) debe finalizar el programa.

---

## 6. Estrategia de evaluación semanal (modificada)

| Componente | Puntos | Descripción |
| :--- | :---: | :--- |
| **Actividad oficial (código .py + documento anexo)** | **70 pts** | Código fuente con menú modular y requerimientos técnicos de tuplas, diccionarios, excepciones, strings y menú, evaluados con la rúbrica de la sección 7, más el documento anexo con capturas. *(Ajustado de 80 a 70 pts para ceder espacio al nuevo criterio obligatorio de la sección 5.)* |
| **Ejercicios extras evaluables (Jupyter)** | **15 pts** | Resolución de los 4 ejercicios extras de la sección 4 en el Notebook `extras_semana5.ipynb` con celdas Markdown de explicación. |
| **Desafíos extras de refuerzo (OBLIGATORIOS)** | **10 pts** | Resolución de los 5 desafíos de la sección 5 dentro del mismo Notebook `extras_semana5.ipynb`. **Entrega obligatoria** — no se consideran opcionales pese a su origen como material autoevaluable. |
| **Uso de Git y GitHub** | **5 pts** | Repositorio público con estructura de carpetas estandarizada e historial mínimo de **3 commits significativos** con mensajes profesionales. |
| **Total semanal** | **100 pts** | |

---

## 7. Rúbrica de evaluación (100 puntos)

> Los sub-criterios de la actividad principal se redujeron proporcionalmente de 80 a 70 puntos para ceder los 10 puntos que ahora ocupan, de forma obligatoria, los "Desafíos extras de refuerzo" de la sección 5.

| Criterio | Puntos | Excelente (100%) | Bueno (75%) | Regular (50%) | Insuficiente (0%) |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Código fuente en Python (.py)** | 12 | Código funcional, libre de errores, correctamente formateado y con funciones modulares coherentes con el menú. | Código funcional con detalles menores de estilo o formato. | Código con errores de ejecución o que no cumple todos los módulos. | No incluye código o no funciona. |
| **Uso de tuplas** | 12 | Cumple los 5 requerimientos: tupla `numeros` (5+), tercer elemento, dos números con `input()` en nueva tupla, conversión a lista ordenada y función que suma y retorna. | Cumple 4 de 5 requerimientos. | Cumple 2-3 requerimientos. | Cumple 1 o ninguno. |
| **Uso de diccionarios** | 10 | Cumple los 4 requerimientos: diccionario `contactos` (3+), adición de contacto por consola, iteración de claves con nombres y función que retorna el teléfono. | Cumple 3 de 4 requerimientos. | Cumple 2 requerimientos. | Cumple 1 o ninguno. |
| **Uso de excepciones** | 9 | Cumple los 3 requerimientos: dos enteros, `try-except` con mensaje controlado y bloque específico `ZeroDivisionError`. | Cumple 2 de 3 requerimientos. | Cumple 1 requerimiento. | No implementa excepciones. |
| **Uso de strings** | 10 | Cumple los 5 requerimientos: variable `mensaje`, `len()`, mayúsculas, `replace()` y función que cuenta palabras. | Cumple 4 de 5 requerimientos. | Cumple 2-3 requerimientos. | Cumple 1 o ninguno. |
| **Menú principal interactivo** | 9 | Menú con ciclo controlado, 5 opciones numéricas, llamadas modulares a funciones y finalización correcta del programa. | Menú funcional con detalles menores (mensajes o formato). | Menú incompleto o con opciones que no llaman a las funciones. | No incluye menú. |
| **Documento anexo con capturas** | 8 | Capturas nítidas de las 5 opciones del menú y de la activación de las excepciones, correctamente ordenadas y etiquetadas. | Capturas completas con detalles menores de orden o nitidez. | Capturas incompletas o sin etiquetar. | No incluye documento anexo. |
| **Ejercicios extras evaluables (Jupyter)** | 15 | Los 4 ejercicios de la sección 4 resueltos correctamente con explicaciones en Markdown. | 4 ejercicios con errores menores, o 3 resueltos correctamente. | 2 ejercicios resueltos correctamente. | 1 o ningún ejercicio resuelto. |
| **Desafíos extras de refuerzo — OBLIGATORIOS** | 10 | Los 5 desafíos de la sección 5 resueltos correctamente, con código funcional y explicación breve de cada uno. | 4 de los 5 desafíos resueltos correctamente. | 2-3 desafíos resueltos correctamente. | 1 o ningún desafío resuelto — al ser de **entrega obligatoria**, la ausencia total se reporta adicionalmente como incumplimiento de entrega. |
| **Git y GitHub** | 5 | Repositorio público, estructura de carpetas estandarizada y al menos 3 commits con mensajes profesionales. | Repositorio público con 3 commits pero mensajes poco descriptivos o estructura irregular. | Repositorio con menos de 3 commits. | No entrega liga del repositorio. |
| **TOTAL** | **100** | | | | |

---

## 8. Lista de entregables y fechas

| Entregable | Archivo | Formato | Fecha límite | ¿Obligatorio? |
| :--- | :--- | :--- | :--- | :---: |
| Código fuente de la actividad | `actividad4_menu_modular.py` | Python (.py) | Viernes por la noche | Sí |
| Documento anexo de capturas | `actividad4_capturas.docx` | Word (.docx) | Viernes por la noche | Sí |
| Ejercicios extras evaluables (4) + Desafíos extras de refuerzo (5) | `extras_semana5.ipynb` (9 ejercicios en total) | Jupyter Notebook (.ipynb) | Viernes por la noche | **Sí — los 9 ejercicios son de entrega obligatoria** |
| Repositorio | Liga pública de GitHub | URL | Viernes por la noche | Sí |

**Nota de entrega:** Los entregables deben subirse al repositorio personal del estudiante (con estructura de carpetas por semana: `semana5/`, etc.) y la liga del repositorio se entrega como evidencia de la actividad. El Notebook `extras_semana5.ipynb` debe incluir, en orden, los 4 ejercicios extras evaluables originales seguidos de los 5 desafíos de refuerzo, ahora de carácter obligatorio.
