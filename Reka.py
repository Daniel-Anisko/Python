import cv2
import mediapipe as mp
class detekcja():
    def __init__(self, czyZdjecie=False, maxLiczbaDloni=1, minPewnoscDetekcji=0.7, minPewnoscPodazania=0.7):
        self.czyZdjecie = czyZdjecie #Parametr mówiący o tym czy
        self.maxLiczbaDloni = maxLiczbaDloni
        self.minPewnoscDetekcji = minPewnoscDetekcji
        self.minPewnoscPodazania = minPewnoscPodazania
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.czyZdjecie,self.maxLiczbaDloni,self.minPewnoscDetekcji,self.minPewnoscPodazania)

    def znajdzRece(self,okno):
        RGB = cv2.cvtColor(okno, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(RGB)


    def znajdzOpuszkiPalcow(self,okno,width,height):
        tabelaPrzechowujacaOpuszki = []
        if self.results.multi_hand_landmarks:
            palceReki = self.results.multi_hand_landmarks[0]
            for numerPalca, palec in enumerate(palceReki.landmark):
                x = int(palec.x * width)
                y = int(palec.y * height)
                if numerPalca % 4 == 0: # 0 -> srodek dloni|4 -> Kciuk|8 -> Wskazujacy|12 -> Srodkowy|16 -> Serdeczny|20 -> Maly
                    tabelaPrzechowujacaOpuszki.append([numerPalca,x,y])
                    cv2.circle(okno, (x,y) , 5 , (255,255,0) , cv2.FILLED)
        return tabelaPrzechowujacaOpuszki
