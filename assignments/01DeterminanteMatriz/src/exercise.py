#Desarrolla una función en Python que reciba una matriz de números enteros de tamaño 2x2 
#y calcule su determinante. det = a*d - c*b

def main():
    #escribe tu código abajo de esta línea
    matriz = []
    det = 0
    for i in range(2) :
        fila = []
        for j in range(2) :
            valor = int(input('Valor '+str(j+1)+' de la fila '+str(i+1)+' : '))
            fila.append(valor)
        matriz.append(fila)
    print(matriz[0])
    print(matriz[1])
    det = ((matriz[0][0]) * (matriz[1][1])) - ((matriz[0][1])*(matriz[1][0]))
    print('La determinante de la matriz 2x2 es: '+str(det))

if __name__=='__main__':
    main()
