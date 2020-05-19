import random
STEVILO_DOVOLJENIH_NAPAK = 10

ZACETEK = 'Z' #nova igra

#konstante za rezultate ugibanj
PRAVILNA_CRKA = '+'
NAPACNA_CRKA = '-'
PONOVLJENA_CRKA = 'o'

#konstante za zmago in poraz
ZMAGA = 'W'
PORAZ = 'X'


bazen_besed = []
with open('Vislice/besede.txt', encoding='UTF-8') as datoteka_bazena:
    for beseda in datoteka_bazena:
        bazen_besed.append(beseda.strip().lower())
class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo.lower()
        if crke is None:
            self.crke = []
        else:
            self.crke = crke.lower()

    def pravilne_crke(self):
        seznam_pravilnih_crk = []
        for i in self.crke:
            if i in self.geslo:
                seznam_pravilnih_crk.append(i)
        return seznam_pravilnih_crk
                
    def napacne_crke(self):
        seznam_napacnih_crk = []
        for i in self.crke:
            if i not in self.geslo:
                seznam_napacnih_crk.append(i)
        return seznam_napacnih_crk

    def stevilo_napak(self):
        return len(self.napacne_crke())
    
    def zmaga(self):
        for c in self.geslo:
            if c not in self.crke:
                return False
        return True
    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def napravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def pravilni_del_gesla(self):
        trenutno = ''
        for crka in self.geslo:
            if crka in self.crke:
                trenutno += crka
            else:
                trenutno += '_'
        return trenutno
    
    def ugibaj(self, ugibana_crka):
        ugibana_crka = ugibana_crka.lower()
        if ugibana_crka in self.crke:
            return PONOVLJENA_CRKA
        self.crke.append(ugibana_crka)

        if ugibana_crka in self.geslo:
            # Uganil je
            if self.zmaga():
                #Preveri ce je ze zmagal s tem
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            #Ni uganil
            if self.poraz():
                #Preveri ce je ze zgubil s tem
                return PORAZ
            else:
                return NAPACNA_CRKA
        
def nova_igra():
    nakljucna_beseda = random.choice(bazen_besed)
    return Igra(nakljucna_beseda)


class Vislice:
    '''
    Skrbi za trenutno stanje več iger (imel bo več objektov tipa igra)
    '''

    def __init__(self):
        #slovar, ki ID-ju priredi objektt njegove igre
        self.igre = {}      #int -> (Igra, stanje)
    
    def prost_id_igre(self):
        '''Vrne nek id za novo igro, ki ga ne uporablja se nobena igra '''
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1
    
    def nova_igra(self):
        # dobimo novi ID

        nov_id = self.prost_id_igre()

        # naredimo novo igre

        sveza_igra = nova_igra()

        # vse to shranimo v self.igre

        self.igre[nov_id] = (sveza_igra, ZACETEK)
        
        # vrnemo nov ID

        return nov_id

    def ugibaj(self, id_igre, crka):
        # dobimo staro igro
        trenutna_igra, _ = self.igre[id_igre]

        # ugibamo crko, dobimo novo stanje
        novo_stanje = trenutna_igra.ugibaj()

        #zapisemo posodobljeno stanje
