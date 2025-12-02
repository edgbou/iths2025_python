lista_filer = ["payload.exe", "notes.txt", "malware.zip", "readme.md"]

lista_filer.append("keylogger.py")

lista_filer[1] = "credentials.txt"

lista_filer.remove("readme.md")

lista_filer.insert(1,"hashdump.log")

print(lista_filer)