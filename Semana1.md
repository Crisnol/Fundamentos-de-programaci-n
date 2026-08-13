# SEMANA 1: FUNDAMENTOS DE PROGRAMACIÓN, ENTORNO DE DESARROLLO Y CONTROL DE VERSIONES CON GIT & GITHUB

**Curso:** Solución de problemas con programación computacional  
**Institución:** Universidad Tecmilenio  
**Rol:** PyCoach — Guía Docente y Material de Clase  

---

## ÍNDICE DEL MATERIAL
1. **Módulo Especial 01:** Instalación de Git y Configuración Inicial
2. **Módulo Especial 02:** Tutorial Básico de Git y GitHub (Primer Repositorio)
3. **Módulo Especial 03:** Guía Interactiva de Jupyter Notebooks
4. **Tema 1:** Solución de problemas con programación computacional (Algoritmos y Flujo Entrada-Proceso-Salida)
5. **Tema 2:** Fundamentos de programación (PSeInt, Pseudocódigo y Entornos IDE)
6. **Tema 3:** Conceptos fundamentales de programación (Variables, Tipos de Datos y Operadores)
7. **Tema 4:** Entradas y salidas simples (`input()`, `print()`, conversiones `int/float/str`)
8. **Actividad Integradora Semanal:** Primer Programa + Gestión en GitHub
9. **Desafíos Extras Autoevaluables:** Ejercicios de refuerzo para los alumnos

---

# MÓDULO ESPECIAL 01: INSTALACIÓN DE GIT Y CONFIGURACIÓN INICIAL

Para trabajar en el curso bajo estándares profesionales e integrar el control de versiones desde el primer día, requerimos instalar Git en nuestro sistema operativo.

### 1.1 Instalación según Sistema Operativo

#### En Windows:
1. Visita la página oficial: [https://git-scm.com/download/win](https://git-scm.com/download/win)
2. Descarga el instalador de 64-bit para Windows (`Git for Windows Setup`).
3. Ejecuta el instalador. Mantén las opciones por defecto recomendadas. Asegúrate de incluir **Git Bash**.

#### En macOS:
1. Abre la Terminal (`Command + Espacio`, escribe `Terminal`).
2. Escribe el comando:
```bash
git --version
```
3. Si no está instalado, macOS te solicitará instalar las **Xcode Command Line Tools**. Acepta e instala.
4. Alternativamente, puedes usar Homebrew: `brew install git`.

#### En Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install git -y
```

---

### 1.2 Configuración Global Obligatoria de Git
Una vez instalado, abre **Git Bash** (en Windows) o la **Terminal** (en macOS/Linux) y configura tu identidad. Esto asociará tus publicaciones (commits) con tu nombre y correo.

```bash
# Configurar tu nombre completo (como aparecerá en GitHub)
git config --global user.name "Tu Nombre Apellido"

# Configurar tu correo electrónico (debe ser el mismo registrado en GitHub)
git config --global user.email "tu_correo@ejemplo.com"

# Definir la rama principal predeterminada como 'main'
git config --global init.defaultBranch main

# Verificación de la configuración realizada
git config --list
```

---

# MÓDULO ESPECIAL 02: TUTORIAL BÁSICO DE GIT Y GITHUB

### 2.1 Creación de Cuenta en GitHub
1. Ingresa a [https://github.com](https://github.com).
2. Haz clic en **Sign up** e ingresa con tu correo institucional o personal.
3. Elige un nombre de usuario profesional (ejemplo: `jgarcia-dev` o `maria-perez-tec`).
4. Verifica tu cuenta a través del correo de confirmación.

---

### 2.2 Flujo de Trabajo Local (Git) y Remoto (GitHub)

El ciclo de trabajo estándar en desarrollo de software sigue estos comandos principales:

```
+------------------+         git add         +------------------+        git commit        +--------------------+        git push        +------------------+
| Área de Trabajo  |  -------------------->  | Staging Area     |  -------------------->  | Repositorio Local  |  --------------------> | Repositorio      |
| (Working Directory)                        | (Área de Preparación)                      | (.git)             |                        | Remoto (GitHub)  |
+------------------+                         +------------------+                         +--------------------+                        +------------------+
```

#### Comandos Esenciales Explicados:
- `git init`: Inicializa un nuevo repositorio Git local en la carpeta actual.
- `git status`: Muestra el estado actual de los archivos (modificados, agregados o sin seguimiento).
- `git add <archivo>` o `git add .`: Agrega cambios al área de preparación (*staging area*).
- `git commit -m "Mensaje claro"`: Guarda una instantánea de los cambios preparados con un mensaje descriptivo.
- `git remote add origin <URL>`: Conecta tu repositorio local con tu repositorio en GitHub.
- `git push -u origin main`: Sube tus commits locales al servidor de GitHub.
- `git clone <URL>`: Descarga una copia exacta de un repositorio público/privado de GitHub a tu computadora.

---

### 2.3 Práctica Guiada: Crear y Subir tu Primer Repositorio

1. **Crear carpeta de trabajo local:**
```bash
mkdir curso-python-semana1
cd curso-python-semana1
```

2. **Inicializar Git localmente:**
```bash
git init
```

3. **Crear un archivo README.md:**
```bash
echo "# Curso de Python - Semana 1" > README.md
```

4. **Preparar y confirmar los cambios (Commit):**
```bash
git status
git add README.md
git commit -m "docs: inicializar repositorio con README"
```

5. **Crear el repositorio en GitHub:**
   - Ve a [GitHub](https://github.com) -> Botón **"+"** -> **New repository**.
   - Nombre: `curso-python-semana1`.
   - Visibilidad: **Público**.
   - **IMPORTANTE:** Deja desmarcadas las casillas de "Add a README file", ".gitignore" y "License" (ya creamos el archivo localmente).
   - Haz clic en **Create repository**.

6. **Vincular y Subir (Push):**
```bash
git remote add origin https://github.com/TU_USUARIO/curso-python-semana1.git
git branch -M main
git push -u origin main
```

---

# MÓDULO ESPECIAL 03: GUÍA INTERACTIVA DE JUPYTER NOTEBOOKS

Jupyter Notebook es un entorno de desarrollo interactivo que permite combinar **texto enriquecido (Markdown)** con **bloques de código ejecutable (Python)**.

### 3.1 Tipos de Celdas
- **Celdas de Código (`Code`):** Contienen código ejecutable de Python. Al presionar `Shift + Enter`, el código se procesa y genera salidas inmediatas.
- **Celdas de Markdown (`Markdown`):** Contienen explicaciones teóricas, fórmulas, imágenes y títulos estilizados.

### 3.2 Sintaxis Esencial de Markdown para Notebooks

```markdown
# Título Principal (H1)
## Subtítulo (H2)
### Sección Temática (H3)

Texto en **negrita** o en *cursiva*.

Listas con viñetas:
- Elemento 1
- Elemento 2

Listas numeradas:
1. Primer paso
2. Segundo paso

Bloque de código dentro de texto: `variable = 10`

> Bloque de cita o nota aclaratoria importante.
```

---

# TEMA 1: SOLUCIÓN DE PROBLEMAS CON PROGRAMACIÓN COMPUTACIONAL

### 1.1 ¿Qué es un Algoritmo?
Un **algoritmo** es una secuencia finita, ordenada y no ambigua de pasos e instrucciones lógicas que permiten resolver un problema específico o realizar una tarea determinada.

#### Características Clave de un Algoritmo:
1. **Preciso:** Debe indicar el orden exacto de ejecución de cada paso.
2. **Definido:** Si se sigue el mismo algoritmo dos o más veces con los mismos datos de entrada, se debe obtener idéntico resultado.
3. **Finito:** Debe terminar en algún momento; cuenta con un número limitado de pasos.

---

### 1.2 El Modelo Entrada - Proceso - Salida (EPS)
Todo programa o algoritmo de computadora opera bajo la estructura lógica fundamental de tres fases:

```
[ Entrada de Datos ]  --->  [ Proceso / Transformación ]  --->  [ Salida de Resultados ]
```

1. **Entrada (Input):** Recolección de los datos iniciales necesarios para resolver el problema (ej. datos digitados por el usuario, lecturas de sensores).
2. **Proceso (Processing):** Conjunto de operaciones matemáticas, comparaciones lógicas y transformaciones ejecutadas sobre los datos de entrada.
3. **Salida (Output):** Despliegue de los resultados obtenidos hacia el usuario (pantalla, archivo, impresora).

---

### 1.3 Ejemplo de Algoritmo en Vida Real y Pseudocódigo
**Problema:** Calcular la velocidad media de un vehículo.

#### Pasos en lenguaje natural:
1. Solicitar la distancia recorrida en kilómetros.
2. Solicitar el tiempo transcurrido en horas.
3. Dividir la distancia entre el tiempo.
4. Mostrar el resultado de la velocidad en km/h.

---

# TEMA 2: FUNDAMENTOS DE PROGRAMACIÓN (PSEINT Y PSEUDOCÓDIGO)

### 2.1 Pseudocódigo y PSeInt
El **pseudocódigo** es un lenguaje intermedio informal que combina la estructura de un lenguaje de programación con frases en lenguaje natural. Permite al estudiante enfocarse en la **lógica algorítmica** antes de preocuparse por la sintaxis estricta de un lenguaje de programación formal como Python.

**PSeInt** es una herramienta educativa especialmente diseñada para escribir y probar diagramas de flujo y pseudocódigo en español.

---

### 2.2 Estructura General en PSeInt vs. Python

#### En Pseudocódigo (PSeInt):
```text
Algoritmo CalcularVelocidad
    Escribir "Ingrese la distancia en kilometros:"
    Leer distancia
    Escribir "Ingrese el tiempo en horas:"
    Leer tiempo
    velocidad <- distancia / tiempo
    Escribir "La velocidad promedio es: ", velocidad, " km/h"
FinAlgoritmo
```

#### Transición a Código Real en Python:
```python
# CÓDIGO PYTHON
distancia = float(input("Ingrese la distancia en kilometros: "))
tiempo = float(input("Ingrese el tiempo en horas: "))
velocidad = distancia / tiempo
print("La velocidad promedio es:", velocidad, "km/h")
```

---

### 2.3 Entornos de Desarrollo Integrados (IDE)
Un **IDE (Integrated Development Environment)** es un software que proporciona herramientas consolidadas para programar:
- Editor de código con resaltado de sintaxis.
- Depurador (*debugger*) para rastrear errores.
- Terminal / Consola de ejecución integrada.
- Ejemplos populares: **VS Code**, **Jupyter Notebook**, **PyCharm**.

---

# TEMA 3: CONCEPTOS FUNDAMENTALES DE PROGRAMACIÓN

### 3.1 Variables y Declaración
Una **variable** es un espacio reservado en la memoria RAM del equipo identificado por un nombre, el cual almacena un valor que puede cambiar durante la ejecución del programa.

```python
# En Python la asignación se realiza mediante el operador `=`
edad = 25
nombre = "Ricardo"
estatura = 1.78
es_estudiante = True
```

#### Reglas de Nombramiento de Variables en Python (PEP 8):
- Usar estilo `snake_case` (letras minúsculas separadas por guiones bajos, ej. `precio_total`).
- Debe iniciar con una letra o un guion bajo (`_`), nunca con un número.
- Sensible a mayúsculas y minúsculas (`edad` no es lo mismo que `Edad`).
- **NO** usar palabras reservadas de Python (`import`, `for`, `class`, `def`, `if`, `print`, `input`).

---

### 3.2 Tipos de Datos Primitivos en Python
Python es un lenguaje de **tipado dinámico**, lo que significa que infiere el tipo de dato automáticamente al asignar un valor.

| Tipo de Dato | Tipo en Python (`type`) | Descripción | Ejemplo |
| :--- | :--- | :--- | :--- |
| **Entero** | `int` | Números enteros sin decimales | `10`, `-5`, `0` |
| **Flotante** | `float` | Números reales con parte decimal | `3.1416`, `-0.01` |
| **Texto / Cadena** | `str` | Secuencia de caracteres entre comillas | `"Hola"`, `'Tecmilenio'` |
| **Booleano** | `bool` | Valores de verdad | `True`, `False` |

---

### 3.3 Operadores Matemáticos y Lógicos

#### Operadores Aritméticos:
```python
a = 10
b = 3

print(a + b)   # Suma -> 13
print(a - b)   # Resta -> 7
print(a * b)   # Multiplicación -> 30
print(a / b)   # División flotante -> 3.3333...
print(a // b)  # División entera (cociente) -> 3
print(a % b)   # Módulo (residuo de la división) -> 1
print(a ** b)  # Potencia (10 elevado a 3) -> 1000
```

#### Operadores Relacionales / Comparación:
- `==` (Igual a)
- `!=` (Diferente de)
- `>` (Mayor que)
- `<` (Menor que)
- `>=` (Mayor o igual que)
- `<=` (Menor o igual que)

---

# TEMA 4: ENTRADAS Y SALIDAS SIMPLES

### 4.1 La Función `print()`
La función `print()` permite enviar datos y mensajes hacia la consola o salida estándar.

```python
# Uso básico con múltiples argumentos
nombre = "Ana"
edad = 20
print("Hola", nombre, "tienes", edad, "años.")

# Formato moderno con f-strings (Recomendado)
print(f"Hola {nombre}, tienes {edad} años.")
```

---

### 4.2 La Función `input()` y Conversión de Tipos (Casting)
La función `input()` permite pausar la ejecución del programa para que el usuario ingrese información desde el teclado.

> **¡REGLA DE ORO DE PYTHON!**  
> Todo dato capturado con `input()` **SIEMPRE** se recibe como un tipo cadena de texto (`str`), sin importar si el usuario escribe números.

```python
# Captura de datos
edad_str = input("Ingresa tu edad: ")
print(type(edad_str)) # <class 'str'>

# Si intentamos sumar directamente sin convertir, ocurrirá un error de concatenación o TypeError.
# Conversión explícita (Casting):
edad = int(edad_str) # Conversión a número entero
proximo_ano = edad + 1
print(f"El próximo año tendrás {proximo_ano} años.")

# Conversión directa en una sola línea
precio = float(input("Ingrese el precio del producto: "))
descuento = precio * 0.10
precio_final = precio - descuento
print(f"Precio final con 10% de descuento: ${precio_final:.2f}")
```

---

# ACTIVIDAD INTEGRADORA SEMANAL (PRÁCTICA EN GUÍAS JUPYTER + GIT)

### Consigna para el Estudiante:
Debes crear un Jupyter Notebook llamado `solucion_semana1.ipynb` dentro de tu repositorio local `curso-python-semana1` que contenga:

1. **Celda Markdown:** Un título general, tu nombre completo, matrícula y una explicación breve del modelo Entrada-Proceso-Salida.
2. **Celda Código:** Un programa interactivo en Python que:
   - Pida al usuario su nombre y su año de nacimiento.
   - Pida al usuario el costo de dos productos consumidos en un establecimiento.
   - Calcule la edad aproximada del usuario (asumiendo año actual 2026).
   - Calcule el subtotal, el IVA (16%) y el total general a pagar.
   - Imprima un ticket formateado usando *f-strings*.

3. **Subir los cambios a GitHub:**
```bash
git add solucion_semana1.ipynb
git commit -m "feat: completar actividad integradora semana 1"
git push origin main
```

---

# DESAFÍOS EXTRAS AUTOEVALUABLES (REFUERZO)

Los siguientes ejercicios extras están diseñados para ser resueltos en tu libreta de Jupyter Notebook para poner a prueba tus habilidades.

### Desafío Extra 1: Convertidor de Temperatura
Crea un programa que pida una temperatura en grados Celsius (`float`) e imprima la conversión equivalente en Fahrenheit y Kelvin.
- Formula Fahrenheit: $F = (C \times 9/5) + 32$
- Formula Kelvin: $K = C + 273.15$

### Desafío Extra 2: Calculadora de Calificación Final
Un curso se evalúa con 3 parciales. Pide las 3 calificaciones individuales en formato decimal (`float`), calcula el promedio aritmético e imprime el resultado redondeado a dos decimales.

### Desafío Extra 3: Descomposición de Tiempo
Escribe un algoritmo en Python que solicite una cantidad entera de segundos (ej. `3665`) y la convierta e imprima expresada en horas, minutos y segundos restantes.
- *Pista:* Utiliza los operadores de división entera `//` y módulo `%`.

---
