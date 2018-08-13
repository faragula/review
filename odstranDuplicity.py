import os



def odstranDuplicity(vstupniSoubor):
    fp = open(vstupniSoubor, encoding='utf8')
    listItemuZeSouboru = fp.read().split("\n")
    fp.close()
    s = set(listItemuZeSouboru)
    bezDuplicit = list(s)


    f = open(vstupniSoubor, 'w', encoding='utf8')
    for kazdy in bezDuplicit:
        f.write(kazdy + '\n')
    f.close()
    return


def odstranDuplicityZeSlozky(slozkaString):

    soubory = os.listdir(slozkaString)
    for soubor in soubory:
        odstranDuplicity(slozkaString+soubor)
#odstranDuplicity("konvertovane38.txt")

odstranDuplicityZeSlozky("VstupOk/")