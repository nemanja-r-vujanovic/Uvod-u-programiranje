# ----------------------------------------------------------------------------------------------------
# Igra "Pogodi rec" - Racunar bira jednu rec i menja redosled slova, igrac pogadja trazenu rec

import random

reci = ("Python", "Programiranje",
        "Kolokvijum", "Ispit")
rec = random.choice(reci)                       # Nasumicno se bira jedna rec
rec = rec.upper()                               # Odabrana rec se konvertuje u velika slova
racunar = rec                                   # Odabrana rec se cuva u promenljivu racunar
ispreturana_rec = ""                            # Pomocni string

while (len(rec) > 0):                           # Petlja se izvrsava sve dok se u reci nalazi bar jedno slovo
    indeks = random.randrange(len(rec))         # Nasumicno se bira jedan indeks (0 <= X < len(rec))
    ispreturana_rec += rec[indeks]              # Pomocni string se nadovezuje sa nasumicno odabranim slovom
    """
    rec = rec[:indeks] + rec[indeks+1:]
    Primer: nasumicno odabrana rec "Python" i indeks 3
    rec = rec[:3] + rec[3+1:] -> rec = Pyton
    """    
    rec = rec[:indeks] + rec[indeks+1:]         # Iz stringa se uklanja nasumicno odabrano slovo    

print(ispreturana_rec)                          # Ispis ispreturane reci
igrac = input("Pogodite trazenu rec: ").upper() # Igracev unos

if (igrac == racunar):
    print("Cestitamo, pogodili ste :)")
else:
    print("Zao nam je, niste pogodili  :(")
print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Kreiranje liste

lista = [1, 2.5, "Tekst", True, False, None]
print("Lista:", lista)
print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Upotreba funkcije len()

lista = [1, 2.5, "Tekst", True, False, None]
print("Duzina liste je: ", len(lista))
print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Indeksiranje liste

lista = [1, 2.5, "Tekst", True, False, None]
print(lista[5])
print(lista[-1])
print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Isecanje liste

lista = [1, 2.5, "Tekst", True, False, None]
print(lista[2:5])
print(lista[-4:-1])
print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Ispisivanje sadrzaja liste koristeci for petlju

lista = [1, 2.5, "Tekst", True, False, None]

for element in lista:
    print(element)
print()

for i in range(len(lista)):
    print(lista[i])
print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Upotreba operatora in sa listom

lista = [1, 2.5, "Tekst", True, False, None]

if (100 in lista):
    print("Broj 100 se nalazi u listi.")
else:
    print("Broj 100 se ne nalazi u listi.")
    
if (100 not in lista):
    print("Broj 100 se ne nalazi u listi.")
else:
    print("Broj 100 se nalazi u listi.")
print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Nadovezivanje lista

lista1 = [1, 2]
lista2 = [3, 4]

lista1 += lista2
print("Nadovezane liste:", lista1)
print()

lista3 = []
for i in range(10):
    broj = int(input(f"Unesite {i+1}. ceo broj: "))
    lista3 += [broj,]                           # Kod nadovezivanja lista zarez nije neophodan; kod nadovezivanja n-torki jeste
print()
print(lista3)
print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Promenljivost liste

lista4 = [1, 2, 5]
lista4[1:3] = [2, 3, 4]                         # Izmena vrednosti na osnovu isecka
lista4[3] = 5                                   # Izmena vrednosti na osnovu indeksa
print(lista4)
print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Brisanje elemenata liste koristeci del

lista5 = [1, 2, 3, 5]
del lista5[3]                                   # Brisanje elementa na osnovu indeksa
# del lista5[1]
# del lista5[1]
del lista5[1:3]                                 # Brisanje elemenata na osnovu isecka
print(lista5)
print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Dodavanje elemenata u listu

lista6 = []
lista6.append(5)
lista6.append(100.999)
lista6.append(True)
lista6.append(False)
lista6.append("Test")
lista6.append(None)
lista6.append(True)
print(lista6)
print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Brisanje elemenata liste koristeci remove

print("Pre brisanja elemenata", lista6)
lista6.remove(True)                             # Brisanje elementa na osnovu vrednosti
lista6.remove(True)
print("Posle brisanja elemenata", lista6)
print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Brisanje svih elemenata liste

lista6.clear()                                  # Brisanje svih elemenata
print(lista6)
print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Sortiranje liste

lista7 = []
lista7.append(5)
lista7.append(63)
lista7.append(72)
lista7.append(41)
lista7.append(63)

lista7.sort()                                   # Isto sto i: lista7.sort(reverse=False) # Lista se sortira u rastucem poretku (od manje ka vecoj)
print("Lista sortirana u rastucem poretku:", lista7)
lista7.sort(reverse=True)                       # Lista se sortira u opadajucem poretku (od vece ka manjoj)
print("Lista sortirana u opadajucem poretku:", lista7)
print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Ostale metode liste

lista8 = []
lista8.append(55)
lista8.append(62)
lista8.append(71)
lista8.append(45)
lista8.append(62)

# Broj pojavljivanja vrednosti
broj_pojavljivanja = lista8.count(62)
print(f"Broj 62 se nalazi {broj_pojavljivanja} puta.")

# Indeks na kojem se pojavljuje vrednost
indeks_elementa = lista8.index(71)
print("Broj 71 se nalazi na indeksu:", indeks_elementa)

# Brisanje elementa na osnovu indeksa (pri cemu ce biti vracena vrednost koja je obrisana)
poslednji_element = lista8.pop()
print("\nObrisali ste poslednji element:", poslednji_element)

obrisani_element = lista8.pop(3)
print("Obrisali ste element na indeksu 3:", obrisani_element)

print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Igra "Loto 7/39" - igrac sastavlja svoju kombinaciju od 7 razlicitih brojeva u opsegu od 1 do 39 i pokusava da pogodi kombinaciju koju je racunar odabrao

import random

igrac = []
while (len(igrac) < 7):
    broj = int(input(f"Unesite {len(igrac)+1}. broj (1-39): "))

    if (1 <= broj <= 39):                       # if (broj >= 1 and broj <= 39):
        if (broj not in igrac):
            igrac.append(broj)
        else:
            print("Taj broj ste vec odigrali!")
    else:
        print("Uneli ste broj koji nije u opsegu 1-39!")

igrac.sort()
print()
print("Igrac:", igrac)

racunar = []
while (len(racunar) < 7):
    odabir = random.randint(1, 39)
    if (odabir not in racunar):
        racunar.append(odabir)

racunar.sort()
print("Racunar:", racunar)

broj_pogodjenih = 0
for odigran_broj in igrac:
    if (odigran_broj in racunar):
        broj_pogodjenih += 1

print("Broj pogodaka:", broj_pogodjenih)
print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Ugnjezdene sekvence

ugnjezdena_sekvenca = (1, 2, 3, [4, 5, 6], 7, 8, 9, (10, 11, 12))

print(ugnjezdena_sekvenca[0])                   # Ispisuje 1
print(ugnjezdena_sekvenca[1])                   # Ispisuje 2
print(ugnjezdena_sekvenca[2])                   # Ispisuje 3
print(ugnjezdena_sekvenca[3])                   # Ispisuje [4, 5, 6]
print(ugnjezdena_sekvenca[4])                   # Ispisuje 7
print(ugnjezdena_sekvenca[5])                   # Ispisuje 8
print(ugnjezdena_sekvenca[6])                   # Ispisuje 9
print(ugnjezdena_sekvenca[7])                   # Ispisuje (10, 11, 12)

print(ugnjezdena_sekvenca[3][0])                # Ispisuje 4
print(ugnjezdena_sekvenca[3][1])                # Ispisuje 5
print(ugnjezdena_sekvenca[3][2])                # Ispisuje 6

"""
Prethodne tri linije koda su mogle biti zapisane i ovako:

print(ugnjezdena_sekvenca[3][-3])               # Ispisuje 4
print(ugnjezdena_sekvenca[3][-2])               # Ispisuje 5
print(ugnjezdena_sekvenca[3][-1])               # Ispisuje 6

print(ugnjezdena_sekvenca[-5][0])               # Ispisuje 4
print(ugnjezdena_sekvenca[-5][1])               # Ispisuje 5
print(ugnjezdena_sekvenca[-5][2])               # Ispisuje 6

print(ugnjezdena_sekvenca[-5][-3])              # Ispisuje 4
print(ugnjezdena_sekvenca[-5][-2])              # Ispisuje 5
print(ugnjezdena_sekvenca[-5][-1])              # Ispisuje 6
"""

print(ugnjezdena_sekvenca[7][0])                # Ispisuje 10
print(ugnjezdena_sekvenca[7][1])                # Ispisuje 11
print(ugnjezdena_sekvenca[7][2])                # Ispisuje 12

# I u prethodne tri linije koda su mogle da se koriste kombinacije pozitivnog i negativnog indeksiranja

print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Raspakivanje sekvence

# Broj varijabli mora da bude jednak broju elemenata u sekvenci
vred1, vred2, vred3, vred4, vred5, vred6, vred7, vred8 = (1, 2, 3, [4, 5, 6], 7, 8, 9, (10, 11, 12)) 

print(vred1, vred2, vred3, vred4, vred5, vred6, vred7, vred8)
print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Deljene reference

lista9 = [123, 456, 789]
lista10 = lista9

print(lista9)
print(lista10)

lista9.remove(456)
lista10.remove(789)

print(lista9)
print(lista10)
print("-" * 50)

# Objasnjenje: su zapravo samo dva imena za istu listu u memoriji; kada menjamo sadrzaj jedne, menja se i sadrzaj one druge
# ----------------------------------------------------------------------------------------------------
# Izbegavanje deljenih referenci

lista11 = [123, 456, 789]
lista12 = lista11[:]                            # Ovim se izbegavaju deljene reference

print(lista11)
print(lista12)

lista11.remove(456)
lista12.remove(789)

print(lista11)
print(lista12)
print("-" * 50)

# Objasnjenje: sada je svaka lista na razlicitoj memorijskoj lokaciji
# ----------------------------------------------------------------------------------------------------
# Kreiranje recnika

# kljuc1: vrednost kljuca1, kljuc2: vrednost kljuca2
recnik1 = {"UPR": "Uvod u Programiranje", "MAT": "Matematika"} 

print(recnik1)                                  # Ispis recnika
print(len(recnik1))                             # Ispis broja kljuceva
print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Pristup vrednostima u recniku

recnik1 = {"UPR": "Uvod u Programiranje", "MAT": "Matematika"}
print(recnik1["UPR"])                           # Ispis vrednosti kljuca "UPR"
print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Upotreba operatora in sa recnikom

recnik1 = {"UPR": "Uvod u Programiranje", "MAT": "Matematika"}

if ("upr" in recnik1):
    print(recnik1["upr"])
else:
    print("Kljuc \"upr\" se ne nalazi u recniku!")

if ("upr" not in recnik1):
    print("Kljuc \"upr\" se ne nalazi u recniku!")
else:
    print(recnik1["upr"])   

print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Pristup vrednostima u recniku upotrebom get() metode

recnik1 = {"UPR": "Uvod u Programiranje", "MAT": "Matematika"}

print(recnik1.get("UPR"))
print(recnik1.get("upr"))
print(recnik1.get("upr", "Taj kljuc se ne nalazi u recniku!"))

if (recnik1.get("upr") == None):
    print("Taj kljuc ne postoji u recniku!")
else:
    print(recnik1.get("upr"))

print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Dodavanje/izmena vrednosti

recnik1["PR1"] = "Programiranje 1"
print(recnik1)
print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Brisanje kljuca i vrednosti

del recnik1["PR1"]
print(recnik1)
print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Ostale metode recnika

print("Kljucevi:", recnik1.keys())              # Ispisuje samo kljuceve
print("Vrednosti:", recnik1.values())           # Ispisuje samo vrednosti
print("Kljucevi i vrednosti:", recnik1.items()) # Ispisuje kljuceve i vrednosti
print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Primer koriscenja recnika

recnik2 = {}
while (True):
    print("-" * 30)
    print("""0 - Izlaz
1 - Ispis sadrzaja recnika
2 - Unos sadrzaja u recnik
3 - Izmena sadrzaja u recniku
4 - Brisanje sadrzaja iz recnika""")
    print("-" * 30)
    
    opcija = int(input("Odaberite opciju iz menija (0-4): "))

    if (0 <= opcija <= 4):                      # if (opcija >= 0 and opcija <= 4):
        if (opcija == 0):
            break

        elif (opcija == 1):
            print("Sadrzaj recnika je:", recnik2)

        elif (opcija == 2):
            kljuc = input("Unesite kljuc: ")                    
            if (kljuc not in recnik2):
                vrednost = input("Unesite vrednost: ")
                recnik2[kljuc] = vrednost
                print("Upisali ste sadrzaj.")
            else:
                print("Taj kljuc se vec nalazi u recniku!")
            
        elif (opcija == 3):
            kljuc = input("Unesite kljuc: ")                    
            if (kljuc not in recnik2):
                print("Taj kljuc se ne nalazi u recniku!")
            else:
                vrednost = input("Unesite novu vrednost: ")
                recnik2[kljuc] = vrednost
                print("Izmenili ste sadrzaj.")

        elif (opcija == 4):
            kljuc = input("Unesite kljuc: ")
            vrednost = recnik2.get(kljuc)
            if (vrednost == None):
                print("Taj kljuc se ne nalazi u recniku!")
            else:
                del recnik2[kljuc]
                print("Obrisali ste sadrzaj.")
    else:
        print("Uneli ste pogresnu opciju!")
# ----------------------------------------------------------------------------------------------------