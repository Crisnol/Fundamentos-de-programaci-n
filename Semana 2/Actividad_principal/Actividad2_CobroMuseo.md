# ACTIVIDAD EVALUABLE 2 — COBRO DE ENTRADAS DEL MUSEO CON RESTRICCIONES DE CONTROL

**Curso:** Solución de problemas con programación computacional
**Semana:** 2 · Temas 5 al 8
**Ponderación:** 6% de la calificación total del curso
**Fechas límite:** 21 de agosto de 2026 (Periodo I) · 23 de octubre de 2026 (Periodo II)
**Entrega:** Viernes por la noche

---

## 1. Descripción del reto

Desarrollar un programa en **Python** para cobrar las entradas de los visitantes que desean recorrer el **Museo de Antropología e Historia**, calculando el precio adecuado para cada visitante y aplicando descuentos por tipo de visitante bajo estrictas condiciones lógicas. El programa debe procesar a los visitantes mediante un **ciclo controlado**, aplicar los descuentos con una **tabla de verdad** que garantice un único descuento por boleto y desplegar el **total detallado** de todas las personas ingresadas.

**Precios base de entrada:**
| Tipo de visitante | Precio |
| :--- | :---: |
| Niños menores de 3 años | Gratis ($0) |
| Menores de edad (de 3 a 17 años) | $30 |
| Mayores de 18 años | $45 |

**Tabla de descuentos oficial:**
| Tipo de visitante | Descuento |
| :--- | :---: |
| Adulto mayor | 12% |
| Profesor | 10% |
| Estudiante | 10% |

Este reto integra las **estructuras de decisión** `if/elif/else` y los operadores lógicos (Tema 5), el **ciclo `while`** con `break` y `continue` (Tema 6), la **depuración con PDB** para garantizar un código libre de errores (Tema 7) y el **ciclo `for`** con acumuladores y procesamiento repetitivo (Tema 8).

---

## 2. Requerimientos técnicos obligatorios

1. **Captura de visitantes:** El usuario debe poder ingresar el número total de visitantes que pagarán boleto, si son mayores de edad y el tipo de visitante de cada uno.
2. **Tabla de verdad de descuentos:** La matriz de descuentos debe estar estructurada lógicamente como una **tabla de verdad**, de modo que **solo se aplique un tipo de descuento por boleto** (adulto mayor 12%, profesor 10%, estudiante 10%).
3. **Ciclo controlado:** Se debe implementar un ciclo controlado (`for` o `while`) para procesar a los visitantes.
4. **`break` y `continue` obligatorios:** Dentro del ciclo es obligatorio el uso de **al menos una cláusula `break`** y **al menos una cláusula `continue`**.
5. **Total detallado:** El programa debe desplegar el total detallado a pagar de todas las personas ingresadas, considerando sus descuentos aplicables **de forma individual**.

---

## 3. Estructura del entregable (80%)

Un **archivo de código fuente ejecutable con extensión `.py`** libre de errores. Se recomienda la siguiente organización interna:

| # | Sección | Detalle |
| :---: | :--- | :--- |
| 1 | **Encabezado y constantes** | Comentarios iniciales (nombre, matrícula, fecha), precio base por edad y porcentajes de descuento como constantes. |
| 2 | **Captura del número de visitantes** | `input()` con conversión a entero del total de visitantes a procesar. |
| 3 | **Ciclo de procesamiento** | Ciclo `for` o `while` que recorre a cada visitante, capturando edad y tipo. Uso obligatorio de `break` y `continue`. |
| 4 | **Tabla de verdad de descuentos** | Estructura `if/elif/else` con operadores lógicos que garantiza un solo descuento por boleto. |
| 5 | **Totales y salida detallada** | Acumulador del total general, detalle del subtotal por visitante, monto de descuento y total final formateado con f-strings. |

**Nombre sugerido del archivo:** `CobroEntradasMuseo.py`

---

## 4. Estrategia de evaluación semanal (80/20)

| Componente | Puntos | Descripción |
| :--- | :---: | :--- |
| **Actividad oficial (archivo .py)** | **80 pts** | Programa ejecutable libre de errores que cumple los 5 requerimientos técnicos, evaluado con la rúbrica de la sección 6. |
| **Ejercicios extras en Jupyter** | **15 pts** | Resolución de los 4 ejercicios extras de la sección 5 en un Notebook `.ipynb` con celdas Markdown de explicación. |
| **Uso de Git y GitHub** | **5 pts** | Repositorio público con estructura de carpetas estandarizada e historial mínimo de **3 commits significativos** con mensajes profesionales. |
| **Total semanal** | **100 pts** | |

---

## 5. Ejercicios extras evaluables (15 puntos)

Resuelve los siguientes 4 ejercicios en un Jupyter Notebook (`extras_semana2.ipynb`). Para cada uno documenta en una celda Markdown el procedimiento y el planteamiento lógico aplicado (decisión, repetición o depuración).

### Extra 1: Control de aforo con break y continue (while)
**Enunciado:** Crea un programa que procese visitantes del museo con un ciclo `while`. Por cada visitante se captura el costo de su boleto ($0 para menores de 3 años, $30 para 3 a 17 años, $45 para mayores de 18). Si el boleto es gratis, muestra "Menor de 3 años, sin cargo" y continúa con el siguiente visitante (usa `continue`). Si el total acumulado alcanza o supera $100, detén el ciclo con `break` y muestra el total.
**Entrada:**
```
Costo del boleto 1: 45
Costo del boleto 2: 0
Costo del boleto 3: 30
Costo del boleto 4: 45
```
**Salida:**
```
Menor de 3 años, sin cargo
Aforo alcanzado, se detiene el registro
Total acumulado: $120.00
```

---

### Extra 2: Estadística de visitantes con for
**Enunciado:** Crea un programa que pida el número total de visitantes y, con un ciclo `for`, capture la edad de cada uno. Debe contar cuántos son adultos (18 años o más) y calcular el promedio de edad de todos los visitantes, mostrando ambos resultados con dos decimales.
**Entrada:**
```
Número de visitantes: 4
Edad del visitante 1: 30
Edad del visitante 2: 45
Edad del visitante 3: 15
Edad del visitante 4: 2
```
**Salida:**
```
Adultos: 2
Promedio de edad: 23.00
```

---

### Extra 3: Depuración de un cobro con PDB
**Enunciado:** El siguiente código pretende calcular el precio final de un boleto de $45 con el descuento del adulto mayor (12%) pero contiene un error de lógica. Inserta `pdb.set_trace()` para rastrear las variables, identifica el error y escribe la versión corregida.
```python
precio = 45
descuento = 12
total = precio - descuento
print(f"Total: ${total:.2f}")
```
**Entrada:** Ninguna (código dado para depurar).
**Salida:**
```
Error de lógica: descuento debe ser el porcentaje 0.12, no 12.
Código corregido: descuento = precio * 0.12 -> Total: $39.60
```

---

### Extra 4: Pirámide de asteriscos con for
**Enunciado:** Crea un programa que pida la altura de una pirámide y la dibuje con asteriscos usando ciclos `for` anidados y el parámetro `end` de `print`.
**Entrada:**
```
Altura de la pirámide: 4
```
**Salida:**
```
*
**
***
****
```

---

## 6. Rúbrica de evaluación (100 puntos)

| Criterio | Puntos | Excelente (100%) | Bueno (75%) | Regular (50%) | Insuficiente (0%) |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Precios base por edad** | 15 | Calcula correctamente $0, $30 y $45 según la edad de cada visitante. | Precios correctos con errores menores de formato o de redondeo. | Errores en una de las tres categorías de precio. | No aplica los precios base o los aplica mal. |
| **Tabla de verdad de descuentos** | 20 | Solo se aplica un descuento por boleto (adulto mayor 12%, profesor 10%, estudiante 10%) usando operadores lógicos. | Descuentos correctos con estructura poco clara u orden incorrecto. | Se aplican descuentos duplicados o incorrectos en algunos casos. | No implementa descuentos ni tabla de verdad. |
| **Ciclo controlado (`for` o `while`)** | 20 | Ciclo correcto que procesa a todos los visitantes con `break` y `continue` obligatorios usados con sentido. | Ciclo funcional pero con `break` o `continue` innecesarios o mal ubicados. | Usa solo `break` o solo `continue`. | No implementa ciclo ni las cláusulas obligatorias. |
| **Total detallado y acumulador** | 15 | Despliega el subtotal, el descuento y el total de cada visitante, y el total general correcto. | Total general correcto con detalle individual incompleto. | Total con errores de acumulación. | No muestra totales o el acumulado es incorrecto. |
| **Código libre de errores y calidad** | 10 | Código depurado, sin errores, con comentarios y formato profesional. | Código funcional con detalles menores de estilo. | Código con errores de ejecución en casos límite. | Código que no ejecuta o no funciona. |
| **Ejercicios extras (Jupyter)** | 15 | 4 ejercicios resueltos correctamente con explicaciones en Markdown. | 4 ejercicios con errores menores, o 3 resueltos correctamente. | 2 ejercicios resueltos correctamente. | 1 o ningún ejercicio resuelto. |
| **Git y GitHub** | 5 | Repositorio público, estructura de carpetas estandarizada y al menos 3 commits con mensajes profesionales. | Repositorio público con 3 commits pero mensajes poco descriptivos o estructura irregular. | Repositorio con menos de 3 commits. | No entrega liga del repositorio. |
| **TOTAL** | **100** | | | | |

---

## 7. Lista de entregables y fechas

| Entregable | Archivo | Formato | Fecha límite |
| :--- | :--- | :--- | :--- |
| Código fuente de la actividad | `CobroEntradasMuseo.py` | Python (.py) | Viernes por la noche |
| Ejercicios extras | `extras_semana2.ipynb` | Jupyter Notebook (.ipynb) | Viernes por la noche |
| Repositorio | Liga pública de GitHub | URL | Viernes por la noche |

**Nota de entrega:** Los tres entregables deben subirse al repositorio personal del estudiante (con estructura de carpetas por semana: `semana1/`, `semana2/`, etc.) y la liga del repositorio se entrega como evidencia de la actividad. La fecha límite es el **21 de agosto de 2026** (Periodo I) o el **23 de octubre de 2026** (Periodo II), según el periodo de clases del estudiante.
