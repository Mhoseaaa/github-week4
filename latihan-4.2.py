def cek_digit_belakang(a, b, c):
    if str(a)[-1] == str(b)[-1] or str(a)[-1] == str(c)[-1] or str(b)[-1] == str(c)[-1]:
        return True
    else:
        return False

# Test-case
input1, input2, input3 = map(int, input("Enter three numbers separated by space: ").split())

output = cek_digit_belakang(input1, input2, input3)
print("Output:", output)