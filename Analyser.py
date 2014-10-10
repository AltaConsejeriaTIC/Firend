#!/usr/bin/env python

import RInteractor as ri

print ri.focos

kilometrosNorteSur = 50 # coordenadas verticales esquina superior derecha
kilometrosEsteOeste = 60 # coordenadas horizonales esquina superior derecha
areaPorPixel = 2 # cantidad de metros cuadrados contenidos en un pixel

# debido a la gran cantidad de focos en la imagen solo se procesar? el primero
# (as? no bloquearan la cuenta por spam)

coordenadaX = (ri.focos[0,0]*areaPorPixel)+kilometrosEsteOeste
coordenadaY = (ri.focos[0,1]*areaPorPixel)+kilometrosNorteSur

