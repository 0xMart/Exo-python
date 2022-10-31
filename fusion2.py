mot1 = input("entrer votre mot 1 ?")
mot2 = input("entrer votre mot 2 ?")

chaine1 = list(mot1)
chainetempo = list(mot2)
chaine2 = chainetempo[::-1]

chaine3=[]
longueur1 = len(chaine1)
longueur2 = len(chaine2)
a=0
longueurmax=len(mot1)
while a < longueurmax:
    if a < longueur1 :
        chaine3.append(chaine1[a])
    if a < longueur2 :
        chaine3.append(chaine2[a])
    a+=1
mot3 =''.join(chaine3)
print (mot3)
