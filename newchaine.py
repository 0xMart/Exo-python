mot = input("entrer votre mot ?")
chaine = list(mot)
longueur = len(chaine)
lettred = chaine[0]
lettref=chaine[longueur-1]

chaine[0]= lettref
chaine[longueur-1] = lettred
mot2 =''.join(chaine)
print(mot2)
print("---------------------")