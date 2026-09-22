# 30 EJERCICIOS DE REFUERZO — SEMANA 7

**Curso:** Solución de problemas con programación computacional
**Alcance:** Temas 17 al 20 (Escritura de archivos · Lectura de archivos · Integración de lectura y escritura · Excepciones en manejo de archivos)

Resuelve los ejercicios conforme avances en los temas. Cada ejercicio incluye el **enunciado**, la **entrada** (para ejercicios de archivos se describe el contenido del archivo de entrada) y la **salida esperada** (en consola o en el archivo resultante). Se recomienda resolverlos en un Jupyter Notebook y subirlos a tu repositorio de GitHub.

---

## BLOQUE 1 · TEMA 17: ESCRITURA DE ARCHIVOS

### Ejercicio 1: Mi primer archivo
**Enunciado:** Crea un programa que abra el archivo `saludo.txt` en modo `'w'`, escriba el texto `Hola, mundo` con `write()` y cierre el archivo con `close()`. Al final, imprime un mensaje de confirmación.
**Entrada:** Ninguna (el archivo `saludo.txt` no existe y se creará).
**Salida:** Consola: `Archivo creado correctamente.` Archivo resultante `saludo.txt`: `Hola, mundo`

---

### Ejercicio 2: Escribir tres líneas separadas
**Enunciado:** Crea un programa que escriba las siguientes tres líneas en el archivo `notas.txt` usando el modo `'w'`. Recuerda que `write()` no agrega el salto de línea automáticamente, así que debes incluir `\n`.
**Entrada:** Ninguna.
**Salida:** Archivo resultante `notas.txt`:
```
Linea 1: aprender Python
Linea 2: manejar archivos
Linea 3: completar el proyecto
```

---

### Ejercicio 3: Anexar un registro con el modo `'a'`
**Enunciado:** Dado el archivo `bitacora.txt` con dos registros, escribe un programa que **anexe** el registro `Registro 3: operacion guardada` al final usando el modo `'a'`, sin borrar el contenido anterior.
**Entrada:** Archivo `bitacora.txt` existente:
```
Registro 1: sistema iniciado
Registro 2: usuario registrado
```
**Salida:** Archivo resultante `bitacora.txt`:
```
Registro 1: sistema iniciado
Registro 2: usuario registrado
Registro 3: operacion guardada
```

---

### Ejercicio 4: Diferencia entre `'w'` y `'a'`
**Enunciado:** Ejecuta las siguientes operaciones sobre el archivo `datos.txt` y explica qué conserva cada modo: (1) escribir `Dato original` con `'w'`; (2) escribir `Sobrescrito` con `'w'`; (3) escribir `Nuevo valor` con `'w'`; (4) escribir `Adicional` con `'a'`.
**Entrada:** Archivo `datos.txt` inicial con `Dato original`.
**Salida:** Archivo resultante `datos.txt` (los dos primeros `'w'` fueron sobrescritos, solo queda el último `'w'` más lo anexado):
```
Nuevo valor
Adicional
```

---

### Ejercicio 5: Escritura con la sentencia `with`
**Enunciado:** Usando la sentencia `with open("config.txt", "w")`, escribe las siguientes tres líneas de configuración. No necesitas llamar a `close()`.
**Entrada:** Ninguna.
**Salida:** Archivo resultante `config.txt`:
```
usuario: ana
nivel: avanzado
idioma: espanol
```

---

### Ejercicio 6: Guardar datos del usuario en un archivo
**Enunciado:** Crea un programa que pida el nombre y la edad del usuario y los guarde en el archivo `datos_usuario.txt` con el formato `Nombre: <nombre>, Edad: <edad>` usando f-strings y el modo `'w'`.
**Entrada:**
```
Ingresa tu nombre: Ana
Ingresa tu edad: 20
```
**Salida:** Consola: `Datos guardados en datos_usuario.txt.` Archivo resultante `datos_usuario.txt`: `Nombre: Ana, Edad: 20`

---

### Ejercicio 7: Tabla de multiplicar guardada en archivo
**Enunciado:** Crea un programa que pida un número entero y escriba su tabla de multiplicar (del 1 al 10) en el archivo `tabla_<numero>.txt` con el formato `n x i = resultado`.
**Entrada:** `7`
**Salida:** Consola: `Tabla guardada en tabla_7.txt.` Archivo resultante `tabla_7.txt`:
```
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
```

---

## BLOQUE 2 · TEMA 18: LECTURA DE ARCHIVOS

### Ejercicio 8: Leer todo el contenido con `read()`
**Enunciado:** Crea un programa que abra el archivo `poema.txt` en modo `'r'`, lea todo su contenido con `read()` y lo imprima en consola.
**Entrada:** Archivo `poema.txt`:
```
El sol brilla
en el cielo azul
de esta manana.
```
**Salida (consola):**
```
El sol brilla
en el cielo azul
de esta manana.
```

---

### Ejercicio 9: Leer líneas con `readline()`
**Enunciado:** Crea un programa que use dos llamadas a `readline()` para leer las dos primeras líneas de `poema.txt` y las imprima limpio usando `strip()`.
**Entrada:** Archivo `poema.txt`:
```
El sol brilla
en el cielo azul
de esta manana.
```
**Salida (consola):**
```
Primera linea: El sol brilla
Segunda linea: en el cielo azul
```

---

### Ejercicio 10: Listar líneas numeradas con `readlines()`
**Enunciado:** Crea un programa que lea el archivo `nombres.txt` con `readlines()` y muestre cada línea numerada en consola.
**Entrada:** Archivo `nombres.txt`:
```
Ana
Luis
Maria
```
**Salida (consola):**
```
1. Ana
2. Luis
3. Maria
```

---

### Ejercicio 11: Iterar sobre líneas con `for`
**Enunciado:** Crea un programa que recorra el archivo `frutas.txt` con un ciclo `for` y muestre en consola el mensaje `Me gusta: <fruta>` por cada línea.
**Entrada:** Archivo `frutas.txt`:
```
manzana
pera
uva
```
**Salida (consola):**
```
Me gusta: manzana
Me gusta: pera
Me gusta: uva
```

---

### Ejercicio 12: Contar las líneas de un archivo
**Enunciado:** Crea un programa que cuente cuántas líneas tiene el archivo `texto.txt` (iterando sobre él con `for`) y muestre el total.
**Entrada:** Archivo `texto.txt` con 5 líneas:
```
Linea 1
Linea 2
Linea 3
Linea 4
Linea 5
```
**Salida (consola):** `El archivo tiene 5 lineas.`

---

### Ejercicio 13: Contar las palabras de un archivo
**Enunciado:** Crea un programa que lea el archivo `frase.txt` con `read()`, cuente las palabras con el método `split()` y muestre el total.
**Entrada:** Archivo `frase.txt`: `Python es un lenguaje de programacion`
**Salida (consola):** `El archivo tiene 6 palabras.`

---

### Ejercicio 14: Buscar líneas con una palabra clave
**Enunciado:** Crea un programa que recorra el archivo `articulo.txt` con `for` e imprima únicamente las líneas que contengan la palabra `Python`.
**Entrada:** Archivo `articulo.txt`:
```
Python es facil
Java es dificil
Python es poderoso
```
**Salida (consola):**
```
Python es facil
Python es poderoso
```

---

### Ejercicio 15: Leer números de un archivo y sumarlos
**Enunciado:** Crea un programa que lea el archivo `numeros.txt` línea por línea, convierta cada una con `int()` y muestre la suma total.
**Entrada:** Archivo `numeros.txt`:
```
10
20
30
```
**Salida (consola):** `La suma de los numeros es: 60`

---

## BLOQUE 3 · TEMA 19: INTEGRACIÓN DE LECTURA Y ESCRITURA

### Ejercicio 16: Copiar un archivo a otro
**Enunciado:** Crea un programa que lea el contenido de `origen.txt` y lo escriba completo en un nuevo archivo `destino.txt`.
**Entrada:** Archivo `origen.txt`: `Contenido a copiar`
**Salida:** Consola: `Copia realizada.` Archivo resultante `destino.txt`: `Contenido a copiar`

---

### Ejercicio 17: Promedio de calificaciones guardado en archivo
**Enunciado:** Crea un programa que lea tres calificaciones de `calificaciones.txt`, calcule el promedio y lo escriba en el archivo `promedio.txt` con el formato `Promedio: <valor>`.
**Entrada:** Archivo `calificaciones.txt`:
```
8
9
10
```
**Salida:** Archivo resultante `promedio.txt`: `Promedio: 9.0`

---

### Ejercicio 18: Reporte de ventas con total y promedio
**Enunciado:** Crea un programa que lea los montos de `ventas.txt` (con `float()`), calcule el total y el promedio, y los escriba en un nuevo archivo `resumen.txt` con dos decimales.
**Entrada:** Archivo `ventas.txt`:
```
100.0
250.5
49.5
```
**Salida:** Archivo resultante `resumen.txt`:
```
Total de ventas: 400.00
Promedio por venta: 133.33
```

---

### Ejercicio 19: Anexar el total al mismo archivo de ventas
**Enunciado:** Crea un programa que lea los montos de `ventas.txt`, calcule el total y lo **anexe** al final del mismo archivo con el formato `Total: <valor>` usando el modo `'a'`, conservando los montos originales.
**Entrada:** Archivo `ventas.txt`:
```
100.0
250.5
49.5
```
**Salida:** Archivo resultante `ventas.txt`:
```
100.0
250.5
49.5
Total: 400.00
```

---

### Ejercicio 20: Ordenar nombres y guardarlos en otro archivo
**Enunciado:** Crea un programa que lea los nombres de `alumnos.txt`, los ordene alfabéticamente con el método `sort()` y los escriba en un nuevo archivo `ordenados.txt`.
**Entrada:** Archivo `alumnos.txt`:
```
Luis
Ana
Carlos
```
**Salida:** Archivo resultante `ordenados.txt`:
```
Ana
Carlos
Luis
```

---

### Ejercicio 21: Guardar un reporte con fecha en tupla
**Enunciado:** Crea un programa que pida el día, mes y año, los almacene en la tupla `Fecha = dia, mes, anio` e integre esa fecha en el encabezado del archivo `reporte.txt` con el formato `Reporte generado el: dia/mes/anio`.
**Entrada:**
```
Dia: 12
Mes: 6
Anio: 2023
```
**Salida:** Consola: `Fecha = (12, 6, 2023)` Archivo resultante `reporte.txt`:
```
Reporte generado el: 12/6/2023
Contenido del reporte
```

---

### Ejercicio 22: Separar números pares e impares en dos archivos
**Enunciado:** Crea un programa que lea los números de `numeros2.txt`, separe los pares en `pares.txt` y los impares en `impares.txt`.
**Entrada:** Archivo `numeros2.txt`:
```
1
2
3
4
5
```
**Salida:** Archivo resultante `pares.txt`:
```
2
4
```
Archivo resultante `impares.txt`:
```
1
3
5
```

---

### Ejercicio 23: Bitácora de operaciones (archivo log)
**Enunciado:** Crea una función `registrar(operacion)` que **anexe** al archivo `log.txt` cada operación con su número consecutivo y la fecha, con el formato `[n] 12/06/2023 - <operacion>`. Llama a la función dos veces.
**Entrada:** Archivo `log.txt` inicial vacío.
**Salida:** Archivo resultante `log.txt`:
```
[1] 12/06/2023 - Alta de usuario
[2] 12/06/2023 - Modificacion de saldo
```

---

## BLOQUE 4 · TEMA 20: EXCEPCIONES EN MANEJO DE ARCHIVOS

### Ejercicio 24: Capturar un archivo inexistente
**Enunciado:** Crea un programa que intente leer el archivo `fantasma.txt` (que no existe) dentro de un bloque `try-except` y capture `FileNotFoundError`.
**Entrada:** Ninguna (el archivo `fantasma.txt` no existe).
**Salida (consola):** `Error: el archivo 'fantasma.txt' no existe.`

---

### Ejercicio 25: Capturar un error de permisos
**Enunciado:** Crea un programa que intente abrir un archivo protegido (sin permisos de acceso o solo de lectura) y capture `PermissionError`, mostrando un mensaje amigable. (El ejemplo puede probarse intentando abrir un directorio como archivo.)
**Entrada:** Un archivo o directorio sin permisos de lectura.
**Salida (consola):** `Error: no tienes permisos para abrir el archivo.`

---

### Ejercicio 26: Nombre de archivo capturado por el usuario
**Enunciado:** Crea un programa que pida el nombre del archivo a abrir y lo lea dentro de un `try-except` que capture `FileNotFoundError`.
**Entrada:**
```
Ingresa el nombre del archivo: inexistente.txt
```
**Salida (consola):** `Error: no se encontro el archivo 'inexistente.txt'.`

---

### Ejercicio 27: Datos no numéricos en un archivo de números
**Enunciado:** Crea un programa que lea las líneas de `datos_malos.txt`, intente convertirlas a `float()` dentro de un `try-except` que capture `ValueError` y sume únicamente las líneas válidas.
**Entrada:** Archivo `datos_malos.txt`:
```
10
hola
20
```
**Salida (consola):**
```
Error: la linea 'hola' no es un numero valido.
La suma de los numeros validos es: 30.0
```

---

### Ejercicio 28: Escritura en una carpeta inexistente
**Enunciado:** Crea un programa que intente escribir en el archivo `no_existe/archivo.txt` (dentro de una carpeta que no existe) y capture `FileNotFoundError`.
**Entrada:** Ninguna (la carpeta `no_existe` no existe).
**Salida (consola):** `Error: la carpeta de destino no existe.`

---

### Ejercicio 29: Función segura de lectura
**Enunciado:** Crea una función `leer_archivo(nombre)` que use `try-except`: si el archivo existe, regresa la cantidad de líneas que contiene; si no existe, regresa el mensaje `Error: no se pudo leer '<nombre>'`. Prueba con `poema.txt` y con `nada.txt`.
**Entrada:** `poema.txt` existe (3 líneas) y `nada.txt` no existe.
**Salida (consola):**
```
poema.txt -> 3 lineas leidas
nada.txt -> Error: no se pudo leer 'nada.txt'
```

---

### Ejercicio 30: Mini menú con control de excepciones
**Enunciado:** Crea un programa con un menú de 2 opciones (`1. Leer archivo`, `2. Salir`) controlado por un ciclo. Al leer, pide el nombre del archivo dentro de un `try-except` que capture `FileNotFoundError`. El usuario lee `menu.txt` (existente), luego `inexistente.txt` y finalmente sale.
**Entrada:** Archivo `menu.txt` con `Hola, mundo`. Capturas: opción `1` y archivo `menu.txt`; opción `1` y archivo `inexistente.txt`; opción `2`.
**Salida (consola):**
```
1. Leer archivo
2. Salir
Selecciona una opcion: 1
Contenido de menu.txt: Hola, mundo
1. Leer archivo
2. Salir
Selecciona una opcion: 1
Error: no se encontro el archivo 'inexistente.txt'.
1. Leer archivo
2. Salir
Selecciona una opcion: 2
Hasta luego.
```
