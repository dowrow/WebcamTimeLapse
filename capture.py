#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Descarga imágenes de IPcams públicas para hacer TimeLapses """

import urllib
import time
import sys
import os

def main(argv):
    """ Descarga una imagen desde una url dada periódicamente y la guarda en una carpeta """
    if len(sys.argv) < 5:
        sys.exit('Este script requiere 4 argumentos: \n'\
        'python capture.py <nombre_de_la_carpeta> '\
        '<horas_a_capturar> <intervalo_en_segundos> <url_de_la_webcam>')
    directory = argv[1]
    hours = int(argv[2])
    seconds_step = int(argv[3])
    webcam_url = argv[4]
    if not os.path.exists(directory):
        os.makedirs(directory)
    print 'Iniciando captura de {} horas.'.format(str(hours))
    print 'Las imágenes se almacenarán en la carpeta "{}".'.format(directory)
    i = 1
    while i * seconds_step <= 60 * 60 * hours:
        image = open(directory + '/' + str(i) + '.jpg', 'wb')
        image.write(urllib.urlopen(webcam_url).read())
        image.close()
        print '>Capturada imagen {}/{}.'.format(str(i), str((hours * 60 * 60) / seconds_step))
        i += 1
        time.sleep(seconds_step)
    exit('La captura se completó correctamente.')

if __name__ == "__main__":
    main(sys.argv)
