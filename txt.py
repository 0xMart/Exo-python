from pathlib import Path
fichier = open("fichier.txt", "a")
numchar = 1024*1024*50
fichier.write("0"* numchar)
fichier.close
Path(r'C:\Users\Malo\Documents\python\fichier.txt').stat()
file_size =Path(r'C:\Users\Malo\Documents\python\fichier.txt').stat().st_size
print("Taille du fichier:", file_size,"octets")
