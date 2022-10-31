from itertools import chain


mot1 = input("entrer votre mot 1 ?")
mot2 = input("entrer votre mot 2 ?")

chaine1 = list(mot1)
chaine2 = list(mot2)
chaine3 = []
longueur1 = len(chaine1)
longueur2 = len(chaine2)

if (longueur1 > longueur2):
    longueurmax = longueur1
    longueurmin = longueur2
else :
    longueurmax = longueur2
    longueurmin = longueur1
for i  in range(0,longueurmax):
    if i%2 == 0 :
        if (i == longueurmin+1) :
            chaine3.append("")
        else :
            chaine3.append(chaine1[i])
    else :
        if (i == longueurmin) :
            chaine3.append("")
        else :
            chaine3.append(chaine2[i])


mot3 =''.join(chaine3)
print(mot3)
print("---------------------")

