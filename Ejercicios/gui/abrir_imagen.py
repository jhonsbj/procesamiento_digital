import PySimpleGUI as sg
import cv2
import filtros
import numpy as np
from datetime import date

def main():
    sg.theme('LightGreen')

    layout = [
      [sg.Text('Filtros', size=(60, 1), justification='center')],
      [sg.Image(filename='', key='-IMAGE-')],
      [sg.Button('Abrir', size=(10,1)), sg.Button('Umbral', size=(10,1)), sg.Button('Guardar', size=(10,1)), sg.Button('Exit', size=(10, 1))]
    ]

    imagen = np.ones((256,256))

    window = sg.Window('OpenCV Integration', layout, location=(800, 400))

    while True:
        event, values = window.read(timeout=20)

        if event == 'Exit' or event == sg.WIN_CLOSED:
            break

        if event == 'Umbral':
            print("Aplicar umbral")
            print(imagen.shape)
            imagen = filtros.contraste(imagen)

        if event == 'Abrir':
            print("Abrir imagen")
            filename = sg.popup_get_file('Abrir archivo (PNG, JPG)') # Abrir solo imagenes JPG o PNG
            imagen = cv2.imread(filename,0) #Validar que el nombre de archivo no este en blanco
            #imagen = cv2.imread("images/004.png",0)
        
        if event == 'Guardar':
            filename = sg.popup_get_file('Guardar Fotografia (PNG) to save to', save_as=True)
            #ruta = sg.popup_get_folder(title='Guardar Fotografia', message="Carpeta destino")
            cv2.imwrite(filename, imagen)
        
        imgbytes = cv2.imencode('.png', imagen)[1].tobytes()
        window['-IMAGE-'].update(data=imgbytes)

    window.close()


main()
