# -*- coding: utf-8 -*-
class Vozilo:
    def __init__(self, znamka, model, st_kilometrov, datum_servisa):
        self.znamka = znamka
        self.model = model
        self.st_kilometrov = st_kilometrov
        self.datum_servisa = datum_servisa

    def dodaj_km(self, novi_km):
        self.st_kilometrov += novi_km

    def posodobi_datum_servisa(self, novi_datum):
        self.datum_servisa = novi_datum

def izpis_voznega_parka(vozila):
    if not vozila:
        print ("V voznem parku ni vnešenih vozil")
    else:
        for index, vozilo in enumerate(vozila):
            print "%s) %s %s z %s prevoženimi kilometri. Zadnji servis je bil %s" % (index+1, vozilo.znamka, vozilo.model, vozilo.st_kilometrov, vozilo.datum_servisa)

def ustvari_vozilo_objekt (znamka, model, st_kilometrov_str, datum_servisa, vozila):
    st_kilometrov_str = st_kilometrov_str.replace(",", ".")
    st_kilometrov = float(st_kilometrov_str)

    novo_vozilo = Vozilo(znamka, model, st_kilometrov, datum_servisa)
    vozila.append(novo_vozilo)
    return True

def dodaj_novo_vozilo(vozila):
    znamka = raw_input("Prosimo vnesite znamko avtomobila: ")
    model = raw_input("Prosimo vnesite model avtomobila: ")
    st_kilometrov_str = raw_input("Prosimo vnesite število kilometrov: ")
    datum_servisa = raw_input("Prosimo vnesite datum zadnjega servisa v obliki(DD.MM.LLLL: ")

    rezultat = ustvari_vozilo_objekt (znamka, model, st_kilometrov_str, datum_servisa, vozila)

    if rezultat:
        print "Uspešno ste dodali novo vozilo: %s %s" % (znamka, model)
    else:
        print "Prosimo vnesite samo število kilometrov"

def izberi_vozilo(vozila):
    print ("Prosimo izberite številko vozila, katerega bi radi urejali: ")
    print ""
    izpis_voznega_parka(vozila)
    print ""

    izbor = raw_input("Katero številko vozila bi radi izbrali?: ")
    return vozila[int(izbor) - 1]

def dodaj_nove_kilometre(vozila):
    izbrano_vozilo = izberi_vozilo(vozila)

    print "Izbrano vozilo: %s %s z %s kilometri" % (izbrano_vozilo.znamka, izbrano_vozilo.model, izbrano_vozilo.st_kilometrov)
    print ""

    novi_km_str = raw_input("Koliko kilometrov bi želeli dodati k obstoječim?: ")
    novi_km = float(novi_km_str)
    izbrano_vozilo.dodaj_km(novi_km)
    print "Novo število kilometrov za %s %s je sedaj: %s" % (izbrano_vozilo.znamka, izbrano_vozilo.model, izbrano_vozilo.st_kilometrov)

def spremeni_datum_servisa(vozila):
    izbrano_vozilo = izberi_vozilo(vozila)

    print "Izbrano vozilo: %s %s z datumom servisa: %s" % (izbrano_vozilo.znamka, izbrano_vozilo.model, izbrano_vozilo.datum_servisa)
    print ""
    novi_datum_servisa = raw_input("Kateri je zadnji datum servisa za to vozilo? (DD.MM.LLLL): ")
    print""
    izbrano_vozilo.posodobi_datum_servisa(novi_datum_servisa)
    print "Datum servisa posodobljen!"

def shrani_datoteko(vozila):
    with open("vozni_park.txt", "w") as vozna_datoteka:
        for vozilo in vozila:
            vozna_datoteka.write("%s,%s,%s,%s\n" %(vozilo.znamka, vozilo.model, vozilo.st_kilometrov, vozilo.datum_servisa))

def main():
    print "Dobrodošli v vaš vozni park!"

    vozila = []

    with open("vozni_park.txt", "r") as vozni_file:
        for line in vozni_file:
            try:
                znamka, model, st_kilometrov_str, datum_servisa = line.split(",")
                ustvari_vozilo_objekt(znamka, model, st_kilometrov_str, datum_servisa, vozila)
            except ValueError:
                continue

    while True:
        print ""
        print "Prosimo izberite eno izmed sledečih opcij:"
        print "a) Ogled voznega parka"
        print "b) Dodaj novo vozilo v vozni park"
        print "c) Uredi število prevoženih kilometrov"
        print "d) Uredi datum zadnjega servisa"
        print "e) Zapusti program"

        izbira = raw_input("Katero opcijo boste izbrali? (a, b, c, d, e): ")
        print ""

        if izbira.lower() == "a":
            izpis_voznega_parka(vozila)
        elif izbira.lower() == "b":
            dodaj_novo_vozilo(vozila)
        elif izbira.lower() == "c":
            dodaj_nove_kilometre(vozila)
        elif izbira.lower() == "d":
            spremeni_datum_servisa(vozila)
        elif izbira.lower() == "e":
            print "Hvala ker ste uporabljali vozni park. Lep dan!"
            shrani_datoteko(vozila)
            break
        else:
            print "Prosimo vnesite samo črke a,b,c,d,e: "

if __name__ == '__main__':
    main()
