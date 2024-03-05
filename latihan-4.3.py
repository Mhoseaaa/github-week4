# Fungsi konversi Celcius ke Fahrenheit
celcius_to_fahrenheit = lambda C: (9/5) * C + 32

# Fungsi konversi Celcius ke Reamur
celcius_to_reamur = lambda C: 0.8 * C

# Meminta input dari user
choice = input("Pilih konversi:\n1. Celsius ke Fahrenheit\n2. Celsius ke Reamur\n")

# Validasi pilihan
if choice == "1":
    
    # Konversi Celsius ke Fahrenheit
    C = float(input("Masukkan suhu dalam Celsius: "))
    F = celcius_to_fahrenheit(C)
    print("Input C =", C, ". Output F =", F)
    
elif choice == "2":
    # Konversi Celsius ke Reamur
    C = float(input("Masukkan suhu dalam Celsius: "))
    R = celcius_to_reamur(C)
    print("Input C =", C, ". Output R =", R)
else:
    print("Pilihan tidak valid")
