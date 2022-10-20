from ast import Try


print("Selamat datang di Toko Komputer Kece")

nama = str(input("Masukkan Nama Anda : "))

belanjaan = []
thisdict = {1:"VGA", 2:"Motherboard", 3:"RAM", 4:"Processor", 5:"PSU"}
laptopdict = {1:"Asus", 2:"Acer", 3:"HP", 4:"Lenovo", 5:"Dell"}

while True:
    print('''\tApa yang anda cari?
    \t1. Part PC
    \t2. Laptop
    \t3. Service
    \t4. Exit Program''')
    pilih = int(input("Masukan Pilihan Anda : "))

    if pilih == 1 :
        
        print('''
        1. VGA
        2. Motherboard
        3. RAM
        4. Processor
        5. PSU
        ''')
        berapa = eval(input("Berapa barang yang ingin anda beli?"))

        for i in range(berapa):
            part = int(input("Silahkan Pilih : "))
            belanjaan.append(thisdict[part])

        print(belanjaan)
        
    elif pilih == 2 :
        print('''
        1. Asus
        2. Acer
        3. HP
        4. Lenovo
        5. Dell
        ''')
        berapa = eval(input("Berapa barang yang ingin anda beli?"))

        for i in range(berapa):
            part = int(input("Silahkan Pilih : "))
            belanjaan.append(laptopdict[part])

        print(belanjaan)

    elif pilih == 3 :
        print('''
        1. Instal Ulang         6. Ganti RAM
        2. Flash BIOS           7. Ganti Hardisk
        3. Ganti Keyboard       
        4. Ganti LCD
        5. Ganti Thermal Paste
        ''')
        berapa = eval(input("Berapa barang yang ingin anda beli?"))

        for i in range(berapa):
            part = int(input("Silahkan Pilih : "))
            belanjaan.append(laptopdict[part])

        print(belanjaan)

    elif pilih == 4 :
        print("Terima Kasih Telah Menggunakan Program Kami")

        print("Atas Nama :", nama.upper(), "\nMemesan", belanjaan)
        break

    else:
        print("Maaf Pilihan Tidak Tersedia")
