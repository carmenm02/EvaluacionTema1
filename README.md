<h1 align="center">	Evaluacion Tema 1</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/carmenm02/EvaluacionTema1.git)

```
## Ejercicio1 :

matriz = [
    [1,1,1,3],
    [2,2,2,7],
    [3,3,3,9],
    [4,4,4,13]
]

matriz[1][-1] = sum(matriz[1][:-1])
matriz[3][-1] = sum(matriz[3][:-1])

print(matriz)
```
```
##Ejercicio2:

cadenadetexto = input("Introduce una cadena de texto: ")

print("¿Es su longitud mayor o igual a 3 y menor de 10?",
len(cadenadetexto) >= 3 and len(cadenadetexto) < 10)
```
```
##Ejercicio 3:

lista1 = list(range(0,11))
print(lista1)
lista2 = list(range(-10,1))
print(lista2)
lista3 = list(range(0,21,2))
print(lista3)
lista4 = list(range(-19,0,2))
print(lista4)
lista5 = list(range(0,51,5))
print(lista5)
```
```
##Ejercicio4:

import sys
from pyparsing import col

if len(sys.argv) == 3:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])

    if filas < 1 or filas > 9 or  columnas < 1 or columnas > 9:
        print("Error")
    else:
        for i in range(filas):
            print(" ")
            for c in range(columnas):
                print(" * ", end='')
else:
    print("Error")
```
