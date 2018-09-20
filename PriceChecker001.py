#https://steamcommunity.com/market/listings/730/Desert%20Eagle%20%7C%20Sunset%20Storm%20%E5%A3%B1%20%28Field-Tested%29

from Item import Item
import urllib.request
from datetime import datetime
from datetime import timedelta
import time
from urllib.error import HTTPError

#kod pro
hvezdickaSMezerou = '%E2%98%85%20'
#čekací hodnota v sekundách mezi jednotlivými iteracemi dotazů
sleep = 6

class elementGrafu:

    def __init__(self, datum, cena, pocet):
        self.datum = datum
        self.cena = cena
        self.pocet = pocet

    def __str__(self):
        return str(self.datum) + ' ' + str(self.cena) + ' ' + str(self.pocet) + 'x'

# vrátí id nazevItemu
# # "SSG%2008%20%7C%20Blood%20in%20the%20Water%20%28Factory%20New%29" má ID 1922739
def vratIdZNazvuItemu(nazevItemu):

    time.sleep(sleep)

    urlListing = 'http://steamcommunity.com/market/listings/730/' + nazevItemu
    sock = urllib.request.urlopen(urlListing)
    li = sock.read()
    sock.close()

    liDoStringu = str(li)
    try:
        oddelpredek = liDoStringu.split('tMarket_LoadOrderSpread( ',1)
        oddelzadek = oddelpredek[1].split(' );\\t// initial load\\r\\n\\t\\t\\tPollOnUserActionAfterInterval',1)
    except IndexError:
        print('problem s linkem ' + urlListing)
    return oddelzadek[0]

#vrátí aktuální nejvyšší bid v dolarech
def aktualniNejvyssiBid(nazevItemu):

    time.sleep(sleep)

    url = 'http://steamcommunity.com/market/itemordershistogram?country=CZ&language=english&currency=1&item_nameid=' + vratIdZNazvuItemu(nazevItemu) +'&two_factor=0'
    sock = urllib.request.urlopen(url)
    li = sock.read()
    sock.close()
    try:
        liDoStringu = str(li)
        oddelpredek = liDoStringu.split('requests to buy at <span class=\\\\\"market_commodity_orders_header_promote\\\\\">$')
        oddelzadek = oddelpredek[1].split('<\\\\/span>')
        vysledek = oddelzadek[0].replace(',','.')
        vysledek = vysledek.replace('-', '0')
    except IndexError:
        print('problem s odkazem ' + url)
        return 0
    return vysledek

#vrací aktuální cenu k přímému nákupu
def aktualniCena(nazevItemu):

    time.sleep(sleep)
    adresa = 'http://steamcommunity.com/market/priceoverview/?currency=1&appid=730&market_hash_name=' + nazevItemu

    sock = urllib.request.urlopen(adresa)
    li = sock.read()
    sock.close()
    liDoStringu = str(li)
    try:
        oddelpredek = liDoStringu.split('ce\":\"$')
        oddelZadek = oddelpredek[1].split('\"')
        vysledek = oddelZadek[0].replace(',','.')
        vysledek = vysledek.replace('-','0')
    except IndexError:
        print('spatny vstup od odkazu: ' + adresa)
        vysledek = 9999
    if(str(vysledek).count(".") > 1):
        listik = str(vysledek).split('.')
        vysledek = listik[0]+listik[1]+'.'+listik[2]
        return float(vysledek)
    return float(vysledek)

#vrací pole objektů elementGrafu v závislosti na pocetDni zadaných
def vratPoleElementuGrafuNdni(listHodnotVGrafu, pocetDni):
    datumPredNDny = datetime.today() - timedelta(days=pocetDni)
    poleElementuVGrafu = []
    for jedenZapisVGrafu in listHodnotVGrafu:
        odstraneneUvozovky = jedenZapisVGrafu.replace('\"','')
        pole = odstraneneUvozovky.split(' ')
        datum = datetime.strptime(str(pole[0] + ' ' + pole[1] + ' ' + pole[2]), '%b %d %Y')
        cena = pole[4].split(',')[1]
        pocet = pole[4].split(',')[2]
        element = elementGrafu(datum,cena,pocet)
        if(element.datum > datumPredNDny):
            poleElementuVGrafu.append(element)
    return poleElementuVGrafu

#vrací průměrou cenu horních peeků
def najdiPrumerMaxim(poleCen, procentMaxim):
    pomerMaxim = int(round(procentMaxim*len(poleCen)))
    serazenePole = sorted(poleCen)
    soucet = 0
    for i in range(0,pomerMaxim):
        soucet = float(serazenePole[i]) + float(soucet)
    if (soucet == 0):
        return 0
    return (soucet/pomerMaxim)

#vrátí průměrnou hodnotu Itemu v $ ze zadaného pole
def prumerZPole(pole):
    soucet = 0
    for i in pole:
        soucet = soucet + i
    prumer = soucet/len(pole)
    return prumer

#zpětné řazení itemů do textových "vstupních" souborů
def pridejAdresuDoSpravnehoSouboru(adresa, nejnizsiNakupnicena):
    cisloNaZarazeni = int(nejnizsiNakupnicena/10)
    jmenoSouboru = 'VstupOK/rozmezi'+ str(cisloNaZarazeni) + '0-' + str(cisloNaZarazeni+1) + '0.txt'
    f = open(jmenoSouboru, 'a', encoding='utf8')
    f.write(adresa.replace('http://steamcommunity.com/market/listings/730/', '') + '\n')
    f.close()

    return

def AnalyzujItem(nazevItemu):
    stringAktualneNejvyssihoBidu = aktualniNejvyssiBid(nazevItemu)
    if stringAktualneNejvyssihoBidu.count('.') > 1 and len(stringAktualneNejvyssihoBidu) > 5:
        nejvyssiBid = float(stringAktualneNejvyssihoBidu.replace('.','',1))
    else:
        nejvyssiBid = float(stringAktualneNejvyssihoBidu)

    nejnizsiNabidka = float(aktualniCena(nazevItemu))

    potencionalniVydelek = nejnizsiNabidka-(nejnizsiNabidka*0.15)-nejvyssiBid
    koeficientVydelku = potencionalniVydelek/(nejvyssiBid/100)

    adresa = 'http://steamcommunity.com/market/listings/730/' + nazevItemu

    time.sleep(sleep)

    sock = urllib.request.urlopen(adresa)
    li = sock.read()
    sock.close()
    liDoStringu = str(li)
    try:
        oddelpredek = liDoStringu.split('(document).ready(function(){\\r\\n\\t\\t\\tvar line1=[[')
        oddelZadek = oddelpredek[1].split(']];\\r\\n\\t\\t')
        listHodnotVTabulce = oddelZadek[0].split('],[')
    except IndexError:
        print("problem s linkem: " + adresa + '\nminule to bylo ze historie prodeju neni dostupna, takovy to item mazu ze seznamu')
    poleElementuVGrafuNdni = vratPoleElementuGrafuNdni(listHodnotVTabulce, 30)

    prodanoZaN = 0
    soucet = 0
    listNaMaxima = []
    for kazdej in poleElementuVGrafuNdni:
        listNaMaxima.append(kazdej.cena)
        prodanoZaN = prodanoZaN + int(kazdej.pocet)
        soucet = soucet + float(kazdej.cena)

    prumerMaxim = najdiPrumerMaxim(listNaMaxima,0.4)

    if(prodanoZaN == 0):
        prumerZaN = -1
    else:
        prumerZaN = soucet/prodanoZaN

    pridejAdresuDoSpravnehoSouboru(adresa,nejvyssiBid)

    item = Item(adresa,nejvyssiBid,nejnizsiNabidka,potencionalniVydelek,koeficientVydelku,prumerZaN,prodanoZaN,prumerMaxim)
    return item

#připíše stringPripsat do vyslednySoubor
def zapisDoSouboru(vyslednySoubor, stringPripsat):
    f = open(vyslednySoubor, 'a', encoding='utf8')
    f.write(stringPripsat + '\n')
    f.close()
    return

#analyzuje itemy ze souboru stringVstupnihoSouboru
def AnalizujItemy(stringVstupnihoSouboru):
    fp = open(stringVstupnihoSouboru, encoding='utf8')
    #list stringu, string musi byt konvertovany v prislusnem tvaru " AK-47%20%7C%20Vulcan%20%28Field-Tested%29 "
    listItemuZeSouboru = fp.read().split("\n")
    fp.close()

    print('pocet itemu k analyze = ' + str(len(listItemuZeSouboru)))

    vyslednyList = []
    progres = 0
    for stringItemu in listItemuZeSouboru:
        try:
            vyslednyItem = AnalyzujItem(stringItemu )
            if(vyslednyItem.celkemProdanoZaN > 8): #uvazuji jen itemy, které jsou prodány alespon nekolikrát
                vyslednyList.append(vyslednyItem)
            zapisDoSouboru('vystupPredbezny.txt', str(vyslednyItem))
            #zápis do souboru vystupPredbezny, i po padu aplikace nemusim poustet znova
        except UnboundLocalError:
            print('AnalizujItemy-UnboundLocalError: neni historie itemu')
        progres = progres + 1
        print("%.2f" % float(progres/len(listItemuZeSouboru)) + " " + stringItemu)
        # progress + vypis "0.00 %E2%98%85%20Karambit%20%7C%20Forest%20DDPAT%20%28Minimal%20Wear%29"
    vyslednyList.sort(key=lambda x: x.koeficientVydelku, reverse=True)
    count = 0
    f = open("VstupOK/bestSellers.txt", 'a', encoding='utf8')
    while (count < 3): #vypíše první 3 itemy do souboru, bestSellers.txt
        f.write(vyslednyList[count].adresa.replace('http://steamcommunity.com/market/listings/730/','') + "\n")
        count = count + 1
    return vyslednyList


listItemu = AnalizujItemy('VstupOK/odstranAktualni.txt')
for it in listItemu:
    print(it)





