#Baca file
file = open("spider.txt")

# #Baca file per barisbaris (default baris 1)
# baris1 = file.readline()
# print(baris1)

# #Ketika dijalanin lagi, otomatis bakal baca file selanjutnya 
# baris2 = file.readline()
# print(baris2)

# #Tutup file
# file.close()
# # baris3 = file.readline()    #Ini akan error
# # print(baris3)

# #Baca file secara keseluruhan dan mengeluarkan baris dalam bentuk string #ex: Hello (baris 1), World(Baris 2)
# #akan jadi 1 string bernama "Hello World"
# seluruh_baris = file.read()
# print(seluruh_baris) 

# #Cara lain baca isi file
# file.close()
# with open("spider.txt") as file:    #Bisa baca meskipun udah di close
#     print(file.readline())

# # #Nulis ke file txt (kalo misalkan kondisi txt kita udah keisi, dia bakal overwrite semua isi txt lama)
# # with open("spider.txt", "w") as file:
# #     file.write("Aku sedang menulis sesuatu")

# # with open("spider.txt") as file:    
# #     print(file.readline())

# #rt nih sama kek "r" = read
# with open("spider.txt", "rt") as textfile:
#     for line in textfile:
#         print(line)

# “r”  open for reading (default)

# “w”  open for writing, truncating the file first

# “x”  open for exclusive creation, failing if the file already exists

# “a”  open for writing, appending to the end of the file if it exists

# “+”  open for both reading and writing

#default nya dia bakalan nulis di kata setelah baris terakhir
with open("spider.txt", "a") as textfile:
    textfile.write("\nizin masuk")          #biar ke baris bawah ditulisnya

#buat file baru
with open("spiderman2.txt", "x") as textfile:
    textfile.write("aku datang co")     

file.close()    #biasakan tutup setelah kelar

