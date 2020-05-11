import random
STEVILO_DOVOLJENIH_NAPAK = 10

#konstante za rezultate ugibanj
PRAVILNA_CRKA = '+'
NAPACNA_CRKA = '-'
PONOVLJENA_CRKA = 'o'

#konstante za zmago in poraz
ZMAGA = 'W'
PORAZ = 'X'


bazen_besed = []
with open('Vislice/besede.txt') as datoteka_bazena:
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
        return ' '.join(self.napavne_crke())

    def pravilni_del_gesla(self):
        trenutno = ''
        for crka in self.geslo:
            if crka in self.crke:
                trenutno += crka
            else:
                trenutno += '_'
    
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
        