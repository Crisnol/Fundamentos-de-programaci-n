# ACTIVIDAD EVALUABLE 1 — CALCULADORA DE TIEMPO DIGITAL

**Curso:** Solución de problemas con programación computacional
**Semana:** 1 · Temas 1 al 4
**Ponderación:** 6% de la calificación total del curso
**Fechas límite:** 14 de agosto de 2026 (Periodo I) · 16 de octubre de 2026 (Periodo II)
**Entrega:** Viernes por la noche

---

## 1. Descripción del reto

Desarrollar una **calculadora interactiva en Python** que permita registrar el tiempo diario (en horas o fracciones de hora) que una persona dedica a distintas plataformas digitales: redes sociales, mensajería, servicios de streaming, videojuegos, entre otras. El programa debe capturar los datos, procesarlos y mostrar un resumen claro y ordenado de los resultados.

Este reto integra el modelo **Entrada-Proceso-Salida** (Tema 1), la lógica algorítmica en **pseudocódigo y PSeInt** (Tema 2), el uso correcto de **variables, tipos de datos y operadores** (Tema 3) y las **entradas y salidas simples** con `input()`, `print()` y conversión de tipos (Tema 4).

---

## 2. Requerimientos técnicos obligatorios

1. **Nombre del usuario:** Solicitar el nombre del usuario mediante la función `input()`.
2. **Mínimo cinco plataformas:** Solicitar el tiempo diario dedicado a **al menos cinco** plataformas digitales diferentes (ej. redes sociales, mensajería, streaming, videojuegos, estudio en línea).
3. **Tiempos parciales:** Emplear la función `float()` para permitir el ingreso de tiempos parciales (ej. `1.5` horas).
4. **Tiempo total:** Calcular la suma del tiempo total diario invertido en actividades digitales.
5. **Porcentaje del día:** Calcular el porcentaje del día (24 horas) utilizado en actividades digitales mediante la fórmula:
   `porcentaje = (tiempo_total / 24) * 100`
6. **Salida ordenada:** Mostrar en pantalla, de forma ordenada y formateada (f-strings), el **nombre del usuario**, el **tiempo total acumulado** y el **porcentaje calculado**.

---

## 3. Estructura del entregable principal (80%)

Un **documento formal en formato Word (.docx)** que contenga las siguientes cuatro secciones:

| # | Sección | Detalle |
| :---: | :--- | :--- |
| 1 | **Algoritmo lógico** | Estructura del problema paso a paso en lenguaje natural (modelo Entrada-Proceso-Salida). |
| 2 | **Pseudocódigo** | Pseudocódigo formal diseñado y probado en **PSeInt**. |
| 3 | **Diagrama de flujo** | Diagrama de flujo del flujo lógico **exportado desde PSeInt** (imagen o captura). |
| 4 | **Código fuente** | Código fuente en Python correspondiente, funcionando de forma correcta. |

---

## 4. Estrategia de evaluación semanal (80/20)

| Componente | Puntos | Descripción |
| :--- | :---: | :--- |
| **Actividad oficial (documento Word)** | **80 pts** | Algoritmo, pseudocódigo, diagrama de flujo y código Python, evaluados con la rúbrica de la sección 6. |
| **Ejercicios extras en Jupyter** | **15 pts** | Resolución de los 4 ejercicios extras de la sección 5 en un Notebook `.ipynb` con celdas Markdown de explicación. |
| **Uso de Git y GitHub** | **5 pts** | Repositorio público con estructura de carpetas estandarizada e historial mínimo de **3 commits significativos** con mensajes profesionales. |
| **Total semanal** | **100 pts** | |

---

## 5. Ejercicios extras evaluables (15 puntos)

Resuelve los siguientes 4 ejercicios en un Jupyter Notebook (`extras_semana1.ipynb`). Para cada uno documenta en una celda Markdown el procedimiento y el modelo EPS aplicado.

### Extra 1: División de cuenta con propina
**Enunciado:** Crea un programa que pida el total de la cuenta de un restaurante, el porcentaje de propina a dejar y el número de personas que pagarán. El programa debe calcular el monto de la propina, el total a pagar con propina y cuánto le toca pagar a cada persona (con dos decimales).
**Entrada:**
```
Total de la cuenta: 250
Porcentaje de propina: 15
Número de personas: 4
```
**Salida:**
```
Propina: $37.50
Total con propina: $287.50
Pago por persona: $71.88
```

---

### Extra 2: Conversor de minutos a días, horas y minutos
**Enunciado:** Crea un programa que pida una cantidad total de minutos (entero) y la convierta a días, horas y minutos restantes. Utiliza los operadores de división entera `//` y módulo `%`. (Pista: 1 día = 1440 minutos, 1 hora = 60 minutos.)
**Entrada:**
```
Total de minutos: 1500
```
**Salida:**
```
1500 minutos = 1 día(s), 1 hora(s), 0 minuto(s)
```

---

### Extra 3: Calificación final ponderada
**Enunciado:** Crea un programa que pida las calificaciones de tres parciales (valores de 0 a 10) y calcule la calificación final considerando una ponderación de **30%, 30% y 40%** respectivamente. Muestra el resultado con dos decimales.
**Entrada:**
```
Parcial 1 (30%): 8
Parcial 2 (30%): 9
Parcial 3 (40%): 7
```
**Salida:**
```
Tu calificación final es: 7.90
```

---

### Extra 4: Conversor de moneda (MXN a USD y EUR)
**Enunciado:** Crea un programa que pida una cantidad en pesos mexicanos y los tipos de cambio del dólar (USD) y del euro (EUR). Debe calcular y mostrar las equivalencias redondeadas a dos decimales. (Fórmula: `cantidad / tipo_de_cambio`.)
**Entrada:**
```
Cantidad en MXN: 1000
Tipo de cambio USD: 18.50
Tipo de cambio EUR: 21.00
```
**Salida:**
```
$1000.00 MXN equivalen a:
USD: 54.05
EUR: 47.62
```

---

## 6. Rúbrica de evaluación (100 puntos)

| Criterio | Puntos | Excelente (100%) | Bueno (75%) | Regular (50%) | Insuficiente (0%) |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Algoritmo lógico estructurado** | 12 | Pasos claros, completos y en orden lógico; modelo EPS identificado correctamente. | Pasos completos con pequeños errores de orden o redacción. | Algoritmo incompleto o desordenado. | No incluye algoritmo. |
| **Pseudocódigo en PSeInt** | 12 | Pseudocódigo correcto, sin errores de sintaxis y probado en PSeInt. | Pseudocódigo correcto con errores menores de sintaxis. | Pseudocódigo con errores que impiden su ejecución. | No incluye pseudocódigo. |
| **Diagrama de flujo (PSeInt)** | 12 | Diagrama completo, correcto y exportado de PSeInt. | Diagrama correcto con detalles menores ausentes. | Diagrama incompleto o con errores de flujo. | No incluye diagrama. |
| **Código fuente en Python** | 24 | Código funcional, libre de errores, correctamente formateado y coherente con los demás entregables. | Código funcional con detalles menores de estilo o formato. | Código con errores de ejecución o que no cumple todos los requerimientos. | No incluye código o no funciona. |
| **Requerimientos técnicos (6 puntos del reto)** | 20 | Cumple los 6 requerimientos: `input()`, 5+ plataformas, `float()`, suma total, porcentaje y salida ordenada. | Cumple 4-5 requerimientos. | Cumple 2-3 requerimientos. | Cumple 1 o ninguno. |
| **Ejercicios extras (Jupyter)** | 15 | 4 ejercicios resueltos correctamente con explicaciones en Markdown. | 4 ejercicios con errores menores, o 3 resueltos correctamente. | 2 ejercicios resueltos correctamente. | 1 o ningún ejercicio resuelto. |
| **Git y GitHub** | 5 | Repositorio público, estructura de carpetas estandarizada y al menos 3 commits con mensajes profesionales. | Repositorio público con 3 commits pero mensajes poco descriptivos o estructura irregular. | Repositorio con menos de 3 commits. | No entrega liga del repositorio. |
| **TOTAL** | **100** | | | | |

---

## 7. Lista de entregables y fechas

| Entregable | Archivo | Formato | Fecha límite |
| :--- | :--- | :--- | :--- |
| Reporte de la actividad | `CalculadoraTiempoDigital.docx` | Word (.docx) | Viernes por la noche |
| Ejercicios extras | `extras_semana1.ipynb` | Jupyter Notebook (.ipynb) | Viernes por la noche |
| Repositorio | Liga pública de GitHub | URL | Viernes por la noche |

**Nota de entrega:** Los tres entregables deben subirse al repositorio personal del estudiante (con estructura de carpetas por semana: `semana1/`, `semana2/`, etc.) y la liga del repositorio se entrega como evidencia de la actividad.
