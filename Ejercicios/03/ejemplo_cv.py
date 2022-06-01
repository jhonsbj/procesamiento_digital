import cv2 as cv
import numpy as np
import pymsgbox

imagen = cv.imread('lena.png',0)

cv.imshow('Lena',imagen)
cv.waitKey(0)
cv.destroyAllWindows()

temp = np.copy(imagen)
largo = len(temp)
ancho = len(temp[0])

pymsgbox.alert('Inicio del filtro de perfilado', 'Filtros')
nuevo_pixel = 0
perfilado = [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]
for i in range(1, largo-1):
    for j in range(1, ancho-1):
        color = 0
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                color = color + perfilado[x+1][y+1] * (imagen[i+x,j+y]*1) 

        if (color < 0):
            color = 0

        if(color > 255):
            color = 255

        temp[i,j] = color

pymsgbox.alert('FIN del filtro de perfilado', 'Filtros')

cv.imshow('Filtro de perfilado',temp)
cv.waitKey(0)
cv.destroyAllWindows()

guardar=pymsgbox.confirm('Desea guardar la imagen?', 'Filtros', ["SI", "NO"])
#guardar = input("Guardar la imagen ? S/N ")

if (guardar.upper() == "SI"):
    nombre = pymsgbox.prompt('Nombre del archivo', default='temp.png')
    cv.imwrite(nombre, temp)

