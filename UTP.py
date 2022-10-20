print("Selamat datang di Toko Komputer Kece")

nama = str(input("Masukkan Nama Anda : "))

while True:
    print('''\tApa yang anda cari?
    \t1. Part PC
    \t2. Laptop
    \t3. Service
    \t4. Exit Program''')
    pilih = int(input("Masukan Pilihan Anda : "))

    if pilih == 1 :
        print("Part apa yang anda cari?")
        print('''1. VGA
        2. Motherboard
        3. RAM
        4. Processor
        5. ''')
        part = int(input("Silahkan Pilih : "))
        #Ntar disini pake collection isinya part computer
        
        

    elif pilih == 2 :
        print("Dua")
        '''
        '''
    elif pilih == 3 :
        print("Tiga")
        '''
        '''
    elif pilih == 4 :
        print("Terima Kasih Telah Menggunakan Program Kami")
        break
    else:
        print("Maaf Pilihan Tidak Tersedia")
