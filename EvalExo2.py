import itertools
import random

#initialisation des nombres random
random1 = random.randrange(0, 21)
random2 = random.randrange(0, 21)
random3 = random.randrange(0, 21)
random4 = random.randrange(0, 21)
random5 = random.randrange(0, 21)
random6 = random.randrange(0, 21)
random7 = random.randrange(0, 21)
random8 = random.randrange(0, 21)
random9 = random.randrange(0, 21)
random10 = random.randrange(0, 21)

#affichages des listes pouir la verification
print("[", random1,random2,random3,random4,random5,"]")
print("[", random6,random7,random8,random9,random10,"]")

liste1=[random1,random2,random3,random4,random5,]
liste2=[random6,random7,random8,random9,random10,]

#boucle pour céer des couple de valeurs puis pour verifier s'il la valeur du couple fait 21
for a,b in itertools.product(liste1, liste2) :
     if(a+b) == 21:
        print ("Res = [", a,b,']')

    
