def cek_angka():
    a = int(input("Masukkan angka pertama: "))
    b = int(input("Masukkan angka kedua: "))
    c = int(input("Masukkan angka ketiga: "))
    
    if a != b and a != c and b != c:
        if a + b == c or a + c == b or b + c == a:
            return True
    return False

print(cek_angka())

########################################################################################
cek_angka = lambda a, b, c: True if a != b and a != c and b != c and (a + b == c or a + c == b or b + c == a) else False