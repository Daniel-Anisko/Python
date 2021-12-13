import math
import cv2
import mouse
import os


class Myszka():
    def __init__(self):
        pass

    def wezKoordynaty(self, tab, palec):
        if len(tab) > 0:
            if palec == "srodek":
                x = tab[0][1]
                y = tab[0][2]
                return x, y
            if palec == "kciuk":
                x = tab[1][1]
                y = tab[1][2]
                return x, y
            elif palec == "wskazujacy":
                x = tab[2][1]
                y = tab[2][2]
                return x, y
            elif palec == "srodkowy":
                x = tab[3][1]
                y = tab[3][2]
                return x, y
            elif palec == "serdeczny":
                x = tab[4][1]
                y = tab[4][2]
                return x, y
            elif palec == "maly":
                x = tab[5][1]
                y = tab[5][2]
                return x, y

    def rysujProstokat(self, okno, x1, y1, x2, y2):
        cv2.rectangle(okno, (x1, y1), (x2, y2), (255, 0, 0))

    def polaczPalce(self, okno, x1, y1, x2, y2):
        cv2.line(okno, (x1, y1), (x2, y2), (255, 0, 0))

    def podazajZaReka(self, x, y):
        mouse.move(x, y)
    def znajdzOdleglosc(self,x1,y1,x2,y2):
        odleglosc = math.hypot(x2-x1,y2-y1)
        return odleglosc
    def lewyPrzyciskMyszki(self,odleglosc):
        if odleglosc <= 20:
            mouse.click()
    def prawyPrzyciskMyszki(self,odleglosc):
        if odleglosc <= 20:
            mouse.right_click()
    def otworzKlawiature(self,odleglosc):
        if odleglosc <= 20:
            #os.startfile("keyboard.py")

