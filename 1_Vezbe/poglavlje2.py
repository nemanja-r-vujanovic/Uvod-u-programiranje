# ----------------------------------------------------------------------------------------------------------------------------------
# Upotreba navodnika u stringovima

print("Python")                         # Ispisuje Python
# print('Python')                       # Ispisuje Python
print("'Python' programiranje")         # Ispisuje 'Python' programiranje
# print('"Python" programiranje')       # Ispisuje "Python" programiranje

# Preporuka: koristiti navodnike (" ") za oznacavanje stringova
# ----------------------------------------------------------------------------------------------------------------------------------
# Prikazivanje vise stringova pomocu jedne naredbe

print("Python", "programiranje")        # Ispisuje Python programiranje
print("Python",
      "programiranje")                  # Ispisuje Python programiranje
# ----------------------------------------------------------------------------------------------------------------------------------
# Zadavanje zavrsnog karaktera u stringu

print("Linija1")                        # Ispisuje Linija1
print("Linija2")                        # Ispisuje Linija2

print("Linija1", end="\n")              # Ispisuje Linija1
print("Linija2")                        # Ispisuje Linija2

print("Linija1", end=" ")               # Ispisuje Linija1 Linija2
print("Linija2")
# ----------------------------------------------------------------------------------------------------------------------------------
# Upotreba izlaznih sekvenci u stringovima

print("\tPython programiranje")         # Ispisuje        Python programiranje
print("Python\nprogramiranje")          # Ispisuje Python, prelazi u novi red, pa ispisuje programiranje
print("Python programiranje \a")        # Ispisuje Python programiranje i aktivira zvucni signal
print("Python \\ programiranje")        # Ispisuje Python \ programiranje
print("\'Python\' programiranje")       # Ispisuje 'Python' programiranje
# print("'Python' programiranje")       # Ispisuje 'Python' programiranje
print("\"Python\" programiranje")       # Ispisuje "Python" programiranje
# print('"Python" programiranje')       # Ispisuje "Python" programiranje
# ----------------------------------------------------------------------------------------------------------------------------------
# Spajanje stringova

print("Python" + "programiranje")       # Ispisuje Pythonprogramiranje
print("Python " + "programiranje")      # Ispisuje Python programiranje
print("Python" + " programiranje")      # Ispisuje Python programiranje
print("Python" + " " + "programiranje") # Ispisuje Python programiranje
print("Python " + " programiranje")     # Ispisuje Python  programiranje
# print("Ocena: " + 10)                 # Greska! 10 nije string!
# ----------------------------------------------------------------------------------------------------------------------------------
# Ponavljanje stringova

print("Python " * 10)                   # Ispisuje Python Python Python Python Python Python Python Python Python Python 
print("-" * 50)                         # Ispisuje --------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------
# Stringovi sa trostrukim navodnicima

# ASCII Art generisan na sajtu: https://patorjk.com/software/taag/
# ASCII Art font: Modular
# Input text: Game Over
print(""" _______  _______  __   __  _______    _______  __   __  _______  ______   
|       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  
|    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  
|   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ 
|   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |
|   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |
|_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|""")

# Preporuka: koristiti trostruke navodnike (""" """) za oznacavanje stringova koji prelaze u vise redova
# ----------------------------------------------------------------------------------------------------------------------------------
# Rad sa brojevima

print(10)                               # Ispisuje 10
print(70 + 30)                          # Ispisuje 100
print(70 - 30)                          # Ispisuje 40
print(70 * 30)                          # Ispisuje 2100
print(70 / 30)                          # Ispisuje 2.33
print(70 // 30)                         # Ispisuje 2
print(70 % 30)                          # Ispisuje 10

# Preporuka za racunanje rezultata celobrojnog deljenja (//): 70 / 30 = 2.33 -> uklonimo tacku i sve iza nje -> 2
# Preporuka za racunanje ostatka celobrojnog deljenja (%): 70 / 30 = 2.33 -> uklonimo tacku i sve iza nje -> 2 -> 70 - 30 * 2 = 10
# ----------------------------------------------------------------------------------------------------------------------------------
# Definisanje promenljivih

tekst = "Primer"                        # tekst je promenljiva tipa string (tekst)
broj1 = 100                             # broj1 je promenljiva tipa int (ceo broj)
broj2 = -10                             # broj2 je promenljiva tipa int (ceo broj)
broj3 = 100.00                          # broj3 je promenljiva tipa float (realan broj)
broj4 = -7.62                           # broj4 je promenljiva tipa float (realan broj)
studenti_prisutni = True                # studenti_prisutni je promenljiva tipa bool
pada_sneg = False                       # pada_sneg je promenljiva tipa bool

print(tekst)                            # Ispisuje Primer
print(broj1)                            # Ispisuje 100
print(broj2)                            # Ispisuje -10
print(broj3)                            # Ispisuje 100.00
print(broj4)                            # Ispisuje -7.62
print(studenti_prisutni)                # Ispisuje True
print(pada_sneg)                        # Ispisuje False

"""
# Ispisuje tip promenljive:
print(type(tekst))                      # Ispisuje <class 'str'>
print(type(broj1))                      # Ispisuje <class 'int'>
print(type(broj2))                      # Ispisuje <class 'int'>
print(type(broj3))                      # Ispisuje <class 'float'>
print(type(broj4))                      # Ispisuje <class 'float'>
print(type(studenti_prisutni))          # Ispisuje <class 'bool'>
print(type(pada_sneg))                  # Ispisuje <class 'bool'>
"""

# Napomena: moguce je ispisati vrednost promenljive samo ukoliko je ona prethodno definisana
# ----------------------------------------------------------------------------------------------------------------------------------
# Metode za obradu stringova

naslov = "   Uvod u programiranje   "
print(naslov)                           # Ispisuje    Uvod u programiranje
print(naslov.upper())                   # Ispisuje    UVOD U PROGRAMIRANJE
print(naslov.lower())                   # Ispisuje    uvod u programiranje
print(naslov.title())                   # Ispisuje    Uvod U Programiranje
print(naslov.replace("o", "*"))         # Ispisuje    Uv*d u pr*gramiranje
print(naslov.replace("o", "*", 1))      # Ispisuje    Uv*d u programiranje
print(naslov.swapcase())                # Ispisuje    uVOD U PROGRAMIRANJE
print(naslov.capitalize())              # Ispisuje    uvod u programiranje
print(naslov.strip())                   # Ispisuje Uvod u programiranje
# print(naslov.strip().capitalize())    # Ispisuje Uvod u programiranje
print(naslov)                           # Ispisuje    Uvod u programiranje
# ----------------------------------------------------------------------------------------------------------------------------------
# Konvertovanje vrednosti

ulaz1 = "123"
izlaz1 = int(ulaz1)                     # Konvertuje string "123" u int 123
print(izlaz1, "->", type(izlaz1))       # Ispisuje 123 -> <class 'int'>

ulaz2 = "123.99"
izlaz2 = float(ulaz2)                   # Konvertuje string "123.99" u float 123.99
print(izlaz2, "->", type(izlaz2))       # Ispisuje 123.99 -> <class 'float'>

ulaz3 = "123"
izlaz3 = float(ulaz3)                   # Konvertuje string "123" u float 123.00
print(izlaz3, "->", type(izlaz3))       # Ispisuje 123.00 -> <class 'float'>

ulaz4 = "123.99"
izlaz4 = float(ulaz4)                   # Konvertuje string "123.99" u float 123.99
izlaz5 = int(izlaz4)                    # Konvertuje float 123.99 u int 123
print(izlaz5, "->", type(izlaz5))       # Ispisuje 123 -> <class 'int'>

ulaz5 = 123                             
izlaz6 = float(ulaz5)                   # Konvertuje int 123 u float 123.00
print(izlaz6, "->", type(izlaz6))       # Ispisuje 123.00 -> <class 'float'>

ulaz6 = 123.99
izlaz7 = int(ulaz6)                     # Konvertuje float 123.99 u int 123
print(izlaz7, "->", type(izlaz7))       # Ispisuje 123 -> <class 'int'>

# Bilo koja vrednost se moze konvertovati u string:
print(type(str(False)))                 # Ispisuje <class 'str'>
print(type(str(True)))                  # Ispisuje <class 'str'>
print(type(str(100)))                   # Ispisuje <class 'str'>
print(type(str(99.99)))                 # Ispisuje <class 'str'>
print(type(str("Python")))              # Ispisuje <class 'str'>
# ----------------------------------------------------------------------------------------------------------------------------------
# Inkrementni operatori

"""
+=
-=
*=
/=
%=
"""

broj = 100
broj += 1                               # broj = broj + 1
broj -= 1                               # broj = broj - 1
broj *= 2                               # broj = broj * 2
broj /= 3                               # broj = broj / 3
broj %= 3                               # broj = broj % 3
print(broj)                             # Ispisuje 0.67

input()                                 # Ceka da pritisnemo Enter
# ----------------------------------------------------------------------------------------------------------------------------------