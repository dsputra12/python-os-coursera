import re

# print(re.search(r"A.*a", "Argentina"))  #mencari string yang diawali huruf A dan diakhiri oleh
# print(re.search(r"A.*a", "Azerbaijan"))
# print(re.search(r"^A.*a$", " Australia "))   #akan mengembalikan none, karena " " 
# #dihitung sebagai substring / kata pertama danspasi dihitung juga sebagai substring terakhir

# r”\d{3}-\d{3}-\d{4}”  This line of code matches U.S. phone numbers in the format 111-222-3333.


# r”^-?\d*(\.\d+)?$”  This line of code matches any positive or negative number, with or without decimal places.
#-10.9


# r”^(.+)\/([^\/]+)\/” This line of code matches any path and filename.
#.+, nangkep huruf yang diawali huruf apapun + huruf apapun
#(.+) buat nangkep user
#\/ buat nangkep /
#([^\/])+ buat nangkep kata apapun selain \ dan dapat diisi lebih dari 1 elemen, misal "tugas"

regex = r"^(.+)\/(([^\/]+)+)(\/$)"
result = re.search(regex, "usr/local/ayam/bogor/kecuubung/tugasrahasia/")
print(result.group(0))