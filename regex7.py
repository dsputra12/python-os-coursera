import re

print(re.search(r"[a-zA-Z]{5}", "a ghost"))     #ngambil 5 huruf pertama

print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared")) #ngambil 5 huruf pertama dari semua kata dan balikin dalam bentuk list

print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared")) #ngambil hanya kata yang terdiri dari 5 huruf

print(re.findall(r"\w{5,10}", "I really like strawberries")) #ngambil 5 - 9 huruf dari seluruh string
 
print(re.findall(r"\w{5,}", "I really like strawberries")) #ngambil semua string yang lebih dari 5 huruf

print(re.search(r"s\w{,20}", "I really like strawhat strawberries")) #search hanya nyari 1, findall nyari semua