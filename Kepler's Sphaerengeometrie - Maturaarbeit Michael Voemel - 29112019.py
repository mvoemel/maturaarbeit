from math import *
from javax.swing import *
from gpanel import *

# P = Planeten; F = Farben; a = Ellipsenhalbachse a; b = Ellipsenhalbachse b; t = Umlaufzeit; g = GPanel-Koordinaten yMin, yMax, xMin, xMax
P = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]#Planeten: Mercury(0), Venus(1), Earth(2), Mars(3), Jupiter(4), Saturn(5), Uranus(6), Neptune(7)
F = ["Red", "Orange", "Yellow", "Lime", "Green", "Cyan", "Blue", "Magenta","Purple", "Black", "Gold"]#Farben: red(0), orange(1), yellow(2), lime(3), green(4), cyan(5), blue(6), magenta(7), purple(8), black(9)
a = [57.91, 108.21, 149.60, 227.92, 778.57, 1433.53, 2872.46, 4495.06]#(km*10^6)
b = [56.67, 108.21, 149.58, 226.92, 777.64, 1431.24, 2869.46, 4494.77]#(km*10^6)
t = [87.969, 224.701, 365.256, 686.980, 4332.589, 10759.22, 30685.4, 60189.0]#(Tage)
TagesSchritteMatrix = [[0,3,3,3,5,10,30,50],[3,0,3,5,10,10,15,50],[3,3,0,5,10,10,20,50],[3,5,5,0,10,10,50,50],[5,10,10,10,0,20,50,100],[10,10,10,10,20,0,50,300],[30,15,20,50,50,50,0,550],[50,50,50,50,100,300,550,0]]#(Tage)
AnzahlTagesSchritteMatrix = [[0,680,850,1150,867,1075,1030,1205],[680,0,974,2350,435,1080,2047,1205],[850,974,0,1120,438,1095,1535,1205],[1150,2350,1120,0,1305,1100,620,1205],[867,435,438,1305,0,1085,7350,607],[1075,1080,1095,1100,1085,0,4305,1000],[1030,2047,1535,620,7350,4305,0,2800],[1205,1205,1205,1205,607,1000,2800,0]]#(Tage)
g = 5000

class program:
    
    def printGPanel(self, event):
        printScreen(0.8)
        dispose()
    
    def clearGPanel(self,event):
        clear()
        
    def Legende(self, selectedIndex1, selectedIndex2):
        AnzahlJahresSchritte = AnzahlTagesSchritteMatrix[selectedIndex1][selectedIndex2]*TagesSchritteMatrix[selectedIndex1][selectedIndex2]/t[2]
        setColor("black")
        text(-4950, -4500, str(P[selectedIndex1] + ", " + P[selectedIndex2]))
        text(-4950, -4650, str(TagesSchritteMatrix[selectedIndex1][selectedIndex2]) + " Tages-Schritte")
        text(-4950, -4800, str(round(AnzahlJahresSchritte, 1)) + " Jahre Zeitspanne")
    
    def Winkel1(self, InputWinkel1, TagesSchritte):
        Winkel1def = 360/InputWinkel1*pi/180*TagesSchritte
        return Winkel1def
        
    def Winkel2(self, InputWinkel2, TagesSchritte):
        Winkel2def = 360/InputWinkel2*pi/180*TagesSchritte
        return Winkel2def
    
    def Raumgerade(self, AnzahlTagesSchritte, W1, W2, Planet1EllipsenseiteAneu, Planet1EllipsenseiteBneu, Planet2EllipsenseiteAneu, Planet2EllipsenseiteBneu):
        lineWidth(1)
        for x in range(1,AnzahlTagesSchritte,1):
            xLineP1 = (math.cos(W1*x))*Planet1EllipsenseiteAneu
            yLineP1 = (math.sin(W1*x))*Planet1EllipsenseiteBneu
            xLineP2 = (math.cos(W2*x))*Planet2EllipsenseiteAneu
            yLineP2 = (math.sin(W2*x))*Planet2EllipsenseiteBneu
            line(xLineP1, yLineP1, xLineP2, yLineP2)
            
    def Mittelpunkt(self, AnzahlTagesSchritte, W1, W2, Planet1EllipsenseiteAneu, Planet1EllipsenseiteBneu, Planet2EllipsenseiteAneu, Planet2EllipsenseiteBneu):
        lineWidth(3)
        for x in range(1,AnzahlTagesSchritte,1):
            xPoint = (((math.cos(W1*x))*Planet1EllipsenseiteAneu)+((math.cos(W2*x))*Planet2EllipsenseiteAneu))/2
            yPoint = (((math.sin(W1*x))*Planet1EllipsenseiteBneu)+((math.sin(W2*x))*Planet2EllipsenseiteBneu))/2
            point(xPoint, yPoint)
       
    def actionCallback(self,event):
        
        selectedIndex1 = self.ComboBox1.selectedIndex
        selectedIndex2 = self.ComboBox2.selectedIndex
        selectedC = self.ComboBoxFarbe.selectedIndex
        
        TagesSchritte = TagesSchritteMatrix[selectedIndex1][selectedIndex2]
        AnzahlTagesSchritte = AnzahlTagesSchritteMatrix[selectedIndex1][selectedIndex2]
        
        #Planet 1 Daten
        InputWinkel1 = t[selectedIndex1]
        W1 = self.Winkel1(InputWinkel1, TagesSchritte)
        Planet1EllipsenseiteA = a[selectedIndex1]
        Planet1EllipsenseiteB = b[selectedIndex1]
        
        #Planet 2 Daten
        InputWinkel2 = t[selectedIndex2]
        W2 = self.Winkel2(InputWinkel2, TagesSchritte)
        Planet2EllipsenseiteA = a[selectedIndex2]
        Planet2EllipsenseiteB = b[selectedIndex2]
            
        if Planet1EllipsenseiteA >= Planet2EllipsenseiteA:
            x = g/Planet1EllipsenseiteA
            Planet1EllipsenseiteAneu = Planet1EllipsenseiteA*x
            Planet1EllipsenseiteBneu = Planet1EllipsenseiteB*x
            Planet2EllipsenseiteAneu = Planet2EllipsenseiteA*x
            Planet2EllipsenseiteBneu = Planet2EllipsenseiteB*x
        else:
            x = g/Planet2EllipsenseiteA
            Planet1EllipsenseiteAneu = Planet1EllipsenseiteA*x
            Planet1EllipsenseiteBneu = Planet1EllipsenseiteB*x
            Planet2EllipsenseiteAneu = Planet2EllipsenseiteA*x
            Planet2EllipsenseiteBneu = Planet2EllipsenseiteB*x
                                    
        if selectedC == 0:
            setColor("red")
        elif selectedC == 1:
            setColor("orange")
        elif selectedC == 2:
            setColor("yellow")
        elif selectedC == 3:
            setColor("lime")
        elif selectedC == 4:
            setColor("green")
        elif selectedC == 5:
            setColor("cyan")
        elif selectedC == 6:
            setColor("blue")
        elif selectedC == 7:
            setColor("magenta")
        elif selectedC == 8:
            setColor("purple")
        elif selectedC == 9:
            setColor("black")
        elif selectedC == 10:
            setColor("gold")
            
        if self.CheckBoxE.isSelected():
            lineWidth(1)
            ellipse(Planet1EllipsenseiteAneu, Planet1EllipsenseiteBneu)
            ellipse(Planet2EllipsenseiteAneu, Planet2EllipsenseiteBneu)
                  
        if self.RadioBtnR.isSelected():
            self.Raumgerade(AnzahlTagesSchritte, W1, W2, Planet1EllipsenseiteAneu, Planet1EllipsenseiteBneu, Planet2EllipsenseiteAneu, Planet2EllipsenseiteBneu)
        elif self.RadioBtnM.isSelected():
            self.Mittelpunkt(AnzahlTagesSchritte, W1, W2, Planet1EllipsenseiteAneu, Planet1EllipsenseiteBneu, Planet2EllipsenseiteAneu, Planet2EllipsenseiteBneu)
        else:
            print "Fehler"
            
        if self.CheckBoxL.isSelected():
            self.Legende(selectedIndex1, selectedIndex2)
                   
        move(0, 0)
            
    def __init__(self):
        
        self.ComboBox1 = JComboBox(P)
        self.ComboBox2 = JComboBox(P)
        self.ComboBoxFarbe = JComboBox(F)
        
        self.CheckBoxE = JCheckBox("Ellipsen")
        self.CheckBoxL = JCheckBox("Legende")
        
        self.RadioBtnR = JRadioButton("Raumgerade")
        self.RadioBtnM = JRadioButton("Mittelpunkt")
        RadioButtonGroup = ButtonGroup()
        RadioButtonGroup.add(self.RadioBtnR)
        RadioButtonGroup.add(self.RadioBtnM)
    
        OkButton = JButton("OK", actionPerformed = self.actionCallback)
        ClearButton = JButton ("Clear", actionPerformed = self.clearGPanel)
        PrintButton = JButton ("Print", actionPerformed = self.printGPanel)
        
        MenuBar = JMenuBar()
        MenuBar.add(self.ComboBox1)
        MenuBar.add(self.ComboBox2)
        MenuBar.add(self.ComboBoxFarbe)
        MenuBar.add(self.CheckBoxE)
        MenuBar.add(self.CheckBoxL)
        MenuBar.add(self.RadioBtnR)
        MenuBar.add(self.RadioBtnM)
        MenuBar.add(OkButton)
        MenuBar.add(ClearButton)
        MenuBar.add(PrintButton)

        makeGPanel(MenuBar, -g, g, -g, g)
        
        title("Kepler's Sphaerengeometrie")
        resizable(False)
        windowSize(1000, 1000)
        windowPosition(10, 10)

        validate()
   
program()
