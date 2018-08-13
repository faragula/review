from Item import Item
import urllib.request
from urllib.error import HTTPError


def nactiSoubor(vstupniSoubor):
    _offsetItemRadek = 5
    fp = open(vstupniSoubor, encoding='utf8')
    _listRadkuZeSouboru = fp.read().split("\n")
    fp.close()
    _pocetItemu = _listRadkuZeSouboru.count("----------------------------------------------------------------------")
    _listItemu = list()

    for x in range(0, _pocetItemu):
        _adresa = _listRadkuZeSouboru[1+(_offsetItemRadek*x)]
        _nejvyssiBid = float(_listRadkuZeSouboru[2+(_offsetItemRadek*x)].split(' ')[3])
        _nejNizsiNabidka = float(_listRadkuZeSouboru[3+(_offsetItemRadek*x)].split(' ')[3])
        _prumerZaN = float(_listRadkuZeSouboru[3+(_offsetItemRadek*x)].split(' ')[8])
        _prumerMaxim = float(_listRadkuZeSouboru[3+(_offsetItemRadek*x)].split(' ')[12])
        _potencionalniVydelek = float(_listRadkuZeSouboru[4+(_offsetItemRadek*x)].split(' ')[2])
        _koeficintVydelku = float(_listRadkuZeSouboru[4+(_offsetItemRadek*x)].split(' ')[5])
        _celkemProdanoZaN = _listRadkuZeSouboru[4+(_offsetItemRadek*x)].split(' ')[10]
        _tempItem = Item(_adresa,_nejvyssiBid,_nejNizsiNabidka,_potencionalniVydelek,_koeficintVydelku,_prumerZaN,_celkemProdanoZaN,_prumerMaxim)
        _listItemu.append(_tempItem)

    _vyslednyListItemu = list()
    for item in _listItemu:
            if(float(item.celkemProdanoZaN) > 8):
                _vyslednyListItemu.append(item)
    _listItemu.sort(key=lambda x: x.koeficientVydelku, reverse=True)
    _vyslednyListItemu.sort(key=lambda x: x.koeficientVydelku, reverse=True)

    print('prvni 3 jsou\n \n \n')
    for prvni3 in range(0, 3):
        print(_listItemu[prvni3])

    print('\n \n \n REGULAR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    for item in _vyslednyListItemu:
        print(item)

nactiSoubor("vystupPredbezny.txt")
