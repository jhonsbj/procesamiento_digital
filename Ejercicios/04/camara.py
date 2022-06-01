import PySimpleGUI as sg
from datetime import date
import cv2

def main():
    #Conectamos a la webcam
    camara = cv2.VideoCapture(0)

    #Elegimos un tema de PySimpleGUI
    sg.theme('DarkGreen5')
    #Definimos los elementos de la interfaz grafica
    layout = [[sg.Image(filename='', key='-image-')],
              [sg.Button('Tomar Fotografia'),sg.Button('Salir')]]
    #Creamos la interfaz grafica
    window = sg.Window('Camara',
                       layout,
                       no_titlebar=False,
                       location=(0, 0))

    image_elem = window['-image-']

    numero = 0
    
    #Iniciamos la lectura y actualizacion
    while camara.isOpened():
        #Obtenemos informacion de la interfaz grafica y video
        event, values = window.read(timeout=0)
        ret, frame = camara.read()

        #Si salimos
        if event in ('Salir', None):
            break

        #Si tomamos foto
        elif event == 'Tomar Fotografia':
            ruta = sg.popup_get_folder(title='Guardar Fotografia', message="Carpeta destino")
            cv2.imwrite(ruta + "/" + str(date.today()) + str(numero) + ".png", frame)

        if not ret:
            break

        #Mandamos el video a la GUI
        imgbytes = cv2.imencode('.png', frame)[1].tobytes()  # ditto
        image_elem.update(data=imgbytes)
        numero = numero + 1

main()