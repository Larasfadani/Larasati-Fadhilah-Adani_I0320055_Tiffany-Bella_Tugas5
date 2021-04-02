print("Selamat datang di aplikasi konversi nilai")
print("Silakan masukkan nama dan nilai anda!")
nama = str(input("Nama: "))
nilai = int(input("Nilai: "))
if nilai >= 60 and nilai <= 64:
    print("Halo,", nama, "! Nilai anda setelah dikonversi adalah C")
elif nilai >= 65 and nilai <= 69:
    print("Halo,", nama, "! Nilai anda setelah dikonversi adalah C+")
elif nilai >= 70 and nilai <= 74:
    print("Halo,", nama, "! Nilai anda setelah dikonversi adalah B")
elif nilai >= 75 and nilai <= 79:
    print("Halo,", nama, "! Nilai anda setelah dikonversi adalah B+")
elif nilai >= 80 and nilai <= 84:
    print("Halo,", nama, "! Nilai anda setelah dikonversi adalah A-")
elif nilai >= 85 and nilai <= 100:
    print("Halo,", nama, "! Nilai anda setelah dikonversi adalah A")
else:
    pass
print("Terima kasih sudah menggunakan aplikasi ini, semoga membantu!")