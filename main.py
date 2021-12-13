# Daniel Aniśko
# Skrypt obsługi komputera za pomocą kamerki internetowej
# TODO
# - LPM (Kciuk i wskazujący) GIT
# - PPM (Kciuk i środkowy) GIT
# - SCROLL (N/A)
# - PORUSZANIE KURSOREM WRAZ Z RUCHEM DŁONI GIT
# - WŁĄCZENIE KLAWIATURY (Kciuk i mały) GIT
# - Napisać własną klawiaturę

import cv2
import mouse
import mediapipe
import os
import numpy
import math
import time
import tkinter as tk
from Reka import detekcja
from Myszka import Myszka
video = cv2.VideoCapture(0)
width = 640
height = 480
video.set(3, width)
video.set(4, height)
reka = detekcja()
myszka = Myszka()

while True:
    sukces,obraz = video.read()
    obraz = cv2.flip(obraz,1)
    obrazRGB = cv2.cvtColor(obraz,cv2.COLOR_BGR2RGB)
    reka.znajdzRece(obraz)
    lista = reka.znajdzOpuszkiPalcow(obraz,width,height)
    #print(lista)
    punktS = myszka.wezKoordynaty(lista, "srodek")
    punktM = myszka.wezKoordynaty(lista, "srodkowy")
    punktW = myszka.wezKoordynaty(lista, "wskazujacy")
    punktK = myszka.wezKoordynaty(lista, "kciuk")
    punktSer = myszka.wezKoordynaty(lista, "serdeczny")
    punktMaly = myszka.wezKoordynaty(lista, "maly")
    myszka.rysujProstokat(obraz, 50, 200, 580 ,460)
    if punktS != None and (50 <=punktS[0] <= 580) and (200 <=punktS[1] <= 460):
        myszka.podazajZaReka((punktS[0] - 50) * 3.8,(punktS[1] - 200) * 4.5)
        time.sleep(0.1)
        myszka.polaczPalce(obraz,punktK[0],punktK[1],punktMaly[0],punktMaly[1])
        odlegloscLPM = myszka.znajdzOdleglosc(punktM[0],punktM[1],punktW[0],punktW[1])
        odlegloscPPM = myszka.znajdzOdleglosc(punktK[0],punktK[1],punktM[0],punktM[1])
        odlegloscKlw = myszka.znajdzOdleglosc(punktK[0],punktK[1],punktMaly[0],punktMaly[1])
        myszka.lewyPrzyciskMyszki(odlegloscLPM)
        myszka.prawyPrzyciskMyszki(odlegloscPPM)
        myszka.otworzKlawiature(odlegloscKlw)
    print(punktS)
    cv2.imshow("Obraz", obraz)
    cv2.waitKey(1)