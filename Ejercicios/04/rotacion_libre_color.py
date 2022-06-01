import numpy as np
import math
import cv2

imagen = cv2.imread("lena.png").astype(np.uint8) #Abrir la imagen a colores

N, M, canal = imagen.shape #Obtener las dimensiones de la imagen en canales

N2 = N/2
M2 = M/2
ct = math.cos(math.radians(35)) 
st = math.sin(math.radians(35))

x = [0,N-1,0,N-1]
y = [0,0,M-1,M-1]
p = [0,0,0,0]
q = [0,0,0,0]

p1, p2 = (0,0)
q1, q2 = (0,0)

for k in range(4):
    xp = x[k] - N2
    yp = y[k] - M2
    xr = xp*ct + yp*st
    yr = -xp*st + yp*ct
    p[k] = xr + N2
    q[k] = yr + M2

for temp in p:
    if temp < p1:
        p1 = temp
    
    if temp > p2:
        p2 = temp

for temp in q:
    if temp < q1:
        q1 = temp
    
    if temp > q2:
        q2 = temp


Np = p2-p1+1
Mp = q2-q1+1

imagen_rot = np.zeros((int(Np), int(Mp), 3),dtype=np.uint8) #Crear la nueva matriz de la imagen con 3 canales

print(imagen_rot.shape)
#sx = p1 + N2
#sy = q1 + M2
sx=int(Np/2-1)
sy=int(Mp/2-1)

for j in range(0,M):
    yp = j - M2
    for i in range(0,N):
        xp = i - N2
        xr = xp*ct + yp*st
        yr = -xp*st + yp*ct
        ip = int(xr + sx)
        jp = int(yr + sy)

        #for c in range(3):
        #imagen_rot[ip, jp, c] =  imagen[i, j,c]
        imagen_rot[ip, jp] =  imagen[i, j] #Canal Azul (B)
        #imagen_rot[ip, jp,1] =  imagen[i, j,1] #Canal Verde(G)
        #imagen_rot[ip, jp,2] =  imagen[i, j,2] #Canal Rojo(R)
        


cv2.imshow("result", imagen_rot)
cv2.waitKey(0)
cv2.destroyAllWindows()