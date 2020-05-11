STEVILO_DOVOLJENIH_NAPAK = 10

#konstante za rezultate ugibanj
PRAVILNA_CRKA = '+'
NAPACNA_CRKA = '-'
PONOVLJENA_CRKA = 'o'

#konstante za zmago in poraz
ZMAGA = 'W'
PORAZ = 'X'

class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo
        if crke is None:
            self.crke = []
        else:
            self.crke = crke

    def pravilne_crke(geslo, crke):
        seznam_pravilnih_crk = []
        for i in crke:
            if i in geslo:
                seznam_pravilnih_crk.append(i)
        return seznam_pravilnih_crk
                
    def napacna_crke(geslo, crke):
        seznam_napacnih_crk = []
        for i in crke:
            if i not in geslo:
                seznam_napacnih_crk.append(i)
        return seznam_napacnih_crk

    def stevilo_napak(geslo, crke):
        return len(seznam_napacnih_crk)
    
    def zmaga(geslo, crke):
        if list(geslo) == seznam_pravilnih_crk:
            if seznam_napacnih_crk <= STEVILO_DOVOLJENIH_NAPAK:
                return ZMAGA 
    def poraz(geslo, crke):
        if seznam_napacnih_crk > STEVILO_DOVOLJENIH_NAPAK:
            if list(geslo) != seznam_pravilnih_crk:
                return PORAZ

    def ugibaj(x):
        if x in crke:
            return PONOVLJENA_CRKA
        else:
            if x in geslo:
                return PRAVILNA_CRKA
            else:
                return NAPACNA_CRKA

        