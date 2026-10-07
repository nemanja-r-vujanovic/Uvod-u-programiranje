# ----------------------------------------------------------------------------------------------------
# Definisanje funkcija

def funkcija1():                           # Definisanje funkcije bez parametara
    print("Zdravo!")

def funkcija2(ime):                        # Definisanje funkcije sa jednim parametrom
    print(ime)

def funkcija3(ime, prezime, broj_indeksa): # Definisanje funkcije sa vise parametara
    print(ime, prezime, broj_indeksa)

def funkcija4():
    return "Zdravo svete!"                 # Funkcija vraca string vrednost (ili bilo koju drugu koja se navede a koja je do sada radjena na predmetu -- podrazumevano vraca None)

funkcija1() # Poziv funkcije
funkcija2("Ime Prezime 1")                 # Poziv funkcije sa zadatim argumentom
funkcija2("Ime Prezime 2")
funkcija3("Ime", "Prezime", "IT-XY/2024")  # Poziv funkcije sa zadatim argumentima

print(funkcija4())
povratna_vrednost = funkcija4()            # Povratna vrednost se cuva u promenljivu (ako treba za kasnije koriscenje)
print(povratna_vrednost)
print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Globalne varijable

def funkcija5():
    print(broj)                            # Ispisuje vrednost globalne varijable

def funkcija6():
    broj = 20                              # Ovo je lokalna varijabla
    print(broj)                            # Ispisuje vrednost lokalne varijable

def funkcija7():
    global broj                            # Varijablu broj proglasava za globalnu varijablu (inace izmena vrednosti ne bi bila moguca)
    broj += 20                             # Menja vrednost globalne varijable
    print(broj)                            # Ispisuje vrednost globalne varijable

broj = 10
funkcija5()
funkcija6()
funkcija7()
print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Pozicioni i keyword argumenti

def funkcija8(ime, prezime, broj_indeksa):
    print(ime, prezime, broj_indeksa)

# Pozicioni argumenti
funkcija8("Prezime", "Ime", "IT-XY/2024")  

# Keyword argumenti
funkcija8(prezime = "Prezime", broj_indeksa = "IT-XY/2024", ime = "Ime") 

print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Default vrednosti parametara

def funkcija9(ime, prezime, broj_indeksa = "IT-XY/2024"):
    print(ime, prezime, broj_indeksa)

funkcija9("Ime", "Prezime", "IT-01/2024")
funkcija9("Ime", "Prezime")                # Ovde ne mora da se zada i treci pozicioni argument jer je trecem parametru dodeljena difoltna vrednost
# ----------------------------------------------------------------------------------------------------
# Igra "Iks-Oks" - primer upotrebe funkcija i globalnih varijabli, kao i gradiva iz poglavlja 1-5

naslov = "Igra \"Iks-Oks\""
print(("-" * 50) + "\n" + ((50 - len(naslov)) // 2 * " ") + naslov)
igra_zavrsena = False
znak = "X"
tabla = (
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
)

def ispisi_tablu():
    ispis = ""

    for i in range(len(tabla)):
        for j in range(len(tabla[i])):
            if (tabla[i][j] == 0):
                znak = " "
            elif (tabla[i][j] == 1):
                znak = "X"
            elif (tabla[i][j] == 2):
                znak = "O"

            if (j < len(tabla[i]) - 1):
                ispis += f" {znak} |"
            else:
                ispis += f" {znak} "

            if (i < 1):
                broj_crtica = len(ispis)

        if (i < len(tabla) - 1):
            crtice = broj_crtica * "-"
            ispis += f"\n{crtice}\n"

    print(f"\n{ispis}")

def odigraj_potez():
    ispisi_tablu()

    POLJA = ("00 | 01 | 02", "10 | 11 | 12", "20 | 21 | 22")
    ispis = "\n"

    for i in range(len(POLJA)):
        if (i < len(POLJA) - 1):
            ispis += POLJA[i] + "\n" + (len(POLJA[i]) * "-") + "\n"
        else:
            global znak
            ispis += POLJA[i] + "\n\n" + "Igrac " + znak + " odaberite vrstu i kolonu: "

    vrsta_kolona = input(ispis)
    vrsta = int(vrsta_kolona[:1])
    kolona = int(vrsta_kolona[1:])

    if ((vrsta >= 0 and vrsta < len(tabla)) and (kolona >= 0 and kolona < len(tabla[0]))):
        if (tabla[vrsta][kolona] != 0):
            print("To polje je vec popunjeno!")
        else:
            if (znak == "X"):
                tabla[vrsta][kolona] = 1
                proveri_pobedu(znak)
                znak = "O"
            elif (znak == "O"):
                tabla[vrsta][kolona] = 2
                proveri_pobedu(znak)
                znak = "X"

def proveri_pobedu(znak):
    if (znak == "X"):
        vrednost = 1
    elif (znak == "O"):
        vrednost = 2

    if (tabla[0][0] == vrednost and tabla[0][1] == vrednost and tabla[0][2] == vrednost):
        prekini_igru(f"\nIgrac {znak} je pobedio.")
    elif (tabla[1][0] == vrednost and tabla[1][1] == vrednost and tabla[1][2] == vrednost):
        prekini_igru(f"\nIgrac {znak} je pobedio.")
    elif (tabla[2][0] == vrednost and tabla[2][1] == vrednost and tabla[2][2] == vrednost):
        prekini_igru(f"\nIgrac {znak} je pobedio.")

    elif (tabla[0][0] == vrednost and tabla[1][0] == vrednost and tabla[2][0] == vrednost):
        prekini_igru(f"\nIgrac {znak} je pobedio.")
    elif (tabla[0][1] == vrednost and tabla[1][1] == vrednost and tabla[2][1] == vrednost):
        prekini_igru(f"\nIgrac {znak} je pobedio.")
    elif (tabla[0][2] == vrednost and tabla[1][2] == vrednost and tabla[2][2] == vrednost):
        prekini_igru(f"\nIgrac {znak} je pobedio.")

    elif (tabla[0][0] == vrednost and tabla[1][1] == vrednost and tabla[2][2] == vrednost):
        prekini_igru(f"\nIgrac {znak} je pobedio.")
    elif (tabla[0][2] == vrednost and tabla[1][1] == vrednost and tabla[2][0] == vrednost):
        prekini_igru(f"\nIgrac {znak} je pobedio.")

    else:
        proveri_nereseno()

def proveri_nereseno():
    popunjena_polja = 0
    for i in range(len(tabla)):
        for j in range(len(tabla[i])):
            if (tabla[i][j] != 0):
                popunjena_polja += 1

    if (popunjena_polja == len(tabla) * len(tabla[0])):
        prekini_igru("\nIgra je zavrsena neresenim rezultatom.")

def prekini_igru(poruka):
    ispisi_tablu()
    print(poruka)
    global igra_zavrsena
    igra_zavrsena = True

# Glavni deo programa:
while (not igra_zavrsena):
    odigraj_potez()
# ----------------------------------------------------------------------------------------------------