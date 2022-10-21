

print("Selamat datang di Toko Komputer Kece")

nama = str(input("Masukkan Nama Anda : "))

print("==================================")
print("\tHallo", nama)
print("==================================")

total = 0

def belanja(total):
    for i in belanjaan:
        print(hargadict[i])
        total = total + hargadict[i]
    print("Total pembayaran Rp", total*Diskon)

belanjaan = []
thisdict = {1:"VGA", 2:"Motherboard", 3:"RAM", 4:"Processor", 5:"PSU"}
laptopdict = {1:"Asus", 2:"Acer", 3:"HP", 4:"Lenovo", 5:"Dell"}
servisdict = {1:"Instal Ulang", 2:"Flash BIOS", 3:"Ganti Keyboard Laptop", 4:"Ganti LCD", 5:"Ganti Thermal Paste", 6:"Ganti RAM", 7:"Ganti Hardisk"}
hargadict = {'VGA':900000, 'Motherboard':825000, 'RAM':500000, 'Processor':1500000, 'PSU':600000,
            'Asus':20990000, 'Acer':15807000, 'HP':26717000, 'Lenovo':27500000, 'Dell':27999000,
            'Instal Ulang':100000, 'Flash BIOS':50000, 'Ganti Keyboard Laptop':200000, 'Ganti LCD':650000, 
            'Ganti Thermal Paste':110000, 'Ganti RAM':550000, 'Ganti Hardisk':700000}
listID = [112233, 456321, 211705]
Diskon = 1.0

while True:
    print('''\tApa yang anda cari?
    \t1. Part PC
    \t2. Laptop
    \t3. Service
    \t4. Exit Program''')
    pilih = int(input("Masukan Pilihan Anda : "))

    if pilih == 1 :
        
        print('''
        1. VGA Rp 900.000
        2. Motherboard Rp 825.000
        3. RAM Rp 500.000
        4. Processor Rp 1.500.000
        5. PSU Rp 600.000
        ''')
        berapa = eval(input("Berapa barang yang ingin anda beli?"))

        for i in range(berapa):
            part = int(input("Silahkan Pilih : "))
            if part < 1 or part > 5:
                print("Maaf Pilihan Tidak Tersedia")
            else:
                belanjaan.append(thisdict[part])

        print(belanjaan)
        
    elif pilih == 2 :
        print('''
        1. Asus Rp 20.990.000
        2. Acer Rp 15.807.000
        3. HP Rp 26.717.000
        4. Lenovo Rp 27.500.000
        5. Dell Rp 27.999.000
        ''')
        berapa = eval(input("Berapa barang yang ingin anda beli?"))

        for i in range(berapa):
            part = int(input("Silahkan Pilih : "))
            if part < 1 or part > 5:
                print("Maaf Pilihan Tidak Tersedia")
            else:
                belanjaan.append(laptopdict[part])

        print(belanjaan)

    elif pilih == 3 :
        print('''
        1. Instal Ulang Rp 100.000
        2. Flash BIOS Rp 50.000
        3. Ganti Keyboard Laptop Rp 200.000
        4. Ganti LCD Rp 650.000
        5. Ganti Thermal Paste Rp 110.000
        6. Ganti RAM Rp 550.000
        7. Ganti Hardisk Rp 700.000
        ''')
        berapa = eval(input("Berapa barang yang ingin anda beli?"))

        for i in range(berapa):
            part = int(input("Silahkan Pilih : "))
            if part < 1 or part > 5:
                print("Maaf Pilihan Tidak Tersedia")
            else:
                belanjaan.append(servisdict[part])

        print(belanjaan)

    elif pilih == 4 :
        print("Terima Kasih Telah Menggunakan Program Kami")

        print("Atas Nama :", nama.upper(), "\nMemesan", belanjaan)

        print()
        ID = str(input("Apakah anda memiliki ID member?(Y/N)"))

        if ID == "Y":
            
            try:
                Nomor_ID = int(input("Masukan nomor ID member: "))
                if Nomor_ID in listID:
                    Diskon = 0.9
                else :
                    print("Nomor ID tidak terdaftar")

            except:
                print("TypeError : Masukan Nomor ID hanya dengan integer")
                Nomor_ID = int(input("Masukan nomor ID member (Percobaan terakhir): "))
                if Nomor_ID in listID:
                    Diskon = 0.9
                else :
                    print("Nomor ID tidak terdaftar")
            
            belanja(total)
            
            break

        else:    
            belanja(total)
            
            break

    else:
        print("Maaf Pilihan Tidak Tersedia")
