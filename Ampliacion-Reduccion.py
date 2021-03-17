import cv2 as cv
import numpy as np

imagen=cv.imread("image.png",0) 
largo = len(imagen)
ancho = len(imagen[0])
temp_aumento = np.zeros((largo*2,ancho*2),dtype=np.uint8)

cv.imshow("Imagen Original",imagen)
cv.waitKey(0)
cv.destroyAllWindows()

#Aumentar tamaño
for i in range(0, largo):
    i_2 = 2*i
    for j in range(0, ancho):
        j_2 = 2*j
        temp_aumento[i_2,j_2] = imagen[i,j]
        temp_aumento[i_2,j_2+1] = imagen[i,j]
        temp_aumento[i_2+1,j_2] = imagen[i,j]
        temp_aumento[i_2+1,j_2+1] = imagen[i,j]

cv.imshow("Aumento de la imagen",temp_aumento)
cv.waitKey(0)
cv.destroyAllWindows()


