###Encabezado de script
numero_global = 8
arrreglo_numeros = [0]*numero_global
###[0],[0],[0],[0]

###Funciones secundarias
def sumatoria(numero_local):
    resultado_sumatoria = 0
    resultado_sumatoria_2 = 0

    for i in range(numero_local):
        arrreglo_numeros[i]= int(input("Ingrese el valor de la posicion del arreglo: \n"))
        resultado_sumatoria = resultado_sumatoria + arrreglo_numeros[i]
        resultado_sumatoria_2 += arrreglo_numeros[1]

    return resultado_sumatoria_2

###Funcion principal
def main():
    resultado_main = 0

    print('Actividad 03 - Sumatoria acumulada - Espacio de memoria estatico')
    resultado_main = sumatoria(numero_global)

    print('El resultado de la sumatoria es: ', resultado_main)

if __name__ == "__main__":
    main()