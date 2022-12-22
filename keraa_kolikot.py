import pygame
from random import randint

# pelin globaalit vakiot
X_RESO = 640
Y_RESO = 480 
X_PISTEET = X_RESO - 155
Y_PISTEET = 0 + 10
ABS_VAK_NOPEUS_0 = 0
ABS_VAK_NOPEUS_1 = 1
RAND_TIMER_MIN = 50
RAND_TIMER_MAX = 100
RAND_TIMER2_MIN = 150
RAND_TIMER2_MAX = 300

LEVEL_RAJA = 10
BONUS_RAJA = 10

ENNATYS_TIEDOSTO = "all_time_record.txt"

class Robotti:
    # luokan pysyvät vakiot luokkamuuttujina
    ROBO_KUVA = "robo.png"
    ROBO_KUVA2 = "robo.png" # jokin uusi kuva, osoittamaan muuta statusta (esim pökertymistä törmayksen jälkeen)
    KOKO_X = 0 # Robotin koko / X
    KOKO_Y = 0 # Robotin koko / Y
    MIN_X = 0 # minimi x, jotta robo näkyy kokonaan 
    MAX_X = 0 # maximi x, jotta robo näkyy kokonaan 
    MIN_X2 = 0 # minimi x, jotta robo näkyy vielä osittainkin
    MAX_X2 = 0 # minimi x, jotta robo näkyy vielä osittainkin
    MED_X = 0  # keskikohta, jotta voi etsiä lähimmän reunan suunnan
    MIN_Y = 0 # minimi Y, jotta robo näkyy kokonaan
    MAX_Y = 0 # maximi Y, jotta robo näkyy kokonaan
    MED_Y = 0  # ei tarvita (...vielä...)

    # tällä metodilla asetetaan luokan muuttujat ennen luokan olioiden luontia
    def init_RoboLuokka():
        alustus_robo = pygame.image.load(Robotti.
        ROBO_KUVA)
        Robotti.KOKO_X = alustus_robo.get_width()
        Robotti.KOKO_Y = alustus_robo.get_height()
        Robotti.MIN_X = 0
        Robotti.MAX_X = X_RESO - alustus_robo.get_width()
        Robotti.MIN_X2 = 0 - alustus_robo.get_width()
        Robotti.MAX_X2 = X_RESO
        Robotti.MED_X = (Robotti.MAX_X - Robotti.MIN_X)/2 # keskikohta, jotta voi etsiä lähimmänb reunana
        Robotti.MIN_Y = 0 - alustus_robo.get_height()
        Robotti.MAX_Y = Y_RESO - alustus_robo.get_height()
        Robotti.MED_Y = (Robotti.MAX_Y - Robotti.MIN_Y)/2 # ei tarvita (...vielä...)

    # tämä alustus vaatii yllänäkyvän luokka-alustuksen ensin...
    def __init__(self):
        self.x = Robotti.MED_X
        self.x_nopeus = ABS_VAK_NOPEUS_0
        self.y = Robotti.MAX_Y
        self.y_nopeus = ABS_VAK_NOPEUS_0
        self.robo = pygame.image.load(Robotti.ROBO_KUVA)

    def uusi_paikka_ja_nopeus(self):
        if self.y < Robotti.MAX_Y: 
            self.x_nopeus = ABS_VAK_NOPEUS_0
            self.y_nopeus = ABS_VAK_NOPEUS_1
            self.y += self.y_nopeus 

        else: 
            self.y = Robotti.MAX_Y
            self.y_nopeus = ABS_VAK_NOPEUS_0
            self.x_nopeus = -ABS_VAK_NOPEUS_1 if self.x < Robotti.MED_X else ABS_VAK_NOPEUS_1  
            self.x += self.x_nopeus

    def nayta(self, naytto: pygame.Surface):
        naytto.blit(self.robo, (self.x, self.y))

class Kolikko:
    # luokan pysyvät vakiot luokkamuuttujina
    KOLIKKO_KUVA = "kolikko.png"
    KOLIKKO_KUVA2 = "kolikko.png" 
    KOKO_X = 0 # kolikon koko / X
    KOKO_Y = 0 # kolikon koko / Y

    MIN_X = 0 # minimi x, jotta kolikko näkyy kokonaan (esim tiputettaessa)
    MAX_X = 0 # maximi x, jotta kolikko näkyy kokonaan (esim tiputettaessa)
    MED_X = 0  # keskikohta
    MIN_Y = 0
    MAX_Y = 0
    MED_Y = 0  # ei tarvita (...vielä...)

    # tällä metodilla asetetaan luokan muuttujat ennen luokan olioiden luontia
    def init_KolikkoLuokka():
        alustus_kolikko = pygame.image.load(Kolikko.KOLIKKO_KUVA)
        Kolikko.KOKO_X = alustus_kolikko.get_width()
        Kolikko.KOKO_Y = alustus_kolikko.get_height()
        Kolikko.MIN_X = 0
        Kolikko.MAX_X = X_RESO - alustus_kolikko.get_width()
        Kolikko.MIN_X2 = 0 - alustus_kolikko.get_width()
        Kolikko.MAX_X2 = X_RESO
        Kolikko.MED_X = (Kolikko.MAX_X - Kolikko.MIN_X)/2 # keskikohta, jotta voi etsiä lähimmänb reunana
        Kolikko.MIN_Y = 0 - alustus_kolikko.get_height()
        Kolikko.MAX_Y = Y_RESO - alustus_kolikko.get_height()
        Kolikko.MED_Y = (Kolikko.MAX_Y - Kolikko.MIN_Y)/2 # ei tarvita (...vielä...)

    # tämä alustus vaatii yllänäkyvän luokka-alustuksen ensin...
    def __init__(self):
        self.x = randint(Kolikko.MIN_X, Kolikko.MAX_X)
        self.x_nopeus = ABS_VAK_NOPEUS_0
        self.y = Kolikko.MIN_Y
        self.y_nopeus = ABS_VAK_NOPEUS_1
        self.kolikko = pygame.image.load(Kolikko.KOLIKKO_KUVA)
        self.havita = False # asetetaan True kun kolikko pitää hävittää näytöltä

    def uusi_paikka_ja_nopeus(self):
        if self.y < Kolikko.MAX_Y: 
            self.x_nopeus = ABS_VAK_NOPEUS_0
            self.y_nopeus = ABS_VAK_NOPEUS_1 * level
            self.y += self.y_nopeus 

    def nayta(self, naytto: pygame.Surface):
        naytto.blit(self.kolikko, (self.x, self.y))

class Hirvio:
    # luokan pysyvät vakiot luokkamuuttujina
    HIRVIO_KUVA = "hirvio.png"
    KOKO_X = 0 # hirvion koko / X
    KOKO_Y = 0 # hirvion koko / Y

    MIN_X = 0 # minimi x, jotta hirvio näkyy kokonaan (esim tiputettaessa)
    MAX_X = 0 # maximi x, jotta hirvio näkyy kokonaan (esim tiputettaessa)
    MED_X = 0  # keskikohta
    MIN_Y = 0
    MAX_Y = 0
    MED_Y = 0  # ei tarvita (...vielä...)

    # tällä metodilla asetetaan luokan muuttujat ennen luokan olioiden luontia
    def init_HirvioLuokka():
        alustus_hirvio = pygame.image.load(Hirvio.HIRVIO_KUVA)
        Hirvio.KOKO_X = alustus_hirvio.get_width()
        Hirvio.KOKO_Y = alustus_hirvio.get_height()
        Hirvio.MIN_X = 0
        Hirvio.MAX_X = X_RESO - alustus_hirvio.get_width()
        Hirvio.MIN_X2 = 0 - alustus_hirvio.get_width()
        Hirvio.MAX_X2 = X_RESO
        Hirvio.MED_X = (Hirvio.MAX_X - Hirvio.MIN_X)/2 # keskikohta, jotta voi etsiä lähimmänb reunana
        Hirvio.MIN_Y = 0 - alustus_hirvio.get_height()
        Hirvio.MAX_Y = Y_RESO - alustus_hirvio.get_height()
        Hirvio.MED_Y = (Hirvio.MAX_Y - Hirvio.MIN_Y)/2 # ei tarvita (...vielä...)

    # tämä alustus vaatii yllänäkyvän luokka-alustuksen ensin...
    def __init__(self):
        self.x = randint(Hirvio.MIN_X, Hirvio.MAX_X)
        self.x_nopeus = ABS_VAK_NOPEUS_0
        self.y = Hirvio.MIN_Y
        self.y_nopeus = ABS_VAK_NOPEUS_1
        self.hirvio = pygame.image.load(Hirvio.HIRVIO_KUVA)
        self.havita = False # asetetaan True kun hirviö pitää hävittää näytöltä

    def uusi_paikka_ja_nopeus(self):
        if self.y < Hirvio.MAX_Y: 
            self.x_nopeus = ABS_VAK_NOPEUS_0
            self.y_nopeus = ABS_VAK_NOPEUS_1 * max(1, level - 2)
            self.y += self.y_nopeus 

    def nayta(self, naytto: pygame.Surface):
        naytto.blit(self.hirvio, (self.x, self.y))

def lue_all_time_record():
    osat = []
    try:
        with open(ENNATYS_TIEDOSTO) as tiedosto:
            for rivi in tiedosto:
                rivi = rivi.replace("/n", "")
                osat = rivi.split(";")
                vanha_ennatys = int(osat[1])
                return vanha_ennatys
    except:
        return -1

def tallenna_all_time_record(uusi_ennatys: int):
    try:
        with open(ENNATYS_TIEDOSTO, "w") as tiedosto:
            stringi = "DefaultPlayer;" + f"{uusi_ennatys}" 
            tiedosto.write(stringi)
    except:
        return -1

def lopeta_peli():
    exit()

if __name__ == "__main__":
    kolikot = []
    hirviot = []

    pygame.init()

    # alusta luokan olioille yhteiset vakiot ennen olioiden luontia
    Kolikko.init_KolikkoLuokka()
    Hirvio.init_HirvioLuokka()
    Robotti.init_RoboLuokka()
    
    naytto = pygame.display.set_mode((X_RESO, Y_RESO))
    pygame.display.set_caption("Kerää kolikot")

    # luodaan eka Kolikko
    kolikko = Kolikko()
    kolikot.append(kolikko)
    
    # eka Hirvio luodaan vasta tasolla 2...
 
    # luodaan robotti
    my_robo = Robotti()
    robo_oikealle = False
    robo_vasemmalle = False

    kello = pygame.time.Clock()

    peli_kaynnissa = True
    uusi_peli_pyydetty = False
    maara_osumat = 0
    ennatys = 0
    all_time_record = 0
    maara_elamat = 3
    bonus_laskuri = 0
    level_laskuri = 0
    level = 1

    all_time_record = lue_all_time_record() 
    vanha_ennatys = max(all_time_record, 0)
    ennatys = max(all_time_record, 0)

    # alusta satunnainen aikaviive uuden olion luomiselle
    random_timer = randint(RAND_TIMER_MIN, RAND_TIMER_MAX)
    random_timer2 = randint(RAND_TIMER2_MIN, RAND_TIMER2_MAX)

    while True:
        if maara_osumat > ennatys:
            ennatys = maara_osumat

        # tason nosto
        if level_laskuri == LEVEL_RAJA:
            level += 1
            level_laskuri = 0

        # lisäelämien anto
        if bonus_laskuri == BONUS_RAJA:
            maara_elamat += 1
            bonus_laskuri = 0

        # tehdäänkö pelin lopetus
        if (maara_elamat <= 0) and peli_kaynnissa:
            kolikot = []
            hirviot = []
            peli_kaynnissa = False

        # tehdäänkö pelin uudelleen käynnistys
        elif not peli_kaynnissa and uusi_peli_pyydetty:
            ## kolikot alustetaan 
            kolikot = []
            kolikko = Kolikko()
            kolikot.append(kolikko)

            ## hirviot alustetaan 
            hirviot = []
            
            # jatketaan samalla robo-oliolla
            my_robo.x = Robotti.MED_X

            # uusi peli alkaa
            peli_kaynnissa = True
            uusi_peli_pyydetty = False
            level = 1
            vanha_ennatys = ennatys
#            ennatys = 0
            maara_elamat = 3
            maara_osumat = 0
            bonus_laskuri = 0
            level_laskuri = 0
            random_timer = randint(RAND_TIMER_MIN, RAND_TIMER_MAX) - min(30, (level - 1) * 5)
            random_timer2 = randint(RAND_TIMER2_MIN, RAND_TIMER2_MAX)

        # luo uusi kolikko viiveen jälkeen
        if random_timer == 0 and peli_kaynnissa:
            kolikko = Kolikko()
            kolikot.append(kolikko)
            random_timer = randint(RAND_TIMER_MIN, RAND_TIMER_MAX)  - min(30, (level - 1) * 5)
        elif peli_kaynnissa:
            random_timer -= 1 # odotellaan vielä uuden luontia
 
        # luo uusi hirvio viiveen jälkeen
        if random_timer2 == 0 and peli_kaynnissa:
            if level >= 2:
                hirvio = Hirvio()
                hirviot.append(hirvio)
                random_timer2 = randint(RAND_TIMER2_MIN, RAND_TIMER2_MAX)
        elif peli_kaynnissa:
            random_timer2 -= 1 # odotellaan vielä uuden luontia

        # tsekkaile tapahtumat
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_LEFT:
                    robo_vasemmalle = True
                if tapahtuma.key == pygame.K_RIGHT:
                    robo_oikealle = True
                if tapahtuma.key == pygame.K_SPACE:
                    if not peli_kaynnissa:
                        uusi_peli_pyydetty = True
                if tapahtuma.key == pygame.K_ESCAPE:
                    if not peli_kaynnissa:
                        uusi_ennatys = max(vanha_ennatys, ennatys)
                        if uusi_ennatys > all_time_record:
                            tallenna_all_time_record(uusi_ennatys)
                        lopeta_peli()

            if tapahtuma.type == pygame.KEYUP:
                if tapahtuma.key == pygame.K_LEFT:
                    robo_vasemmalle = False
                if tapahtuma.key == pygame.K_RIGHT:
                    robo_oikealle = False

            if tapahtuma.type == pygame.QUIT:
                uusi_ennatys = max(vanha_ennatys, ennatys)
                if uusi_ennatys > all_time_record:
                    tallenna_all_time_record(uusi_ennatys)
                lopeta_peli()


        if robo_oikealle:
            my_robo.x += 10
        if robo_vasemmalle:
            my_robo.x -= 10

        # päivitä kolikkojen paikat ja olemus tapahtumien perusteella
        for kolikko in kolikot:
            kolikko.uusi_paikka_ja_nopeus()
 
        # päivitä hirviöiden paikat ja olemus tapahtumien perusteella
        for hirvio in hirviot:
            hirvio.uusi_paikka_ja_nopeus()

        # laske pisteet ja laita tsekkaa osumat
        x_robo_left = my_robo.x
        x_robo_right = my_robo.x + my_robo.KOKO_X
        for kolikko in kolikot:
            if kolikko.x + Kolikko.KOKO_X > x_robo_left and kolikko.x < x_robo_right:
                if kolikko.y >= Kolikko.MAX_Y - Robotti.KOKO_Y:
                    maara_osumat +=1
                    level_laskuri +=1
                    bonus_laskuri +=1
                    kolikko.havita = True
            else:
                if kolikko.y >= Kolikko.MAX_Y:
                    maara_elamat -=1
                    kolikko.havita = True

        kolikot2 = []
        kolikot2 = [k for k in kolikot if not k.havita ]
        kolikot = kolikot2

        # tsekkaa hirvio osumat
        x_robo_left = my_robo.x
        x_robo_right = my_robo.x + my_robo.KOKO_X
        for hirvio in hirviot:
            if hirvio.x + Hirvio.KOKO_X > x_robo_left and hirvio.x < x_robo_right:
                if hirvio.y >= Hirvio.MAX_Y - Robotti.KOKO_Y:
                    maara_elamat -= 1
                    hirvio.havita = True
            else:
                if hirvio.y >= Hirvio.MAX_Y:
                    hirvio.havita = True

        hirviot2 = []
        hirviot2 = [h for h in hirviot if not h.havita ]
        hirviot = hirviot2


        # päivitä näyttö
        if peli_kaynnissa:
            naytto.fill((min(255, 50 + level*30), min(255, 50 + level*30), min(255, 140 + level*20)))
        else: # asetetaan pysähtyneen peli väri sellaiseksi, että teksti näkyy...
            naytto.fill((80, 80, 140))

        # laitetaan robot näytettäväksi
        my_robo.nayta(naytto)

        # laitetaan kolikot näytettäväksi
        for kolikko in kolikot:   
            kolikko.nayta(naytto)

        # laitetaan hirviot näytettäväksi
        for hirvio in hirviot:   
            hirvio.nayta(naytto)

        # pisteet näytille
        fontti0 = pygame.font.SysFont("Arial", 24)
        level_str = f"Taso: {level}"
        teksti0 = fontti0.render(level_str, True, (0, 255, 255))
        naytto.blit(teksti0, (20, Y_PISTEET + 0))

        if peli_kaynnissa:        
            fontti0 = pygame.font.SysFont("Arial", 24)
            elamat_str = "Elämät: "
            teksti0b = fontti0.render(elamat_str, True, (0, 255, 255))
            naytto.blit(teksti0b, (20, Y_PISTEET + 25))

            fontti1 = pygame.font.SysFont("Arial", 48)
            elamat_str2 = "* " * maara_elamat
            teksti0c = fontti1.render(elamat_str2, True, (255, 0, 0))
            naytto.blit(teksti0c, (120, Y_PISTEET + 25))


        fontti2 = pygame.font.SysFont("Arial", 24)
        pisteet_str = f"Pisteet:  {maara_osumat}"
        teksti2 = fontti2.render(pisteet_str, True, (0, 255, 255))
        naytto.blit(teksti2, (X_PISTEET, Y_PISTEET + 0))

        fontti3 = pygame.font.SysFont("Arial", 24)
        ennatys_str = f"Ennätys:  {ennatys}"
        teksti3 = fontti3.render(ennatys_str, True, (0, 255, 255))
        naytto.blit(teksti3, (X_PISTEET, Y_PISTEET + 25))

        # pelin lopetus näytille
        if not peli_kaynnissa:
            peli_ohi_str = "Game over."
            fontti4 = pygame.font.SysFont("Arial", 24)
            teksti4 = fontti4.render(peli_ohi_str, True, (0, 255, 0))
            naytto.blit(teksti4, (100, 100))

            if ennatys > vanha_ennatys:
                ennatys_str = f"Onnittelut! Uusi ennätys: {ennatys} ({vanha_ennatys})"
                fontti5 = pygame.font.SysFont("Arial", 24)
                teksti5 = fontti3.render(ennatys_str, True, (0, 255, 0))
                naytto.blit(teksti5, (100, 130))

            ohjeet_str = "Paina <välilyönti> jatkaaksesi"
            fontti6 = pygame.font.SysFont("Arial", 24)
            teksti6 = fontti6.render(ohjeet_str, True, (0, 255, 255))
            naytto.blit(teksti6, (100, 180))
 
            lopetus_str = "Paina <ESC> lopettaaksesi"
            fontti7 = pygame.font.SysFont("Arial", 24)
            teksti7 = fontti7.render(lopetus_str, True, (0, 255, 255))
            naytto.blit(teksti7, (100, 210))


        # päivitä näyttö
        pygame.display.flip()    

        # aseta näytön päivitystahti
        kello.tick(60)

