# Tambah barang
def tambah() :
    import os
    os.system("CLS")
    print("\n   - Tambah Sepatu -")
    print("\nMasukkan data sepatu baru")
    sepatu = input("Masukkan Nama Sepatu : ")
    ukuran = input("Masukkan Ukuran      : ")
    stok = input("Masukkan Jumlah Stok : ")
    data = open("datasepatu.txt","a")
    data.writelines([sepatu+","+ukuran+","+stok+ "\n"])
    print("\n[Data Sepatu Berhasil Ditambahkan]")
    data.close()

    print("\nIngin menambahkan sepatu lagi? (Ya/Tidak) ", end=" ")
    tambahdata = input (" : ")
    if tambahdata == "y" or tambahdata == "Y":
        tambah()
    else :
        print("\nTekan [ENTER] untuk kembali ke menu.")
        input()
        menu()

# Menghapus barang
def hapus_barang() :
	import os
	os.system("CLS")
	print("\n             - Hapus Data Sepatu -")
	data = open("datasepatu.txt", "r")
	output = []
	str = input("\nMasukkan nama sepatu yang ingin dihapus       : ")
	for hapus in data:
		if not hapus.startswith(str):
			output.append(hapus)
			
	data = open("datasepatu.txt.","w")
	data.writelines(output)
	print("\n[Data Sepatu Telah Terhapus]")
	data.close()
	print("\nIngin menghapus data sepatu lagi? (Ya/Tidak)", end=" ")
	hapusdata = input(" : ")
	if hapusdata == "y" or hapusdata == "Y":
		hapus_barang()
	else :
		print("\nTekan [ENTER] untuk kembali ke menu")
		input()
		menu()

# mengedit barang :
def edit_barang() :
	import os
	os.system("CLS")
	print("\n            - Ubah Data Sepatu -")
	baru = input("\nMasukkan nama sepatu yang ingin diperbarui : ")
	print("\nMasukkan data baru")
	namabaru = input("Nama Sepatu	: ")
	ukuranbaru = input("Ukuran	: ")
	stokbaru = input("Jumlah Stok	: ")
	data = open("datasepatu.txt", "r")
	isi = data.readlines()
	
	i=0
	for data_sepatu in isi:
			content = data_sepatu.split(",")
			if  content[0] == baru:
				content[0] = namabaru
				content[1] = ukuranbaru
				content[2] = stokbaru+"\n"
				xg = ",".join(content)
				isi[i]=xg
			i += 1
			
	data = open("datasepatu.txt","w")
	isi = data.writelines(isi)
	print("\n[Data Sepatu Berhasil Diubah]")
	data.close()
	print("\nIngin mengubah data sepatu lagi? (Ya/Tidak)", end=" ")
	ubahdata = input(" : ")
	if ubahdata == "y" or ubahdata == "Y":
		edit_barang()
	else :
		print("\nTekan [ENTER] untuk kembali ke menu")
		input()
		menu()

# Daftar barang
def daftar_barang():
    import os
    os.system("CLS")
    print("List Barang Yang Tersedia".center(44,'=') + "\n")
    data = open("datasepatu.txt","r")
    isi = data.readlines()
    isi.sort()
    if len(isi) == 0:
        print("\n[Barang Tidak Tersedia]")
    else :
        i = 1
        for datasepatu in isi:
           content = datasepatu.split(",")
           print(str(i) + ".",end=" ")
           print("Nama Barang : "+ content[0])
           print("   Ukuran      : "+ content[1])
           print("   Stok Sepatu : " + content[2])
           i += 1
    print("\nTekan [ENTER] untuk kembali ke menu.")
    data.close()
    input()
    menu()
    
# cek barang
def cek_barang():
	import os
	os.system("CLS")
	print("\n          - Pencarian Barang -")
	cari = input("\nMasukkan nama barang yang ingin dicari : ")
	data = open("datasepatu.txt","r")
	isi = data.readlines()
	isi.sort()
	
	for data_sepatu in isi:
			content = data_sepatu.split(",")
			if content[0] == cari:
				print("\nNama Barang	: "+content[0])
				print("Ukuran		: "+content[1])
				print("Jumlah Stok	: "+content[2])
        			
	print("\n\nTekan [ENTER] untuk kembali ke menu")
	data.close()
	input()
	menu()

# menu
def menu():
    print("-"*50)
    print("PROGRAM BARANG".center(50,'='))
    print("-"*50 + "\n")
    print("1. Tambah Barang")
    print("2. Hapus Barang")
    print("3. Edit Barang")
    print("4. Daftar Barang")
    print("5. Cek Nama Barang")
    print("6. Keluar\n")
    print("-"*50)
    pilihan = input("Pilih menu \t: ").upper()
    if pilihan == "1" or pilihan == "TAMBAH BARANG":
        tambah()
    elif pilihan == "2" or pilihan == "HAPUS BARANG":
        hapus_barang()
    elif pilihan == "3" or pilihan == "EDIT BARANG":
        edit_barang()
    elif pilihan == "4" or pilihan == "DAFTAR Barang":
        daftar_barang()
    elif pilihan == "5" or pilihan == "CEK NAMA BARANG":
        cek_barang()
    elif pilihan == '6':
            A = False
            exit = input("\nTekan [ENTER] untuk keluar.")
            print(' TERIMAKASIH '.center(50,"="))
                                        
menu()