#Import library "datetime" untuk meng-extract date hari ini
#nantinya akan digunakan untuk meng-extract tahun ini dalam menghitung umur mobil
from datetime import date
currentYear = date.today().year

dictMobil = { 
    '000':  #Unique keys
    {
        'Brand' : 'Honda',
        'Tipe': 'Brio',
        'Umur': 5,
        'Harga' : 100000
    },

    '001':
    {
        'Brand' : 'Toyota',
        'Tipe': 'Avanza',
        'Umur': 2,
        'Harga' : 200000
    },
    
    '002':
    {
        'Brand' : 'Honda',
        'Tipe': 'Jazz',
        'Umur': 2,
        'Harga' : 150000
    },

    '003':
    {
        'Brand' : 'BMW',
        'Tipe': 'Series3',
        'Umur': 2,
        'Harga' : 300000
    }
}

cart = {}               # Mobil yang ingin disewa tapi belum bayar
mobil_disewa = {}       # Mobil yang sedang disewa

##################### Menampilkan Daftar Mobil #######################
def menampilkanDaftarMobil() :
    while True :
        menu = input('''

            ########## Daftar Mobil ##########

            List Menu :
            1. Melihat Semua Mobil
            2. Melihat Mobil Tertentu
            3. Melihat Mobil yang sedang disewa
            4. Kembali ke Menu Utama

            Masukkan angka Menu yang ingin dijalankan : ''')

        if(menu == '1') :
            menampilkanDaftarMobil_Semua()
        elif(menu == '2') :
            menampilkanDaftarMobil_Tertentu()
        elif(menu == '3') :
            menampilkanDaftarMobil_Disewa()
        elif(menu == '4') :
            break

def menampilkanDaftarMobil_Semua():
    if dictMobil == {}:
        print('\n---------- Tidak ada mobil yang tersedia ----------')
    else: 
        print('\n###############################################################################################')
        print('                                     Daftar Semua Mobil                                          ')
        print('###############################################################################################')
        print('Kode Mobil\t| Brand Mobil  \t| Tipe Mobil\t| Umur Mobil (tahun)\t| Harga sewa (per jam)')
        print('----------------|---------------|---------------|-----------------------|---------------------')
        for kode in dictMobil.keys() :
            print('{}       \t| {}    \t| {}    \t| {}                  \t| {:,}'.format(kode , dictMobil[kode]['Brand'] , dictMobil[kode]['Tipe'] , dictMobil[kode]['Umur'] , dictMobil[kode]['Harga']))


def menampilkanDaftarMobil_Tertentu():
    if dictMobil == {}:
        print('\n---------- Tidak ada Mobil yang tersedia ----------')

    else: 
        kode = input('\nMasukkan kode mobil [xxx, contoh:001]: ')
        if kode in dictMobil:
            print('\nKode Mobil\t| Brand Mobil  \t| Tipe Mobil\t| Umur Mobil (tahun)\t| Harga sewa (per jam)')
            print('----------------|---------------|---------------|-----------------------|---------------------')
            print('{}       \t| {}    \t| {}    \t| {}                  \t| {:,}'.format(kode , dictMobil[kode]['Brand'] , dictMobil[kode]['Tipe'] , dictMobil[kode]['Umur'] , dictMobil[kode]['Harga']))
        else:
            print('\n---------- Maaf, tidak ada mobil dengan kode tersebut --------') 

def menampilkanDaftarMobil_Disewa():
    if mobil_disewa == {}:
        print('\n---------- Tidak ada mobil yang sedang disewa ----------')
    else:
        print('\n###############################################################################################')
        print('                                  Daftar mobil yang disewa                                       ')
        print('###############################################################################################')
        print('Kode Mobil\t| Brand Mobil  \t| Tipe Mobil\t| Umur Mobil (tahun)\t| Harga sewa (per jam)')
        print('----------------|---------------|---------------|-----------------------|---------------------')
        for kode in mobil_disewa:
            print('{}       \t| {}    \t| {}    \t| {}                  \t| {:,}'.format(kode , mobil_disewa[kode]['Brand'] , mobil_disewa[kode]['Tipe'] , mobil_disewa[kode]['Umur'] , mobil_disewa[kode]['Harga']))


##################### Menambah Daftar Mobil #######################

def menambahDaftarMobil():
    while True :
        menu = input('''
            ########## Tambah Daftar Mobil ##########

            List Menu :
            1. Menambah Daftar Mobil
            2. Kembali ke Menu Utama

            Masukkan angka Menu yang ingin dijalankan : ''')

        if(menu == '1') :
            menambahMobil()
        elif(menu == '2') :
            break

def menambahMobil() :
    kodeMobil = input('\nMasukkan Kode Mobil [xxx, contoh:001]:')
    if (kodeMobil in dictMobil.keys() or kodeMobil in mobil_disewa.keys()):
        print('\n----- Kode mobil {} sudah ada. Silahkan input kode mobil yang lain -----'.format(kodeMobil))

    elif (kodeMobil.isnumeric() and len(kodeMobil)==3):
        brandMobil = input('Masukkan Brand Mobil : ').capitalize()
        tipeMobil = input('Masukkan Tipe Mobil : ').capitalize()
        
        while True:
            tahunBeli = (input('Masukkan Tahun Beli [xxxx, contoh: 2015]: '))
            if (tahunBeli.isnumeric() and len(tahunBeli)==4 and int(tahunBeli)<=currentYear):
                break
            else:
                print("----- Format Tahun yang Anda isi salah. Silahkan isi lagi! -----")
        
        while True:
            hargaSewa = (input('Masukkan Harga Sewa per jam [contoh: 100000]: '))
            if (hargaSewa.isnumeric()):
                break
            else:
                print("----- Format Harga Sewa yang Anda isi salah. Silahkan isi lagi! -----")

        simpan = input('Apakah data mau disimpan? [Y/N]: ').upper()

        while True:
            if simpan == 'Y':

                dictMobil[kodeMobil]={}
                dictMobil[kodeMobil]['Brand'] = brandMobil
                dictMobil[kodeMobil]['Tipe'] = tipeMobil
                
                if (currentYear - int(tahunBeli)==0):  
                    dictMobil[kodeMobil]['Umur'] = 1 
                else:
                    dictMobil[kodeMobil]['Umur'] = currentYear - int(tahunBeli)
                
                dictMobil[kodeMobil]['Harga'] = int(hargaSewa)

                print('\n----- Data mobil telah tersimpan -----')
                menampilkanDaftarMobil_Semua()
                break

            elif simpan == 'N':
                print ('\n ---------- Data Mobil tidak tersimpan ----------')
                break
    else:
        print('\n---------- Maaf, format kode mobil yang Anda input salah. Silahkan ulangi lagi ----------') 


##################### Mengupdate Daftar Mobil #######################

def updateDaftarMobil():
    while True:
        menu = input('''
            ##### Update (Ubah) Daftar Mobil #####

            List Menu :
            1. Update Daftar Mobil
            2. Kembali ke Menu Utama

            Masukkan angka menu yang ingin dijalankan : ''')

        if(menu == '1') :
            updateMobil()
        elif(menu == '2') :
            break

def updateMobil():
    menampilkanDaftarMobil_Semua()
    kodeMobil = input('\nMasukkan kode mobil yang mau di-update: ')
    if (kodeMobil in dictMobil.keys()):
        print('\nKode Mobil\t| Brand Mobil  \t| Tipe Mobil\t| Umur Mobil (tahun)\t| Harga sewa (per jam)')
        print('----------------|---------------|---------------|-----------------------|---------------------')
        print('{}       \t| {}    \t| {}    \t| {}              \t| {:,}\n'.format(kodeMobil , dictMobil[kodeMobil]['Brand'] , dictMobil[kodeMobil]['Tipe'] , dictMobil[kodeMobil]['Umur'] , dictMobil[kodeMobil]['Harga']))
        
        lanjutupdate = input('Apakah Anda ingin lanjut meng-update data [Y/N]? ').upper()
        
        if lanjutupdate == "Y":
            kolomUpdate = input('Pilih kolom yang ingin diubah [Brand/Tipe/Umur/Harga]: ').capitalize()

            if kolomUpdate == "Brand" or kolomUpdate == "Tipe":
                brand_or_tipe_Update = input('Input {} baru: '.format(kolomUpdate)).capitalize()
                while True:
                    update = input('Apakah Anda yakin mau meng-update data diatas [Y/N]? ').upper()
                    if update == 'Y':
                        dictMobil[kodeMobil]['{}'.format(kolomUpdate)] = brand_or_tipe_Update
                        print('\n---------- Data mobil telah terupdate ----------')
                        menampilkanDaftarMobil_Semua()
                        break
                    elif update == 'N':
                        print ('\n---------- Data Anda tidak terupdate ----------')
                        break

            elif kolomUpdate == "Umur":
                umur_Update = input('Input tahun beli [xxxx, contoh: 2010]: ')
                if (umur_Update.isnumeric() and len(umur_Update)==4 and int(umur_Update)<=currentYear):
                    while True:
                        update = input('Apakah Anda yakin mau meng-update data diatas [Y/N]? ').upper()
                        if update == "Y":       
                            if (currentYear - int(umur_Update) == 0):                    
                                dictMobil[kodeMobil]['{}'.format(kolomUpdate)] = 1
                                print('\n---------- Data sudah terupdate ----------')
                                menampilkanDaftarMobil_Semua()
                                break
                            else:
                                dictMobil[kodeMobil]['{}'.format(kolomUpdate)] = currentYear - int(umur_Update)
                                print('\n---------- Data sudah terupdate ----------')
                                menampilkanDaftarMobil_Semua()
                                break
                        elif update == "N":
                            print ('\n---------- Data tidak terupdate ----------') 
                            break    
                else:
                    print("\n---------- Format tahun yang Anda masukkan salah. Silahkan coba lagi ----------")          
            
            elif kolomUpdate == "Harga":
                hargaUpdate = input('Input harga sewa baru: ')
                if (hargaUpdate.isnumeric()):
                    while True:
                        update = input('Apakah Anda yakin mau meng-update data diatas [Y/N]? ').upper()
                        if update == "Y":
                            dictMobil[kodeMobil]['{}'.format(kolomUpdate)] = int(hargaUpdate)
                            print('\n----- Data sudah terupdate -----')
                            menampilkanDaftarMobil_Semua()
                            break                         
                        elif update == "N":
                            print ('\n----- Data tidak terupdate -----')
                            break
                else:
                    print("\n---------- Format yang Anda masukkan salah! Silahkan coba lagi ----------")      
            
            else:
                print('\n---------- Format "Kolom" Anda masukkan salah. Silahkan coba lagi ----------')

        elif lanjutupdate == "N":
            print ('\n---------- Data tidak terupdate ----------')
        
        else:
            print('\n---------- Format yang Anda masukkan salah. Silahkan coba lagi ----------')
            
    else:
        print('\n---------- Maaf, kode mobil yang Anda cari tidak tersedia. Silahkan coba lagi ----------')
 

##################### Menghapus Daftar Mobil #######################

def menghapusDaftarMobil():
    while True :
        menu = input('''
            ##### Hapus Daftar Mobil #####

            List Menu :
            1. Menghapus Daftar Mobil
            2. Kembali ke Menu Utama

            Masukkan angka Menu yang ingin dijalankan : ''')

        if(menu == '1') :
            menghapusMobil()
        elif(menu == '2') :
            break
   
def menghapusMobil() :
    if dictMobil == {}:
        print('--- Data Mobil tidak tersedia ---')
    else:
        menampilkanDaftarMobil_Semua()
        kodeMobil = input('\nMasukkan kode mobil yang ingin dihapus : ')
        if (kodeMobil in dictMobil.keys()):
            while True: 
                hapus = input('Apakah data mau dihapus? [Y/N]: ').upper()
                if hapus == "Y":
                    del dictMobil[kodeMobil]
                    print ("\n----- Data mobil yang Anda pilih telah dihapus -----")
                    break
                elif hapus == "N":
                    break
        else:
            print("----- Maaf, data yang Anda cari tidak ada. Silahkan coba lagi -----")


##################### Menyewa Mobil #######################

def menyewaDaftarMobil():
    while True :
        menu = input('''
            ##### Menu Sewa Mobil #####

            List Menu :
            1. Melihat Daftar Mobil
            2. Melakukan Pembayaran
            3. Kembali ke Menu Utama

            Masukkan angka Menu yang ingin dijalankan : ''')

        if(menu == '1') :
            menyewaMobil()
        elif(menu == '2') :
            pembayaranMobil()
        elif(menu == '3') :
            break

def menyewaMobil() :
    while True:
        if dictMobil != {}:
            menampilkanDaftarMobil_Semua()
            kodeMobil = input('\nMasukkan kode Mobil yang ingin disewa [xxx]: ')
            if (kodeMobil in dictMobil.keys()):
                print('\nKode Mobil\t| Brand Mobil  \t| Tipe Mobil\t| Umur Mobil (tahun)\t| Harga sewa (per jam)')
                print('----------------|---------------|---------------|-----------------------|---------------------')           
                print('{}       \t| {}    \t| {}    \t| {}              \t| {:,}\n'.format(kodeMobil , dictMobil[kodeMobil]['Brand'] , dictMobil[kodeMobil]['Tipe'] , dictMobil[kodeMobil]['Umur'] , dictMobil[kodeMobil]['Harga']))

                tanya = input('Apakah Anda mau menyewa mobil ini? [Y/N] ').upper()
                
                if tanya == "Y":
                    while True:
                        lamaSewa = input('Berapa lama Anda ingin menyewa mobil ini [dalam jam]: ')
                        if(lamaSewa.isnumeric() and lamaSewa != '0') :
                            cart[kodeMobil]=dictMobil[kodeMobil]
                            cart[kodeMobil]['Lama']=int(lamaSewa)
                            cart[kodeMobil]['Total']=int(lamaSewa)*int(dictMobil[kodeMobil]['Harga'])
                            del dictMobil[kodeMobil]
                            break
                        else:
                            print('----- Maaf, format yang Anda input salah. Silahkan coba lagi -----')
                
                    print('\n###########################################################################################################################################')
                    print('                                                   Daftar Mobil yang ingin disewa                                                          ')
                    print('###########################################################################################################################################')
                    print('Kode Mobil\t| Brand Mobil  \t| Tipe Mobil\t| Umur Mobil (tahun)\t| Harga sewa (per jam)\t| Lama Sewa (jam)\t| Total Pembayaran')
                    print('----------------|---------------|---------------|-----------------------|-----------------------|-----------------------|------------------')                
                    for item in cart :
                        print('{}       \t| {}    \t| {}    \t| {}              \t| {:,}            \t| {}              \t| {:,}'.format(item , cart[item]['Brand'] , cart[item]['Tipe'] , cart[item]['Umur'] , cart[item]['Harga'], cart[item]['Lama'], cart[item]['Total']))
                    
                    lanjut_sewa = input('\nApakah Anda ingin menyewa mobil yang lain? [Y/N]  ').upper()
                    if(lanjut_sewa == 'Y'):
                        print('\n')
                    elif(lanjut_sewa == 'N'):
                        break
                
                elif tanya == "N":
                    print ('\n---------- Mobil tidak jadi disewa ----------') 
                    break

                else:
                    print('\n---------- Format yang anda input salah ----------')
                    break
            
            else:
                print('\n---------- Kode mobil yang Anda cari tidak ada ----------')
                break
        
        else:
            print('---------- Tidak ada mobil yang tersedia ----------')
            break

def pembayaranMobil():
    if cart != {}:
        print('\n###########################################################################################################################################')
        print('                                                         BILLING                                                                ')
        print('###########################################################################################################################################')
        print('Kode Mobil\t| Brand Mobil  \t| Tipe Mobil\t| Umur Mobil (tahun)\t| Harga sewa (per jam)\t| Lama Sewa (jam)\t| Total Pembayaran')
        print('----------------|---------------|---------------|-----------------------|-----------------------|-----------------------|------------------')                     
        totalHarga = 0
        for item in cart :
            print('{}       \t| {}    \t| {}    \t| {}              \t| {:,}            \t| {}              \t| {:,}'.format(item , cart[item]['Brand'] , cart[item]['Tipe'] , cart[item]['Umur'] , cart[item]['Harga'], cart[item]['Lama'], cart[item]['Total']))
            totalHarga += cart[item]['Total']

        mau_bayar = input('\nApakah bill-nya sudah benar?[Y/N] ').upper()
        if mau_bayar == "Y":
            while True :
                print('\nTotal Yang Harus Dibayar = {:,}'.format(totalHarga))
                jmlUang = int(input('Masukkan jumlah uang : '))
                if(jmlUang > totalHarga) :
                    kembali = jmlUang - totalHarga
                    print('\n----- Terima kasih telah menyewa mobil di Rental Mobil Purwadhika ----- ')
                    print('----- Uang kembali anda: {:,} -----'.format(kembali))
                    mobil_disewa.update(cart)
                    cart.clear()
                    break
                elif(jmlUang == totalHarga) :
                    print('\n----- Terima kasih telah menyewa mobil di Rental Mobil Purwadhika ----- ')
                    mobil_disewa.update(cart)
                    cart.clear()
                    break
                else :
                    kekurangan = totalHarga - jmlUang
                    print('\n----- Maaf, uang anda kurang sebesar {:,}-----'.format(kekurangan))
                    print('\n----- Silahkan input lagi-----'.format(kekurangan))
        
        elif mau_bayar == "N":
            print('\n---------- Daftar mobil yang ingin Anda sewa terhapus ----------')
            dictMobil.update(cart)
            cart.clear()
        
        else:
            print('\n---------- Format yang Anda masukkan salah ----------')
            print('\n---------- Daftar mobil yang ingin Anda sewa terhapus ----------')
            dictMobil.update(cart)
            cart.clear()
  
    else:
        print('\n---------- Anda tidak memiliki tagihan yang tertunda ----------')

##################### Homepage #######################
def homepage():
    while True :
        pilihanMenu = input('''
            #####################################################
                 Selamat Datang di Rental Mobil Purwadhika 
            #####################################################

            List Menu untuk Staff:
            1. Melihat Daftar Mobil
            2. Menambah Data Mobil
            3. Mengubah Data Mobil
            4. Menghapus Data Mobil

            List Menu untuk Customer:
            5. Menyewa Mobil

            Keluar aplikasi:
            6. Exit Aplikasi


            Masukkan angka Menu yang ingin dijalankan : ''')       

        if(pilihanMenu == '1') :
            menampilkanDaftarMobil()
        elif(pilihanMenu == '2') :
            menambahDaftarMobil()
        elif(pilihanMenu == '3') :
            updateDaftarMobil()
        elif(pilihanMenu == '4') :
            menghapusDaftarMobil()
        elif(pilihanMenu == '5') :
            menyewaDaftarMobil()
        elif(pilihanMenu == '6') :
            break

homepage()