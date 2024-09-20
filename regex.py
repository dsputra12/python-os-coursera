import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

# Adjusted regex to capture the entire log message including the error details
regex3 = r"^(\w+) (\d{2}) (\d{2}):(\d{2}):(\d{2}) (\w+) (\w+)\[(\d+)\]"
# regex3 = r"^(\w+) (\d{2}) (\d{2}):(\d{2}):(\d{2}) (\w+) (\w+) \[(\d+)\]"

result3 = re.search(regex3, log)
# Check if result3 is None
if result3:
    print("Nangkep seluruh log sampe kode error: ", result3.group(0))
    print("Nangkep bulan: ", result3.group(1))
    print("Nangkep tanggal: ", result3.group(2))
    print("Nangkep jam: ", result3.group(3))
    print("Nangkep menit: ", result3.group(4))
    print("Nangkep detik: ", result3.group(5))
    print("Nangkep nama komputer: ", result3.group(6))
    print("Nangkep nama error: ", result3.group(7))
    print("Nangkep kode error: ", result3.group(8))
else:
    print("No match found. Check the log format and regex pattern.")


# index = log.index("[")      #Mulai dari [ dan dianggap sebagai index 0
# print(log[index+1:index+6])

# regex = r"\[(\d+)\]"
# result = re.search(regex, log)

# print("Nangkep kode error: ", result[1])

# r"\[(\d+)\]"
# r"\  [    \" #[ posisi awal
# r " (\d+)  "  #(d+) akan mengambil kumpulan angka
# r"\      \]" #[ posisi akhir

#result[0] = [12345]
#result[1] = 12345

# Literals: Matches the exact characters.

# Example: cat matches the text "cat".
# Metacharacters: Characters with special meanings.

# . (dot): Matches any single character except a newline.
# Example: a.c matches "abc", "a1c", etc.
# ^: Matches the start of a line.
# Example: ^cat matches "cat" only if it's at the beginning of a line.
# $: Matches the end of a line.
# Example: cat$ matches "cat" only if it's at the end of a line.
# Character Classes: Matches any one of a set of characters.

# [abc]: Matches either "a", "b", or "c".
# [a-z]: Matches any lowercase letter.
# Quantifiers: Specify the number of occurrences.

# *: Matches 0 or more occurrences of the previous character or group.
# Example: a* matches "", "a", "aa", etc.
# +: Matches 1 or more occurrences of the previous character or group.
# Example: a+ matches "a", "aa", etc.
# ?: Matches 0 or 1 occurrence of the previous character or group.
# Example: a? matches "" or "a".
# Groups and Capturing: Groups multiple characters or patterns.

# (abc): Matches the sequence "abc".
# (a|b): Matches "a" or "b".
# Escaping: Use \ to escape metacharacters.

# Example: \. matches a literal dot.
# Examples
# Match an Email: ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$

# ^[a-zA-Z0-9._%+-]+: Matches the beginning part of an email.
# @[a-zA-Z0-9.-]+: Matches the domain name.
# \.[a-zA-Z]{2,}$: Matches the top-level domain.
# Match a Phone Number: ^\d{3}-\d{3}-\d{4}$

# ^\d{3}: Matches the area code.
# -\d{3}: Matches the first part of the number.
# -\d{4}$: Matches the last part of the number.

# (\w+) matches and captures one or more word characters (letters)

# regex2 = r"^(\w+) \d{2}"
# pada kode ini, rumus regex yang akan tersimpan di object, hanyalah (\w+) karena ada ()


# result2 = re.search(regex2, log)
# print("Nangkep tanggal ", result2[1])

#result [0] dia bakal manggil July 31
#result [1] dia bakal manggil July, karena dia bakal nangkep rumus regex pertama, yaitu ^(\w+)
