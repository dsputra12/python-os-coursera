import re
# print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))   #hanya menangkap string yang dipisahkan oleh tanda baca

# print(re.split(r"([.?!])", "One sentence. Another one? And the last one!")) #memisahkan string oleh tanda baca dan tanda baca tersebut

# print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com"))

print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada"))   #Ada Lovelace

