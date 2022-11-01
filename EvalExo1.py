#definition de nos borne aleatoirement
import random
randomalpha = random.randrange(0, 100)
randombeta = random.randrange(0, 100)
randomdelta = random.randrange(0, 100)
randomgamma = random.randrange(0, 100)
Borne1=[]
Borne2=[]
#affichage de nos borne pour vérifier l'efficacite du programme
print("[", randomalpha,randombeta,"]")
print("[", randomgamma,randomdelta,"]",)

#determination des grands et petit de chaques bornes
if (randomalpha < randombeta ) :
    randommin1 = randomalpha
    randommax1 = randombeta
else :
    randommin1 = randombeta
    randommax1 = randomalpha   
if (randomgamma < randomdelta ) :
    randommin2 = randomgamma
    randommax2 = randomdelta
else :
    randommin2 = randomdelta
    randommax2 = randomgamma


while randommin1 <= randommax1 :
    Borne1.append(randommin1)
    randommin1 +=1

while randommin2 <= randommax2 :
    Borne2.append(randommin2)
    randommin2+=1


ensemble = set(Borne1).intersection(Borne2)

if ensemble == set() :
    print ("res = no")
else :
    print ("res = yes")

    
