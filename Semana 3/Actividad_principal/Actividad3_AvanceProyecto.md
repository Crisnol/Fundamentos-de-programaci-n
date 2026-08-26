# ACTIVIDAD EVALUABLE 3 — AVANCE DEL RETO/PROYECTO (FASE I)

**Curso:** Solución de problemas con programación computacional
**Semana:** 3 · Integración de los Temas 1 al 8
**Ponderación:** 25% de la calificación total del curso
**Fechas límite:** 28 de agosto de 2026 (Periodo I) · 30 de octubre de 2026 (Periodo II)
**Entrega:** Viernes por la noche

---

## 1. Descripción del avance

En la Semana 3 se entrega el **Avance del Reto/Proyecto (Fase I)** de la agenda oficial del curso (sección 4). Su objetivo es **diseñar la arquitectura conceptual, las reglas de negocio e implementar la lógica base** de la solución técnica para resolver una problemática real identificada en un área organizacional.

Esta semana **no introduce temas nuevos**: se integran los **Temas 1 al 8** vistos en las dos primeras semanas:

| Tema | Concepto integrado en el avance |
| :---: | :--- |
| 1 | Algoritmos y modelo Entrada-Proceso-Salida (EPS). |
| 2 | Pseudocódigo y diagrama de flujo con PSeInt. |
| 3 | Variables, tipos de datos y operadores. |
| 4 | Entradas y salidas simples (`input()`, `print()`, casting). |
| 5 | Estructuras de decisión (`if`, `elif`, `else`). |
| 6 | Estructura de repetición `while` (menús y acumuladores). |
| 7 | *Debugging* con PDB para depurar el prototipo. |
| 8 | Estructura de repetición `for` (recorridos conocidos). |

---
## 2. Los 8 requerimientos técnicos obligatorios (agenda sección 4)

| # | Requerimiento | Especificación exacta |
| :---: | :--- | :--- |
| 1 | **Análisis Organizacional** | Identificar una empresa u organización real, seleccionar un área específica de impacto operativo y describir sus necesidades. |
| 2 | **Definición del Problema** | Formular con precisión la problemática técnica a resolver y delimitar las **reglas de negocio** (cómo opera actualmente el área y bajo qué restricciones). |
| 3 | **Listado de Requerimientos** | Detallar los requerimientos funcionales que el software debe realizar para solucionar el problema. |
| 4 | **Clasificación de Datos** | Identificar y documentar los tipos de datos requeridos por la solución (enteros, flotantes, cadenas, booleanos). |
| 5 | **Operadores del Lenguaje** | Identificar y justificar los operadores matemáticos, relacionales y lógicos que serán clave en el código. |
| 6 | **Estructuras de Control** | Enumerar las estructuras condicionales (ej. `if-else`) e iterativas (ej. `while`, `for`) que dirigirán el flujo del programa. |
| 7 | **Diseño Algorítmico** | Elaborar el diagrama de flujo detallado en **PSeInt** con el flujo de trabajo funcional y exportar el **pseudocódigo formal** de trabajo. |
| 8 | **Prototipo de Código** | Desarrollar la versión inicial (prototipo ejecutable) en Python que refleje la lógica base y corra de forma correcta en consola. |

---

## 3. Estructura del entregable principal (80%)

El entregable principal es un **documento formal en formato Word (.docx)** que contenga las siguientes secciones:

| # | Sección del documento | Contenido |
| :---: | :--- | :--- |
| 1 | **Análisis técnico** | Desarrollo de los requerimientos 1 al 6: análisis organizacional, definición del problema con reglas de negocio, listado de requerimientos, clasificación de datos, operadores del lenguaje y estructuras de control. |
| 2 | **Pseudocódigo** | Pseudocódigo formal de trabajo (Requerimiento 7), probado en **PSeInt**. |
| 3 | **Diagrama de flujo** | Imagen del diagrama de flujo detallado **exportado desde PSeInt** (Requerimiento 7). |
| 4 | **Prototipo de código** | Archivo ejecutable inicial de Python en un archivo **`.py`** (Requerimiento 8), que refleje la lógica base y corra correctamente en consola. |

**Estructura de carpetas sugerida en el repositorio** (según la guía de entregas del curso):

```text
fundamentos-de-programacion/
└── semana-3/
    └── avance-proyecto/
        ├── reporte_avance.docx      <-- Documento Word con los 8 requerimientos
        ├── diagrama_flujo.png       <-- Imagen del diagrama de flujo (PSeInt)
        └── prototipo_inicial.py     <-- Prototipo ejecutable de Python
```

---

## 4. Estrategia de evaluación semanal (80/20)

| Componente | Puntos | Descripción |
| :--- | :---: | :--- |
| **Actividad oficial del avance (documento Word + `.py`)** | **80 pts** | Los 8 requerimientos del avance (sección 2), evaluados con la rúbrica de la sección 6. |
| **Jupyter de práctica semanal** | **15 pts** | Notebook `.ipynb` con la práctica de integración de los Temas 1 al 8, documentada con celdas Markdown. |
| **Uso de Git y GitHub** | **5 pts** | Repositorio público con estructura de carpetas estandarizada e historial mínimo de **3 commits significativos** con mensajes profesionales. |
| **Total semanal** | **100 pts** | |

> **IMPORTANTE:** Esta semana **NO tiene ejercicios extra evaluables**. Debido a que la semana se concentra en el **Avance del Proyecto (Fase I)**, los únicos componentes evaluables son la **actividad oficial del avance (80 pts)**, el **Jupyter de práctica semanal (15 pts)** y el **uso de Git y GitHub (5 pts)**.

---

## 5. Jupyter de práctica semanal (no confundir con ejercicios extra)

A diferencia de otras semanas, esta semana **no se asignan ejercicios extra evaluables**. En su lugar, el notebook de práctica (`practica_semana3.ipynb`) documenta tu repaso e integración de los Temas 1 al 8.

**Recomendación de práctica:** resuelve una selección de los **25 ejercicios complementarios NO evaluables** del archivo `Ejercicios_Semana3.md` para consolidar las habilidades de decisión, ciclos y acumuladores que exige el avance. Documenta en una celda Markdown, por cada ejercicio, el modelo EPS aplicado y la explicación del procedimiento.

---

## 6. Rúbrica de evaluación (100 puntos)

| Criterio | Puntos | Excelente (100%) | Bueno (75%) | Regular (50%) | Insuficiente (0%) |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Análisis Organizacional** (Req. 1) | 10 | Empresa/organización real identificada, área de impacto clara y necesidades bien descritas. | Organización identificada con descripción parcial de necesidades. | Organización vaga o área de impacto mal definida. | No incluye el análisis organizacional. |
| **Definición del Problema y reglas de negocio** (Req. 2) | 12 | Problema formulado con precisión y reglas de negocio completas y delimitadas. | Problema claro con reglas de negocio incompletas. | Problema impreciso o reglas de negocio ausentes. | No define el problema. |
| **Listado de Requerimientos** (Req. 3) | 10 | Requerimientos funcionales completos, claros y verificables. | Requerimientos completos con detalles menores imprecisos. | Requerimientos incompletos o poco claros. | No incluye el listado de requerimientos. |
| **Clasificación de Datos** (Req. 4) | 8 | Tipos de datos identificados y documentados correctamente (int, float, str, bool). | Tipos de datos identificados con errores menores. | Clasificación incompleta o con errores. | No clasifica los datos. |
| **Operadores del Lenguaje** (Req. 5) | 8 | Operadores matemáticos, relacionales y lógicos identificados y justificados. | Operadores identificados con justificación parcial. | Operadores incompletos o sin justificar. | No identifica operadores. |
| **Estructuras de Control** (Req. 6) | 12 | Estructuras condicionales e iterativas enumeradas correctamente y alineadas al flujo. | Estructuras enumeradas con errores menores. | Estructuras incompletas o mal asignadas. | No enumera estructuras de control. |
| **Diseño Algorítmico (diagrama + pseudocódigo)** (Req. 7) | 10 | Diagrama de flujo detallado en PSeInt y pseudocódigo formal correctos y exportados. | Diagrama y pseudocódigo correctos con detalles menores. | Diagrama o pseudocódigo incompleto o con errores. | No incluye diagrama ni pseudocódigo. |
| **Prototipo de Código (.py)** (Req. 8) | 8 | Prototipo ejecutable que refleja la lógica base y corre correctamente en consola. | Prototipo funcional con detalles menores de estilo o validación. | Prototipo con errores de ejecución o lógica parcial. | No incluye el `.py` o no funciona. |
| **Jupyter de práctica semanal** | 15 | Práctica de integración resuelta y documentada con celdas Markdown de explicación. | Práctica con errores menores o documentación parcial. | Práctica incompleta o sin explicaciones. | No entrega el notebook. |
| **Git y GitHub** | 5 | Repositorio público, estructura de carpetas estandarizada y al menos 3 commits con mensajes profesionales. | Repositorio público con 3 commits pero mensajes poco descriptivos. | Repositorio con menos de 3 commits. | No entrega la liga del repositorio. |
| **TOTAL** | **100** | | | | |

---

## 7. Lista de entregables y fechas

| Entregable | Archivo | Formato | Fecha límite |
| :--- | :--- | :--- | :--- |
| Reporte del avance (análisis técnico + pseudocódigo) | `reporte_avance.docx` | Word (.docx) | Viernes por la noche |
| Diagrama de flujo (exportado de PSeInt) | `diagrama_flujo.png` | Imagen (.png) | Viernes por la noche |
| Prototipo de código inicial | `prototipo_inicial.py` | Python (.py) | Viernes por la noche |
| Jupyter de práctica semanal | `practica_semana3.ipynb` | Jupyter Notebook (.ipynb) | Viernes por la noche |
| Repositorio | Liga pública de GitHub | URL | Viernes por la noche |

**Fechas límite oficiales:** **28 de agosto de 2026** (Periodo I) · **30 de octubre de 2026** (Periodo II).

**Nota de entrega:** Todos los entregables se suben al repositorio personal del estudiante dentro de la carpeta `semana-3/avance-proyecto/`, y la liga del repositorio se entrega como evidencia de la actividad.

---

## 8. Recordatorio de integridad académica

El avance del proyecto es un trabajo individual. Queda prohibida la copia total o parcial de código de internet o de compañeros, así como el uso de herramientas de inteligencia artificial para generar la lógica de los programas sin la autorización expresa del docente y sin referenciar explícitamente su uso. Las faltas se sancionan conforme al reglamento de integridad académica del curso (nota DA y demás consecuencias estipuladas).
