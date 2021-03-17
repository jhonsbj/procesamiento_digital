

def negativo_color(im):
    tiempoIn = time.time()
    ruta = ("pubg.png" + im)
    im = Image.open(ruta)
    im.show()
    im5 = im
    i = 0
    while i < im5.size[0]:
        j = 0
        while j < im5.size[1]:
            r, g, b = im5.getpixel((i,j))
            rn = 255 - r
            gn = 255 - g
            bn = 255 - b
            pixel = tuple([rn, gn, bn])
            im5.putpixel((i,j), pixel)
            j+=1
        i+=1
    im5.show()
    tiempoFin = time.time()
    print('El Proceso Tardo: ', tiempoFin - tiempoIn, 'Segundos')