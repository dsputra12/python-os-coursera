import re
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")

print(result)
print(result.groups()) #print hasil string yang diambil dalam bentuk tuple
print(result[0])    #dikembalikan dalam bentuk string
print(result[1])
print(result[2])
hasil = "{} {}".format(result[2], result[1])
print(hasil)