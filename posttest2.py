import os
import time

tiket = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    clear_screen()
    print("-----------------------------------------------")
    print("Aplikasi Penjualan Tiket PT. CRF Barakatak")
    print("-----------------------------------------------")
    print("[1] Pesan Tiket")
    print("[0] Keluar")
    pilihmenu = str(input("Pilih menu> "))

    if(pilihmenu == "1"):
        pesan_tiket()
    elif (pilihmenu == "0"):
        close()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()
        
def close():
    clear_screen()
    print("-------------------------------------------------------------")
    print("Terima kasih telah menggunakan Aplikasi Pejualan Tiket")
    print("-------------------------------------------------------------")
    time.sleep(3)
    exit()

def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    menu()

def pesan_tiket():
    clear_screen()
    print("-Pesan Tiket-")

    print("Rute Dari:\nBPN (Balikpapan)\nSMD (Samarinda)\nBDJ (Banjarmasin)")
    rute_dari = str(input("Code Rute> "))
    tiket.insert(0,rute_dari)
    if(rute_dari == "BPN"):
        print("Rute Tujuan:\nSMD (Samarinda)\nBDJ (Banjarmasin)")
        rute_tujuan = str(input("Code Rute> "))
        tiket.insert(1,rute_tujuan)
        if(rute_tujuan == "SMD"):
            berangkat = str(input("Berangkat> "))
            tiket.insert(2,berangkat)
            penumpang = int(input("Jumlah Penumpang> "))
            tiket.insert(3,penumpang)
            print("Kelas: - Ekonomi - Bisnis")
            kelas = str(input("Kelas> "))
            tiket.insert(4,kelas)
            clear_screen()
            print("-Pesan Tiket-")
            nama = str(input("Nama Penumpang> "))
            tiket.insert(5,nama)
            total = tiket[3]*300000
            print("Total: Rp. %d" % (total))
            bayar = float(input("Bayar> "))
            if(bayar >= total):
                print("------------------------------------")
                print("PENJUALAN TIKET PT.CRF BARAKTAK")
                print("------------------------------------")
                print("Nama Penumpang: %s" % (tiket[5]))
                print("Rute Dari: %s" % (tiket[0]))
                print("Rute Tujuan: %s" % (tiket[1]))
                print("Berangkat: %s" % (tiket[2]))
                print("Jumlah Penumpang: %d" % (tiket[3]))
                print("Kelas: %s" % (tiket[4]))
                back_to_menu()
            else:
                print("Uang anda tidak cukup!")
                time.sleep(1.5)
                pesan_tiket()
        elif(rute_tujuan == "BDJ"):
            berangkat = str(input("Berangkat> "))
            tiket.insert(2,berangkat)
            penumpang = int(input("Jumlah Penumpang> "))
            tiket.insert(3,penumpang)
            print("Kelas: - Ekonomi - Bisnis")
            kelas = str(input("Kelas> "))
            tiket.insert(4,kelas)
            clear_screen()
            print("-Pesan Tiket-")
            nama = str(input("Nama Penumpang> "))
            tiket.insert(5,nama)
            total = tiket[3]*350000
            print("Total: Rp. %d" % (total))
            bayar = float(input("Bayar> "))
            if(bayar >= total):
                print("------------------------------------")
                print("PENJUALAN TIKET PT.CRF BARAKTAK")
                print("------------------------------------")
                print("Nama Penumpang: %s" % (tiket[5]))
                print("Rute Dari: %s" % (tiket[0]))
                print("Rute Tujuan: %s" % (tiket[1]))
                print("Berangkat: %s" % (tiket[2]))
                print("Jumlah Penumpang: %d" % (tiket[3]))
                print("Kelas: %s" % (tiket[4]))
                back_to_menu()
            else:
                print("Uang anda tidak cukup!")
                time.sleep(1.5)
                pesan_tiket()
        else:
            print("Code Rute Salah!")
            time.sleep(1.5)
            pesan_tiket()
    elif(rute_dari == "SMD"):
        print("Rute Tujuan:\nBPN (Balikpapan)\nBDJ (Banjarmasin)")
        rute_tujuan = str(input("Code Rute> "))
        tiket.insert(1,rute_tujuan)
        if(rute_tujuan == "BPN"):
            berangkat = str(input("Berangkat> "))
            tiket.insert(2,berangkat)
            penumpang = int(input("Jumlah Penumpang> "))
            tiket.insert(3,penumpang)
            print("Kelas: - Ekonomi - Bisnis")
            kelas = str(input("Kelas> "))
            tiket.insert(4,kelas)
            clear_screen()
            print("-Pesan Tiket-")
            nama = str(input("Nama Penumpang> "))
            tiket.insert(5,nama)
            total = tiket[3]*300000
            print("Total: Rp. %d" % (total))
            bayar = float(input("Bayar> "))
            if(bayar >= total):
                print("------------------------------------")
                print("PENJUALAN TIKET PT.CRF BARAKTAK")
                print("------------------------------------")
                print("Nama Penumpang: %s" % (tiket[5]))
                print("Rute Dari: %s" % (tiket[0]))
                print("Rute Tujuan: %s" % (tiket[1]))
                print("Berangkat: %s" % (tiket[2]))
                print("Jumlah Penumpang: %d" % (tiket[3]))
                print("Kelas: %s" % (tiket[4]))
                back_to_menu()
            else:
                print("Uang anda tidak cukup!")
                time.sleep(1.5)
                pesan_tiket()
        elif(rute_tujuan == "BDJ"):
            berangkat = str(input("Berangkat> "))
            tiket.insert(2,berangkat)
            penumpang = int(input("Jumlah Penumpang> "))
            tiket.insert(3,penumpang)
            print("Kelas: - Ekonomi - Bisnis")
            kelas = str(input("Kelas> "))
            tiket.insert(4,kelas)
            clear_screen()
            print("-Pesan Tiket-")
            nama = str(input("Nama Penumpang> "))
            tiket.insert(5,nama)
            total = tiket[3]*300000
            print("Total: Rp. %d" % (total))
            bayar = float(input("Bayar> "))
            if(bayar >= total):
                print("------------------------------------")
                print("PENJUALAN TIKET PT.CRF BARAKTAK")
                print("------------------------------------")
                print("Nama Penumpang: %s" % (tiket[5]))
                print("Rute Dari: %s" % (tiket[0]))
                print("Rute Tujuan: %s" % (tiket[1]))
                print("Berangkat: %s" % (tiket[2]))
                print("Jumlah Penumpang: %d" % (tiket[3]))
                print("Kelas: %s" % (tiket[4]))
                back_to_menu()
            else:
                print("Uang anda tidak cukup!")
                time.sleep(1.5)
                pesan_tiket()
        else:
            print("Code Rute Salah!")
            time.sleep(1.5)
            pesan_tiket()
    elif(rute_dari == "BDJ"):
        print("Rute Tujuan:\nBPN (Balikpapan)\nSMD (Samarinda)")
        rute_tujuan = str(input("Code Rute> "))
        tiket.insert(1,rute_tujuan)
        if(rute_tujuan == "BPN"):
            berangkat = str(input("Berangkat> "))
            tiket.insert(2,berangkat)
            penumpang = int(input("Jumlah Penumpang> "))
            tiket.insert(3,penumpang)
            print("Kelas: - Ekonomi - Bisnis")
            kelas = str(input("Kelas> "))
            tiket.insert(4,kelas)
            clear_screen()
            print("-Pesan Tiket-")
            nama = str(input("Nama Penumpang> "))
            tiket.insert(5,nama)
            total = tiket[3]*350000
            print("Total: Rp. %d" % (total))
            bayar = float(input("Bayar> "))
            if(bayar >= total):
                print("------------------------------------")
                print("PENJUALAN TIKET PT.CRF BARAKTAK")
                print("------------------------------------")
                print("Nama Penumpang: %s" % (tiket[5]))
                print("Rute Dari: %s" % (tiket[0]))
                print("Rute Tujuan: %s" % (tiket[1]))
                print("Berangkat: %s" % (tiket[2]))
                print("Jumlah Penumpang: %d" % (tiket[3]))
                print("Kelas: %s" % (tiket[4]))
                back_to_menu()
            else:
                print("Uang anda tidak cukup!")
                time.sleep(1.5)
                pesan_tiket()
        elif(rute_tujuan == "SMD"):
            berangkat = str(input("Berangkat> "))
            tiket.insert(2,berangkat)
            penumpang = int(input("Jumlah Penumpang> "))
            tiket.insert(3,penumpang)
            print("Kelas: - Ekonomi - Bisnis")
            kelas = str(input("Kelas> "))
            tiket.insert(4,kelas)
            clear_screen()
            print("-Pesan Tiket-")
            nama = str(input("Nama Penumpang> "))
            tiket.insert(5,nama)
            total = tiket[3]*300000
            print("Total: Rp. %d" % (total))
            bayar = float(input("Bayar> "))
            if(bayar >= total):
                print("------------------------------------")
                print("PENJUALAN TIKET PT.CRF BARAKTAK")
                print("------------------------------------")
                print("Nama Penumpang: %s" % (tiket[5]))
                print("Rute Dari: %s" % (tiket[0]))
                print("Rute Tujuan: %s" % (tiket[1]))
                print("Berangkat: %s" % (tiket[2]))
                print("Jumlah Penumpang: %d" % (tiket[3]))
                print("Kelas: %s" % (tiket[4]))
                back_to_menu()
            else:
                print("Uang anda tidak cukup!")
                time.sleep(1.5)
                pesan_tiket()
        else:
            print("Code Rute Salah!")
            time.sleep(1.5)
            pesan_tiket()
    else:
        print("Code Rute Salah!")
        time.sleep(1.5)
        pesan_tiket()

if __name__ == "__main__":
    while True:
        menu()
