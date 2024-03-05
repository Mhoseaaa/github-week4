def cek_digit_belakang(a, b, c):
    if str(a)[-1] == str(b)[-1] or str(a)[-1] == str(c)[-1] or str(b)[-1] == str(c)[-1]:
        return True
    else:
        return False

# Test-case
print(cek_digit_belakang(30, 20, 18))
print(cek_digit_belakang(145, 5, 100))
print(cek_digit_belakang(71, 187, 18))
print(cek_digit_belakang(1024, 14, 94))
print(cek_digit_belakang(53, 8900, 658))