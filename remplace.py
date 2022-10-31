mot = input("entrer votre mot ?")
chaine = list(mot)
longueur = len(chaine)
lettre1 = chaine[0]
texte="*"
for i in range (1,longueur):
    if chaine[i] == lettre1:
        chaine[i] = texte
mot2 =''.join(chaine)
print(mot2)
print("---------------------")