# ----------------------------------------------------------------------------------------------------
# Uzimanje podataka od korisnika

ime = input("Unesite ime: ")                                 # Ceka da unesemo string i pritisnemo Enter
ceo_broj = int(input("Unesite ceo broj: "))                  # Ceka da unesemo ceo broj i pritisnemo Enter
realan_broj = float(input("Unesite realan broj: "))          # Ceka da unesemo realan broj i pritisnemo Enter

print("\nIme:", ime)                                         # Ispisuje uneto ime
print("Ceo broj:", ceo_broj)                                 # Ispisuje uneti ceo broj
print("Realan broj", realan_broj)                            # Ispisuje uneti realan broj
print("-" * 50)                                              # Radi preglednosti ispisa
# ----------------------------------------------------------------------------------------------------
# Generisanje slucajnih brojeva

import random                                                # Uvozi modul random za rad sa slucajnim brojevima

nasumican_broj1 = random.randint(1, 10)                      # Generise slucajan int od 1 do 10 (1 <= X <= 10)
nasumican_broj2 = random.randrange(10)                       # Generise slucajan int od 0 do 9 (0 <= X < 10)
nasumican_broj3 = random.randrange(10) + 1                   # Generise slucajan int od 0 do 9, pa dodaje 1 -> rezultat slucajan int od 1 do 10
nasumican_broj4 = random.randrange(1, 10)                    # Generise slucajan int od 1 do 9 (1 <= X < 10)
                                             
print("Nasumican broj 1:", nasumican_broj1)                  # Ispis prvog generisanog broja
print("Nasumican broj 2:", nasumican_broj2)                  # Ispis drugog generisanog broja
print("Nasumican broj 3:", nasumican_broj3)                  # Ispis treceg generisanog broja
print("Nasumican broj 4:", nasumican_broj4)                  # Ispis cetvrtog generisanog broja
print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Operatori za poredjenje
                                             
print("5 == 5?", 5 == 5)                                     # Poredi da li su brojevi jednaki -> True znaci da jesu
print("5 != 3?", 5 != 3)                                     # Poredi da li su brojevi razliciti -> True znaci da jesu
print("5 > 3?", 5 > 3)                                       # Poredi da li je prvi broj veci od drugog -> True znaci da jeste
print("5 < 3?", 5 < 3)                                       # Poredi da li je prvi broj manji od drugog -> False znaci da nije
print("5 >= 3?", 5 >= 3)                                     # Poredi da li je prvi broj veci ili jednak drugom -> True znaci da jeste
print("5 <= 3?", 5 <= 3)                                     # Poredi da li je prvi broj manji ili jednak drugom -> False znaci da nije
print("Jabuka < Mandarina?", "Jabuka" < "Mandarina")         # Poredi stringove po abecedi -> True znaci J < M
print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Upotreba if, elif i else naredbi
                                  
broj1 = int(input("Unesite broj 1: "))    
broj2 = int(input("Unesite broj 2: "))    

if (broj1 > broj2):                                          # Ako je prvi broj veci od drugog
    print("\nBroj " + str(broj1) + " je veci od broja " + str(broj2) + ".")    
elif (broj1 < broj2):                                        # Ako je prvi broj manji od drugog
    print("\nBroj " + str(broj1) + " je manji od broja " + str(broj2) + ".")    
else:                                                        # Ako su jednaki
    print("\nBroj " + str(broj1) + " je jednak broju " + str(broj2) + ".")

print("-" * 50) 
# ----------------------------------------------------------------------------------------------------
# Tretiranje vrednosti kao uslova                            

"""                                                 
Kratko objasnjenje:                                          
if ime      -> Ako string NIJE prazan          
if not ime  -> Ako je string PRAZAN

if broj     -> Ako broj NIJE nula             
if not broj -> Ako je broj NULA                          
"""
                                  
ime = input("Unesite ime: ")                        

if not ime:                                                  # Ako nije uneto (samo pritisnut Enter tj. unet prazan string)
    print("Niste uneli ime!")
else:
    prezime = input("Unesite prezime: ")  
    if not prezime:                                          # Ako nije uneto
        print("Niste uneli prezime!")
    else:
        datum_rodjenja = input("Unesite datum rodjenja: ")  
        if not datum_rodjenja:                               # Ako nije unet         
            print("Niste uneli datum rodjenja!")
        else:
            mejl = input("Unesite mejl: ") 
            if not mejl:                                     # Ako nije unet              
                print("Niste uneli mejl!")
            else:
                lozinka1 = input("Unesite lozinku: ")        # Unos lozinke
                if lozinka1:                                 # Ako je uneta
                    lozinka2 = input("Potvrdite lozinku: ")  # Potvrda lozinke
                    if (lozinka1 == lozinka2):               # Ako se poklapaju
                        print("\nKreirali ste nalog.")
                    else:                                    # Ako se ne poklapaju
                        print("\nLozinke se ne poklapaju!")  
                else:
                    print("Niste uneli lozinku!")

print("-" * 50) 
# ----------------------------------------------------------------------------------------------------
# Logicki operatori (not, and, or)

"""
Logicko NE - not
print(not True) -> False
print(not False) -> True

Logicko I: 
Logicko I - and
print(True and True) -> True
print(True and False) -> False
print(False and True) -> False
print(False and False) -> False

Logicko ILI:
Logicko ILI - or
print(True or True) -> True
print(True or False) -> True
print(False or True) -> True
print(False or False) -> False
"""

broj = int(input("Unesite broj od 1 do 10: ")) 

# Logicko I (and): svi uslovi moraju biti ispunjeni/tacni
"""
Ako prvi uslov (broj > 0) nije ispunjen, drugi uslov (broj < 11) nece ni biti proveravan;
Ako prvi uslov (broj > 0) jeste ispunjen, drugi uslov (broj < 11) ce biti proveravan, pa ako je i drugi uslov ispunjen onda ce naredba print(broj) biti izvrsena;

Ukratko: kod koriscenja "logickog I" svi uslovi moraju da budu ispunjeni da bi se if naredba izvrsila
"""
if (broj > 0 and broj < 11):                                 # Da li je broj u opsegu od 1 do 10
    print(broj)
else:
    print("Uneli ste broj van opsega!")

broj = int(input("Unesite broj od 1 do 10: ")) 

# Logicko ILI (or): samo jedan od uslova mora biti ispunjen/tacan
"""
Ako prvi uslov (broj < 1) jeste ispunjen, drugi uslov (broj > 10) nece ni biti proveravan;
Ako prvi uslov (broj < 1) nije ispunjen, drugi uslov (broj > 10) ce biti proveravan, pa ako ni drugi uslov nije ispunjen onda naredba print("Uneli ste broj van opsega!") nece biti izvrsena;

Ukratko: kod koriscenja "logickog ILI" samo jedan uslov mora da bude ispunjen da bi se if naredba izvrsila
"""
if (broj < 1 or broj > 10):                                  # Da li je broj van opsega 1-10
    print("Uneli ste broj van opsega!")
else:
    print(broj)

print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# While petlja

# Ispis brojeva od 1 do 10:
brojac = 1                                                   # Inicijalna vrednost brojaca je 1
while (brojac <= 10):                                        # Petlja se izvrsava dok je brojac <= 10                            
    print(brojac)                                            # Ispis trenutne vrednosti brojaca 
    brojac += 1                                              # Uvecavanje brojaca za 1                                                              
print("-" * 50)

# Ispis brojeva od 0 do 100 po 5:
brojac = 0                                                   # Inicijalna vrednost brojaca je 0
while (brojac <= 100):                                       # Petlja se izvrsava dok je brojac <= 100                             
    print(brojac)                                            # Ispis trenutne vrednosti brojaca        
    brojac += 5                                              # Uvecavanje brojaca za 5                
print("-" * 50)

# Ispis brojeva od 100 do 0:
brojac = 100                                                 # Inicijalna vrednost brojaca je 100
while (brojac >= 0):                                         # Petlja se izvrsava dok je brojac >= 0                              
    print(brojac)                                            # Ispis trenutne vrednosti brojaca  
    brojac -= 1                                              # Smanjivanje brojaca za 1               
print("-" * 50)

# Ispis brojeva od 100 do 1 po 5:
brojac = 100                                                 # Inicijalna vrednost brojaca je 100
while (brojac >= 1):                                         # Petlja se izvrsava dok je brojac >= 1                              
    print(brojac)                                            # Ispis trenutne vrednosti brojaca  
    brojac -= 5                                              # Smanjivanje brojaca za 5               
print("-" * 50)

# Ponavljanje dok korisnik ne unese "zato"
odgovor = ""                                                 # Inicijalno prazan string
while (odgovor != "zato"):                                   # Radi dok odgovor NIJE "zato"
    odgovor = input("Zasto? ").lower()                       # Pretvara odgovor u mala slova
print("-" * 50)

# Naredba break - prekidanje ciklusa
brojac = 0
while (brojac <= 100):                                       
    brojac += 1                                               
    if (brojac == 13):                                       # Kad brojac dostigne 13
        break                                                # Ciklus se PREKIDA
    else:
        print(brojac)        

print()

# Naredba continue - preskakanje trenutnog ciklusa
brojac = 0
while (brojac <= 100):                                       
    brojac += 1                                               
    if (brojac == 13):                                       # Kad brojac dostigne 13
        continue                                             # Ciklus se PRESKACE
    else:
        print(brojac)  

print("-" * 50) 
# ----------------------------------------------------------------------------------------------------
# Igra "Pogodi broj v1" - igrac pogadja broj

import random                                                # Uvoz modula random
racunar = random.randint(1, 100)                             # Racunar bira broj od 1 do 100
# print(racunar)                                             # Otkrivanje broja radi testiranja

pokusaji = 0
while (pokusaji < 5):                                        # Igrac ima 5 pokusaja
    igrac = int(input("Unesite broj od 1 do 100: "))         # Igrac bira broj od 1 do 100
    
    if (igrac > 0 and igrac < 101):                          # Provera da li je uneo broj od 1 do 100  
        pokusaji += 1

        if (igrac == racunar):                               # Pogodak!
            print("Pogodili ste trazeni broj :)")
            break
        elif (racunar > igrac):                              # Premali broj
            print("Trazeni broj je veci.")
        elif (racunar < igrac):                              # Prevelik broj
            print("Trazeni broj je manji.")
    else:
        print("Uneti broj nije u opsegu od 1 do 100!")

print("-" * 50)
# ----------------------------------------------------------------------------------------------------
# Igra "Pogodi broj v2" - racunar pogadja broj

igrac = int(input("Unesite broj od 1 do 10000: "))           # Igrac bira broj od 1 do 10000

if (igrac > 0 and igrac < 10001):                            # Provera da li je uneo broj od 1 do 10000
    brojac = 0
    while (True):                                            # Racunar pogadja sve dok ne pogodi
        racunar = random.randint(1, 10000)                   # Racunar bira broj od 1 do 10000
        brojac += 1

        if (racunar == igrac):                               # Pogodak!
            print("Racunar je pogodio trazeni broj", igrac)
            print("Pogodio ga je iz " + str(brojac) + ". pokusaja")
            # print(f"Pogodio ga je iz {brojac}. pokusaja")  # Bolji nacin
            break
else:
    print("Niste uneli odgovarajuci broj!")
# ----------------------------------------------------------------------------------------------------