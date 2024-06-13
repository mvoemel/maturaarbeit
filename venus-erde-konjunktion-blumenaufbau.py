from gpanel import *
from math import *

makeGPanel("ErdeVenusBlume",-150, 150, -150, 150)
resizable(False)
windowSize(1500, 1500)
windowPosition(10, 10)

#Erde
setColor("blue")
circle(149.60)
#Venus
setColor("green")
circle(108.21)

def RaumgeradeEV():
    t=974           #Anzahl 3-Tage Schritte (hier 8 Jahre)
    we=0.051606         #Winkel Erde in Bogenmass
    wv=0.083887         #Winkel Venus in Bogenmass
    for x in range(1,t,1):
        lineWidth(1)
        setColor("red")
        xErde = (math.cos(we*x))*149.60
        yErde = (math.sin(we*x))*149.60
        xVenus = (math.cos(wv*x))*108.21
        yVenus = (math.sin(wv*x))*108.21
        line(xErde, yErde, xVenus, yVenus)
        delay(25)

RaumgeradeEV()
