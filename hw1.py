import re


def find_between(s, first, last):
    try:
        start = s.index(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


Metascore = " "
minetto = " "

def find_between_r(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""

def ay(num):
    if num == 1:
        m = "January"
    elif num == 2:
        m = "February"
    elif num == 3:
        m = "March"
    elif num == 4:
        m = "April"
    elif num == 5:
        m = "May"
    elif num == 6:
        m = "June"
    elif num == 7:
        m = "July"
    elif num == 8:
        m = "August"
    elif num == 9:
        m = "September"
    elif num == 10:
        m = "October"
    elif num == 11:
        m = "November"
    elif num == 12:
        m = "December"
    return m


def LIST():
    print("Listing...")
    
    for films in x:
        print(films)
    print("...")


def findDateFilms(dateStart, dateFinish):
    contDate = contents
    names = find_between(contDate, dateStart, dateFinish)
    x = re.findall(".*\(20..\)", names)
    print(x)


def findGenre(genre):
    for a in range(len(genre)):
        for b in range(len(genre[a])):
            print(genre[a][b])


# , end= ", "

def printList(genre):
    for a in range(len(genre)):
        print(genre[a])


def findSinopsis(Onefilm, genre):
    try:
        meta = re.findall(".*Metascore", Onefilm)
        if meta != " ":
            sinop = find_between_r(Onefilm,"Metascore\n\n\n    ", "\n\nDirector:")
            return sinop
        else:
            sinop = find_between_r(Onefilm, genre[-1][-1] + "\n\n\n\n\n    ", "\n\nDirector:")
            return sinop
    except ValueError:
        sinop = "--"
        return sinop

def findDir(Onefilm):
    try:
        dirs = find_between_r(Onefilm, "Director", "\n\n\n")
        director = dirs.split('\n')
        if len(director) >= 2 : director = re.findall("(.*)\n\|\n\n(.*)", dirs)
        for st in range(len(director)):
            print(director[st])
    except ValueError:
        print ("--")


def findStars(Onefilm):
    try:
        stars = find_between_r(Onefilm, "Stars:", "\n\n")
        star = stars.split('\n')
        for st in range(len(star)):
            print(star[st] + "  ")  # , end=" "
    except ValueError:
        print("--")


def findPYear(name):
    try:
        contYear = contents
        whole = find_between_r(contYear, name + " (", ")")
        print(whole)
    except ValueError:
        print("--")


def infoOneFilm(name):
    contInfo = contents
    fil = find_between(contInfo, name, "if ")
    genre = re.findall("(.*)\n\|\n(.*)", fil)
    if not genre:
        genre = re.findall("(.*)\n-\n(.*)", fil)
    print("Info... ")
    print(name)
    min = re.findall(".*min", fil)
    if min != " ":
        try: minetto = find_between_r(fil, ")\n\n\n", "min")
        except ValueError: minetto = "--"
    meta = re.findall(".*Metascore", fil)
    if meta != " ":
        try: Metascore = find_between_r(fil, genre[-1][-1] + "\n\n\n", "\n        Metascore")
        except ValueError:Metascore="--"
    print("Production Year:")  # , end=" "
    findPYear(name)

    print("Genre:")  # , end=" "
    findGenre(genre)
    print("")
    print("Synopsis: " + findSinopsis(fil, genre) )  # , end=" "
    print("Min: " + minetto)
    print("Metascore: " + Metascore)

    print("Director: " )  # , end=" "
    findDir(fil)

    print("Stars:")  # , end=" "
    findStars(fil)

    print("...")

def DATUM(ayibul,contents):
    if ayibul == "january":
        date = re.findall('January .*', contents)
    elif ayibul == "february":
        date = re.findall('February .*', contents)
    elif ayibul == "march":
        date = re.findall('March .*', contents)
    elif ayibul == "april":
        date = re.findall('April .*', contents)
    elif ayibul == "may":
        date = re.findall('May .*', contents)
    elif ayibul == "june":
        date = re.findall('June .*', contents)
    elif ayibul == "july":
        date = re.findall('July .*', contents)
    elif ayibul == "august":
        date = re.findall('August .*', contents)
    elif ayibul == "september":
        date = re.findall('September .*', contents)
    elif ayibul == "october":
        date = re.findall('October .*', contents)
    elif ayibul == "november":
        date = re.findall('November .*', contents)
    elif ayibul == "december":
        date = re.findall('December .*', contents)
    return date

def nMethod(komut):
    if komut == "LIST":
        LIST()
    else:
        command = komut.split(" ")
        if command[0] == "INFO":
            infoOneFilm(komut[5:len(komut)])
        else:
            if len(command) == 2:
                print("Listing " + command[1] + " ...")
                froGen = command[1].split(":")
                if froGen[0] == "genre":
                    gens = froGen[1].split(",")
                    for sayi in range(len(x)):
                        denet = 0
                        cListing = contents
                        tekfilm = find_between(cListing, x[sayi], "if ")
                        genrefilm = re.findall("(.*)\n\|\n(.*)",tekfilm )
#print(genrefilm)
                        if not genrefilm:
                            genrefilm = re.findall("(.*)-(.*)",tekfilm )
#print(genrefilm)
                        for a in range(len(genrefilm)):
                            for b in range(len(genrefilm[a])):
                                for c in range(len(gens)):
                                    if gens[c] == genrefilm[a][b]: denet = denet + 1
                        if denet == len(gens): print( find_between_r(x[sayi], " ", " (") )
                elif froGen[0] == "from":
                    dats = froGen[1].split("-")
                    year = dats[0]
                    inte = int(dats[1])
                    month = ay(inte)
                    day = dats[2]
                    findo = ".*\(" + year + "\)"
                    for cepteTarih in range(len(date)):
                        cTarih = date[cepteTarih].split(" ")
                        if cTarih[0] == month:
                            if cTarih[1] > day:
                                contT = contents
                                listeTarih = find_between_r(contT, date[cepteTarih], "Copyright")
                                xe = re.findall(findo, listeTarih)
                        break
                    printList(xe)
                    print("....")
                    
            elif len(command) == 3 and command[0] != "INFO":
                print("Listing " + command[1] + " " + command[2] + " ...")
                form = command[1].split(":")
                datsfrom = form[1].split("-")
                yearfrom = datsfrom[0]
                inte = int(datsfrom[1])
                monthfrom = ay(inte)
                dayfrom = datsfrom[2]
                to = command[2].split(":")
                datsto = to[1].split("-")
                yearto = datsto[0]
                inteto = int(datsto[1])
                monthto = ay(inteto)
                dayto = int(datsto[2])
                startStr = ""
                for allTarih in range(len(date)):
                    all = date[allTarih].split(" ")
                    if all[0] == monthfrom:
                        if all[1] >= dayfrom:
                            startStr = date[allTarih]
                            break
                for allTo in range(len(date)):
                    allt = date[allTo].split(" ")
                    if allt[0] == monthto:
                        if int(allt[1]) >= dayto:
                            finishStr = date[allTo]
                            ctAra = contents
                            aratarih = find_between_r(ctAra, startStr, finishStr)
                            xara = re.findall(".*\(20..\)", aratarih)
                            break
                printList(xara)
                print("....")

don=" "
while don != "12414t":
    try:
        komut = input()
        if komut != "LIST":
            co = komut.split(" ")
            if co[0] == "INPUT":
                dosya = komut
                doc = find_between_r(dosya, "INPUT ", ".txt")
                ayibul = doc.split("_")
                document = dosya.split(" ")
                f = open(document[1], "r")# , encoding='windows-1252'
                print("Loading " + document[1] + " ..." )
                contents = f.read()
                date = DATUM(ayibul[0],contents)
                x = re.findall(".*\(20..\)",contents )
            else: nMethod(komut)
        else: nMethod(komut)
    except EOFError:
        exit(0)








#don = "12414t"
