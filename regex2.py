import re

result = re.search(r"aza", "plaza")
print(result)

print(re.search(r"^x", "xenon"))

#mencari string "aza" dalam string plaza, dan menampilkan posisi aza dalam string plaza

#kalau ga menemukan string yang diinginkan, secara default akan mengembalikan None

print(re.search(r"p.ng", "pinguin")) #akan mencari seluruh string yang ada huruf p, dan diikuti oleh n dan g

print(re.search(r"p.", "pinguin")) #akan mencari seluruh string yang memuat huruf p

print(re.search(r"p.ng", "Pangaea", re.IGNORECASE)) #mengabaikan case sensitive

