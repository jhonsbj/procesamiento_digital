import PySimpleGUI as sg
import cv2
import operaciones
import numpy as np 
from datetime import date

def main():
    
    sg.theme('LightGreen')
    w,h = sg.window.get_screen_size()
    
    menu_sec = ['Abrir',['Abrir A','Abrir B','Guardar',],]

    contenedor1 = [[sg.Image(filename='', key='-IMAGE1-',right_click_menu=menu_sec)]]
    contenedor2 = [[sg.Image(filename='', key='-IMAGE2-',right_click_menu=menu_sec)]]
    contenedor3 = [[sg.Image(filename='', key='-IMAGE3-',right_click_menu=menu_sec)]]

    layout = [
        [sg.Menu(menu_def, tearoff=False, pad=(200,1))],
        [sg.Text('Operaciones',size=(60,1), key='-nombre_archivo-',)],
        [sg.Column(contenedor1, size(w/3, h-100), scrollable=True),
        sg.Column(contenedor2, size(w/3, h-100), scrollable=True, element_justification='center'),
        sg.Column(contenedor3, size(w/3, h-100), scrollable=True, element_justification='center')],
        [sg.Button('Abrir A',size=(15,2), font='Consolas 11'),
        sg.Button('Abrir B',size=(15,2), font='Consolas 11'),
        sg.Button('Guardar', size=(15,2), font='Consolas 11'),
        sg.Button('Salir', size=(15,2), font='Consolas 11')]
    ]

    imagen1 = np.ones((1024,600))
    imagen2 = np.ones((1024,600))
    imagen3 = np.ones((1024,600))

    window = sg.window('Calculadora de Imagenes', layout, location=(0,0))

    while True:
        event, values = window.read(timeout=50)

        #Abrir Imagen A
        if event == 'Abrir A':
            filename = sg.poput_get_file('Abrir archivo (PNG, JPG)', file_types=(("Archivos PNG","*.png"),), no_window=True)
            imagen1 = cv2.imread(filename)
            window['-nombre_archivo-'].update(filename)
        
        #Imagen B
        if event == 'Abrir B':
            filename = sg.poput_get_file('Abrir archivo (PNG, JPG)', file_types=(("Archivos PNG","*.png"),), no_window=True)
            if len(filename):
                imagen2 = cv2.imread(filename)
                window['-nombre_archivo-'].update(filename)

        #Salir
        if event == 'Salir' or event == sg.WIN_CLOSED:
            break;

        #Guardar
        if event == 'Guardar':
            filename = sg.poput_get_file('Guardar imagen (PNG)', save_as=True, file_types=(("Archivos PNG","*.png"),), no_window=True)
            try:
                cv2.imwrite(filename,imagen3)
                window['-nombre_archivo-'].update(filename)
            except:
                sg.poput_error("No se guardó el archivo")
        
        #Suma
        if event == 'Suma':
            imagen = operaciones.suma(imagen1, imagen2)

        #Resta
        if event == 'Resta':
            imagen = operaciones.resta(imagen1, imagen2)

        #Multiplicación
        if event == 'Multiplicacion':
            imagen = operaciones.multiplicacion(imagen1, imagen2)

        #XOR
        if event == 'XOR':
            imagen = operaciones.XOR(imagen1, imagen2)

        #NAND
        if event == 'NAND':
            imagen = operaciones.NAND(imagen1, imagen2)


        imgbytes1 = cv2.imencode('.png',imagen1)[1].tobytes()
        imgbytes2 = cv2.imencode('.png',imagen2)[1].tobytes()
        imgbytes3 = cv2.imencode('.png',imagen3)[1].tobytes()

        window['-IMAGE1-'].update(data=imgbytes)
        window['-IMAGE2-'].update(data=imgbytes)
        window['-IMAGE3-'].update(data=imgbytes)
    
    window.close()
main()