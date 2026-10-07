# ----------------------------------------------------------------------------------------------------
# For petlja

rec = input("Unesite rec: ")                 # Unos reci
for slovo in rec:                            # Prolaz kroz svako slovo u reci
    print(slovo)                             # Ispis jednog po jednog slova
print()                                      # Prazan red radi preglednosti

for i in range(10):                          # For petlja koja se izvrsava 10 puta
    print("Zdravo!")                         # Ispisuje deset puta Zdravo!
print()                                

for i in range(10):                          # range(10) znaci od 0 do 9
    print(i)                                 # Ispisuje brojeve od 0 do 9
print()                                

for i in range(0, 10):                       # range(10) znaci od 0 do 9
    print(i)                                 # Ispisuje brojeve od 0 do 9
print()                                

for i in range(50, 101):                     # range(50, 101) znaci od 50 do 100
    print(i, end=" ")                        # Ispisuje sve u jednom redu
print()                                      # Prazan red radi preglednosti

for i in range(0, 11, 2):                    # range(0, 11, 2) znaci od 0 do 10 koracima po 2
    print(i)                                 # Ispisuje brojeve: 0 2 4 6 8 10
print()                                

for i in range(100, 0, -1):                  # range(100, 0, -1) znaci od 100 do 1 korakom po 1 (unazad)
    print(i)                                 # Ispisuje brojeve od 100 do 1
print()                                

for i in range(100, -1, -5):                 # range(100, -1, -5) znaci od 100 do 0 koracima po 5 (unazad)
    print(i)                                 # Ispisuje brojeve: 100 95 90 85 80... 0
print("-" * 50)                                
# ----------------------------------------------------------------------------------------------------
# Upotreba operatora in sa stringom

prog_jezik = "Python"                  

if ("y" in prog_jezik):                      # Proverava da li je "y" u stringu
    print("Slovo y se nalazi u reci.") 
else:
    print("Slovo y se ne nalazi u reci.")

if ("a" not in prog_jezik):                  # Proverava da li "a" NIJE u stringu
    print("Slovo a se ne nalazi u reci.")
else:
    print("Slovo a se nalazi u reci.")

print("-" * 50)                             
# ----------------------------------------------------------------------------------------------------
# Upotreba funkcije len()

prog_jezik = "Python"                  
print("Duzina stringa je:", len(prog_jezik)) # Ispis duzine stringa
print("-" * 50)                                
# ----------------------------------------------------------------------------------------------------
# Indeksiranje stringova

prog_jezik = "Python"                  

print(prog_jezik[0])                         # Ispis slova na indeksu 0: P
print(prog_jezik[1])                         # Ispis slova na indeksu 1: y
print(prog_jezik[2])                         # Ispis slova na indeksu 2: t
print(prog_jezik[3])                         # Ispis slova na indeksu 3: h
print(prog_jezik[4])                         # Ispis slova na indeksu 4: o
print(prog_jezik[5])                         # Ispis slova na indeksu 5: n
print()                               

print(prog_jezik[-6])                        # Ispis slova na negativnom indeksu -6: P
print(prog_jezik[-5])                        # Ispis slova na negativnom indeksu -5: y
print(prog_jezik[-4])                        # Ispis slova na negativnom indeksu -4: t
print(prog_jezik[-3])                        # Ispis slova na negativnom indeksu -3: h
print(prog_jezik[-2])                        # Ispis slova na negativnom indeksu -2: o
print(prog_jezik[-1])                        # Ispis slova na negativnom indeksu -1: n
print("-" * 50)                                
# ----------------------------------------------------------------------------------------------------
# Indeksiranje stringova koristeci for petlju

prog_jezik = "Python"                  

for i in range(len(prog_jezik)):             # Prolazak kroz sve indekse stringa
    print(prog_jezik[i])                     # Ispis slova preko indeksa

print("-" * 50)                                
# ----------------------------------------------------------------------------------------------------
# Nastavljanje stringova

string_sa_brojevima = ""                     # Prazan string

for i in range(1, 11):                       # For petlja koja se izvrsava 10 puta
    string_sa_brojevima += str(i)            # Dodavanje broja u string
print(string_sa_brojevima)                   # Ispis rezultata
print("-" * 50)                                
# ----------------------------------------------------------------------------------------------------
# Definisanje konstanti

PI = 3.14                                    # Definisanje konstante (VELIKA SLOVA)
print(PI)                                    # Ispis vrednosti konstante
print("-" * 50)                               
# ----------------------------------------------------------------------------------------------------
# Isecanje stringova

predmet = "Python"                     

print(predmet[1:4])                          # Isecak: yth
print(predmet[0:1])                          # Isecak: P
print(predmet[5:6])                          # Isecak: n
print(predmet[-6:-2])                        # Pyth (isto kao predmet[0:4])

print(predmet[:3])                           # Isecak: Pyt 
print(predmet[2:])                           # Isecak: thon 
print(predmet[:])                            # Isecak: Python
print("-" * 50)                                 
# ----------------------------------------------------------------------------------------------------
# Kreiranje n-torki

ntorka1 = ("Python", 10, 99.99, True, False) # N-torka sa vise tipova
print(ntorka1)                               # Ispis n-torke

ntorka2 = ()                                 # Prazna n-torka

ntorka3 = ("Python")                         # Ovo NIJE n-torka
ntorka4 = ("Python",)                        # Ovo JESTE n-torka (ZAREZ JE VAZAN)

print("-" * 50)                                       
# ----------------------------------------------------------------------------------------------------
# Ispisivanje duzine n-torke

ntorka1 = ("Python", 10, 99.99, True, False)   
print("Duzina ntorke je:", len(ntorka1))     # Ispis duzine/kapaciteta ntorke
print("-" * 50)                                        
# ----------------------------------------------------------------------------------------------------
# Indeksiranje n-torke

ntorka1 = ("Python", 10, 99.99, True, False)   

print(ntorka1[2])                            # Ispis 99.99
print(ntorka1[-3])                           # Ispis 99.99
print("-" * 50)                                       
# ----------------------------------------------------------------------------------------------------
# Indeksiranje n-torke koristeci for petlju

ntorka1 = ("Python", 10, 99.99, True, False)   

for element in ntorka1:                      # Prolazak kroz sve elemente ntorke
    print(element)                           # Ispis elementa

print()

for i in range(len(ntorka1)):                # Prolazak kroz sve indekse ntorke
    print(ntorka1[i])                        # Ispis elementa preko indeksa

print("-" * 50)                                        
# ----------------------------------------------------------------------------------------------------
# Isecanje n-torke

ntorka1 = ("Python", 10, 99.99, True, False)   

print(ntorka1[3:5])                          # Isecak (True, False)
print(ntorka1[-1:-3])                        # Isecak () (UNAZAD NE RADI)
print("-" * 50) 
# ----------------------------------------------------------------------------------------------------
# Upotreba operatora in sa n-torkom 

ntorka1 = ("Python", 10, 99.99, True, False)   

if ("Python" in ntorka1):                    # Proverava da li postoji element
    print("'Python' se nalazi u ntorki.")    
else:    
    print("'Python' se ne nalazi u ntorki.")

if ("Python" not in ntorka1):                # Proverava da li NE postoji element
    print("'Python' se ne nalazi u ntorki.")
else:    
    print("'Python' se nalazi u ntorki.")

print("-" * 50)                                       
# ----------------------------------------------------------------------------------------------------
# Nadovezivanje n-torki

ntorka5 = ()                                 # Prazna n-torka

for i in range(10):                          # Uzimamo 10 brojeva od korisnika
    broj = int(input("Unesite " + str(i+1) + ". ceo broj: "))
    ntorka5 += (broj,)                       # Dodajemo broj u n-torku

print()
print(ntorka5)                               # Ispis konacne n-torke
# ----------------------------------------------------------------------------------------------------