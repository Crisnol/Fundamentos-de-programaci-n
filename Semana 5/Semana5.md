# SEMANA 5: TUPLAS, DICCIONARIOS, EXCEPCIONES Y STRINGS (ESTRUCTURAS AVANZADAS DE DATOS)

**Curso:** Solución de problemas con programación computacional  
**Institución:** Universidad Tecmilenio  
**Rol:** PyCoach — Guía Docente y Material de Clase  

---

## ÍNDICE DEL MATERIAL
1. **Tema 13:** Tuplas (Creación, indexación, inmutabilidad, empaquetado/desempaquetado, anexar en nueva tupla, conversión a lista)
2. **Tema 14:** Diccionarios (Claves y valores, acceso, agregar/actualizar, métodos `keys`/`values`/`items`, iteración)
3. **Tema 15:** Excepciones (`try`/`except`, `ValueError`, `ZeroDivisionError`, bloques específicos, mensajes controlados)
4. **Tema 16:** Strings (Métodos `upper`/`lower`/`len`/`replace`/`split`/`find`, slicing, f-strings, conteo de palabras)
5. **Actividad Integradora Semanal:** Notebook con las 4 estructuras + Gestión en GitHub
6. **Desafíos Extras Autoevaluables:** Ejercicios de refuerzo para los alumnos

---

# TEMA 13: TUPLAS

Una **tupla** es una secuencia ordenada e **inmutable** de elementos en Python. A diferencia de las listas, una vez creada una tupla no se pueden agregar, eliminar ni modificar sus elementos. Se define con paréntesis `()`.

### 13.1 Creación de Tuplas

```python
# Tupla de números enteros
numeros = (10, 20, 30, 40, 50)

# Tupla de cadenas de texto
frutas = ("manzana", "plátano", "cereza")

# Tupla con tipos mixtos
datos = ("Ana", 20, 1.65, True)

# Tupla de un solo elemento (obligatorio el paréntesis y la coma)
unico = (5,)

print(type(numeros))  # <class 'tuple'>
print(len(numeros))   # 5
```

---

### 13.2 Indexación de Tuplas

Al igual que las listas y los strings, los elementos de una tupla se acceden por su **índice**, que inicia en `0`. También se permiten **índices negativos** (desde el final).

```python
numeros = (10, 20, 30, 40, 50)

print(numeros[0])    # 10  (primer elemento)
print(numeros[2])    # 30  (tercer elemento)
print(numeros[4])    # 50  (quinto elemento)
print(numeros[-1])   # 50  (último elemento)
print(numeros[-3])   # 30  (tercer elemento desde el final)
```

---

### 13.3 Inmutabilidad de las Tuplas

El intentar modificar, eliminar o agregar un elemento directamente sobre una tupla existente genera un error de tipo `TypeError`. Esta propiedad vuelve a las tuplas ideales para almacenar datos que no deben cambiar (coordenadas, fechas, constantes).

```python
numeros = (10, 20, 30)

# El siguiente código provoca un error:
numeros[0] = 99
# TypeError: 'tuple' object does not support item assignment
```

---

### 13.4 Empaquetado y Desempaquetado

Python permite **empaquetar** varios valores en una sola tupla y **desempaquetar** una tupla asignando sus elementos a variables individuales en una sola línea.

```python
# Empaquetado: varios valores se agrupan en una tupla
punto = (3, 5)

# Desempaquetado: cada elemento se asigna a una variable
x, y = punto
print(x)  # 3
print(y)  # 5

# Desempaquetado directo de la tupla
a, b, c = (7, 8, 9)
print(a, b, c)  # 7 8 9
```

---

### 13.5 Anexar Elementos en una Nueva Tupla

Como la tupla es inmutable, para "agregarle" elementos se crea una **nueva tupla** concatenando la original con otra tupla mediante el operador `+`. Esto es especialmente útil cuando se capturan valores con `input()`.

```python
numeros = (10, 20, 30)

# Captura de dos números adicionales mediante input()
extra1 = int(input("Ingresa el primer número extra: "))
extra2 = int(input("Ingresa el segundo número extra: "))

# Se anexan los números capturados creando UNA NUEVA tupla
numeros_extendida = numeros + (extra1, extra2)
print(numeros_extendida)

# Entrada: 40 y 50
# Salida:  (10, 20, 30, 40, 50)
```

---

### 13.6 Conversión de Tupla a Lista y Ordenamiento

La función `list()` convierte una tupla en una lista, lo que permite aplicar métodos de ordenamiento como `sort()` (inmutable sobre la tupla, pero permitidos sobre la lista resultante).

```python
desorden = (8, 3, 12, 5, 1)

# Conversión de tupla a lista
lista = list(desorden)

# Ordenamiento ascendente de la lista
lista.sort()
print(lista)   # [1, 3, 5, 8, 12]

# Ordenamiento descendente
lista.sort(reverse=True)
print(lista)   # [12, 8, 5, 3, 1]
```

---

### 13.7 Funciones con Tuplas: Suma que Retorna Valor

Una función que recibe una tupla como parámetro puede recorrerla, sumar sus elementos y **retornar** el resultado con la palabra clave `return` para mostrarlo en pantalla.

```python
def suma_tupla(t):
    total = 0
    for n in t:
        total += n
    return total

numeros = (10, 20, 30, 40, 50)
resultado = suma_tupla(numeros)
print("La suma de la tupla es:", resultado)   # 150
```

> **Nota para la Actividad 4:** Este tema aporta los requerimientos de la tupla `numeros`, el acceso al tercer elemento, el anexado de dos números con `input()`, la conversión a lista con ordenamiento y la función que suma y retorna.

---

# TEMA 14: DICCIONARIOS

Un **diccionario** es una colección de pares **clave : valor** encerrados entre llaves `{}`. Permite guardar datos asociados, por ejemplo, el nombre de un contacto (clave) con su número de teléfono (valor).

### 14.1 Claves y Valores

La **clave** es un identificador único e inmutable (generalmente un string o un número). El **valor** puede ser cualquier tipo de dato (número, string, lista, otro diccionario, etc.).

```python
contactos = {
    "Ana": "555-0101",
    "Luis": "555-0102",
    "Mía": "555-0103"
}

print(type(contactos))  # <class 'dict'>
print(len(contactos))   # 3 (número de pares clave-valor)
```

---

### 14.2 Acceso a Valores

Se accede al valor mediante la clave entre corchetes `[]` o con el método `get()`. La diferencia es que `get()` devuelve un valor por defecto si la clave no existe, sin generar error.

```python
contactos = {
    "Ana": "555-0101",
    "Luis": "555-0102",
    "Mía": "555-0103"
}

print(contactos["Ana"])                 # 555-0101
print(contactos.get("Luis"))            # 555-0102
print(contactos.get("Pedro", "Sin registro"))  # Sin registro
```

---

### 14.3 Agregar y Actualizar Elementos

Para **agregar** una nueva pareja se asigna un valor a una clave que no existía. Para **actualizar** se asigna un nuevo valor a una clave ya existente. Ambos casos usan la misma sintaxis.

```python
contactos = {
    "Ana": "555-0101",
    "Luis": "555-0102"
}

# Agregar un nuevo contacto
contactos["Mía"] = "555-0103"
print(contactos)
# {'Ana': '555-0101', 'Luis': '555-0102', 'Mía': '555-0103'}

# Actualizar el teléfono de un contacto existente
contactos["Luis"] = "555-0202"
print(contactos["Luis"])   # 555-0202
```

---

### 14.4 Métodos `keys()`, `values()` y `items()`

- `keys()`: devuelve las claves del diccionario.
- `values()`: devuelve los valores del diccionario.
- `items()`: devuelve cada pareja clave-valor.

```python
contactos = {
    "Ana": "555-0101",
    "Luis": "555-0102",
    "Mía": "555-0103"
}

print(contactos.keys())    # dict_keys(['Ana', 'Luis', 'Mía'])
print(contactos.values())  # dict_values(['555-0101', '555-0102', '555-0103'])
print(contactos.items())   # dict_items([('Ana', '555-0101'), ('Luis', '555-0102'), ('Mía', '555-0103')])
```

---

### 14.5 Iteración sobre Diccionarios

El ciclo `for` recorre el diccionario. Al iterar directamente sobre el diccionario se obtienen las **claves**; combinado con `keys()`, `values()` o `items()` se obtiene la información deseada.

```python
contactos = {
    "Ana": "555-0101",
    "Luis": "555-0102",
    "Mía": "555-0103"
}

# Iterar sobre las claves e imprimir solo los nombres
for nombre in contactos.keys():
    print(nombre)
# Salida:
# Ana
# Luis
# Mía

# Iterar con items() e imprimir nombre y teléfono
for nombre, telefono in contactos.items():
    print(f"{nombre}: {telefono}")
# Salida:
# Ana: 555-0101
# Luis: 555-0102
# Mía: 555-0103
```

---

### 14.6 Funciones con Diccionarios: Búsqueda de Teléfono

Una función modular puede recibir el diccionario y un nombre, y **retornar** el teléfono correspondiente. Si la clave existe, se muestra el teléfono obtenido; si no, se despliega un mensaje amigable.

```python
def buscar_telefono(contactos, nombre):
    return contactos.get(nombre, "Contacto no encontrado")

contactos = {
    "Ana": "555-0101",
    "Luis": "555-0102",
    "Mía": "555-0103"
}

telefono = buscar_telefono(contactos, "Luis")
print("El teléfono de Luis es:", telefono)   # El teléfono de Luis es: 555-0102

telefono = buscar_telefono(contactos, "Pedro")
print("El teléfono de Pedro es:", telefono)  # El teléfono de Pedro es: Contacto no encontrado
```

> **Nota para la Actividad 4:** Este tema aporta el diccionario `contactos` con tres registros, la adición de un contacto por consola, la iteración de claves para imprimir nombres y la función que retorna el teléfono.

---

# TEMA 15: EXCEPCIONES

Una **excepción** es un error que ocurre durante la ejecución del programa y que, si no se maneja, provoca que el programa se detenga. Con `try`/`except` podemos anticipar estos errores y desplegar **mensajes controlados** en lugar de crashear.

### 15.1 ¿Qué es una Excepción?

Ejemplos comunes de excepciones en Python:
- `ValueError`: se intenta convertir texto no numérico con `int()` o `float()`.
- `ZeroDivisionError`: se intenta dividir un número entre cero.
- `TypeError`: se opera con tipos incompatibles (ej. `"Hola" + 5`).
- `IndexError`: se accede a un índice inexistente de una secuencia.

---

### 15.2 Estructura Básica `try` / `except`

El código que puede fallar se coloca dentro del bloque `try`. Si ocurre un error, el bloque `except` lo captura y ejecuta el código de recuperación.

```python
try:
    edad = int(input("Ingresa tu edad: "))
    print("Edad registrada:", edad)
except ValueError:
    print("Error: Debes ingresar solo números enteros.")
```

> **Ejecución de ejemplo 1:** Entrada `25` → Salida `Edad registrada: 25`  
> **Ejecución de ejemplo 2:** Entrada `abc` → Salida `Error: Debes ingresar solo números enteros.`

---

### 15.3 Capturando `ValueError`

La conversión de caracteres no numéricos o vacíos a `int()` dispara un `ValueError`. Es la excepción más frecuente al leer entradas del usuario.

```python
try:
    numero = int(input("Ingresa un número entero: "))
    print("El doble es:", numero * 2)
except ValueError:
    print("Mensaje controlado: El dato ingresado no es un número entero.")
```

> **Ejecución de ejemplo:** Entrada `hola` → Salida `Mensaje controlado: El dato ingresado no es un número entero.`

---

### 15.4 Bloques de Excepción Específicos: `ZeroDivisionError`

Se pueden usar **varios bloques `except`**, cada uno para un tipo de error específico. Esto permite desplegar mensajes personalizados según el fallo ocurrido.

```python
try:
    a = int(input("Ingresa el dividendo: "))
    b = int(input("Ingresa el divisor: "))
    print("El resultado de la división es:", a / b)
except ValueError:
    print("Error: Debes ingresar números enteros.")
except ZeroDivisionError:
    print("Error: No es posible dividir entre cero.")
```

> **Ejecución de ejemplo 1:** Entradas `8` y `2` → Salida `El resultado de la división es: 4.0`  
> **Ejecución de ejemplo 2:** Entradas `10` y `0` → Salida `Error: No es posible dividir entre cero.`

---

### 15.5 Bloques `else` y `finally`

- `else`: se ejecuta solo si no ocurrió ninguna excepción.
- `finally`: se ejecuta siempre, haya o no error (ideal para cierres o mensajes de fin).

```python
try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("Error de división entre cero.")
else:
    print("División exitosa:", resultado)   # División exitosa: 5.0
finally:
    print("El bloque finally siempre se ejecuta.")
```

---

### 15.6 Mensajes Controlados al Usuario

La combinación de ciclos con `try`/`except` permite construir programas robustos que **repiten la solicitud** hasta recibir un dato válido, ofreciendo mensajes amigables en cada intento fallido.

```python
while True:
    try:
        numero = int(input("Ingresa un número entero válido: "))
        break
    except ValueError:
        print("Dato inválido. Inténtalo nuevamente.")

print("Número capturado:", numero)
```

> **Nota para la Actividad 4:** Este tema aporta el bloque `try-except` para números enteros con mensaje controlado y el bloque específico de `ZeroDivisionError` para el divisor cero.

---

# TEMA 16: STRINGS (CADENAS DE CARACTERES)

Un **string** es una secuencia inmutable de caracteres entre comillas. Python ofrece métodos y operaciones para transformarlo, medirlo, buscarlo y formatearlo.

### 16.1 Métodos `upper()`, `lower()` y Función `len()`

- `upper()`: convierte todo el texto a mayúsculas.
- `lower()`: convierte todo el texto a minúsculas.
- `len()`: devuelve la cantidad de caracteres (función, no método).

```python
mensaje = "Hola Mundo"

print(len(mensaje))         # 10
print(mensaje.upper())      # HOLA MUNDO
print(mensaje.lower())      # hola mundo
```

---

### 16.2 Métodos `replace()`, `split()` y `find()`

- `replace(a, b)`: reemplaza todas las ocurrencias de la cadena `a` por la cadena `b`.
- `split()`: divide el texto en una lista de palabras (por espacios por defecto).
- `find(palabra)`: devuelve el índice inicial de la primera ocurrencia; si no existe, devuelve `-1`.

```python
mensaje = "Python es un lenguaje poderoso"

print(mensaje.replace("poderoso", "increíble"))
# Python es un lenguaje increíble

palabras = mensaje.split()
print(palabras)
# ['Python', 'es', 'un', 'lenguaje', 'poderoso']

print(mensaje.find("lenguaje"))   # 13
print(mensaje.find("Java"))       # -1
```

---

### 16.3 Slicing de Strings

El slicing permite extraer porciones del texto usando la sintaxis `[inicio:fin:paso]`. El índice `fin` no se incluye en el resultado.

```python
texto = "Hola Mundo"

print(texto[0:4])    # Hola   (caracteres 0 al 3)
print(texto[5:])     # Mundo  (del índice 5 al final)
print(texto[::-1])   # odnuM aloH  (texto invertido)
```

---

### 16.4 Formato con f-strings

Los **f-strings** permiten insertar variables y expresiones directamente dentro de un texto anteponiendo una `f` a las comillas y usando llaves `{}`.

```python
nombre = "Ana"
edad = 20

print(f"{nombre} tiene {edad} años.")
# Ana tiene 20 años.

precio = 92.80
print(f"Total a pagar: ${precio:.2f}")
# Total a pagar: $92.80
```

---

### 16.5 Conteo de Palabras con una Función

Una función que recibe un string puede **retornar** la cantidad de palabras que contiene: basta con dividir el texto con `split()` y medir la longitud de la lista resultante con `len()`.

```python
def contar_palabras(texto):
    return len(texto.split())

mensaje = "Aprender programación es divertido"
total = contar_palabras(mensaje)
print("El mensaje tiene", total, "palabras")
# El mensaje tiene 4 palabras
```

> **Nota para la Actividad 4:** Este tema aporta la variable `mensaje`, el uso de `len()`, la conversión a mayúsculas, el `replace()` de una palabra clave y la función que cuenta palabras.

---

# ACTIVIDAD INTEGRADORA SEMANAL (PRÁCTICA EN GUÍAS JUPYTER + GIT)

### Consigna para el Estudiante:
Debes crear un Jupyter Notebook llamado `solucion_semana5.ipynb` dentro de la carpeta `semana5/` de tu repositorio local, que contenga:

1. **Celda Markdown:** Un título general, tu nombre completo, matrícula y una explicación breve de las cuatro estructuras trabajadas (tuplas, diccionarios, excepciones y strings).
2. **Celda Código:** Un programa interactivo en Python que:
   - Cree una tupla `numeros` con al menos cinco elementos numéricos e imprima su tercer elemento.
   - Capture dos números adicionales con `input()` y los anexe en una nueva tupla.
   - Convierta la tupla en lista, la ordene y la muestre.
   - Calcule la suma de todos los elementos con una función que retorne el valor.
   - Cree un diccionario `contactos` con tres registros, agregue uno nuevo por consola e imprima solo los nombres con `keys()`.
   - Implemente un bloque `try-except` que capture un `ValueError` y un bloque específico `ZeroDivisionError` al dividir dos enteros.
   - Defina un `mensaje`, imprima su longitud con `len()`, lo convierta a mayúsculas, reemplace una palabra clave con `replace()` y cuente sus palabras con una función.
   - Cada sección se muestre con encabezados formateados con f-strings.

3. **Subir los cambios a GitHub:**
```bash
git add semana5/solucion_semana5.ipynb
git commit -m "feat: completar actividad integradora semana 5"
git push origin main
```

---

# DESAFÍOS EXTRAS AUTOEVALUABLES (REFUERZO)

Los siguientes ejercicios extras están diseñados para ser resueltos en tu libreta de Jupyter Notebook para poner a prueba tus habilidades.

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
