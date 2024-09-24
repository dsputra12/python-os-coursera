import re

regex = r"([\w\.-]+)"
log = "a.iam dsdsd -.dsds -------"
hasil = re.findall(regex, log )
print(hasil)