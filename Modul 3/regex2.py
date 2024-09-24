import re

# result = re.search(r"aza", "plaza")
# print(result)

# print(re.search(r"^x", "xenon"))

# #mencari string "aza" dalam string plaza, dan menampilkan posisi aza dalam string plaza

# #kalau ga menemukan string yang diinginkan, secara default akan mengembalikan None

# print(re.search(r"p.ng", "pinguin")) #akan mencari seluruh string yang ada huruf p + huruf bebas + diikuti oleh n dan g

# print(re.search(r"p.", "pinguin")) #akan mencari seluruh string yang memuat huruf p + 1 huruf bebas

# print(re.search(r"p.ng", "Pangaea", re.IGNORECASE)) #mengabaikan case sensitive

# print(re.search(r"[Pp]ython", "python")) #bisa ngebaca kata python yang p nya kecil / gede

# print(re.search(r"[a-z]way", "The end of the highway")) #bakalan ngebaca huruf kecil apapun + way

# print(re.search(r"[a-z]way", "What a way to go"))   #karena way ga diikuti huruf apapun, bakalan ngebalikin none

# print(re.search("cloud[a-zA-Z0-9]", "cloudy"))  #bakalan ngebaca huruf apapun yang diakhir huruf apapun + angka


# print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces.")) #kalau ^ ada di dalam [], artinya negasi, ^a-zA-Z, semua elemen yang bukan huruf pertama
# print(re.search(r"^[a-zA-Z]", "This is a sentence with spaces.")) #mencari huruf pertama apapun dalam string

# print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces.")) #mencari karakter pertama yang bukun huruf apapun + spasi

# print(re.search(r"cat|dog", "I like cats.")) #atau

# print(re.search(r"cat|dog", "I love dogs!")) # atau

print(re.search(r"cat|dog", "I like both dogs and cats.")) #akan mencari yang pertama kali muncul

print(re.findall(r"cat|dog", "I like both dogs and cats.")) #akan mengembalikan seluruh elemen yang ditemukan dari nilai atau apabil ada di dalam string




