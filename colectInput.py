

def createInput(od, do):
    funguj = True
    while(funguj):
        fp = open("VstupOK/rozmezi"+str(od) + "-" + str(od+10) + ".txt", encoding='utf8')
        listItemuZeSouboru = fp.read().split("\n")
        fp.close()

        with open('aktulaniInput.txt', 'a') as the_file:
            for l in listItemuZeSouboru:
                the_file.write(l + "\n")
        if(od == do):
            funguj = False
        else:
            od = od + 10

##130 170(180 300)
createInput(130,180)