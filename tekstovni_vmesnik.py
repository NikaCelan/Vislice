import model

trenutna_igra = model.nova_igra()

def izpis_poraz(igra):
    return f'IZGUBIL SI, geslo je bilo : {igra.geslo}'

def izpis_zmage(igra):
    return f'ČESTITM, ZMAGAL SI. Potreboval si {len(igra.napacne_crke())} ugibov'

def izpis_igre(igra):
    text = (
        f'Stanje gesla: {igra.pravilni_del_gesla()} \n' +
        f'Imaš še {model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()} dovoljenih napak'
    )
    return text

def zahtevaj_vnos():
    return input('Vpiši naslednjo črko:')

def pozeni_vmesik():
    #Naredimo novo igro

    trenutna_igra = model.nova_igra()
    
    while True:
        #Pokazemo stanje
        print(izpis_igre(trenutna_igra))

        crka = zahtevaj_vnos()

        trenutna_igra.ugibaj(crka)

        #Preveri zmago/poraz
        if trenutna_igra.zmaga():
            print(izpis_zmage(trenutna_igra))
            break
        if trenutna_igra.poraz():
            print(izpis_poraz(trenutna_igra))
            break
        #Tu pol skocimo spet na zacetek
        #Namesto breka lahko napisemo tudi samo Return
    
pozeni_vmesik()