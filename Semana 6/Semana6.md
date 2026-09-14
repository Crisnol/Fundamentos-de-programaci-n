# SEMANA 6: REPASO INTEGRAL (TEMAS 1 AL 16) Y CERTIFICACIÓN CISCO NETWORKING ACADEMY

**Curso:** Solución de problemas con programación computacional  
**Institución:** Universidad Tecmilenio  
**Rol:** PyCoach — Guía Docente y Material de Clase  

**Semana:** 6 · Repaso y Consolidación  
**Temas cubiertos:** Temas 1 al 16  
**Actividad de la semana:** ACTIVIDAD 5 — Certificación de Cisco Networking Academy (6%)  
**Fechas límite:** 18 de septiembre de 2026 (Periodo I) · 20 de noviembre de 2026 (Periodo II)

---

## ÍNDICE DEL MATERIAL
1. **Bloque A:** Fundamentos y modelo Entrada-Proceso-Salida (Temas 1 y 2)
2. **Bloque B:** Variables, operadores y entrada/salida (Temas 3 y 4)
3. **Bloque C:** Decisiones y ciclos (Temas 5, 6, 7 y 8)
4. **Bloque D:** Listas, matrices y funciones (Temas 9, 10, 11 y 12)
5. **Bloque E:** Tuplas, diccionarios, excepciones y strings (Temas 13, 14, 15 y 16)
6. **Actividad 5 — Certificación de Cisco Networking Academy:** Avance y acreditación
7. **Guía de registro y avance en Cisco Skills for All:** Paso a paso
8. **Plan de repaso sugerido:** Distribución de la semana
9. **Desafíos Extras Autoevaluables:** Ejercicios de refuerzo

---

# BLOQUE A: FUNDAMENTOS Y MODELO ENTRADA-PROCESO-SALIDA (TEMAS 1 Y 2)

### A.1 Resumen de conceptos
- Un **algoritmo** es una secuencia finita, ordenada y no ambigua de pasos para resolver un problema. Debe ser **preciso**, **definido** y **finito**.
- Todo programa opera bajo el modelo **Entrada - Proceso - Salida (EPS)**: los datos de **entrada** se transforman mediante el **proceso** y producen los **resultados de salida**.
- El **pseudocódigo** describe la lógica en lenguaje natural estructurado; **PSeInt** permite escribirlo y probarlo antes de codificar en Python.

### A.2 Ejemplo integrado en Python
```python
# Velocidad media aplicando el modelo Entrada-Proceso-Salida
distancia = float(input("Distancia recorrida (km): "))   # ENTRADA
tiempo = float(input("Tiempo transcurrido (h): "))       # ENTRADA
velocidad = distancia / tiempo                            # PROCESO
print(f"Velocidad media: {velocidad:.2f} km/h")           # SALIDA
```
**Ejemplo de ejecución:** distancia = `120`, tiempo = `2` → `Velocidad media: 60.00 km/h`.

---

# BLOQUE B: VARIABLES, OPERADORES Y ENTRADA/SALIDA (TEMAS 3 Y 4)

### B.1 Resumen de conceptos
- La **variable** es un espacio de memoria identificado por un nombre que almacena un valor modificable. En Python se usa `snake_case` y no se pueden usar palabras reservadas.
- **Tipos de datos primitivos:** `int`, `float`, `str`, `bool`. Python es de **tipado dinámico** (el tipo se infiere al asignar).
- **Operadores aritméticos:** `+`, `-`, `*`, `/`, `//`, `%`, `**`. **Operadores relacionales:** `==`, `!=`, `>`, `<`, `>=`, `<=`.
- La función `input()` **siempre** devuelve texto (`str`); para operar numéricamente se requiere conversión explícita con `int()` o `float()` (casting).
- La función `print()` envía datos a la consola; los *f-strings* (`f"{variable}"`) permiten formatear la salida.

### B.2 Ejemplo integrado en Python
```python
# Ticket de compra con subtotal, IVA y total
producto1 = float(input("Precio del producto 1: "))
producto2 = float(input("Precio del producto 2: "))
subtotal = producto1 + producto2
iva = subtotal * 0.16
total = subtotal + iva
print(f"Subtotal: ${subtotal:.2f}")
print(f"IVA (16%): ${iva:.2f}")
print(f"Total a pagar: ${total:.2f}")
```
**Ejemplo de ejecución:** producto1 = `120`, producto2 = `80` →
```
Subtotal: $200.00
IVA (16%): $32.00
Total a pagar: $232.00
```

---

# BLOQUE C: DECISIONES Y CICLOS (TEMAS 5, 6, 7 Y 8)

### C.1 Resumen de conceptos
- **Estructuras de decisión:** `if`, `elif` y `else` permiten ramificar el flujo según condiciones lógicas.
- **Estructura `while`:** repite un bloque mientras una condición sea verdadera; ideal para validación de entrada y menús.
- **Estructura `for`:** recorre secuencias y rangos (`range(inicio, fin, paso)`); se combina con `break` (interrumpir) y `continue` (saltar a la siguiente iteración).
- **Debugging:** el módulo estándar **PDB** (`python -m pdb script.py` o `breakpoint()`) permite pausar, inspeccionar variables y localizar errores de lógica.

### C.2 Ejemplos integrados en Python
```python
# Decisión múltiple con if / elif / else
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres menor de edad")
```
**Ejemplo de ejecución:** edad = `20` → `Eres mayor de edad`.

```python
# Validación de entrada con while (solo acepta 0-100)
calificacion = -1
while calificacion < 0 or calificacion > 100:
    calificacion = int(input("Calificación (0-100): "))
print(f"Calificación válida: {calificacion}")
```
**Ejemplo de ejecución:** entrada = `120` (rechazada), luego `85` → `Calificación válida: 85`.

```python
# Suma de pares del 1 al 20 usando for con continue
suma = 0
for i in range(1, 21):
    if i % 2 != 0:
        continue
    suma += i
print(f"La suma de los pares del 1 al 20 es: {suma}")
```
**Ejemplo de ejecución:** `La suma de los pares del 1 al 20 es: 110` (2 + 4 + 6 + 8 + 10 + 12 + 14 + 16 + 18 + 20).

---

# BLOQUE D: LISTAS, MATRICES Y FUNCIONES (TEMAS 9, 10, 11 Y 12)

### D.1 Resumen de conceptos
- Las **listas** son colecciones ordenadas y mutables; se indexan desde `0`, permiten `append()`, `len()`, *slicing* `lista[inicio:fin]` y recorridos con `for`.
- Las **listas de listas (matrices)** organizan datos en renglones y columnas; se recorren con ciclos anidados.
- Las **funciones que no regresan valor** ejecutan acciones sin `return`. Las **funciones que regresan valor** usan `return` y devuelven un resultado al punto de llamada.

### D.2 Ejemplos integrados en Python
```python
# Función que regresa valor: promedio de calificaciones
def promedio(calificaciones):
    total = 0
    for c in calificaciones:
        total += c
    return total / len(calificaciones)

notas = [8, 9, 10]
print(f"Promedio: {promedio(notas)}")
```
**Ejemplo de ejecución:** `Promedio: 9.0`.

```python
# Matriz (lista de listas) mostrada con una función que NO regresa valor
tabla = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def mostrar_matriz(m):
    for fila in m:
        for celda in fila:
            print(celda, end=" ")
        print()

mostrar_matriz(tabla)
```
**Ejemplo de ejecución:**
```
1 2 3 
4 5 6 
7 8 9 
```

```python
# Slicing de listas: invertir
numeros = [1, 2, 3, 4, 5]
print(numeros[::-1])
```
**Ejemplo de ejecución:** `[5, 4, 3, 2, 1]`.

---

# BLOQUE E: TUPLAS, DICCIONARIOS, EXCEPCIONES Y STRINGS (TEMAS 13, 14, 15 Y 16)

### E.1 Resumen de conceptos
- Las **tuplas** son colecciones inmutables y ordenadas; se accede con índices y son útiles para datos que no deben cambiar.
- Los **diccionarios** almacenan pares *clave-valor*; se consultan por clave y se recorren con `clave in diccionario`, `.keys()`, `.values()`.
- Las **excepciones** se controlan con `try-except`; ejemplos comunes: `ValueError`, `KeyError`, `ZeroDivisionError`, `FileNotFoundError`.
- Los **strings** son cadenas inmutables; métodos útiles: `len()`, `.upper()`, `.lower()`, `.replace()`, `.split()`, `.strip()`.

### E.2 Ejemplos integrados en Python
```python
# Tuplas: acceso y suma de elementos
coordenadas = (3, 4, 5)
print(coordenadas[0])            # 3
numeros = (4, 8, 15, 16, 23, 42)
print(sum(numeros))              # 108
```
**Ejemplo de ejecución:**
```
3
108
```

```python
# Diccionario con manejo de excepciones (KeyError)
contactos = {"Ana": "555-1234", "Beto": "555-5678", "Carla": "555-9012"}
nombre = input("Buscar contacto: ")
try:
    print(f"Teléfono de {nombre}: {contactos[nombre]}")
except KeyError:
    print(f"{nombre} no está en la agenda")
```
**Ejemplo de ejecución:** nombre = `Beto` → `Teléfono de Beto: 555-5678`; nombre = `Luis` → `Luis no está en la agenda`.

```python
# Excepciones en operaciones numéricas
try:
    a = int(input("Dividendo: "))
    b = int(input("Divisor: "))
    print(a / b)
except ValueError:
    print("Error: ingresa números enteros")
except ZeroDivisionError:
    print("Error: no se puede dividir entre cero")
```
**Ejemplo de ejecución:** a = `10`, b = `0` → `Error: no se puede dividir entre cero`.

```python
# Strings: longitud, mayúsculas, reemplazo y separación
mensaje = "aprende python"
print(len(mensaje))                             # 14
print(mensaje.upper())                          # APRENDE PYTHON
print(mensaje.replace("python", "programacion"))  # aprende programacion
print(mensaje.split())                          # ['aprende', 'python']
```
**Ejemplo de ejecución:**
```
14
APRENDE PYTHON
aprende programacion
['aprende', 'python']
```

---

# ACTIVIDAD 5 — CERTIFICACIÓN DE CISCO NETWORKING ACADEMY (6%)

Esta semana **no se abordan temas nuevos**: el contenido se orienta al **repaso y consolidación** de los Temas 1 al 16 y a la **acreditación de la certificación externa** de Cisco Networking Academy.

**Requerimientos académicos (agenda oficial):**
1. Registrarse formalmente en el portal de **Cisco Academy (*Skills for All with Cisco*)**.
2. Completar todas las lecturas, ejercicios interactivos y laboratorios de práctica del curso oficial **Fundamentos de Python 1** (*Python Essentials 1*).
3. Acreditar formalmente el examen de certificación **CISCO Fundamentos de Python 1 - Examen de Sección** y obtener la **insignia digital** correspondiente.

**Entregable:** Un documento académico de reporte con las capturas de pantalla de la **bitácora de avance** y de la **calificación oficial aprobatoria con la insignia digital**.

Los detalles completos de la actividad, la estructura del entregable, la rúbrica de 100 puntos y las fechas límite están en el archivo **`Actividad6_CertificacionNetAcad.md`** de esta misma carpeta.

---

# GUÍA DE REGISTRO Y AVANCE EN CISCO SKILLS FOR ALL

Sigue este orden paso a paso para completar la ACTIVIDAD 5 antes de la fecha límite (18 de septiembre de 2026 / 20 de noviembre de 2026).

### Paso 1. Crear tu cuenta en el portal
1. Ingresa al portal oficial: [https://skillsforall.com](https://skillsforall.com).
2. Haz clic en **Sign Up / Create Account**.
3. Regístrate con un correo electrónico que revises con frecuencia (institucional recomendado) y elige una contraseña segura.
4. Completa tu perfil con tu nombre completo, país (México) e idioma preferido.
5. Confirma tu cuenta a través del correo de verificación que recibirás.

### Paso 2. Acceder al curso oficial
1. Inicia sesión en tu cuenta.
2. Busca el curso oficial **"Fundamentos de Python 1"** (*Python Essentials 1*) en el catálogo de cursos de programación.
3. Revisa que el curso esté alojado bajo el programa de **Cisco Networking Academy / Skills for All**.
4. Haz clic en **Enroll / Inscribirme** para activar el curso en tu panel (*Dashboard*).

### Paso 3. Completar lecturas, ejercicios y laboratorios (bitácora de avance)
1. Recorre los módulos del curso en orden: conceptos de programación, tipos de datos, decisiones, ciclos, funciones, tuplas, diccionarios, excepciones y strings (contenido alineado con los Temas 1 al 16 del curso).
2. Realiza **todas** las lecturas obligatorias de cada sección.
3. Resuelve los **ejercicios interactivos** integrados en la plataforma.
4. Completa los **laboratorios de práctica** usando el editor/simulador de Python que la plataforma proporciona.
5. La plataforma registra tu avance en la **bitácora de actividades**: esta evidencia es la que se captura para el reporte.

### Paso 4. Repasar con el material del curso
- Antes de presentar el examen, repasa los **Bloques A a E** de este documento y resuelve los 25 ejercicios de `Ejercicios_Semana6.md`.
- Verifica que domines: operadores y casting, `if/elif/else`, `while` y `for`, listas y matrices, funciones con y sin `return`, tuplas, diccionarios, `try-except` y métodos de strings.

### Paso 5. Presentar el examen de sección
1. Cuando hayas completado el avance formativo del curso, ingresa al examen oficial: **CISCO Fundamentos de Python 1 - Examen de Sección**.
2. Preséntalo con calma, en un solo intento bien preparado; verifica tu conexión a internet antes de iniciar.
3. Para **acreditar** necesitas obtener la **calificación aprobatoria** que la propia plataforma indica al finalizar el examen.
4. Guarda una **captura de pantalla nítida** de la pantalla de resultado con tu calificación oficial.

### Paso 6. Obtener y evidenciar tu insignia digital
1. Al acreditar, la plataforma (a través de **Credly** u otro emisor digital) te otorgará una **insignia digital** de *Python Essentials 1*.
2. Activa/reclama tu insignia en tu perfil y descárgala o captúrala en pantalla.
3. Guarda una **captura de pantalla** que muestre la insignia obtenida junto con tu nombre.

### Paso 7. Elaborar el reporte
1. Redacta el documento de reporte descrito en `Actividad6_CertificacionNetAcad.md`.
2. Incluye las capturas de la **bitácora de avance** y de la **calificación oficial + insignia**.
3. Sube el reporte a tu repositorio y entrega la liga en la fecha límite correspondiente.

---

# PLAN DE REPASO SUGERIDO (DISTRIBUCIÓN DE LA SEMANA)

| Día | Actividad sugerida | Material |
| :---: | :--- | :--- |
| **Día 1** | Repasar Bloques A y B: algoritmo EPS, variables, operadores e input/output | Semana6.md · Temas 1-4 |
| **Día 2** | Repasar Bloque C: decisiones y ciclos | Semana6.md · Temas 5-8 |
| **Día 3** | Repasar Bloque D: listas, matrices y funciones | Semana6.md · Temas 9-12 |
| **Día 4** | Repasar Bloque E: tuplas, diccionarios, excepciones y strings | Semana6.md · Temas 13-16 |
| **Día 5** | Avance en la plataforma: lecturas, ejercicios y laboratorios de Python Essentials 1 | Cisco Skills for All |
| **Día 6** | Presentar el examen de sección y obtener la insignia | CISCO Fundamentos de Python 1 |
| **Día 7** | Elaborar y entregar el reporte con las capturas | Actividad6_CertificacionNetAcad.md |

---

# DESAFÍOS EXTRAS AUTOEVALUABLES (REFUERZO)

Estos retos consolidan varios temas a la vez. Resuélvelos en tu Jupyter Notebook y súbelos a tu repositorio. No son evaluables esta semana.

### Desafío Extra 1: Inventario con diccionarios y excepciones
Crea un programa con un diccionario de productos y precios. Pide el nombre de un producto y muestra su precio; si no existe, muestra un mensaje controlado con `try-except KeyError`. Finalmente, muestra el costo total del inventario (suma de los precios).
- *Pista:* Combina Temas 14 (diccionarios) y 15 (excepciones).

### Desafío Extra 2: Lista de calificaciones con funciones
Escribe un programa que pida calificaciones hasta ingresar `-1`, las almacene en una lista y use dos funciones: una que regrese el promedio y otra que **no** regrese valor pero imprima si el grupo está aprobado (promedio >= 7) o reprobado.
- *Pista:* Combina Temas 9 (listas), 11 y 12 (funciones).

### Desafío Extra 3: Procesador de frases
Escribe un programa que pida una frase, la convierta a mayúsculas, cuente cuántas palabras tiene (`.split()`) y reemplace la palabra "python" por "programacion" si aparece.
- *Pista:* Combina Tema 16 (strings) con `len()` y métodos de cadenas.

---

**Recuerda:** el objetivo de esta semana es **consolidar** los Temas 1 al 16 y **acreditar** la certificación externa. Aprovecha el repaso para resolver los 25 ejercicios de `Ejercicios_Semana6.md` y llegar al examen de sección con confianza.
