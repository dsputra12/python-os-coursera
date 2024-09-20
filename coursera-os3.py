import os 

#current working directory
print(os.getcwd())

# #buat directory atau folder baru
# os.mkdir("test")

# #change directory (tapi ga mutlak ngubah directory langsung secara terminal ?)
# os.chdir("test")
# print(os.getcwd())

# #apus directory
# os.rmdir("test")

#Mencari list directory yang berada di dalam directory sedang bekerja (cwd)
list_file = os.listdir("Coursera Python OS")
print(list_file)