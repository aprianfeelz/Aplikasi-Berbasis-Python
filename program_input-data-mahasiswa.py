nim = []
nama = []
asal = []

pilihan = 1
while pilihan != 0 :
    print ("1. masukan data.")
    print ("2. tampilkan data.")
    print ("3. hapus data.")
    print ("0. exit.")

    pilihan = int(input("masukan pilihan anda : "))
    print('')
    print('')
    print('')
    if pilihan == 1 :
        masnim = input("Masukan NIM : ")
        nim.append({'nim' : masnim})
        masnama = input("Masukan Nama : ")
        nama.append({'nama' : masnama})
        masasal = input("Masukan Asal : ")
        asal.append({'asal' : masasal})
        
        
    elif pilihan == 2 :
        penentu = True
        for i in range (len(nim)) :
            if penentu :
                print ("NIM\tNAMA\tASAL")
            print (nim[i]['nim'],'\t',nama[i]['nama'],'\t',asal[i]['asal'])
            penentu = False
            
    elif pilihan == 3 :
        masnim = input("Masukan NIM : ")
        for i in range (len(nim)) :
            if masnim == nim[i]['nim'] :
                print (i)
                del nim[i]
                del nama[i]
                del asal[i]
                break
    print('')
    print('')
    print('')