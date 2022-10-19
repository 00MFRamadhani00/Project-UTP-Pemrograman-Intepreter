print("Selamat datang di Toko Komputer Kece")

nama = str(input("Masukkan Nama Anda : "))

while True:
    print('''\tApa yang anda cari?
    \t1. Part PC
    \t2. Laptop
    \t3. Service
    \t4. Exit Program''')
    pilih = input("Masukan Pilihan Anda : ")

    if pilih == 1 :
        while next == True:
            print("Part apa yang anda cari?")
            print('''1. VGA
            2. Motherboard
            3. RAM
            4. Processor
            5. ''')
            part = eval(input("Silahkan Pilih : "))
            #Ntar disini pake collection isinya part computer
            next = input('''Ada lagi?
            Y untuk lanjut''')
            if next == "Y":
                next == True
            else:
                next == False
            #Entah bagaimana ini tidak mau terbaca *emot batu*
        

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
