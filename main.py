



class Uitgaven:
    def __init__(self, naam, MatchList, overig = False, inkomsten = False):
        self.naam = naam
        self.matchList = MatchList
        self.uitgaven = list()
        self.totaal = 0.0
        self._overig = overig
        self._inkomsten = inkomsten

    def sorteerUitgaven(self, uitgavenLijst):
        if self._overig is True:
            for a in reversed(uitgavenLijst):
                self.uitgaven.append(a)
                uitgavenLijst.remove(a)
        elif self._inkomsten is True:
            print("entering")
            for a in range(5):
                for a in reversed(uitgavenLijst):
                    print(a[5].lower())
                    if a[5].lower() == "bij":
                        self.uitgaven.append(a)
                        uitgavenLijst.remove(a)
        else:
            for a in range(5):
                for a in uitgavenLijst:
                    for t in reversed(self.matchList): #kijkt of die overeenkomt met iets uit matchlist
                        if t.lower() in a[1].lower() and a[5].lower() is not "bij":#a[5] is bij/af
                            # print("match:", a)
                            self.uitgaven.append(a)
                            uitgavenLijst.remove(a)
        for a in self.uitgaven:
            self.totaal += float(a[6])
        self.totaal = round(self.totaal, 2)

class uitgavenMatrix:
    def __init__(self, lijstMetUitgaven):
        self.lijst = lijstMetUitgaven
        self.w = int()
        self.h = int()
        self.matrix = ""
        self.aantalOmschrijvingsVelden = 4 #aantal velden dat begruikt wordt in de omschrijving


    def maakMatrix(self, filler = ""):
        self.checkLengte() #zet de w en h waardes vast voor de matrix gemaakt wordt.
        #self.h = 5
        self.matrix = [[filler for x in range(self.w)] for y in range(self.h)]

    def print(self):
        #print("printing grid...")
        #print(self.matrix)
         for i in range(self.h):
             print(self.matrix[i])


    def checkLengte(self):
        #kijkt hoe groot de langste list is voor de H waarde door te kijken naar de lengte van de Uitgaven classe
        mostItems = 0
        for i in self.lijst:
            #print("test:", i.naam, len(i.uitgaven))
            if len(i.uitgaven) > mostItems:
                mostItems = len(i.uitgaven)
                #print("nieuwe waarde mostitems:", mostItems)
        self.h = mostItems + 2 #2 extra regels voor de final en omschrijving.
        self.w = len(self.lijst) * self.aantalOmschrijvingsVelden # 3 plekken, , datum, plaats, bedrag
        #print(self.h)

    def vulMatrix(self):
        #eerste rij vullen met omschrijving
        for i in range(len(self.lijst)):
            #self.matrix[0][i * self.aantalOmschrijvingsVelden + 0] = "wtf is dit"
            self.matrix[0][i * self.aantalOmschrijvingsVelden + 1] = "Datum"
            self.matrix[0][i * self.aantalOmschrijvingsVelden + 2] = "Omschrijving"
            self.matrix[0][i * self.aantalOmschrijvingsVelden + 3] = "bedrag"

        #voer de uitgaven in
        classeCounter = 0
        for i in self.lijst:
            self.matrix[0][classeCounter * self.aantalOmschrijvingsVelden] = i.naam
            h = 1;
            w = classeCounter *self.aantalOmschrijvingsVelden
            for y in i.uitgaven:
                datum = y[0]
                datum = datum[-2:] + '-' + datum[4:6] + '-' + datum[:4]
                self.matrix[h][w + 1] = datum #datum
                self.matrix[h][w + 2] = y[1] #omschrijving
                self.matrix[h][w + 3] = y[6] #bedrag
                h += 1
            classeCounter += 1
            #print(classeCounter)

        # voer de totalen in
        classeCounter = 0
        for i in self.lijst:
            self.matrix[self.h - 1][classeCounter * self.aantalOmschrijvingsVelden + 2] = "totaal:"
            self.matrix[self.h - 1][classeCounter * self.aantalOmschrijvingsVelden + 3] = str(i.totaal)
            classeCounter += 1

    #     Matrix[0][0] = "Geld Bij"
    #     Matrix[0][1] = "datum"
    #     Matrix[0][2] = "omschrijving"
    #     Matrix[0][3] = "bedrag"

    def schrijfWeg(self):
        eindFile = open("resultaat.csv", "w")
        regel = ""
        for i in self.matrix:
            regel = ""
            for x in i:
                regel += str(x)
                regel += ';'
            eindFile.writelines(regel + '\n')
        # eindFile.writelines("eindbedrag:;"+str(eindbedrag))

        eindFile.close()


    def run(self):
        pass
        self.maakMatrix()



def maakUitgaven(file):
    uitgavenFile = open(file, "r")
    lijst = list()

    for x in uitgavenFile:

        uitgavenTemp = x
        if uitgavenTemp[1:6] == "Datum":
            continue
        uitgavenTemp = uitgavenTemp.split(",")
        dataList = list()
        for l in uitgavenTemp:
            l = l.replace("\"", "")
            dataList.append(l)
            #print(l)
        dataList[6] = dataList[6] + '.' + dataList[7]   #voegt bedrag samen
        dataList.pop(7)
        #print(dataList[6])
        #print("datalist: ", dataList)
        lijst.append(dataList)
    uitgavenFile.close()
    return lijst
#
#
# def flushResultaten():
#     w, h = 20, 20; #20 20
#     Matrix = [["" for x in range(w)] for y in range(h)]
#
#
#     print(len(Matrix[0]))
#     Matrix.append("testtestestest")
#
#     #geld bij
#     Matrix[0][0] = "Geld Bij"
#     Matrix[0][1] = "datum"
#     Matrix[0][2] = "omschrijving"
#     Matrix[0][3] = "bedrag"
#
#     counter = 1
#     eindbedrag = 0.0
#     for x in geldBij:
#         Matrix[counter][1] = x[0] #datum
#         Matrix[counter][2] = x[1] #omschrijving
#         Matrix[counter][3] = x[6] #geldbedrag
#         counter += 1
#         eindbedrag += float(x[6])
#
    eindFile = open("resultaat.csv", "w")
    regel = ""
    for i in Matrix:
        regel = ""
        for x in i:
            regel += str(x)
            regel += ';'
        eindFile.writelines(regel + '\n')
    #eindFile.writelines("eindbedrag:;"+str(eindbedrag))

    eindFile.close()

#     for i in range(w):
#         print(Matrix[i])
#     print(eindbedrag)






lijst = maakUitgaven("uitgaven.csv")

uitgaven = list()

etenMat = ["Jumbo", "albert heijn", "dirk", "hoogvliet", "ah to go", "smullers", "takeaway.com", "domino", \
           "HAAGSE H.SCHOOL", "L.M.A. van Damme", "Studieverenigi Delft NLD", "McLeidschenhage"]
uitgaanMat = ["Pool", "proeflokaal"]
vasteLastenMat = ["anwb","transip", "vgz zorgverzekeraar", "artsen zonder grenzen", "kpn - mobiel", "spotify", "engie" \
                  ,"evides"]
bezineMat = ["argos", "texaco"]

inkomsten = Uitgaven("inkomsten", None, inkomsten=True)
uitgaven.append(inkomsten)

eten = Uitgaven("eten",etenMat)
uitgaven.append(eten)


uitgaan = Uitgaven("uitgaan", uitgaanMat)
uitgaven.append(uitgaan)

vasteLasten = Uitgaven("vasteLasten", vasteLastenMat)
uitgaven.append(vasteLasten)

bezine = Uitgaven("bezine", bezineMat)
uitgaven.append(bezine)

overig = Uitgaven("overig", None, overig=True)
uitgaven.append(overig)

for i in uitgaven:
    i.sorteerUitgaven(lijst)

print(overig.uitgaven)

matrix = uitgavenMatrix(uitgaven)

matrix.maakMatrix(filler="")
matrix.vulMatrix()
matrix.schrijfWeg()

matrix.print()
#print(len(matrix.lijst))
#print(overig.uitgaven)






