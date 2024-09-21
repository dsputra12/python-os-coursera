import re

# print(re.search(r".com", "welcome"))    #1 huruf bebas + string com

# # print(re.search(r"\.com", "xcomwelcome")) #1 huruf bebas + diikuti string com dan harus di awal string

# # print(re.search(r"\.com", "mydomain.com")) #mencari .com pertama

# print(re.search(r"\.com", "mydomain gmail.com")) #alasan penggunaan \, karena dot special chararacter,
# #jadi harus dideklarasikan bersama \ jadi \., kalo tanpa \. , dia bakala nyari string ".com" 

print(re.search(r"\w*", "This is an example")) #nyari word pertama, bisa kosong, huruf, dana angka

print(re.search(r"\w*", "And_this_is_another")) #dihiung satu kata

