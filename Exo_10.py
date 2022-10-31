from random import randint, randrange
import random, string

nombre = input("entrer un chiffre ?")
nombre = int (nombre)
liste = ["chien","chat", "poisson", "rat", "lion", "gepard", "test"]
lister = []

for i in range (0,nombre) :
    ramdom = randint(0,6)
    lister.append(liste [ramdom])

print (lister)

