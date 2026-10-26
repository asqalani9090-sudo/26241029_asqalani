nama = input("Masukkan nama Anda: ")
nim = input("Masukkan NIM Anda: ")
prodi = input("Masukkan program studi Anda: ")
nim_2digit = int(input("Masukkan 2 digit terakhir NIM Anda: "))

print("======================================")
print("         HASIL PROGRAM IDENTITAS DIRI")
print("======================================")

print("Nama                 : ", nama)
print("NIM                  : ", nim)
print("Program Studi        : ", prodi)
print("2 Digit Terakhir NIM : ", nim_2digit)

print("======================================")

nama ="Asqalani Syihab"
print("nama :" , nama)
print("tipe data nama : ", type(nama))

nim = 26241029
print("nim :" , nim)
print("tipe data nim : ", type (nim))

prodi ="pendidikan teknologi informasi"
print("prodi :" , prodi)
print("tipe data prodi : ", type(prodi))

dua_digit_nim = 29
print("2 Digit Terakhir NIM : ", dua_digit_nim)
print("tipe data dua_digit_nim : ", type(dua_digit_nim))



# Menampilkan tipe data dari setiap masing-masing variabel
print("======================================")
print(f"tipe data nama       : {type(nama)}")
print(f"tipe data nim        : {type(nim)}")
print(f"tipe data prodi      : {type(prodi)}")
print(f"tipe data nim_2digit : {type(nim_2digit)}")
print("======================================")