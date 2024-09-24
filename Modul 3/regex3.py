import re

# print(re.search(r"Py.*n", "Pygmalion")) # mencari string  yang diawali string py dan diakhiri oleh huruf n terakhir dalam string

# print(re.search(r"Py.*n", "Python Programming")) #python programmin

# print(re.search(r"Py[a-z]*n", "Pytsdsdsdsdsn Programming")) #mencari string Py + string bebas pertama yang diakhiri oleh huruf n

# print(re.search(r"Py[a-z]*n", "Pyn"))


# print(re.search(r"o+l+", "ollllllllllllllloldfish")) #mencari string pertama yang berisi 1 atau lebih o yang diikuti 1 atau lebih l

# print(re.search(r"o+l+", "woolly"))
# print(re.search(r"o+l+", "boil"))

# print(re.search(r"p?each", "To each their own"))    #opsional, bisa menangkap peach atau pun each
# print(re.search(r"p?each", "I like peaches"))