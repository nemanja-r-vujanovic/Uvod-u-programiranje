# ----------------------------------------------------------------------------------------------------
# Upisivanje sadrzaja u tekstualni fajl

"""
Modovi pristupa:
"w" (write) - upisivanje u fajl
"a" (append) - apendovanje u fajl
"r" (read) - citanje iz fajla

Dodatni modovi pristupa:
"w+" (write + read) - upisivanje i citanje iz fajla
"a+" (append + read) - apendovanje i citanje iz fajla
"r+" (read + write) - citanje i upisivanje u fajl

"w" ne cuva prethodni sadrzaj
"a" cuva prethodni sadrzaj
"r" i "r+" mogu da prouzrokuju gresku ako navedeni fajl ne postoji
"""

fajl = open("primer.txt", "w")
fajl.write("AAA\n") # Upisivanje stringa u fajl
fajl.write("BBB\n")
lista_podataka = ["CCC\n", "DDD\n"] 
fajl.writelines(lista_podataka) # Upisivanje liste stringova u fajl
fajl.close()
# ----------------------------------------------------------------------------------------------------
# Apendovanje sadrzaja u tekstualni fajl

fajl = open("primer.txt", "a")
fajl.write("EEE\n")
fajl.write("FFF\n")
lista_podataka = ["GGG\n", "HHH\n"] 
fajl.writelines(lista_podataka)
fajl.close()
# ----------------------------------------------------------------------------------------------------
# Ispisivanje sadrzaja tekstualnog fajla koristeci funkciju read()

fajl = open("primer.txt", "r")
# print(fajl.read()) # Ispisuje citav sadrzaj fajla
print(fajl.read(5)) # Ispisuje prvih 5 karaktera
print(fajl.read(2)) # Ispisuje sledeca 2 karaktera
print(fajl.read(1)) # Ispisuje sledeci karakter
print()
fajl.close()
# ----------------------------------------------------------------------------------------------------
# Ispisivanje sadrzaja tekstualnog fajla koristeci funkciju readline()

fajl = open("primer.txt", "r")
# print(fajl.readline()) # Ispisuje sadrzaj tekuce linije
print(fajl.readline(4))
print(fajl.readline(2))
print(fajl.readline(1))
print()
fajl.close()
# ----------------------------------------------------------------------------------------------------
# Ispisivanje sadrzaja tekstualnog fajla koristeci funkciju readlines()

fajl = open("primer.txt", "r")
lista = fajl.readlines() # Citav sadrzaj fajla se cuva u listu

for element in lista:
    print(element, end="")
print("\n")

for i in range(len(lista)):
    print(lista[i], end="")  
print("\n")

fajl.close()
# ----------------------------------------------------------------------------------------------------
# Ispisivanje sadrzaja tekstualnog fajla koristeci for petlju

fajl = open("primer.txt", "r")
for sadrzaj in fajl:
    print(sadrzaj, end="")
print("\n")
fajl.close()
# ----------------------------------------------------------------------------------------------------
# Primer rada sa fajlom

naslov = "Evidencija studenata"
print(("-" * 100) + "\n" + ((100 - len(naslov)) // 2 * " ") + naslov)
FAJL = "studenti.txt"

# Mod "a" pravi fajl ako ne postoji i cuva postojeci sadrzaj.
fajl = open(FAJL, "a")
fajl.close()

def ispisi_meni():
    print("-" * 30)
    print("""0 - izlaz
1 - ispis sadrzaja fajla
2 - unos sadrzaja u fajl
3 - izmena sadrzaja u fajlu
4 - brisanje sadrzaja iz fajla""")
    print("-" * 30)

    opcija = int(input("Unesite opciju (0-4): "))    
    if (opcija < 0 or opcija > 4):
        print("Uneli ste pogresnu opciju!")        
    else:
        return opcija

def ispisi_sadrzaj():
    fajl = open(FAJL, "r")
    lista = fajl.readlines()

    for i in range(len(lista)):
        if (i % 3 == 0):
            print()
        print(lista[i], end="")

    fajl.close()

def unesi_sadrzaj(): 
    print()   
    podaci = {"Ime i prezime": "", "Broj indeksa": "", "Ocena": ""}
    podaci_uneti = True

    for podatak in podaci.keys():
        unos = input(f"{podatak}: ").strip()
        if (unos):
            podaci[podatak] = unos
        else:
            print(f"{podatak} je podatak koji niste uneli!")
            podaci_uneti = False
            break            

    if (podaci_uneti):
        fajl = open(FAJL, "a")

        string = ""        
        for podatak in podaci.keys():
            string += podatak + ": " + podaci[podatak] + "\n"

        fajl.write(string)
        fajl.close()    

        print("\nUneli ste sadrzaj u fajl.") 

def izmeni_sadrzaj():
    broj_indeksa = input("\nBroj indeksa: ").strip()

    if (not broj_indeksa):
        print("Niste uneli broj indeksa!")        
    else:
        broj_indeksa = "Broj indeksa: " + broj_indeksa + "\n"
        fajl = open(FAJL, "r")
        lista = fajl.readlines()
        fajl.close()

        if (broj_indeksa not in lista):
            print("Taj broj indeksa ne postoji u evidenciji!")
        else:
            ime_prezime = input("Izmenite ime i prezime: ")

            if (not ime_prezime):
                print("Niste uneli ime i prezime!")
            else:
                ocena = input("Izmenite ocenu: ")

                if (not ocena):
                    print("Niste uneli ocenu!")
                else:                    
                    pozicija = lista.index(broj_indeksa)
                    lista[pozicija - 1] = "Ime i prezime: " + ime_prezime + "\n"
                    lista[pozicija + 1] = "Ocena: " + ocena + "\n"

                    fajl = open(FAJL, "w")                                                            
                    for linija in lista:
                        fajl.write(linija)
                    fajl.close()

                    print("\nIzmenili ste sadrzaj u fajlu.")       

def obrisi_sadrzaj():
    broj_indeksa = input("\nBroj indeksa: ").strip()

    if (not broj_indeksa):
        print("Niste uneli broj indeksa!")
    else:
        broj_indeksa = "Broj indeksa: " + broj_indeksa + "\n"
        fajl = open(FAJL, "r")
        lista = fajl.readlines()
        fajl.close()

        if (broj_indeksa not in lista):
            print("Taj broj indeksa ne postoji u evidenciji!")
        else:            
            pozicija = lista.index(broj_indeksa)            
            del lista[pozicija - 1 : pozicija + 2]
            
            fajl = open(FAJL, "w")
            for linija in lista:
                fajl.write(linija)
            fajl.close()

            print("\nObrisali ste sadrzaj iz fajla.")    

while (True):
    odabir = ispisi_meni()

    if (odabir == 0):
        break
    elif (odabir == 1):
        ispisi_sadrzaj()
    elif (odabir == 2):
        unesi_sadrzaj()
    elif (odabir == 3):
        izmeni_sadrzaj()
    elif (odabir == 4):
        obrisi_sadrzaj()
# ----------------------------------------------------------------------------------------------------
# Obrada izuzetaka

print()

try:
    broj = int(input("Unesite broj: "))
except:
    print("Doslo je do greske pri konverziji!")
    print("Proverite da li ste uneli ceo broj.")

try:
    broj = int(input("Unesite broj: "))
except (ValueError):
    print("Doslo je do greske pri konverziji!")
    print("Proverite da li ste uneli ceo broj.")

try:
    broj = int(input("Unesite broj: "))
except (TypeError, ValueError):
    print("Doslo je do greske pri konverziji!")
    print("Proverite da li ste uneli ceo broj.")

try:
    broj = int(input("Unesite broj: "))
except (TypeError):
    print("Doslo je do 'TypeError' greske!")
except (ValueError):
    print("Doslo je do 'ValueError' greske!")

try:
    broj = int(input("Unesite broj: "))
except ValueError as ve:
    print("Doslo je do greske pri konverziji!")
    print("Proverite da li ste uneli ceo broj.")
    print("Konkretna greska je:", ve)

try:
    broj = int(input("Unesite broj: "))
except:
    print("Doslo je do greske pri konverziji!")
    print("Proverite da li ste uneli ceo broj.")
else:
    print("Sve je proslo bez greske.")
# ----------------------------------------------------------------------------------------------------