# Meminta input dua digit terakhir NIM 
a = int(input("Digit a: "))
b = int(input("Digit b: "))

# Membuat dua kondisi Boolean berdasarkan nilai digit >= 5
kondisi1 = a >= 5
kondisi2 = b >= 5

# Menampilkan hasil evaluasi Boolean dari kondisi1 dan kondisi2
print("digit a : ", a)
print("digit b : ", b)
print("kondisi1 : ", kondisi1)
print("kondisi2 : ", kondisi2)
print("NOT :", not kondisi1)
print("AND :", kondisi1 and kondisi2)
print("OR :", kondisi1 or kondisi2) 
print("XOR :", kondisi1 ^ kondisi2)

# OR butuh satu True,XOR butuh nilai yang beda,jadi True Or True = True tapi True XOR True = False