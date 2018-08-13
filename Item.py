class Item:

    def __init__(self, adresa,nejvyssiBid,nejnizsiNabidka,potencionalniVydelek,koeficientVydelku,prumerZaN,celkemProdanoZaN, prumerMaxim):
        self.adresa = adresa
        self.nejvyssiBid = nejvyssiBid
        self.nejNizsiNabidka = nejnizsiNabidka
        self.potencionalniVydelek = potencionalniVydelek
        self.koeficientVydelku = koeficientVydelku
        self.prumerZaN = prumerZaN
        self.celkemProdanoZaN = celkemProdanoZaN
        self.prumerMaxim = prumerMaxim

    def __str__(self):
        return '----------------------------------------------------------------------\n' + str(self.adresa) + '\n' +  'nakupni cena je: ' + str(self.nejvyssiBid)+ ' $\nprodejni cena je: '+ str(self.nejNizsiNabidka) + '' \
        ' $ prumerna cena je: ' + str("%.2f" % self.prumerZaN)  + ' prumer maxim je: ' + str("%.2f" % self.prumerMaxim)+ '\npotencionalni vydelek: ' + str("%.2f" % self.potencionalniVydelek) + ' $ '\
        'procenta: ' + str("%.2f" % self.koeficientVydelku) + ' % za mesic prodano: ' + str(self.celkemProdanoZaN)

###----------------------------------------------------------------------
###http://steamcommunity.com/market/listings/730/%E2%98%85%20StatTrak%E2%84%A2%20Karambit%20%7C%20Case%20Hardened%20%28Battle-Scarred%29
###nakupni cena je: 203.89 $
###prodejni cena je: 320.98 $ prumerna cena je: -1.00 prumer maxim je: 0.00
###potencionalni vydelek: 68.94 $ procenta: 33.81 % za mesic prodano: 0
