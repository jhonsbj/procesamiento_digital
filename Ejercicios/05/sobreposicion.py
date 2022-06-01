import cv2 as cv
import numpy as np

f = cv.imread('fondo.png')
a = cv.imread('foto2.jpg')
u = cv.imread('segmento.jpg')
r = np.copy(f)
'''temp_f_u = np.copy(f)
temp_a_u = np.copy(f)'''

largo = len(f)
ancho = len(f[0])

for i in range(0, largo):
    color = [0,0,0]
    for j in range(0, ancho): 

        for c in (0,1,2):
            temp_f_u = 0
            temp_a_u = 0

            if f[i,j,c] and not u[i,j,c]:
                temp_f_u = f[i,j,c] 

            if(a[i,j,c] and u[i,j,c]):
                temp_a_u = a[i,j,c]

            color = temp_f_u + temp_a_u
                
            r[i,j,c] = color

cv.imshow('Sobreposicion',r)
cv.waitKey(0)
cv.destroyAllWindows()

nombre = "sobreposicion.png"
cv.imwrite(nombre, r)

