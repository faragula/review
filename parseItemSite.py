


def parseData(vstupniSoubor, vystupniSoubor):
    fp = open(vstupniSoubor, encoding='utf8')
    listItemuZeSouboru = fp.read().split("\n")
    fp.close()

    f = open(vystupniSoubor, 'w', encoding='utf8')
    for kazdy in listItemuZeSouboru:
        if "(" in kazdy:
            if "Wallet (160,82€)" not in kazdy:
                f.write(kazdy + '\n')
                print(kazdy)
    return


parseData("itemy2403.txt", "seznamItemu2.txt")