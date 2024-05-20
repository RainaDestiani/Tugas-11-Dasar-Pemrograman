def hitung_kata(kalimat):
    kata_kata = kalimat.split()
    jumlahkata = len(kata_kata)
    return jumlahkata

kalimat = " ini adalah contoh kalimat"
print(hitung_kata(kalimat))