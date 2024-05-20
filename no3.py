def hitungkeliling_dan_hitungluas(P,L):
    keliling = 2 * ( P + L )
    luas     = P * L
    return [keliling, luas]

P = 5
L = 3
keliling, luas = hitungkeliling_dan_hitungluas(P,L)
print(f"luas {luas}, keliling {keliling}")