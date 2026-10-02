# Decimalni u binarni:
print(format(365, "b"))                 # 101101101

# Binarni u decimalni:
print(int("101101101", 2))              # 365

# Decimalni u heksadecimalni:
print(format(365, "x"))                 # 16d

# Heksadecimalni u decimalni:
print(int("16d", 16))                   # 365

# Binarni u heksadecimalni:
print(format(int("101101101", 2), "x")) # 16d

# Heksadecimalni u binarni:
print(format(int("16D", 16), "b"))      # 101101101