import random
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def tulokset(pelaaja: str) -> dict:
    """Palauttaa pelaajan tulokset"""
    pisteet = {}
    pisteet["Ykköset"] = pelaajat[pelaaja][0]
    pisteet["Kakkoset"] = pelaajat[pelaaja][1]
    pisteet["Kolmoset"] = pelaajat[pelaaja][2]
    pisteet["Neloset"] = pelaajat[pelaaja][3]
    pisteet["Viitoset"] = pelaajat[pelaaja][4]
    pisteet["Kuutoset"] = pelaajat[pelaaja][5]
    pisteet["Välisumma"] = pelaajat[pelaaja][6]
    pisteet["Pari "] = pelaajat[pelaaja][7]
    pisteet["Kaksi paria"] = pelaajat[pelaaja][8]
    pisteet["Kolme samaa"] = pelaajat[pelaaja][9]
    pisteet["Neljä samaa"] = pelaajat[pelaaja][10]
    pisteet["Pieni suora"] = pelaajat[pelaaja][11]
    pisteet["Iso suora"] = pelaajat[pelaaja][12]
    pisteet["Täyskäsi"] = pelaajat[pelaaja][13]
    pisteet["Sattuma"] = pelaajat[pelaaja][14]
    pisteet["Yatzy"] = pelaajat[pelaaja][15]
    pisteet["Summa"] = pelaajat[pelaaja][16]

    return pisteet
    
    
    

def tulosta_tulokset(pelaaja: str, pisteet: dict):
    """Tulostaa pelaajan tulokset"""
    print(f"{pelaaja}: ")
    for pisteNimi in pisteet:
        print(f"{pisteNimi}: {pisteet[pisteNimi]}")


def heita_nopat() -> list:
    """Heittää noppaa pelaajalle"""
    nopat = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    return nopat


def vaihtoehdot(pisteet: dict) -> dict:
    """Tarkistaa noppa tuloksien mahdollisuudet"""
    global noppaTulokset
    vaihtoehto = {}

    # ykköset - kutoset
    if noppaTulokset.count(1) >= 1:
        vaihtoehto["Ykköset"] = 1 * noppaTulokset.count(1)
    if noppaTulokset.count(2) >= 1:
        vaihtoehto["Kakkoset"] = 2 * noppaTulokset.count(2)
    if noppaTulokset.count(3) >= 1:
        vaihtoehto["Kolmoset"] = 3 * noppaTulokset.count(3)
    if noppaTulokset.count(4) >= 1:
        vaihtoehto["Neloset"] = 4 * noppaTulokset.count(4)
    if noppaTulokset.count(5) >= 1:
        vaihtoehto["Viitoset"] = 5 * noppaTulokset.count(5)
    if noppaTulokset.count(6) >= 1:
        vaihtoehto["Kuutoset"] = 6 * noppaTulokset.count(6)

    # pari, kolme samaa, neljä samaa, yatzy
    i = 1
    kaksiParia = 0
    while i < 7:
        if noppaTulokset.count(i) >= 2:
            vaihtoehto[f"{i} Pari "] = 2 * i
            kaksiParia += 1
            if kaksiParia == 1:
                pari1 = i
            elif kaksiParia == 2:
                pari2 = i
        if noppaTulokset.count(i) >= 3:
            vaihtoehto[f"Kolme samaa {i}"] = 3 * i
            kolmeSamaa = i
        if noppaTulokset.count(i) >= 4:
            vaihtoehto[f"Neljä samaa {i}"] = 4 * i
        if noppaTulokset.count(i) == 5:
            vaihtoehto["Yatzy"] = 5 * i   
        i += 1

    # kakspari
    if kaksiParia == 2:
        vaihtoehto[f"Kaksi paria, {pari1} ja {pari2}"] = (2 * pari1) + (2 * pari2)

    # täyskäsi
    set_res = set(noppaTulokset)
    list_res = (list(set_res))
    if len(list_res) == 2:
        eka = list_res[0]
        toka = list_res[1]
        maara1 = noppaTulokset.count(eka)
        maara2 = noppaTulokset.count(toka)
        if maara1 == 2 or maara1 == 3:
            if maara2 == 2 or maara2 == 3:
                vaihtoehto[f"Täyskäsi, {maara1} * {eka} ja {maara2} * {toka}"] = (maara1 * eka) + (maara2 * toka)
    
    # pikku suora
    if noppaTulokset.__contains__(1) and noppaTulokset.__contains__(2) and noppaTulokset.__contains__(3) and noppaTulokset.__contains__(4) and noppaTulokset.__contains__(5):
        vaihtoehto["Pieni suora"] = 15
    
    # Suuri suora
    if noppaTulokset.__contains__(6) and noppaTulokset.__contains__(2) and noppaTulokset.__contains__(3) and noppaTulokset.__contains__(4) and noppaTulokset.__contains__(5):
        vaihtoehto["Iso suora"] = 20
    
    # Sattuma
    vaihtoehto["Sattuma"] = noppaTulokset[0] + noppaTulokset[1] + noppaTulokset[2] + noppaTulokset[3] + noppaTulokset[4]
    

    popittavat = []
    for piste in vaihtoehto:
        # Pari on vaikea koska sen eteen on sijoitettu parin luvut, joten on käytettävä erikoistapausta
        if piste.__contains__("Pari "):
            if int(pisteet["Pari "]) != 0:
                popittavat.append(piste)
        elif piste.__contains__("Kolme"):
            if int(pisteet["Kolme samaa"]) != 0:
                popittavat.append(piste)
        elif piste.__contains__("Neljä"):
            if int(pisteet["Neljä samaa"]) != 0:
                popittavat.append(piste)
        elif piste.__contains__("Kaksi paria"):
            if int(pisteet["Kaksi paria"]) != 0:
                popittavat.append(piste)
        elif piste.__contains__("Täyskäsi"):
            if int(pisteet["Täyskäsi"]) != 0:
                popittavat.append(piste)
        else:
            if int(pisteet[piste]) != 0:
                popittavat.append(piste)
    for pop in popittavat:
        vaihtoehto.pop(pop)
    if len(vaihtoehto) < 1:
        return -1
    return vaihtoehto



def tallenna(tiedosto: str):
    """Tallentaa pelin tulokset tiedostoon, että peliä voi jatkaa myöhemmin"""
    with open(f"{tiedosto}.txt", "w") as tiedosto:
        for rivi in pelaajat:
            tiedosto.write(f"{rivi}\n")
            for numero in pelaajat[rivi]:
                tiedosto.write(f"{numero}\n")


def lataa(tiedosto: str):
    """Lataa aikaisemman pelin"""
    with open (f"{tiedosto}.txt") as t:
        i = 0
        tiedosto = []
        for rivi in t:
            tiedosto.append(rivi.strip())
        while True:
            tulokset = []
            for rivi in tiedosto[i+1: i+18]:
                tulokset.append(rivi)
            pelaajat[tiedosto[i]] = tulokset
            i += 18
            if i+18 > len(tiedosto):
                break

def uusi_peli():
    """Aloittaa uuden pelin ja kysyy pelaajien nimet"""
    pelin_nimi = input("Anna pelin nimi: ")
    while True:
        nimi = input("Anna nimi, tyhjä aloittaa pelin: ")
        if nimi == "":
            break
        pelaajat[nimi] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    tallenna(pelin_nimi)

def tulosta_UI():
    """Tulostaa UI:n"""
    print("1. Heitä nopat")
    print("2. Tallenna peli ja lopeta")

def tallennaTulos(pelaaja: str, valinta: tuple, pisteet: dict):
    """Tallentaa valitun tuloksen pelaajan listaan"""
    nimi = valinta[0]
    i = 0
    while i < len(pelaajat[pelaaja]):
        if nimi.__contains__(list(pisteet.keys())[i]):
            pelaajat[pelaaja][i] = valinta[1]
        i += 1
    # Lasketaan välisumma ja summa
    if int(pelaajat[pelaaja][0]) + int(pelaajat[pelaaja][1]) + int(pelaajat[pelaaja][2]) + int(pelaajat[pelaaja][3]) + int(pelaajat[pelaaja][4]) + int(pelaajat[pelaaja][5]) >= 63:
        pelaajat[pelaaja][6] = 50

    summa = 0
    laskin = 0
    while laskin < 16:
        summa += int(pelaajat[pelaaja][laskin])
        laskin += 1
    pelaajat[pelaaja][16] = summa


def tulostaNopat():
    """Tulostaa komian version noppa tuloksista"""
    print(" _____    _____    _____    _____    _____")
    print("|     |  |     |  |     |  |     |  |     |")
    print(f"|  {noppaTulokset[0]}  |  |  {noppaTulokset[1]}  |  |  {noppaTulokset[2]}  |  |  {noppaTulokset[3]}  |  |  {noppaTulokset[4]}  |")
    print("|_____|  |_____|  |_____|  |_____|  |_____|")

def valitse(vaihtoehdot: dict) -> tuple:
    """Kysyy pelaajalta minkä noppayhdistelmän hän haluaa tallentaa tuloksiin"""
    # Kysytään pelaajaa valitsemaan noppayhdistelmä vaihtoehdoista
    i = 0
    lista = {}
    for vaihtoehto in vaihtoehdot:
        print(f"{i}. {vaihtoehto}")
        lista[list(vaihtoehdot.keys())[i]] = list(vaihtoehdot.values())[i]
        i += 1
    print("Valinta:")
    valinta = int(input())
    palautus = (list(lista.keys())[valinta], list(lista.values())[valinta])
    return palautus

def voitto(pisteet: dict) -> str:
    """Tarkistaa voittajan jos pelaaja on saanut kaikki noppa yhdistelmät"""
    # Tarkistetaan onko pelaaja saanut kaikkiin noppa yhdistelmät
    nollat = 0
    for piste in pisteet:
        if piste != "Välisumma":
            if int(pisteet[piste]) == 0:
                nollat += 1
    # Jos pelaaja on saanut kaikki yhdistelmät, katsotaan onko kenelläkään enemmän pisteitä ja tulostetaan voittaja
    if nollat == 0:
        suurin = 0
        for pelaaja in pelaajat:
            if int(pelaajat[pelaaja][16]) > suurin:
                suurin = int(pelaajat[pelaaja][16])
                voittaja = f"{pelaaja} voitti pelin, pistemäärällä: {pelaajat[pelaaja][16]}"
        return voittaja
    else:
        return ""

def kenen_vuoro(pelaajat: dict) -> int:
    """Palauttaa kenen vuoro kun peli on ladattu"""
    vahiten_pisteita = 0
    kuka = 0
    laskin = 0
    for pelaaja in pelaajat:
        pisteet = tulokset(pelaaja)
        nollat = 0
        for piste in pisteet:
            if piste != "Välisumma":
                if int(pisteet[piste]) == 0:
                    nollat += 1
        if vahiten_pisteita < nollat:
            kuka = laskin
            vahiten_pisteita = nollat
        laskin += 1
    return kuka

        

    

def peli():
    """Pää peli"""
    # Aloitus ruutu
    global pelaajat
    global noppaTulokset
    print("1. Aloita uusi peli")
    print("2. Lataa peli")
    valinta = int(input())
    # i = kenen vuoro
    i = 0
    if valinta == 1:
        uusi_peli()
    elif valinta == 2:
        tiedosto = input("Syötä tallenteen nimi: ")
        pelin_nimi = tiedosto
        lataa(tiedosto)
        i = kenen_vuoro(pelaajat)

    # Peli alkaa
    while True:
        os.system('cls')
        if i >= len(pelaajat):
            i = 0
        # Kenen vuoro
        pelaaja = list(pelaajat.keys())[i]
        print(f"Pelaajan {pelaaja} vuoro")
        # Pelaajan pisteet
        pisteet = tulokset(pelaaja)
        # Tulosta pelaajan pisteet
        tulosta_tulokset(pelaaja, pisteet)
        # UI tulostus ja valinta
        tulosta_UI()
        valinta = int(input())
        if valinta == 1:
            # Heitä nopat
            os.system('cls')
            noppaTulokset = heita_nopat()
            tulostaNopat()
            vaihtoehdot_ = vaihtoehdot(pisteet)
            if vaihtoehdot_ != -1:
                print("Valitse tallennettava tulos:")
                valinta = valitse(vaihtoehdot_)
                tallennaTulos(pelaaja, valinta, pisteet)
            else:
                print("Ei tallennettavia tuloksia.")

            # Tarkistetaan onko pelaaja saanut kaikki tulokset
            pisteet = tulokset(pelaaja)
            voittaja = voitto(pisteet)
            if voittaja != "":
                print(voittaja)
                tallenna(pelin_nimi)
                break
                    


        elif valinta == 2:
            # Tallenna ja lopeta peli
            tallenne = input("Anna tallenteen nimi:")
            tallenna(tallenne)
            break

        i += 1

        

# Main program
# Pelaajat säilytetään globaalissa sanakirjassa
# Avaimena on pelaajan nimi ja arvona lista tuloksista
pelaajat = {}
noppaTulokset = [1,1,1,1,1]
pelin_nimi = ""

peli()

print("Kiitos pelaamisesta!")
loppu = input("Paina mitä tahansa poistuaksesi.")
