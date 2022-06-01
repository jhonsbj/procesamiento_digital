import cv2 as cv
import numpy as np

imagen1 = cv.imread('fondo3.jpg') # imagen normal
imagen2 = cv.imread('umbral.png',0) # imagen binaria

cv.imshow('Imagen A',imagen1)
cv.waitKey(0)
cv.imshow('Imagen B',imagen2)
cv.waitKey(0)
cv.destroyAllWindows()

temp = np.copy(imagen1)
largo = len(temp)
ancho = len(temp[0])

for i in range(0, largo):
    for j in range(0, ancho): 
        color = [0,0,0]
        try:
            if (imagen1[i,j,0] or imagen2[i,j]):
                color[0] = imagen1[i,j,0]

            if (imagen1[i,j,1] or imagen2[i,j]):
                color[1] = imagen1[i,j,1]

            if (imagen1[i,j,2] or imagen2[i,j]):
                color[2] = imagen1[i,j,2]
                
            temp[i,j,0] = color[0]
            temp[i,j,1] = color[1]
            temp[i,j,2] = color[2]
        except Exception:
            continue

cv.imshow('OR',temp)
cv.waitKey(0)
cv.destroyAllWindows()

nombre = "OR.png"
cv.imwrite(nombre, temp)


temp = np.copy(imagen1)
largo = len(temp)
ancho = len(temp[0])

for i in range(0, largo):
    for j in range(0, ancho): 
        color = [0,0,0]
        try:
            if (imagen1[i,j,0] and imagen2[i,j]):
                color[0] = imagen1[i,j,0]

            if (imagen1[i,j,1] and imagen2[i,j]):
                color[1] = imagen1[i,j,1]

            if (imagen1[i,j,2] and imagen2[i,j]):
                color[2] = imagen1[i,j,2]
                
            temp[i,j,0] = color[0]
            temp[i,j,1] = color[1]
            temp[i,j,2] = color[2]
        except Exception:
            continue

cv.imshow('AND',temp)
cv.waitKey(0)
cv.destroyAllWindows()

nombre = "AND.png"
cv.imwrite(nombre, temp)

temp = np.copy(imagen1)
largo = len(temp)
ancho = len(temp[0])

for i in range(0, largo):
    for j in range(0, ancho): 
        color = [0,0,0]
        try:
            
            if (imagen1[i,j,0] and not imagen2[i,j]):
                color[0] = imagen1[i,j,0]

            if (imagen1[i,j,1] and not imagen2[i,j]):
                color[1] = imagen1[i,j,1]

            if (imagen1[i,j,2] and not imagen2[i,j]):
                color[2] = imagen1[i,j,2]
                
            temp[i,j,0] = color[0]
            temp[i,j,1] = color[1]
            temp[i,j,2] = color[2]
        except Exception:
            continue

cv.imshow('NAND',temp)
cv.waitKey(0)
cv.destroyAllWindows()

nombre = "NAND.png"
cv.imwrite(nombre, temp)

temp = np.copy(imagen1)
largo = len(temp)
ancho = len(temp[0])

for i in range(0, largo):
    for j in range(0, ancho): 
        color = [0,0,0]
        try:
                
            if (imagen1[i,j,0] or imagen2[i,j]):
                color[0] = imagen1[i,j,0]

            if (imagen1[i,j,1] or imagen2[i,j]):
                color[1] = imagen1[i,j,1]

            if (imagen1[i,j,2] or imagen2[i,j]):
                color[2] = imagen1[i,j,2]

            if (imagen1[i,j,0] and imagen2[i,j]):
                color[0] = 0

            if (imagen1[i,j,1] and imagen2[i,j]):
                color[1] = 0

            if (imagen1[i,j,2] and imagen2[i,j]):
                color[2] = 0
                
            temp[i,j,0] = color[0]
            temp[i,j,1] = color[1]
            temp[i,j,2] = color[2]
        except Exception:
            continue

cv.imshow('XOR',temp)
cv.waitKey(0)
cv.destroyAllWindows()

nombre = "XOR.png"
cv.imwrite(nombre, temp)