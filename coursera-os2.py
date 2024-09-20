import os

# #delete file
# os.remove("spider.txt")

# #rename
# os.rename("spiderman2.txt", "aku_berubah.txt")

#cek file ada atau ga
hasil = os.path.exists("aku2_berubah.txt")
print(hasil)

#cek ukuran file
size = os.path.getsize("aku_berubah.txt")
print(size)     #size disini banyaknya elemen dalam file

#cek mtime (This code will provide a unix timestamp for the file)
time = os.path.getmtime("aku_berubah.txt")
print(time)

#time stamp normal
import datetime
timestamp = os.path.getmtime("aku_berubah.txt")
time = datetime.datetime.fromtimestamp(timestamp)
print(time)

#abspath
abs_path = os.path.abspath("spider.txt")
print(abs_path)

# #Windows file directory
# C:\my-directory\target-file.txt

# #Windows file directory written in Python
# C:/my-directory/target-file.txt.

# os.getcwd()

# #CWD command for external files:
# outputs['current_directory_before'] = os.getcwd()


# Absolute path: C:/users/admin/docs/stuff.txt
# PWD : C:/users/admin/
# relative path to stuff.txt : docs/stuff.txt