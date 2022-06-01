import numpy as np
import math
import cv2
    
def interpolacion(temp_imagen, escala):

    N, M = temp_imagen.shape # El tamaño de la imagen de entrada (fila, columna)
    
            # Tamaño de la imagen de salida
    N1 = int(N * escala)
    M1= int(M * escala)
    
    nueva_imagen = np.zeros ((N1, M1)) # imagen de salida
    
    for i in range(N1-1):
        for j in range(M1-1):
            temp_x = i / N1 * N
            temp_y = j / M1* M
    
            x1 = int(temp_x)
            y1 = int(temp_y)
    
            x2 = x1
            y2 = y1 + 1
    
            x3 = x1 + 1
            y3 = y1
    
            x4 = x1 + 1
            y4 = y1 + 1
    
            u = temp_x - x1
            v = temp_y - y1
    
            if x4 >= N:
                x4 = N - 1
                x2 = x4
                x1 = x4 - 1
                x3 = x4 - 1
                
            if y4 >= M:
                y4 = M - 1
                y3 = y4
                y1 = y4 - 1
                y2 = y4 - 1
    
            nueva_imagen[i, j] = (1-u)*(1-v)*int(temp_imagen[x1, y1]) + (1-u)*v*int(temp_imagen[x2, y2]) + u*(1-v)*int(temp_imagen[x3, y3]) + u*v*int(temp_imagen[x4, y4])
    return nueva_imagen
    
# Read image
imagen = cv2.imread("lena_gray_25.png",0).astype(np.uint8)
salida = interpolacion(imagen,10).astype(np.uint8)
# Save result
cv2.imshow("result", salida)
cv2.waitKey(0)
cv2.destroyAllWindows()