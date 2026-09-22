# ACTIVIDAD EVALUABLE 7 — ENTREGA FINAL DEL PROYECTO (FASE II)

**Curso:** Solución de problemas con programación computacional
**Semana:** 7 · Temas 17, 18, 19 y 20
**Ponderación:** 35% de la calificación total del curso
**Actividad:** 1155 - Entrega Final del Proyecto
**Fechas límite:** 25 de septiembre de 2026 (Periodo I) · 27 de noviembre de 2026 (Periodo II)
**Entrega:** Viernes por la noche

---

## 1. Descripción del reto

Llevar a su versión final el **proyecto integrador** iniciado en la Fase I (Semana 3, Avance del Proyecto). La solución debe resolver una **problemática real de negocios** en un área organizacional de impacto, incorporando ahora conceptos avanzados de Python: **manejo de errores robusto**, **persistencia en archivos externos**, **interfaces lógicas de control de inactividad**, y una **depuración técnica documentada** del código.

Esta fase integra directamente los cuatro temas de la semana:
- **Tema 17:** Escritura de archivos (modos `'w'` y `'a'`, `write()`, `close()`, sentencia `with`).
- **Tema 18:** Lectura de archivos (`read()`, `readline()`, `readlines()`, iteración sobre líneas).
- **Tema 19:** Integración de lectura y escritura de archivos.
- **Tema 20:** Excepciones en manejo de archivos (`FileNotFoundError`, `PermissionError`, `try-except`).

---

## 2. Requerimientos técnicos obligatorios de programación

El programa en Python **debe cumplir estrictamente** los siguientes 10 requerimientos (tal como se definen en la agenda oficial del curso):

1. **Identificación de Usuario:** Solicitar el nombre o *nickname* del usuario al iniciar el programa.
2. **Bienvenida Dinámica:** Generar un mensaje de bienvenida formal que incorpore el nombre del usuario mediante el uso de operadores de cadenas (*strings*).
3. **Pantalla de Carga:** Diseñar una función dedicada que genere una pausa interactiva de carga de sistema de **máximo 5 segundos**, mostrando un aviso dinámico en consola antes de dar paso a la pantalla principal.
4. **Menú como Matriz:** Implementar un menú de opciones principal controlado por un ciclo `while` para la manipulación de documentos y archivos de datos. Las opciones del menú deben presentarse y seleccionarse a través de un formato o representación en forma de **matriz**.
5. **Control de Inactividad del Usuario:** Utilizar un ciclo `for` para medir el tiempo de inactividad del usuario en el menú principal. Si transcurren **10 minutos** sin interacción u opción seleccionada, el programa debe suspender temporalmente el menú y desplegar un mensaje consultando si desea continuar. El usuario deberá escribir expresamente `"si"` para continuar en el menú o `"no"` para regresar a la pantalla de inicio del programa.
6. **Captura de Fecha Estructurada:** Solicitar al usuario que ingrese la fecha de operación en formato numérico (día, mes, año; ej. `12/06/2023`). El programa debe almacenar estrictamente este valor en una tupla bajo la sintaxis: `Fecha = dia, mes, anio`. Esta fecha estructurada de la tupla deberá integrarse automáticamente cada vez que el programa cree o modifique un archivo de texto.
7. **Persistencia en Archivos de Texto:**
   - **Lectura de Archivos:** El programa debe contar de manera previa con **cuatro o más archivos de texto (.txt) creados**. Al seleccionar la opción de lectura en el menú, el programa debe mostrar estos archivos disponibles estructurados en forma de lista o diccionario para que el usuario pueda ingresar el nombre del archivo específico que desea abrir y desplegar su contenido.
   - **Escritura e Integración:** Implementar opciones robustas para crear y escribir/anexar datos a archivos de texto externos de forma permanente, asegurando la persistencia real del sistema.
8. **Control de Excepciones del Sistema:** Implementar manejadores de excepciones `try-except` para controlar todos los errores posibles de tiempo de ejecución en persistencia de datos (ej. capturar errores si se intenta abrir un archivo inexistente `FileNotFoundError`, si hay un nombre mal escrito o si hay fallos de permisos).
9. **Depuración Técnica (Debugging):** Realizar un debugging técnico completo en consola utilizando el módulo estándar **`PDB`** para localizar fallas de lógica de control, documentando las correcciones realizadas.
10. **Comentarios de Calidad:** Documentar de manera extensa el código fuente con comentarios descriptivos relevantes que faciliten el futuro mantenimiento del software por terceros.

---

## 3. Estructura del entregable principal (80%)

El entregable es un **reporte académico final escrito** (formato de reporte) acompañado de las carpetas de código. Incluye la **documentación y justificación de los criterios evaluativos de diseño lógico**, y las carpetas con el **código en Python (.py) completamente depurado y comentado** junto con los **archivos de texto de prueba** del sistema.

| # | Componente | Detalle |
| :---: | :--- | :--- |
| 1 | **Reporte académico final** | Documento formal que documenta y justifica el diseño lógico: problemática de negocio, reglas de negocio, arquitectura de la solución, justificación de los 10 requerimientos y evidencias. |
| 2 | **Carpeta de código fuente** | Archivos `.py` completamente depurados, con **comentarios extensos de calidad** y correctamente organizados. |
| 3 | **Archivos de texto de prueba** | **Cuatro o más archivos `.txt`** creados de antemano para demostrar la persistencia (lectura, escritura y anexado) del sistema. |
| 4 | **Evidencia de depuración con PDB** | Registro/documentación de las fallas de lógica localizadas con `PDB` y las correcciones realizadas (puede integrarse al reporte). |

---

## 4. Estrategia de evaluación semanal (80/20)

| Componente | Puntos | Descripción |
| :--- | :---: | :--- |
| **Entrega Final del Proyecto (Fase II)** | **80 pts** | Reporte académico final + código `.py` depurado y comentado + archivos de texto de prueba, evaluados con la rúbrica de la sección 6. |
| **Ejercicios extras en Jupyter** | **0 pts** | Esta semana **NO** tiene ejercicios extra evaluables. |
| **Uso de Git y GitHub** | **20 pts** | Repositorio público con estructura de carpetas estandarizada e historial mínimo de **3 commits significativos** con mensajes profesionales. |
| **Total semanal** | **100 pts** | |

> **NOTA IMPORTANTE — SIN EJERCICIOS EXTRA EVALUABLES:**
> Esta semana NO tiene ejercicios extra evaluables. A diferencia de las semanas 1 a 6, en la Semana 7 **no se solicita** un archivo `extras_semana7.ipynb` con retos adicionales evaluados (los 15 puntos de ejercicios extras de la estrategia general 80/20). Toda la ponderación evaluable de la semana se concentra en la **Entrega Final del Proyecto (Fase II)** y en el **control de versiones (Git y GitHub)** con el que se entrega la evidencia.

---

## 5. Rúbrica de evaluación (100 puntos)

| Criterio | Puntos | Excelente (100%) | Bueno (75%) | Regular (50%) | Insuficiente (0%) |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Identificación de usuario y bienvenida dinámica** | 10 | Solicita el nombre o *nickname* al inicio y genera bienvenida formal con operadores de cadenas. | Cumple ambos puntos con detalles menores de formato. | Cumple solo uno de los dos puntos. | No los implementa. |
| **Pantalla de carga (máx. 5 segundos)** | 5 | Función dedicada con pausa de carga de máximo 5 s y aviso dinámico en consola. | Función correcta con aviso poco dinámico o duración ligeramente mayor. | Pausa implementada sin función dedicada o sin aviso. | No la implementa. |
| **Menú como matriz con `while`** | 10 | Menú principal controlado por `while`, con opciones presentadas en forma de **matriz**. | Menú funcional con `while` pero representación de matriz incompleta. | Menú sin forma de matriz o sin control de `while`. | No implementa menú. |
| **Control de inactividad (10 min con `for`)** | 10 | Ciclo `for` mide 10 minutos de inactividad, suspende el menú y pregunta `"si"`/`"no"` para continuar o regresar al inicio. | Control implementado con detalles menores de mensajes. | Control parcial (sin pregunta `"si"`/`"no"` o sin regreso al inicio). | No lo implementa. |
| **Captura de fecha en tupla `Fecha = dia, mes, anio`** | 10 | Almacena la fecha estrictamente en tupla con la sintaxis indicada y la integra automáticamente en cada archivo creado/modificado. | Tupla correcta pero no se integra en todos los archivos. | Captura fecha sin usar tupla o sin integrarla. | No captura fecha. |
| **Persistencia en archivos de texto (4+ .txt)** | 15 | Cuenta con 4 o más `.txt`, muestra archivos disponibles en lista/diccionario, permite elegir y desplegar contenido, y permite crear/escribir/anexar de forma permanente. | Cumple 3 de los 4 puntos. | Cumple 2 puntos. | Cumple 1 o ninguno. |
| **Control de excepciones `try-except`** | 10 | Controla `FileNotFoundError`, nombres mal escritos y fallos de permisos con mensajes amigables; el programa nunca se detiene abruptamente. | Controla los errores con detalles menores. | Controla solo algunos errores. | No implementa excepciones. |
| **Depuración técnica con PDB** | 10 | Debugging completo con el módulo `PDB`, fallas localizadas y correcciones documentadas. | Depuración realizada con documentación incompleta. | Uso de PDB parcial sin documentación. | No usa PDB. |
| **Comentarios de calidad** | 10 | Código documentado de forma extensa y descriptiva que facilita el mantenimiento por terceros. | Comentarios suficientes con algunos bloques sin documentar. | Comentarios escasos o poco descriptivos. | Código sin comentarios. |
| **Reporte académico final** | 10 | Reporte formal que documenta y justifica los criterios de diseño lógico, con evidencias y estructura completa. | Reporte completo con detalles de presentación menores. | Reporte incompleto o sin justificación del diseño. | No entrega reporte. |
| **TOTAL** | **100** | | | | |

---

## 6. Lista de entregables y fechas

| Entregable | Archivo / Evidencia | Formato | Fecha límite |
| :--- | :--- | :--- | :--- |
| Reporte académico final | Reporte del proyecto (Fase II) | Documento formal (Word o PDF) | Viernes por la noche |
| Código fuente | Carpetas con archivos `.py` depurados y comentados | Código Python (.py) | Viernes por la noche |
| Archivos de prueba | Cuatro o más archivos `.txt` de persistencia | Archivos de texto (.txt) | Viernes por la noche |
| Evidencia de depuración | Documentación de las correcciones con `PDB` | Sección del reporte | Viernes por la noche |
| Repositorio | Liga pública de GitHub con historial de commits | URL | Viernes por la noche |

**Fechas límite oficiales:**
- **Periodo I:** 25 de septiembre de 2026
- **Periodo II:** 27 de noviembre de 2026

**Nota de entrega:** Todos los entregables deben subirse al repositorio personal del estudiante (con estructura de carpetas por semana: `semana1/`, `semana2/`, ..., `semana7/`) y la liga del repositorio se entrega como evidencia de la actividad.
