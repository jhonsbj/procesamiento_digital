import numpy as np
import cv2 as cv

def interpolacion (C1,D1,pixel_actual, pixel_derecha, pixel_abajo, pixel_esquina):
    alfa = 1-C1
    beta = 1-(1-C1)
    alfa_p = 1-D1
    beta_p = 1-(1-D1)

    return alfa*alfa_p*pixel_actual + beta*alfa_p*pixel_derecha + alfa*beta_p*pixel_abajo + alfa_p*beta_p*pixel_esquina

imagen=cv.imread("foto.png",0) 

N, M  = imagen.shape

escalado = 10

N_p = int(N*escalado)
M_p = int(M*escalado)

temp = np.zeros((N_p, M_p),dtype=np.uint8)

cv.imshow("Imagen original %s " % str(imagen.shape), imagen)
cv.waitKey(0)
cv.destroyAllWindows()

F1 = N/N_p
F2 = M/M_p

for i_p in range (0,N_p):

    p=i_p*F1
    C1 = p - abs(p)
    i = int(p) 

    for j_p in range(0,M_p):

        q=j_p*F2
        D1 = q-abs(q)
        j = int(q)
        try: 
            temp[i_p,j_p] = interpolacion(C1,D1,imagen[i,j],imagen[i+1,j],imagen[i,j+1],imagen[i+1,j+1])
        except:
            temp[i_p,j_p] = imagen[i,j]

cv.imshow("Imagen Escalada al %s" % str(temp.shape), temp)
cv.waitKey(0)
cv.destroyAllWindows()