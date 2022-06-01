#Transformación básica

import cv2 as cv
import numpy as np

imagen=cv.imread("edificio.jpg",0) 

temp = np.copy(imagen)
mx = len(temp)-1
my = len(temp[0])-1

temp_rotada = np.zeros((my+1,mx+1),dtype=np.uint8)

cv.imshow("Imagen original", imagen)
cv.waitKey(0)
cv.destroyAllWindows()

#Rota la imagen 180 grados
for x in range(0,mx):
    for y in range(0,my):
        temp[x,y]=imagen[mx-x,my-y]

cv.imshow("Rotacion 180",temp)
cv.waitKey(0)
cv.destroyAllWindows()

#Rota la imagen 90 grados
for x in range (0,my):
    for y in range(0,mx):
        temp_rotada[x,y]=imagen[y,my-x]

cv.imshow("Rotacion 90 grados",temp_rotada)
cv.waitKey(0)
cv.destroyAllWindows()

#Rota la imagen 270 grados
for x in range (0,my):
    for y in range(0,mx):
        temp_rotada[x,y]=imagen[mx-y,x]   

cv.imshow("Rotacion 270 grados",temp_rotada)
cv.waitKey(0)
cv.destroyAllWindows()

#Reflejo vertical
for x in range (0,mx):
    for y in range(0,my):
        temp[x,y]=imagen[mx-x,y]

cv.imshow("Reflejo vertical",temp)
cv.waitKey(0)
cv.destroyAllWindows()

#Reflejo horizontal
for x in range (0,mx):
    for y in range(0,my):
        temp[x,y]=imagen[x,my-y]

cv.imshow("Reflejo horiontal",temp)
cv.waitKey(0)
cv.destroyAllWindows()