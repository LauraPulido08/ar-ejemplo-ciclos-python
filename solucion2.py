# Problema01 (uso ciclo for)
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

#El uso del ciclo for es cuando conocemos a cantidad de veces
#que se va a repetir el ciclo, por eso se debe pedir la cantidad
#de jugadores que se va a ingresar primero

cantidad_jugadores = int(input("¿Cuántos jugadores desea ingresar?: "))

#Bucle for
for contador in range(1, cantidad_jugadores+1): #se le suma 1 a cantidad para
                                                #para que se incluya la cantidad ingresada
    print(f"\nIngrese la información del jugador {contador}:")
    nombre = input("Nombre del jugador: ")
    posicion = input("Posición en el campo de juego: ")
    #edad = input("Edad del jugador: ") #edad en str
    #edad = int(edad) #edad en int
    edad = int(input("Edad del jugador: "))
    #estatura = input("Estatura del jugador (en metros): ") #estatura en str
    #estatura = float(estatura) #estatura en float
    estatura = float(input("Estatura del jugador: "))

# Acumulación de datos en cadenas

    reporte_jugadores = f"{reporte_jugadores}{contador}. {nombre} - {posicion}, edad {edad}, estatura {estatura:.2f}\n"
    reporte_edades = f"{reporte_edades}{edad}\n"

    suma_edades = suma_edades + edad
    suma_estaturas = suma_estaturas + estatura

#Cálculo de promedios

if cantidad_jugadores > 0:
    promedio_edades = suma_edades/cantidad_jugadores
    promedio_estaturas = suma_estaturas/cantidad_jugadores
else:
    promedio_edades = 0
    promedio_estaturas = 0

#Impresión del reporte final

print(reporte_jugadores)
print(reporte_edades)
print(f"Promedio de edades: {promedio_edades:.1f}")
print(f"Promedio de estaturas: {promedio_estaturas:.2f}")

"""
salida:
Listado de Jugadores
1. Alexander Dominguez - Arquero, edad 32, estatura 1.95
2. Xavier Arreaga - Defensa, edad 24, estatura 1.85
3. Moisés Caicedo - Mediocentro, edad 19, estatura 1.88
4. Ángel Mena - Delantero, edad 32, estatura 1.75
5. Michael  Estrada - Delantero, edad 27, estatura 1.93

Listado de Edades
32
24
19
32
27

Promedio de edades: 26.8
Promedio de estaturas: 1.87

"""