# SEMANA 7: MANEJO DE ARCHIVOS Y ENTREGA FINAL DEL PROYECTO (FASE II)

**Curso:** Solución de problemas con programación computacional  
**Institución:** Universidad Tecmilenio  
**Rol:** PyCoach — Guía Docente y Material de Clase  

---

## ÍNDICE DEL MATERIAL
1. **Tema 17:** Escritura de archivos (`open()` con modo `'w'` y `'a'`, `write()`, `close()`, sentencia `with`)
2. **Tema 18:** Lectura de archivos (`read()`, `readline()`, `readlines()`, iteración sobre líneas)
3. **Tema 19:** Integración de lectura y escritura de archivos
4. **Tema 20:** Excepciones en manejo de archivos (`FileNotFoundError`, `PermissionError`, `try-except`)
5. **Actividad Integradora Semanal:** Programa con persistencia en archivos + gestión en GitHub
6. **Desafíos Extras Autoevaluables:** Ejercicios de refuerzo para los alumnos

> **IMPORTANTE:** Esta semana corresponde a la **ENTREGA FINAL DEL PROYECTO (Fase II)** con ponderación del **35%** de la calificación total del curso (actividad **1155 - Entrega Final del Proyecto**, Temas 17, 18, 19 y 20). Fecha límite: **25 de septiembre de 2026** (Periodo I) · **27 de noviembre de 2026** (Periodo II). Consulta el archivo `Actividad7_EntregaFinalProyecto.md` para los 10 requerimientos obligatorios.

---

# TEMA 17: ESCRITURA DE ARCHIVOS

### 17.1 ¿Por qué persistir datos en archivos?
Hasta ahora, toda la información procesada por nuestros programas vivía únicamente en la memoria RAM y se perdía al cerrar la consola. Con los **archivos de texto externos (.txt)** podemos **guardar datos de forma permanente** en el disco duro, de modo que un programa pueda crearlos, consultarlos y modificarlos en ejecuciones futuras. Este concepto se conoce como **persistencia de datos** y es la base de la persistencia que exige la Entrega Final del Proyecto.

```
[ Datos en memoria ]  --->  (open + write)  --->  [ Archivo .txt en el disco ]
```

---

### 17.2 La función `open()` y los modos de apertura
La función `open()` abre (o crea) un archivo y devuelve un **objeto de archivo** sobre el que trabajamos. Su forma general es:

```python
open("nombre_del_archivo.txt", "modo")
```

| Modo | Significado | ¿Qué hace? |
| :---: | :--- | :--- |
| `'w'` | *write* (escritura) | Crea el archivo para escribir. **Si el archivo ya existe, lo SOBRESCRIBE desde cero.** |
| `'a'` | *append* (anexar) | Abre el archivo para **anexar al final**, sin borrar el contenido anterior. Si no existe, lo crea. |
| `'r'` | *read* (lectura) | Abre el archivo **solo para leer**. (Se estudia a detalle en el Tema 18). |

> **REGLA DE ORO:** El modo `'w'` destruye el contenido anterior del archivo. Úsalo con precaución. Si necesitas conservar lo existente y agregar más datos, usa el modo `'a'`.

---

### 17.3 Escritura con `write()` y `close()`
El método `write(texto)` escribe una cadena de texto en el archivo. El método `close()` cierra el archivo y **guarda los cambios en el disco**.

```python
archivo = open("saludo.txt", "w")
archivo.write("Hola, este es mi primer archivo.\n")
archivo.close()
print("Archivo creado correctamente.")
```

**Salida en consola:**
```
Archivo creado correctamente.
```

**Contenido resultante de `saludo.txt`:**
```text
Hola, este es mi primer archivo.
```

> **NOTA IMPORTANTE:** `write()` **NO agrega el salto de línea automáticamente**. Si queremos que cada dato ocupe una línea distinta, debemos escribir explícitamente el carácter `\n` al final.

```python
archivo = open("notas.txt", "w")
archivo.write("Linea 1\n")
archivo.write("Linea 2\n")
archivo.close()
```

**Contenido resultante de `notas.txt`:**
```text
Linea 1
Linea 2
```

---

### 17.4 Escritura con modo anexar `'a'`
Cuando usamos el modo `'a'` (append), el puntero se coloca al final del archivo y el contenido anterior **se conserva intacto**.

```python
# Primero creamos el archivo con dos registros
with open("bitacora.txt", "w") as archivo:
    archivo.write("Registro 1: inicio del sistema\n")

# Después anexamos dos registros más sin borrar el anterior
with open("bitacora.txt", "a") as archivo:
    archivo.write("Registro 2: usuario conectado\n")
    archivo.write("Registro 3: operacion completada\n")
```

**Contenido resultante de `bitacora.txt`:**
```text
Registro 1: inicio del sistema
Registro 2: usuario conectado
Registro 3: operacion completada
```

---

### 17.5 La sentencia `with` (gestor de contexto)
La sentencia `with` abre el archivo y lo **cierra automáticamente** al terminar el bloque de código, incluso si ocurre un error. Es la forma **recomendada** de trabajar con archivos, pues evita olvidar el `close()`.

```python
with open("config.txt", "w") as archivo:
    archivo.write("usuario: ana\n")
    archivo.write("nivel: avanzado\n")
    archivo.write("idioma: espanol\n")
```

**Contenido resultante de `config.txt`:**
```text
usuario: ana
nivel: avanzado
idioma: espanol
```

> El patrón `with open(...) as archivo:` equivale a abrir el archivo, ejecutar el bloque y cerrarlo automáticamente al salir. En este curso **siempre** utilizaremos esta sintaxis.

---

### 17.6 Ejemplo práctico: guardar datos del usuario
```python
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")

with open("datos_usuario.txt", "w") as archivo:
    archivo.write(f"Nombre: {nombre}, Edad: {edad}\n")

print("Datos guardados en datos_usuario.txt.")
```

**Entrada:**
```
Ingresa tu nombre: Ana
Ingresa tu edad: 20
```

**Salida en consola:**
```
Datos guardados en datos_usuario.txt.
```

**Contenido resultante de `datos_usuario.txt`:**
```text
Nombre: Ana, Edad: 20
```

---

# TEMA 18: LECTURA DE ARCHIVOS

Para leer un archivo lo abrimos con el modo `'r'`. Antes de probar los ejemplos, crearemos un archivo de prueba con el siguiente contenido:

**Contenido de `poema.txt`:**
```text
El sol brilla
en el cielo azul
de esta manana.
```

### 18.1 Lectura completa con `read()`
El método `read()` lee **todo el contenido** del archivo y lo devuelve como una sola cadena de texto.

```python
with open("poema.txt", "r") as archivo:
    contenido = archivo.read()
print(contenido)
```

**Salida en consola:**
```text
El sol brilla
en el cielo azul
de esta manana.
```

---

### 18.2 Lectura línea a línea con `readline()`
El método `readline()` lee **una sola línea** (hasta el siguiente salto de línea `\n`). Cada llamada avanza a la siguiente línea.

```python
with open("poema.txt", "r") as archivo:
    linea1 = archivo.readline()
    linea2 = archivo.readline()

print("Primera linea:", linea1.strip())
print("Segunda linea:", linea2.strip())
```

**Salida en consola:**
```
Primera linea: El sol brilla
Segunda linea: en el cielo azul
```

> El método `strip()` elimina los espacios y el salto de línea (`\n`) que quedan al inicio y al final de cada línea leída, de modo que la impresión se vea limpia.

---

### 18.3 Lectura de todas las líneas con `readlines()`
El método `readlines()` lee **todas las líneas** y las devuelve en una **lista**, donde cada elemento es una línea (incluyendo su `\n`).

```python
with open("poema.txt", "r") as archivo:
    lineas = archivo.readlines()

print("Total de lineas:", len(lineas))
for i, linea in enumerate(lineas, 1):
    print(f"{i}: {linea.strip()}")
```

**Salida en consola:**
```
Total de lineas: 3
1: El sol brilla
2: en el cielo azul
3: de esta manana.
```

---

### 18.4 Iterar sobre las líneas con `for`
La forma más eficiente de recorrer un archivo es **iterar directamente sobre el objeto de archivo** con un ciclo `for`: en cada vuelta, `linea` toma el valor de una línea del archivo.

```python
with open("poema.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())
```

**Salida en consola:**
```text
El sol brilla
en el cielo azul
de esta manana.
```

---

### 18.5 Resumen de métodos de lectura

| Método | ¿Qué lee? | ¿Qué devuelve? |
| :--- | :--- | :--- |
| `read()` | Todo el archivo | Una sola cadena (`str`) |
| `readline()` | Una línea a la vez | Una cadena (`str`) |
| `readlines()` | Todas las líneas | Una lista (`list`) de cadenas |
| `for linea in archivo:` | Línea por línea | Un objeto iterable |

---

# TEMA 19: INTEGRACIÓN DE LECTURA Y ESCRITURA DE ARCHIVOS

### 19.1 El flujo completo: leer → procesar → escribir
Los programas de aplicación reales combinan los dos temas anteriores: **leen datos de un archivo, los procesan en memoria y guardan los resultados en otro archivo** (o los anexan al mismo). Este flujo sigue el modelo Entrada-Proceso-Salida visto en la Semana 1:

```
[ Archivo de entrada ]  --->  (lectura con 'r')  --->  [ Procesamiento ]  --->  (escritura con 'w' o 'a')  --->  [ Archivo de salida ]
```

---

### 19.2 Ejemplo: reporte de ventas desde un archivo
Supongamos que la tienda registra sus ventas del día en `ventas.txt`:

**Contenido de `ventas.txt`:**
```text
100.0
250.5
49.5
```

El siguiente programa lee cada monto, calcula el total y el promedio, y guarda el resumen en un nuevo archivo `resumen.txt`:

```python
# LECTURA: procesamos los montos
with open("ventas.txt", "r") as archivo:
    montos = [float(linea.strip()) for linea in archivo]

# PROCESO: calculamos total y promedio
total = sum(montos)
promedio = total / len(montos)

# ESCRITURA: guardamos el resumen en un archivo nuevo
with open("resumen.txt", "w") as archivo:
    archivo.write(f"Total de ventas: {total:.2f}\n")
    archivo.write(f"Promedio por venta: {promedio:.2f}\n")

# VERIFICACIÓN: leemos y mostramos el resultado guardado
with open("resumen.txt", "r") as archivo:
    print(archivo.read())
```

**Salida en consola:**
```
Total de ventas: 400.00
Promedio por venta: 133.33
```

**Contenido resultante de `resumen.txt`:**
```text
Total de ventas: 400.00
Promedio por venta: 133.33
```

> Observa cómo el mismo programa usa tres veces la sentencia `with`: una para leer, otra para escribir y otra para verificar lo escrito.

---

### 19.3 Copiar el contenido de un archivo a otro
```python
with open("origen.txt", "r") as origen:
    contenido = origen.read()

with open("destino.txt", "w") as destino:
    destino.write(contenido)

print("Copia realizada.")
```

**Contenido de `origen.txt`:**
```text
Contenido a copiar
```

**Contenido resultante de `destino.txt`:** idéntico al de `origen.txt`.
**Salida en consola:** `Copia realizada.`

---

### 19.4 Anexar resultados al mismo archivo de datos
Cuando queremos conservar los datos originales y agregar un resultado, combinamos la lectura (para calcular) con la escritura en modo `'a'` (para anexar):

```python
with open("ventas.txt", "r") as archivo:
    montos = [float(linea.strip()) for linea in archivo]

total = sum(montos)

with open("ventas.txt", "a") as archivo:
    archivo.write(f"Total: {total:.2f}\n")

print("Total anexado al archivo ventas.txt")
```

**Contenido resultante de `ventas.txt` (después de ejecutar):**
```text
100.0
250.5
49.5
Total: 400.00
```

---

### 19.5 Buenas prácticas al integrar lectura y escritura
1. Usa **siempre** la sentencia `with` para que los archivos se cierren automáticamente.
2. Usa `strip()` al leer para eliminar los saltos de línea y convertir con `int()` o `float()` según el tipo de dato.
3. Separa el código en tres fases claras: **lectura, procesamiento y escritura**.
4. Si el archivo de salida no debe conservar datos previos, usa `'w'`; si debe conservarlos, usa `'a'`.

---

# TEMA 20: EXCEPCIONES EN MANEJO DE ARCHIVOS

### 20.1 ¿Qué es una excepción?
Una **excepción** es un error que ocurre durante la ejecución del programa y que, si no se controla, lo detiene de forma abrupta mostrando un *traceback*. Con el bloque **`try-except`** podemos "atrapar" esos errores y responder con mensajes amigables en lugar de que el programa se detenga.

### 20.2 Excepciones más comunes al trabajar con archivos

| Excepción | ¿Cuándo ocurre? |
| :--- | :--- |
| `FileNotFoundError` | Se intenta abrir un archivo que **no existe** o escribir en una carpeta inexistente. |
| `PermissionError` | El sistema operativo **niega el acceso** (archivo solo de lectura, sin permisos, o se intenta abrir un directorio como archivo). |
| `ValueError` | Al convertir el contenido leído (ej. una línea no numérica con `float()`). |

---

### 20.3 Manejo básico con `try-except`
```python
try:
    with open("inexistente.txt", "r") as archivo:
        print(archivo.read())
except FileNotFoundError:
    print("Error: el archivo no existe en la carpeta.")
```

**Salida en consola:**
```
Error: el archivo no existe en la carpeta.
```

El programa **no se detiene**: muestra el mensaje controlado y continúa.

---

### 20.4 Varios `except` para distintos errores
Podemos controlar cada tipo de error con un bloque `except` específico y, al final, un `except` general como red de seguridad:

```python
try:
    with open("datos.txt", "r") as archivo:
        contenido = archivo.read()
    print("Lectura exitosa:")
    print(contenido)
except FileNotFoundError:
    print("Error: el archivo 'datos.txt' no existe.")
except PermissionError:
    print("Error: no tienes permisos para abrir 'datos.txt'.")
except Exception as error:
    print(f"Ocurrio un error inesperado: {error}")
```

**Salida en consola (si `datos.txt` no existe):**
```
Error: el archivo 'datos.txt' no existe.
```

---

### 20.5 La cláusula `else`: código que se ejecuta solo si no hubo error
```python
try:
    with open("poema.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe.")
else:
    print("El archivo se leyo correctamente.")
    print(contenido)
```

**Salida en consola:**
```
El archivo se leyo correctamente.
El sol brilla
en el cielo azul
de esta manana.
```

---

### 20.6 Ejemplo integrador: lectura segura con nombre ingresado por el usuario
```python
nombre_archivo = input("Ingresa el nombre del archivo a abrir: ")

try:
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            print(linea.strip())
except FileNotFoundError:
    print(f"Error: no se encontro el archivo '{nombre_archivo}'.")
except PermissionError:
    print(f"Error: no tienes permisos para abrir '{nombre_archivo}'.")
```

**Entrada:**
```
Ingresa el nombre del archivo a abrir: poema.txt
```

**Salida en consola:**
```
El sol brilla
en el cielo azul
de esta manana.
```

Si el usuario escribe un nombre inexistente, el programa muestra un mensaje controlado y no se detiene. Este control de excepciones es uno de los **requerimientos obligatorios** de la Entrega Final del Proyecto.

---

# ACTIVIDAD INTEGRADORA SEMANAL (PRÁCTICA EN GUÍAS JUPYTER + GIT)

### Consigna para el Estudiante:
Debes crear un Jupyter Notebook llamado `solucion_semana7.ipynb` dentro de tu repositorio local de esta semana que demuestre el dominio de los 4 temas.

1. **Celda Markdown:** Un título general, tu nombre completo, matrícula y una explicación breve de los modos de apertura de archivos (`'r'`, `'w'`, `'a'`) y de la persistencia de datos.
2. **Celda Código:** Un programa en Python que:
   - Cree un archivo `inventario.txt` en modo `'w'` con un encabezado y dos productos.
   - Anexe un tercer producto en modo `'a'`.
   - Lea el archivo completo en modo `'r'` e imprima su contenido línea por línea.

   ```python
   with open("inventario.txt", "w") as archivo:
       archivo.write("Producto,Cantidad,Precio\n")
       archivo.write("Laptop,5,15000\n")
       archivo.write("Mouse,20,250\n")

   with open("inventario.txt", "a") as archivo:
       archivo.write("Teclado,15,450\n")

   with open("inventario.txt", "r") as archivo:
       for linea in archivo:
           print(linea.strip())
   ```

   **Salida esperada en consola:**
   ```
   Producto,Cantidad,Precio
   Laptop,5,15000
   Mouse,20,250
   Teclado,15,450
   ```

3. **Celda Código:** Una versión robusta del programa anterior que capture `FileNotFoundError` con `try-except` cuando intente leer un archivo inexistente.
4. **Subir los cambios a GitHub:**
```bash
git add solucion_semana7.ipynb
git commit -m "feat: completar actividad integradora semana 7"
git push origin main
```

> **RECORDATORIO:** La entrega oficial evaluable de esta semana es la **Entrega Final del Proyecto (Fase II)**. Consulta `Actividad7_EntregaFinalProyecto.md` para los 10 requerimientos y la rúbrica de evaluación.

---

# DESAFÍOS EXTRAS AUTOEVALUABLES (REFUERZO)

Los siguientes desafíos están diseñados para resolverse en tu libreta de Jupyter Notebook y ponen a prueba el manejo de archivos de los Temas 17 al 20.

### Desafío Extra 1: Registro de contactos
Crea un programa que pida el nombre y el teléfono de un contacto y los **anexe** al archivo `contactos.txt` con el formato `nombre|telefono`. Después lee el archivo y muestra todos los contactos registrados.

**Ejemplo de archivo resultante:**
```text
ana|555-1234
luis|555-9876
```

### Desafío Extra 2: Analizador de texto
Crea un programa que lea un archivo `texto.txt` y muestre cuántas **líneas**, cuántas **palabras** y cuántos **caracteres** (sin contar saltos de línea) contiene.
- *Pista:* Cuenta las palabras con `len(linea.split())` y los caracteres con `len(linea.strip())`.

### Desafío Extra 3: Reporte de calificaciones
Crea un programa que lea 5 calificaciones de un archivo `calif.txt` (una por línea), calcule el **promedio** y escriba en `reporte_final.txt` el promedio y el estado `APROBADO` (promedio >= 7) o `NO APROBADO`.

### Desafío Extra 4: Bitácora segura con excepciones
Crea una función `registrar(operacion)` que **anexe** cada operación al archivo `bitacora_segura.txt`. El programa debe capturar `PermissionError` con `try-except` y mostrar un mensaje de error controlado si no se puede escribir.

### Desafío Extra 5: Verificación de existencia antes de leer
Crea un programa que pregunte el nombre de un archivo y, antes de leerlo, verifique si **existe** en la carpeta usando la función `os.path.exists()`. Si existe, muestra su contenido; si no, muestra un mensaje de error sin detener el programa.
- *Pista:* Al inicio del programa agrega `import os`.

---

**Temas cubiertos en esta semana:** Escritura de archivos (Tema 17) · Lectura de archivos (Tema 18) · Integración de lectura y escritura (Tema 19) · Excepciones en manejo de archivos (Tema 20).
