print ("NIM \t: 5200411413")
print ("Nama \t: Juan Fredrick Pandia")
print ("===========================================")

ram = int(input("Masukkan Kapasitas RAM \t\t= "))
petabit = int(input("Kapasistas Petabit \t\t= "))
sistemoperasi = int(input("Kapasitas RAM Sistem Operasi \t= "))
ramsatu = int(input("Kapasitas RAM Program 1 \t= "))
ramdua = int(input("Kapasitas RAM Program 2 \t= "))

#rumus untuk menghitung
kapasitaspetabit = ram/petabit
totalram = sistemoperasi+ramsatu+ramdua
ramtpakai = ram - totalram
blok0 = ram - kapasitaspetabit
blok1 = ram/petabit

print ("===========================================")
print ("Kapasitas RAM                        =",ram)
print ("Kapasitas Petabit                    =",petabit)
print ("Kapasitas Perpetabit                 =",kapasitaspetabit)
print ("Total Kapasitas RAM yang digunakan   =",totalram)
print ("Total Kapasitas RAM Tidak digunakan  =",ramtpakai)
print ("Jumlah Blok Bernilai 0               =",blok0)
print ("Jumlah Blok Bernilai 1               =",blok1)
print ("===========================================")