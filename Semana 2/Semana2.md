# SEMANA 2: ESTRUCTURAS DE DECISIÓN, REPETICIÓN Y DEBUGGING CON PDB

**Curso:** Solución de problemas con programación computacional  
**Institución:** Universidad Tecmilenio  
**Rol:** PyCoach — Guía Docente y Material de Clase  

---

## ÍNDICE DEL MATERIAL
1. **Tema 5:** Estructuras de decisión (`if`, `else`, `elif`, anidamiento y operadores lógicos `and`/`or`/`not`)
2. **Tema 6:** Estructura de repetición `while` (ciclos controlados por condición, contadores, acumuladores, `break` y `continue`)
3. **Tema 7:** *Debugging* (depuración de código con PDB: errores de sintaxis, lógica y ejecución)
4. **Tema 8:** Estructura de repetición `for` (`range()`, iteración, sumas, acumuladores y patrones con `print`)
5. **Actividad Integradora Semanal:** Cobro de boletos + depuración (práctica en Guías Jupyter + Git)
6. **Desafíos Extras Autoevaluables:** Ejercicios de refuerzo para los alumnos

---

# TEMA 5: ESTRUCTURAS DE DECISIÓN

### 5.1 ¿Qué es una Estructura de Decisión?
Una **estructura de decisión** permite que un programa ejecute un bloque de instrucciones u otro, dependiendo de si una condición lógica se cumple (`True`) o no (`False`). Gracias a ella, el programa deja de ejecutar las instrucciones en línea recta y *decide* qué camino tomar.

```
[ Condición ]  --True-->  [ Bloque A ]
      |
      +---------False---->  [ Bloque B ]
```

---

### 5.2 La sentencia `if`, `else` y `elif` en Python

#### `if` simple (decisión con una sola opción):
```python
edad = 20
if edad >= 18:
    print("Eres mayor de edad")
```

#### `if-else` (dos caminos mutuamente excluyentes):
```python
edad = 16
if edad >= 18:
    print("Puedes entrar")
else:
    print("Acceso restringido")
```

#### `if-elif-else` (múltiples caminos):
```python
edad = 15
if edad < 3:
    precio = 0
elif edad <= 17:
    precio = 30
else:
    precio = 45
print(f"El boleto cuesta: ${precio:.2f}")
```

#### Anidamiento (`if` dentro de `if`):
```python
edad = 70
if edad >= 18:
    if edad >= 60:
        print("Aplica descuento de adulto mayor (12%)")
    else:
        print("No aplica descuento por edad")
```

---

### 5.3 Operadores Lógicos: `and`, `or`, `not`
Los operadores lógicos permiten **combinar condiciones**:

| Operador | Significado | Ejemplo | Resultado |
| :--- | :--- | :--- | :---: |
| `and` | Ambas condiciones deben ser verdaderas | `edad >= 18 and edad < 60` | `True` solo si las dos son `True` |
| `or` | Al menos una condición debe ser verdadera | `tipo == "profesor" or tipo == "estudiante"` | `True` si una u otra es `True` |
| `not` | Niega el valor de verdad | `not es_mayor` | Invierte `True` en `False` y viceversa |

```python
edad = 65
tipo = "adulto_mayor"

es_mayor = edad >= 18          # True
aplica_descuento = (edad >= 60) and (tipo == "adulto_mayor")   # True and True -> True
no_es_estudiante = not (tipo == "estudiante")                  # not False -> True
```

#### La "Tabla de Verdad" de la Actividad 2
Para que **solo se aplique un descuento por boleto**, se evalúan los tipos en orden de prioridad y la primera condición que se cumpla "gana" el descuento:

| ¿Mayor de edad? | Tipo de visitante | Descuento | Boleto |
| :---: | :--- | :---: | :---: |
| Sí | Adulto mayor (12%) | 12% | `45 - 45*0.12 = 39.60` |
| Sí | Profesor (10%) | 10% | `45 - 45*0.10 = 40.50` |
| Sí | Estudiante (10%) | 10% | `45 - 45*0.10 = 40.50` |
| Sí | Otro | 0% | `45.00` |
| No | Menor de 3 años | Boleto gratis | `0.00` |
| No | De 3 a 17 años | 0% | `30.00` |

```python
precio = 45
if tipo == "adulto_mayor":
    descuento = precio * 0.12          # 5.40
elif tipo == "profesor" or tipo == "estudiante":
    descuento = precio * 0.10          # 4.50
else:
    descuento = 0
total = precio - descuento
print(f"Total a pagar: ${total:.2f}")  # Ej. adulto mayor: $39.60
```

---

### 5.4 Estructuras de decisión en PSeInt
```text
Algoritmo ClasificarEdad
    Escribir "Ingrese la edad del visitante:"
    Leer edad
    Si edad < 3 Entonces
        Escribir "Entrada gratis"
    SiNo
        Si edad <= 17 Entonces
            Escribir "Boleto: $30"
        SiNo
            Escribir "Boleto: $45"
        FinSi
    FinSi
FinAlgoritmo
```

> PSeInt usa `Si ... Entonces`, `SiNo`, `FinSi` y los conectores lógicos `Y` (`and`), `O` (`or`) y `NO` (`not`).

---

# TEMA 6: ESTRUCTURA DE REPETICIÓN - WHILE

### 6.1 El ciclo `while`
El ciclo `while` repite un bloque de instrucciones **mientras la condición se cumpla** (`True`). Es un ciclo *controlado por condición*: no sabemos cuántas veces se repetirá, solo que se repite hasta que la condición cambie.

```python
contador = 1
while contador <= 5:
    print(contador)
    contador = contador + 1
```
Salida:
```
1
2
3
4
5
```

> **Riesgo:** si la condición nunca cambia, el ciclo se ejecuta para siempre (ciclo infinito). Siempre modifica la variable de control dentro del bloque.

---

### 6.2 Contadores y Acumuladores
- **Contador:** variable que se incrementa en una cantidad constante (`i = i + 1`) para contar repeticiones.
- **Acumulador:** variable que suma valores variables dentro del ciclo (`total = total + valor`) para totalizar.

```python
# Contador y acumulador combinados
total = 0
i = 1
while i <= 10:
    total = total + i          # acumulador
    i = i + 1                  # contador
print(f"La suma del 1 al 10 es: {total}")   # 55
```

---

### 6.3 La sentencia `break`
`break` **interrumpe por completo** el ciclo en el momento en que se ejecuta.

```python
total = 0
while True:
    costo = float(input("Costo del boleto (0 para terminar): "))
    if costo == 0:
        break                          # sale del ciclo
    total = total + costo
print(f"Total: ${total:.2f}")
```

---

### 6.4 La sentencia `continue`
`continue` **salta el resto de la iteración actual** y pasa a la siguiente vuelta del ciclo.

```python
total = 0
i = 1
while i <= 5:
    edad = int(input(f"Edad del visitante {i}: "))
    i = i + 1
    if edad < 3:
        continue                       # no cobra boleto, siguiente visitante
    if edad <= 17:
        total = total + 30
    else:
        total = total + 45
print(f"Total a pagar: ${total:.2f}")
```

**Verificación:** con edades `2, 15, 30` → el visitante de 2 años se omite con `continue`; el de 15 años suma 30 y el de 30 suma 45. Total = `75.00`.

---

### 6.5 El ciclo `while` en PSeInt
```text
Algoritmo SumarBoletos
    Definir total, costo Como Real
    total <- 0
    Mientras costo <> 0 Hacer
        Escribir "Costo del boleto (0 para terminar):"
        Leer costo
        Si costo = 0 Entonces
            Salir                    // equivale a break
        FinSi
        total <- total + costo
    FinMientras
    Escribir "Total a pagar: $", total
FinAlgoritmo
```

> PSeInt usa `Mientras ... Hacer ... FinMientras` y `Repetir ... Hasta Que`. El equivalente de `break` es `Salir`. Como no existe `continue`, se recomienda incrementar la variable de control antes de continuar o reestructurar la condición.

---

# TEMA 7: DEBUGGING (DEPURACIÓN DE CÓDIGO CON PDB)

### 7.1 Tipos de errores
| Tipo de error | Descripción | Ejemplo |
| :--- | :--- | :--- |
| **Error de sintaxis** | El código no respeta las reglas del lenguaje y no puede ejecutarse. | `print("Hola` (falta la comilla de cierre) |
| **Error de lógica** | El código ejecuta pero produce un resultado incorrecto. | `promedio = a + b + c / 3` (falta paréntesis) |
| **Error de ejecución** (*runtime*) | El código se detiene en plena ejecución por una operación inválida. | `10 / 0` → `ZeroDivisionError` |

---

### 7.2 Depurador PDB: `pdb.set_trace()`
El módulo **PDB** (*Python DeBugger*) permite detener la ejecución en una línea concreta e inspeccionar las variables paso a paso.

```python
import pdb

def calcular_total(precio, descuento):
    pdb.set_trace()                 # el programa se detiene aquí
    precio_final = precio - (precio * descuento)
    return precio_final

print(calcular_total(45, 0.12))     # 45 - (45 * 0.12) = 39.60
```

Cuando el programa llega a `pdb.set_trace()`, aparece el indicador `(Pdb)` y se pueden usar los comandos:

| Comando | Significado |
| :--- | :--- |
| `n` | Ejecuta la siguiente línea (`next`). |
| `c` | Continúa la ejecución hasta el final (`continue`). |
| `p` | Imprime el valor de una variable o expresión (`p precio`). |
| `l` | Lista el código alrededor de la línea actual (`list`). |
| `q` | Sale del depurador (`quit`). |

**Sesión típica:**
```
> .../museo.py(3)calcular_total()
-> precio_final = precio - (precio * descuento)
(Pdb) p precio
45
(Pdb) p precio * descuento
5.4
(Pdb) n
(Pdb) p precio_final
39.6
(Pdb) c
Total a pagar: 39.60
```

---

### 7.3 Depuración paso a paso en PSeInt
PSeInt incluye un modo **"Pasar a paso" (Depurar)** que ejecuta el algoritmo línea por línea y muestra en una tabla el valor actual de cada variable, equivalente al comportamiento de `pdb` en Python. Es la herramienta recomendada para rastrear errores de lógica en pseudocódigo antes de pasar al código real.

**Ejemplo de error lógico a detectar:** en `total = total + precio` dentro de un ciclo sin incremento de contador, el modo de depuración revela que la variable de control nunca cambia (ciclo infinito).

---

# TEMA 8: ESTRUCTURA DE REPETICIÓN - FOR

### 8.1 La función `range()`
La estructura `for` recorre una secuencia de valores generada por `range()`:

- `range(6)` → `0, 1, 2, 3, 4, 5` (del 0 al 5).
- `range(1, 6)` → `1, 2, 3, 4, 5` (inicio, final sin incluir).
- `range(5, 0, -1)` → `5, 4, 3, 2, 1` (paso negativo, cuenta regresiva).

```python
for i in range(1, 6):
    print(i)
```
Salida:
```
1
2
3
4
5
```

---

### 8.2 Sumas y acumuladores con `for`
```python
# Suma del 1 al 10
total = 0
for i in range(1, 11):
    total = total + i
print(f"La suma del 1 al 10 es: {total}")      # 55

# Acumulador de pares
suma_pares = 0
for i in range(1, 11):
    if i % 2 == 0:
        suma_pares = suma_pares + i
print(f"La suma de los pares es: {suma_pares}") # 2+4+6+8+10 = 30
```

---

### 8.3 Patrones con `print`
Al combinar un `for` con un `print` sin salto de línea (parámetro `end`), se pueden dibujar figuras en consola:

```python
for i in range(1, 6):
    print("*" * i)
```
Salida:
```
*
**
***
****
*****
```

Patrón numérico con `for` anidado:
```python
filas = 4
for i in range(1, filas + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
```
Salida:
```
1
12
123
1234
```

---

### 8.4 El ciclo `for` en PSeInt
```text
Algoritmo SumaFor
    Definir i, total Como Entero
    total <- 0
    Para i <- 1 Hasta 10 Hacer
        total <- total + i
    FinPara
    Escribir "La suma del 1 al 10 es: ", total   // 55
FinAlgoritmo
```

> PSeInt usa `Para variable <- inicio Hasta fin Hacer ... FinPara`. Para contar hacia atrás se usa `Hasta fin Con Paso -1`.

---

# ACTIVIDAD INTEGRADORA SEMANAL (PRÁCTICA EN GUÍAS JUPYTER + GIT)

### Consigna para el Estudiante:
Debes crear un Jupyter Notebook llamado `solucion_semana2.ipynb` dentro de tu repositorio local `curso-python-semana2` que contenga:

1. **Celda Markdown:** Un título general, tu nombre completo, matrícula y una explicación breve de las estructuras de decisión y repetición vistas esta semana.
2. **Celda Código (decisiones):** Un programa que pida la edad de un visitante del museo y calcule su boleto según la tabla de precios ($0 para menores de 3 años, $30 de 3 a 17, $45 para mayores de 18), aplicando los descuentos de la tabla de verdad (adulto mayor 12%, profesor 10%, estudiante 10%).
3. **Celda Código (repetición):** Un programa que procese a un número N de visitantes con un ciclo `for` o `while`, usando obligatoriamente al menos una vez `break` y una vez `continue`, y que despliegue el total detallado.
4. **Celda Código (debugging):** Agrega `pdb.set_trace()` dentro de una función de descuento, ejecuta la depuración con los comandos `n`, `p`, `c` y documenta en una celda Markdown qué valor encontraste.
5. **Celda Código (patrones):** Dibuja un patrón en consola con `for` y `print` (triángulo de asteriscos o numérico).

**Subir los cambios a GitHub:**
```bash
git init
git add solucion_semana2.ipynb
git commit -m "feat: completar actividad integradora semana 2"
git push -u origin main
```

---

# DESAFÍOS EXTRAS AUTOEVALUABLES (REFUERZO)

Los siguientes ejercicios extras están diseñados para ser resueltos en tu libreta de Jupyter Notebook para poner a prueba tus habilidades.

### Desafío Extra 1: Calculadora de descuentos con tabla de verdad
Crea un programa que pida el tipo de visitante (`adulto_mayor`, `profesor`, `estudiante` u `otro`) y calcule el precio final de un boleto base de $45, garantizando que solo se aplique un descuento. Verifica que el adulto mayor pague $39.60 y que profesor y estudiante paguen $40.50.

### Desafío Extra 2: Suma acumulada con `while`
Crea un programa que sume números capturados con `input()` hasta que el usuario escriba `0`, momento en el cual el ciclo se rompe con `break` y se muestra el total acumulado.

### Desafío Extra 3: Pirámide con `for`
Crea un programa que pida la altura de una pirámide y la dibuje con asteriscos usando ciclos `for` anidados. Para altura `4` la salida debe ser:
```
*
**
***
****
```

### Desafío Extra 4: Depuración de un promedio
El siguiente código tiene un error de lógica. Depúralo con `pdb.set_trace()` y corrígelo:
```python
a = 8
b = 9
c = 10
promedio = a + b + c / 3
```
El promedio correcto debe ser `9.0`.

### Desafío Extra 5: Validación con operadores lógicos
Crea un programa que pida edad y tipo de visitante. Usa `and`/`not` para determinar si un visitante de 70 años con tipo `adulto_mayor` aplica el descuento del 12% y muestre el total a pagar (`$39.60`).

---

**Nota de referencia:** Recuerda que la Actividad Evaluable 2 "Cobro de Entradas del Museo con Restricciones de Control" (6% de la calificación) integra los cuatro temas de esta semana. Consulta el archivo `Actividad2_CobroMuseo.md` para conocer sus requerimientos exactos y la fecha límite de entrega.
