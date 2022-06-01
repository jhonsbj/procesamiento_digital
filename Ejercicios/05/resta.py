import cv2 as cv
import numpy as np

imagen1 = cv.imread('foto1.jpg')
imagen2 = cv.imread('foto2.jpg')

cv.imshow('Imagen A',imagen1)
cv.waitKey(0)
cv.imshow('Imagen B',imagen2)
cv.waitKey(0)
cv.destroyAllWindows()

temp = np.copy(imagen1)
largo = len(temp)
ancho = len(temp[0])

for i in range(0, largo):
    color = [0,0,0]
    for j in range(0, ancho): 
        color[0] = imagen1[i,j,0]*1 - imagen2[i,j,0]*1
        color[1] = imagen1[i,j,1]*1 - imagen2[i,j,1]*1
        color[2] = imagen1[i,j,2]*1 - imagen2[i,j,2]*1
            
        temp[i,j,0] = abs(color[0])
        temp[i,j,1] = abs(color[1])
        temp[i,j,2] = abs(color[2])

cv.imshow('Suma de Imagenes',temp)
cv.waitKey(0)
cv.destroyAllWindows()

nombre = "segmentacion.png"
cv.imwrite(nombre, temp)

