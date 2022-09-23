#Para hacer el punto 2 debo hacer primero el 1, ya que necesito crear antes las filas y las columnas

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

    