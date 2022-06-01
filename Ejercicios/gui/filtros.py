import numpy as np

def contraste(imagen):

    temp = np.copy(imagen)
    largo = len(temp)
    ancho = len(temp[1])

    for i in range(0, largo):
        for j in range(0, ancho):
            nuevo_color = 128
            color = temp[i,j]

            if (color < 128):
                nuevo_color = 0
            
            if (color > 128):
                nuevo_color = 255
            
            temp[i,j]=nuevo_color

    return temp

def aclarar(imagen):
    return None

def oscurecer(imagen):
    return None

def mejorar(imagen):
    return None
