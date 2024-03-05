# Fungsi konversi Celcius ke Fahrenheit
celcius_to_fahrenheit = lambda C: (9/5) * C + 32

# Fungsi konversi Celcius ke Reamur
celcius_to_reamur = lambda C: 0.8 * C

# Test-case 1
C = 100.0
F = celcius_to_fahrenheit(C)
print("Input C =", C, ". Output F =", F)

# Test-case 2
C = 80.0
R = celcius_to_reamur(C)
print("Input C =", C, ". Output R =", R)

# Test-case 3
C = 0.0
F = celcius_to_fahrenheit(C)
print("Input C =", C, ". Output F =", F)