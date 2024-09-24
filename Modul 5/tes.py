from validations import validate_user

# validate_user("", -1)   #error 1

# hasil = validate_user("", 1)
# print(hasil)    #False, karena bukan alphanumeric

# hasil = validate_user("myuser", 1)  #true
# print(hasil)

# hasil = validate_user(88, 1)  #error 2, karena integer tidak memiliki panjang
# print(hasil)

# hasil = validate_user([], 1)  #masuk ke error 2, karena yang dihitung panjang list kosong, yaitu 0
# print(hasil)

hasil = validate_user(["name1"], 1)  #masuk ke error 3, karena alphanumeric hanya bekerja di string, bukan list
print(hasil)