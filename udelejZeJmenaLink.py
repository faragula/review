from datetime import datetime
'''
karambitUltravioleBSStatTrak = '%E2%98%85%20StatTrak%E2%84%A2%20Karambit%20%7C%20Ultraviolet%20%28Battle-Scarred%29'
karambit = '%E2%98%85%20Karambit'
p250 = 'P250%20%7C%20Steel%20Disruption%20%28Factory%20New%29'
huntsmanKnifeBorealForestStatTrak = '%E2%98%85%20StatTrak%E2%84%A2%20Huntsman%20Knife%20%7C%20Boreal%20Forest%20%28Minimal%20Wear%29'
flipKnifeFreehandMinimalWear = '%E2%98%85%20Flip%20Knife%20%7C%20Freehand%20%28Minimal%20Wear%29'
p250StatTrak = 'StatTrak%E2%84%A2%20P250%20%7C%20Steel%20Disruption%20%28Factory%20New%29'
idp250StatTrak = 3442147

mezera = '%20'
svislyZnak = '%7C'
zacatekZavorky = '%28'
konecZavorky = '%29'
statTrak = 'StatTrak%E2%84%A2%20'
hvezdickaSMezerou = '%E2%98%85%20'

pokus = '★ StatTrak™ Butterfly Knife | Blue Steel (Well-Worn)'
'''

def zapisDoSouboru(toCoPiseDoSouboru):
    f = open('konvertovane.txt', 'a')
    f.write(str(datetime.today()))
    f.close()
    return


def vyhodDuplicity(listItemu):
    s = set(listItemu)
    bezDuplicit = list(s)

    return bezDuplicit

def parsujJmenoItemu(jmenoItemu):
    jmenoItemu1 = jmenoItemu.replace('★ ','%E2%98%85%20')
    jmenoItemu2 = jmenoItemu1.replace('™ ','%E2%84%A2%20')
    jmenoItemu3 = jmenoItemu2.replace(' | ', '%20%7C%20')
    jmenoItemu4 = jmenoItemu3.replace(' (', '%20%28')
    jmenoItemu5 = jmenoItemu4.replace(')', '%29')
    jmenoItemu6 = jmenoItemu5.replace(')', '%29')
    jmenoItemu7 = jmenoItemu6.replace(' ', '%20')
    jmenoItemu8 = jmenoItemu7.replace('弐', '%E5%BC%90')
    jmenoItemu9 = jmenoItemu8.replace('壱', '%E5%A3%B1')
    jmenoItemu10 = jmenoItemu9.replace('龍王', '%E9%BE%8D%E7%8E%8B')

    return jmenoItemu10

def konvertujSoubor(vstupníSouborVeFormatuString,vystupniSouborVeFormatuString):
    fp = open(vstupníSouborVeFormatuString, encoding='utf8')
    listItemuZeSouboru = fp.read().split("\n")
    fp.close()

    bezDuplicit =  vyhodDuplicity(listItemuZeSouboru)

    f = open(vystupniSouborVeFormatuString, 'w', encoding='utf8')
    for kazdy in bezDuplicit:
        f.write(parsujJmenoItemu(kazdy) + '\n')
    f.close()
    return

konvertujSoubor('seznamItemu2.txt', 'novytestvystup1.txt')
