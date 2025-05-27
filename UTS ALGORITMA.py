import time

def tampilkanMenu():
    print("\nMENU CATATAN")
    print("1. Tambah")
    print("2. Hapus")
    print("3. Lihat")
    print("4. Keluar Program")

def main():
    CatatanHarian = []

    while True:
        tampilkanMenu()
        Pilihan = input("Pilih menu (1-4): ")

        if Pilihan == "1":
            Waktu = time.strftime("%Y-%m-%d %H:%M:%S")
            Isi = input("Isi catatan: ")
            Catatan = [Waktu, Isi]
            CatatanHarian.append(Catatan)
            print("Catatan ditambahkan")

        elif Pilihan == "2":
            if not CatatanHarian:
                print("Belum ada catatan")
                continue

            SemuaCatatan = ", ".join([f"{Catatan[0]} {Catatan[1]}" for Catatan in CatatanHarian])
            print(f"\nSemua Catatan: [{SemuaCatatan}]")

            HapusIsi = input("Masukkan isi catatan yang ingin dihapus: ")
            Ditemukan = False
            for Catatan in CatatanHarian:
                if Catatan[1] == HapusIsi:
                    CatatanHarian.remove(Catatan)
                    print("Catatan berhasil dihapus")
                    Ditemukan = True
                    break
                
            if not Ditemukan:
                print("Catatan tidak ditemukan")

        elif Pilihan == "3":
            if not CatatanHarian:
                print("Belum ada catatan")
            else:
                SemuaCatatan = ", ".join([f"{Catatan[0]} {Catatan[1]}" for Catatan in CatatanHarian])
                print(f"\nSemua Catatan: [{SemuaCatatan}]")

        elif Pilihan == "4":
            break

        else:
            print("Masukkan angka 1-4")
main()