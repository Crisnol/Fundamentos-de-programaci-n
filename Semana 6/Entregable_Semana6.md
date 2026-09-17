# ENTREGABLE SEMANA 6 — DIVISIÓN 50/50

**Curso:** Solución de problemas con programación computacional  
**Semana:** 6 · Repaso integral (Temas 1 al 16)  
**Ponderación:** 100% (dividido en dos componentes iguales)  
**Fecha límite:** 18 de septiembre de 2026 (Periodo I) · 20 de noviembre de 2026 (Periodo II)

---

## 1. Componente A — Certificación Cisco Networking Academy (50%)

**Descripción:** Evidencia de la acreditación oficial en la plataforma Cisco Skills for All.

**Qué entregar:**
- Captura de pantalla de la **bitácora de avance** del curso *Fundamentos de Python 1* (*Python Essentials 1*), mostrando el progreso completado en lecturas, ejercicios interactivos y laboratorios.
- Captura de pantalla de la **calificación oficial aprobatoria** del examen *CISCO Fundamentos de Python 1 - Examen de Sección*.
- Captura de pantalla de la **insignia digital** obtenida (junto con el nombre del estudiante).

**Rúbrica (50 puntos máximo):**

| Criterio | Puntos | Excelente (100%) | Bueno (75%) | Regular (50%) | Insuficiente (0%) |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Bitácora de avance** | 15 | Captura nítida que demuestra la totalidad de lecturas, ejercicios y laboratorios completados. | Captura con mayoría de módulos completados (1-2 pendientes). | Captura de avance parcial (varios módulos pendientes). | No presenta captura de bitácora. |
| **Calificación oficial** | 20 | Calificación aprobatoria claramente visible y legible. | Calificación aprobatoria visible pero con captura de baja nitidez. | Calificación visible sin acreditar (reprobatoria) o captura confusa. | No presenta evidencia del examen. |
| **Insignia digital** | 15 | Insignia de *Python Essentials 1* claramente visible y asociada al nombre. | Insignia visible con detalles menores de nitidez o recorte. | Insignia poco legible o no asociada al estudiante. | No presenta la insignia. |

---

## 2. Componente B — Ejercicios de Repaso Integral en Python (50%)

**Descripción:** Ejecución y entrega de los **25 ejercicios de repaso del `Ejercicios_Semana6.md`**, resueltos **100% en Python**, en un Jupyter Notebook y subidos al repositorio.

**Nota de actualización:** Los primeros ejercicios del archivo original basados en PSeInt (pseudocódigo) y en análisis teórico fueron **reemplazados por ejercicios de programación en Python**, de forma que el 100% de los entregables requieran código Python ejecutable.

**Qué entregar:**
- Enlace al repositorio GitHub con el notebook (`Entregable_Semana6.ipynb` o similar) que contenga las soluciones a los 25 ejercicios.
- Cada ejercicio debe incluir: enunciado, código Python ejecutado y salida esperada coincidiendo con la del enunciado.

---

## 3. Los 25 Ejercicios (100% Python)

### BLOQUE 1 · TEMAS 1 Y 2: ALGORITMOS Y MODELO EPS

#### Ejercicio 1: Área de un triángulo
Escribe un programa en Python que aplique el modelo Entrada-Proceso-Salida para calcular el área de un triángulo (`area = (base * altura) / 2`), usando `input()`, `float()` y `print()`.
**Entrada:** `base = 8`, `altura = 5`
**Salida:** `El área del triángulo es: 20.0`

#### Ejercicio 2: Conversión de Celsius a Fahrenheit
Escribe un programa en Python que pida una temperatura en grados Celsius y la convierta a Fahrenheit (`F = C * 9/5 + 32`).
**Entrada:** `celsius = 30`
**Salida:** `30 grados Celsius equivalen a 86.0 grados Fahrenheit`

#### Ejercicio 3: Interés simple (antes en PSeInt)
Escribe un programa en Python que pida capital, tasa y tiempo, y calcule el interés simple (`interes = capital * (tasa / 100) * tiempo`).
**Entrada:** `capital = 2000`, `tasa = 6`, `tiempo = 2`
**Salida:** `El interés simple es: 240.0`

### BLOQUE 2 · TEMAS 3 Y 4: VARIABLES, OPERADORES Y ENTRADA/SALIDA

#### Ejercicio 4: Precedencia de operadores (antes de análisis teórico)
Escribe un programa en Python que calcule `4 * 3 + 10 // 3 - 8 % 5`, muestre el resultado y **imprima el orden de evaluación aplicado** (`12 + 3 - 3`).
**Salida:**
```
4 * 3 + 10 // 3 - 8 % 5 = 12 + 3 - 3 = 12
```

#### Ejercicio 5: Casting tras `input()` (antes de análisis teórico)
Escribe un programa en Python que pida un número con `input()`, demuestre que devuelve `str` (`type()`), intente `x + 1` dentro de `try-except` capturando `TypeError`, y finalmente haga `int(x)` para sumar y obtener el resultado correcto.
**Entrada:** `"25"`
**Salida:** `x es tipo str`, `x + 1 genera TypeError`, `int(x) + 1 = 26`

#### Ejercicio 6: Conversión de horas a segundos
Crea un programa que pida una cantidad de horas (`float`) y la convierta a segundos (1 hora = 3600 segundos), mostrando el resultado formateado.
**Entrada:** `3`
**Salida:** `3 horas equivalen a 10800 segundos`

#### Ejercicio 7: Descuento del 15% con f-strings
Crea un programa que pida el precio de un artículo y aplique un 15% de descuento, mostrando el monto del descuento y el precio final con dos decimales usando f-strings.
**Entrada:** `460`
**Salida:**
```
Descuento (15%): $69.00
Precio final: $391.00
```

### BLOQUE 3 · TEMAS 5, 6, 7 Y 8: DECISIONES, CICLOS Y DEBUGGING

#### Ejercicio 8: Número par o impar
**Entrada:** `17` → **Salida:** `17 es un número impar`

#### Ejercicio 9: Mayor de tres números
**Entrada:** `12`, `45`, `23` → **Salida:** `El mayor de los tres números es: 45`

#### Ejercicio 10: Suma acumulada con `while`
Pide números mientras sean distintos de `0` (el `0` termina el ciclo y no se suma).
**Entrada:** `5`, `8`, `2`, `0` → **Salida:** `La suma de los números es: 15`

#### Ejercicio 11: Tabla de multiplicar con `for`
**Entrada:** `6` → **Salida:** tabla del 6 del `6 x 1 = 6` al `6 x 10 = 60`

#### Ejercicio 12: Suma de pares del 1 al 20 con `for` y `continue`
**Salida:** `La suma de los números pares del 1 al 20 es: 110`

### BLOQUE 4 · TEMAS 9, 10, 11 Y 12: LISTAS, MATRICES Y FUNCIONES

#### Ejercicio 13: Suma de una lista con función que regresa valor (sin `sum()`)
**Entrada:** `[10, 20, 30, 40]` → **Salida:** `La suma de los elementos es: 100`

#### Ejercicio 14: Máximo de una lista con función que regresa valor (sin `max()`)
**Entrada:** `[7, 3, 9, 2]` → **Salida:** `El elemento máximo es: 9`

#### Ejercicio 15: Matriz y suma de la diagonal principal
**Entrada:** `[[1,2,3],[4,5,6],[7,8,9]]` → **Salida:** `La suma de la diagonal principal es: 15`

#### Ejercicio 16: Promedio con función que no regresa valor
**Entrada:** `[8, 9, 10, 7]` → **Salida:** `El promedio es: 8.50`

#### Ejercicio 17: Invertir una lista con slicing
**Entrada:** `[1, 2, 3, 4, 5]` → **Salida:** `Lista invertida: [5, 4, 3, 2, 1]`

#### Ejercicio 18: Factorial con función recursiva
**Entrada:** `5` → **Salida:** `El factorial de 5 es: 120`

### BLOQUE 5 · TEMAS 13, 14, 15 Y 16: TUPLAS, DICCIONARIOS, EXCEPCIONES Y STRINGS

#### Ejercicio 19: Tupla: acceso y suma con función
**Entrada:** `(4, 8, 15, 16, 23, 42)` → **Salida:**
```
El tercer elemento es: 15
La suma de la tupla es: 108
```

#### Ejercicio 20: Diccionario: buscar teléfono de un contacto
**Entrada:** `Beto` → **Salida:** `El teléfono de Beto es: 5555678`

#### Ejercicio 21: Diccionario de calificaciones y promedios
**Entrada:** `{"Ana": [8, 9, 10], "Beto": [7, 7, 8]}` → **Salida:**
```
Ana: 9.00
Beto: 7.33
```

#### Ejercicio 22: Excepción de división entre cero
**Entrada:** `10`, `0` → **Salida:** `Error: No se puede dividir entre cero.`

#### Ejercicio 23: Excepción de valor no numérico
**Entrada:** `"abc"` → **Salida:** `Error: Debes ingresar un número entero.`

#### Ejercicio 24: Contar palabras de un string
**Entrada:** `"Python es un lenguaje de programacion"` → **Salida:** `El mensaje tiene 6 palabras.`

#### Ejercicio 25: Longitud, mayúsculas y reemplazo de un string
**Entrada:** `"aprende python"` → **Salida:**
```
Longitud: 14
En mayúsculas: APRENDE PYTHON
Reemplazo: aprende programacion
```

---

## 4. Rúbrica del Componente B (50 puntos máximo)

| Criterio | Puntos | Excelente (100%) | Bueno (75%) | Regular (50%) | Insuficiente (0%) |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Cobertura de ejercicios** | 20 | Los 25 ejercicios están completos y resueltos **100% en Python**. | 20-24 ejercicios completos y correctos. | 15-19 ejercicios completos. | Menos de 15 ejercicios o mayoría incorrectos. |
| **Calidad del código** | 10 | Código limpio, bien estructurado, con nombres descriptivos y sin PSeInt/pseudocódigo. | Código funcional con mínima falta de estilo. | Código funcional pero desordenado o con comentarios ausentes. | Código que no ejecuta o con errores lógicos mayores. |
| **Coincidencia de salidas** | 10 | **Todas** las salidas coinciden con las esperadas en los enunciados. | La mayoría de salidas coinciden (20/25). | Algunas salidas coinciden, otras no. | Ninguna salida coincide o no se entregan salidas. |
| **Entrega en repositorio** | 10 | Enlace público al repositorio con notebook organizado y nombrado correctamente. | Enlace funcional pero estructura básica. | Enlace roto o notebook en formato incorrecto. | No se entrega repositorio o enlace inválido. |

---

## 5. Consideraciones Generales

- **Entrega:** Documento de reporte (`Entregable_Semana6.md`) y notebook de ejercicios subidos al repositorio personal (carpeta `semana6/`) con liga pública de GitHub.
- **Ponderación total:** 50% Certificación Cisco + 50% Ejercicios de repaso en Python = 100%.
- **Nota:** Los 50% del Componente B (ejercicios) reemplazan a los 20 puntos que la agenda original destinaba a la calidad documental, otorgando peso evaluable a los ejercicios de repaso (antes no evaluables).
- **Importante:** Esta semana **no hay ejercicios extra evaluables adicionales**. El total semanal se divide exactamente a la mitad: 50% certificación Cisco y 50% ejercicios de repaso en Python.