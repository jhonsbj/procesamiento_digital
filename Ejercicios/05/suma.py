import cv2 as cv
import numpy as np

imagen1 = cv.imread('edificio_2.jpg',0)
imagen2 = cv.imread('yo_mero.png',0)

cv.imshow('Imagen A',imagen1)
cv.waitKey(0)
cv.imshow('Imagen B',imagen2)
cv.waitKey(0)
cv.destroyAllWindows()

temp = np.copy(imagen1)
largo = len(temp)
ancho = len(temp[0])

for i in range(1, largo):
    for j in range(1, ancho):
        color = imagen1[i,j]*0.4 + imagen2[i,j]*0.6

        temp[i,j] = color 


cv.imshow('Suma de Imagenes',temp)
cv.waitKey(0)
cv.destroyAllWindows()

nombre = "suma.png"
cv.imwrite(nombre, temp)

