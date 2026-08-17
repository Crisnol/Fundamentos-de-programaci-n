##CALCULADORA DE TIEMPO DIGITAL

userName = input("Bienvenido ingrese su nombre: ")

timeYoutube = float(input("Ingrese el tiempo ocupado en Youtube (hrs): "))
timeInstagram = float(input("Ingrese el tiempo ocupado en Instagram (hrs): "))
timeWhatsApp = float(input("Ingrese el tiempo ocupado en WhatsApp (hrs): "))
timeSpotify = float(input("Ingrese el tiempo ocupado en Spotify (hrs): "))
timeNetflix = float(input("Ingrese el tiempo ocupado en Netflix (hrs): "))
timeGames = float(input("Ingrese el tiempo ocupado en Videojuegos (hrs): "))

totalTime = timeYoutube + timeInstagram + timeWhatsApp + timeSpotify + timeNetflix + timeGames
pocentaje = (totalTime/24)*100

print(f"\n{userName}, Este es tu resumen diario del tiempo en diferentes plataformas")
print(f"Tiempo total acumulado: {totalTime} hrs")
print(f"Porcentaje de tu dia: {pocentaje}%\n")

