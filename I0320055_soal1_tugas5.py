print("Selamat datang di Hotel Del Luna, silakan masukkan nama dan jenis kelamin anda!")
nama = str(input("Siapa nama anda? "))
jk = str(input("Apa jenis kelamin anda? (P/L) "))
if jk == 'P':
    print("Selamat datang, Nyonya", nama, "!")
else:
    print("Selamat datang, Tuan", nama, "!")
print()