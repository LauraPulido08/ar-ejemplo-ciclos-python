# Problema01 (use ciclo while)
# Generar una solución que permita ingresar jugadores de fútbol; por cada jugador se debe solicitar:
# Nombre el jugador
# Posición en el campo de juego
# Edad
# Estatura

# Inicialización de variables
reporte_jugadores = "Listado de Jugadores\n"
reporte_edades = "Listado de Edades\n"
suma_edades = 0
suma_estaturas = 0
contador = 0  # Contador para numeración de jugadores
bandera = True

# Bucle para ingreso de datos
while bandera:
    print("\nIngrese la información del jugador:")
    nombre = input("Nombre del jugador: ")
    posicion = input("Posición en el campo de juego: ")
    edad = input("Edad del jugador: ") #edad en str
    edad = int(edad) #edad en int
    #edad=18
    estatura = input("Estatura del jugador (en metros): ") #estatura en str
    estatura = float(estatura) #estatura en float
    #estatura= 1.62

    # Acumulación de datos en cadenas
    contador = contador + 1
    #contador=     0    + 1  | 1
    reporte_jugadores = f"{reporte_jugadores}{contador}. {nombre} -{posicion}, edad {edad}, estatura {estatura:.2f}\n"
    reporte_edades = f"{reporte_edades}{edad}\n"
    
    # Acumulación de sumas para promedio
    suma_edades = suma_edades + edad
    #suma_edades=      0      + 18  | 18
    suma_estaturas = suma_estaturas + estatura
    #suma_estaturas=        0       + 1.62  | 1.62

    # Preguntar al usuario si desea continuar
    continuar = input("¿Desea ingresar otro jugador? (Sí/No): ")
    if continuar != "si":
        bandera = False

# Cálculo de promedios
if contador > 0:
    promedio_edades = suma_edades / contador
    promedio_estaturas = suma_estaturas / contador
else:
    promedio_edades = 0
    promedio_estaturas = 0

# Impresión del reporte final
print(reporte_jugadores)
print(reporte_edades)
print(f"Promedio de edades: {promedio_edades:.1f}")
print(f"Promedio de estaturas: {promedio_estaturas:.2f}")

"""
salida:
Listado de Jugadores
1. Alexander Dominguez -Arquero, edad 32, estatura 1.95
2. Xavier Arreaga -Defensa, edad 24, estatura 1.85
3. Moisés Caicedo -Mediocentro, edad 19, estatura 1.88
4. Ángel Mena -Delantero, edad 32, estatura 1.75
5. Michael Estrada  -Delantero, edad 27, estatura 1.93

Listado de Edades
32
24
19
32
27

Promedio de edades: 26.8
Promedio de estaturas: 1.87
"""