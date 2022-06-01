import cv2 as cv
import numpy as np

f = cv.imread('/home/lunatico/code/imagendigitial/images/foto_a.jpg')
a = cv.imread('/home/lunatico/code/imagendigitial/images/foto2.jpg')
u = cv.imread('/home/lunatico/code/imagendigitial/images/umbral.png', 0)
r = np.copy(f)

largo = len(a)
ancho = len(a[0])

for i in range(0, largo):
    for j in range(0, ancho): 

        for c in (0,1,2):
            temp_f_u = 0
            temp_a_u = 0

            try:
                if f[i+250,j+50,c] and not u[i,j]:
                    temp_f_u = f[i+250,j+50,c] 

                if(a[i,j,c] and u[i,j]):
                    temp_a_u = a[i,j,c]

                r[i+250,j+50,c]  = temp_f_u + temp_a_u
            except Exception :
                continue
    
cv.imshow('Sobreposicion',r)
cv.waitKey(0)
cv.destroyAllWindows()

nombre = "sobreposicion.png"
cv.imwrite(nombre, r)

