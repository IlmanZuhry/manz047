# Fungsi untuk melakukan operasi aritmatika
def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y == 0:
        return "Error: Pembagian dengan nol tidak diperbolehkan"
    else:
        return x / y

# Menu
def kalkulator():
    print("Kalkulator Sederhana")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Keluar")
# Sistem kalkulator
    while True:
        pilihan = input("Pilih operasi (1-5): ")

        if pilihan == "1":
            x = float(input("Masukkan angka pertama: "))
            y = float(input("Masukkan angka kedua: "))
            print(f"{x} + {y} = {tambah(x, y)}")
        elif pilihan == "2":
            x = float(input("Masukkan angka pertama: "))
            y = float(input("Masukkan angka kedua: "))
            print(f"{x} - {y} = {kurang(x, y)}")
        elif pilihan == "3":
            x = float(input("Masukkan angka pertama: "))
            y = float(input("Masukkan angka kedua: "))
            print(f"{x} * {y} = {kali(x, y)}")
        elif pilihan == "4":
            x = float(input("Masukkan angka pertama: "))
            y = float(input("Masukkan angka kedua: "))
            print(f"{x} / {y} = {bagi(x, y)}")
        elif pilihan == "5":
            print("Keluar dari program")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

# Jalankan fungsi utama
kalkulator()